# -*- coding: utf-8 -*-
"""
边狱巴士（Limbus Company）人格抽取插件

功能：
- 单抽：模拟单次人格抽取
- 十连：模拟十连抽取（2行5列网格布局）
- 非酋/欧皇指数：根据抽卡记录评估运气
- 多卡池支持：支持切换不同卡池

使用指令：
- /tq单抽 或 /tq抽卡 - 进行单次抽取
- /tq十连 - 进行十连抽取
- /tq非酋指数 - 查看非酋评级
- /tq欧皇指数 - 查看欧皇评级
- /tq池列表 - 查看可用卡池
- /tq切池 池名 - 切换卡池
"""
import os
from pathlib import Path
from typing import Optional

import yaml

from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api.message_components import Image, Plain
from astrbot.api import logger

from .identities import (
    IDENTITIES,
    RARITY_SSS,
    RARITY_SS,
    RARITY_S,
    IMAGES_DIR,
    DEFAULT_IMAGE,
    get_identities_by_sinner,
)
from .gacha_core import GachaCore, LuckTracker
from .render_text import (
    format_single_pull_result,
    format_ten_pull_result,
    format_unlucky_index,
    format_lucky_index,
    format_pool_list,
    format_pool_switch_result,
)
from .render_image import create_grid_composite, cleanup_temp_file


# 默认配置
DEFAULT_CONFIG = {
    "rarity_rates": {
        "SSS": 2.9,
        "SS": 12.8,
        "S": 81.7,
    },
    "pity": {
        "enabled": True,
        "guarantee_rarity": "SS",
        "pity_rates": {
            "SSS": 2.98,
            "SS": 97.02,
        },
    },
    "pools": {
        "常驻池": {
            "enabled": True,
            "description": "包含所有可抽取人格",
            "filter": None,
        },
    },
    "default_pool": "常驻池",
    "command_prefix": "tq",
    "luck_index": {
        "unlucky_thresholds": [
            {"threshold": 200, "rating": "超级非酋", "message": "连抽200发都没见到000？你是不是得罪了月计？"},
            {"threshold": 150, "rating": "大非酋", "message": "150抽无000，建议去拜拜裁判鸟"},
            {"threshold": 100, "rating": "非酋", "message": "100抽无000，正常发挥，继续努力"},
            {"threshold": 50, "rating": "小非酋", "message": "50抽无000，才刚开始，不用慌"},
            {"threshold": 0, "rating": "普通", "message": "运气尚可，继续加油"},
        ],
        "lucky_thresholds": [
            {"threshold": 5, "window": 10, "rating": "超级欧皇", "message": "天选之人！请收下我的膝盖！"},
            {"threshold": 3, "window": 10, "rating": "大欧皇", "message": "这运气简直逆天，买彩票去吧！"},
            {"threshold": 2, "window": 20, "rating": "欧皇", "message": "运气不错，继续保持！"},
            {"threshold": 1, "window": 10, "rating": "小欧", "message": "刚出了000？恭喜恭喜～"},
            {"threshold": 0, "window": 10, "rating": "普通", "message": "运气普通，继续抽吧"},
        ],
    },
    "image": {
        "ten_pull_layout": {
            "rows": 2,
            "cols": 5,
            "spacing": 5,
            "target_height": 120,
        },
    },
}


@register("astrbot_plugin_limbus", "Jhh003", "边狱巴士人格抽取插件，支持单抽和十连", "1.1.0")
class LimbusGachaPlugin(Star):
    """边狱巴士人格抽取插件"""
    
    def __init__(self, context: Context):
        super().__init__(context)
        # 获取插件目录路径
        self.plugin_dir = Path(__file__).parent
        self.images_dir = self.plugin_dir / IMAGES_DIR
        self.config_path = self.plugin_dir / "config.yaml"
        
        # 加载配置
        self.config = self._load_config()
        
        # 初始化抽卡引擎
        self.gacha_core = self._create_gacha_core()
        
        # 初始化运气追踪器
        self.luck_tracker = LuckTracker()
        
        # 用户当前卡池：{user_id: pool_name}
        self.user_pools: dict[str, str] = {}
        
    def _load_config(self) -> dict:
        """
        加载配置文件
        
        Returns:
            配置字典
        """
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    config = yaml.safe_load(f)
                    if config:
                        # 合并默认配置
                        return self._merge_config(DEFAULT_CONFIG, config)
            except (IOError, yaml.YAMLError) as e:
                logger.warning(f"加载配置文件失败: {e}，使用默认配置")
        
        return DEFAULT_CONFIG.copy()
    
    def _merge_config(self, default: dict, override: dict) -> dict:
        """
        递归合并配置
        
        Args:
            default: 默认配置
            override: 覆盖配置
            
        Returns:
            合并后的配置
        """
        result = default.copy()
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._merge_config(result[key], value)
            else:
                result[key] = value
        return result
    
    def _create_gacha_core(self) -> GachaCore:
        """
        创建抽卡引擎实例
        
        Returns:
            GachaCore 实例
        """
        rarity_rates = self.config.get("rarity_rates", DEFAULT_CONFIG["rarity_rates"])
        pity_config = self.config.get("pity", DEFAULT_CONFIG["pity"])
        
        return GachaCore(
            rarity_rates=rarity_rates,
            pity_rates=pity_config.get("pity_rates"),
            pity_enabled=pity_config.get("enabled", True),
            pity_guarantee_rarity=pity_config.get("guarantee_rarity", "SS"),
        )
        
    async def initialize(self):
        """插件初始化"""
        logger.info("边狱巴士人格抽取插件初始化完成")
        # 检查图片目录是否存在
        if not self.images_dir.exists():
            logger.warning(f"图片目录不存在: {self.images_dir}，请创建并添加图片资源")
            self.images_dir.mkdir(parents=True, exist_ok=True)
    
    def _get_image_path(self, image_name: str) -> Optional[str]:
        """
        获取人格头像图片的完整路径
        
        Args:
            image_name: 图片文件名
            
        Returns:
            图片完整路径，如果图片不存在则返回默认图片路径或 None
        """
        image_path = self.images_dir / image_name
        if image_path.exists():
            return str(image_path)
        
        # 尝试使用默认图片
        default_path = self.images_dir / DEFAULT_IMAGE
        if default_path.exists():
            return str(default_path)
        
        return None
    
    def _get_user_pool(self, user_id: str) -> tuple[str, list[dict]]:
        """
        获取用户当前的卡池
        
        Args:
            user_id: 用户ID
            
        Returns:
            (卡池名称, 卡池人格列表)
        """
        pool_name = self.user_pools.get(user_id, self.config.get("default_pool", "常驻池"))
        pools_config = self.config.get("pools", {})
        
        if pool_name not in pools_config:
            pool_name = self.config.get("default_pool", "常驻池")
        
        pool_config = pools_config.get(pool_name, {})
        pool_filter = pool_config.get("filter")
        
        if pool_filter is None:
            # 常驻池，包含所有人格
            return pool_name, IDENTITIES
        
        filter_type = pool_filter.get("type")
        filter_value = pool_filter.get("value")
        
        if filter_type == "sinner":
            # 罪人专属池
            return pool_name, get_identities_by_sinner(filter_value)
        
        # 默认返回所有人格
        return pool_name, IDENTITIES
    
    def _get_user_id(self, event: AstrMessageEvent) -> str:
        """
        获取用户ID
        
        Args:
            event: 消息事件
            
        Returns:
            用户ID字符串
        """
        return str(event.get_sender_id())
    
    @filter.command("tq单抽")
    async def gacha_single(self, event: AstrMessageEvent):
        """边狱巴士单抽 - 模拟单次人格抽取"""
        user_id = self._get_user_id(event)
        pool_name, pool = self._get_user_pool(user_id)
        
        result = self.gacha_core.draw_single(pool, fallback_pool=IDENTITIES)
        
        # 记录抽卡结果
        self.luck_tracker.record_pull(user_id, result.get("rarity", ""))
        
        # 构建结果消息
        result_text = format_single_pull_result(result)
        
        # 尝试获取图片
        image_path = self._get_image_path(result.get("image", ""))
        
        if image_path:
            # 如果图片存在，发送图片和文字
            yield event.chain_result([
                Plain(result_text),
                Image.fromFileSystem(image_path)
            ])
        else:
            # 如果图片不存在，只发送文字
            yield event.plain_result(result_text + "\n\n(图片资源未配置)")
    
    @filter.command("tq抽卡")
    async def gacha_single_alias(self, event: AstrMessageEvent):
        """边狱巴士抽卡 - 单抽的别名指令"""
        async for result in self.gacha_single(event):
            yield result
    
    @filter.command("tq十连")
    async def gacha_ten(self, event: AstrMessageEvent):
        """边狱巴士十连 - 模拟十连抽取"""
        user_id = self._get_user_id(event)
        pool_name, pool = self._get_user_pool(user_id)
        
        results = self.gacha_core.draw_multiple(pool, count=10, fallback_pool=IDENTITIES)
        
        # 记录抽卡结果
        self.luck_tracker.record_pulls(user_id, results)
        
        # 统计稀有度
        rarity_count = self.gacha_core.count_by_rarity(results)
        
        # 构建精简版结果消息
        result_text = format_ten_pull_result(results, rarity_count, RARITY_SSS, pool_name)
        
        # 收集存在的图片路径
        image_paths = []
        for result in results:
            image_path = self._get_image_path(result.get("image", ""))
            if image_path:
                image_paths.append(image_path)
        
        # 获取图片布局配置
        image_config = self.config.get("image", {}).get("ten_pull_layout", {})
        
        # 创建网格布局的合成图片（2行5列）
        composite_path = create_grid_composite(
            image_paths,
            rows=image_config.get("rows", 2),
            cols=image_config.get("cols", 5),
            spacing=image_config.get("spacing", 5),
            target_height=image_config.get("target_height", 120),
        )
        
        if composite_path:
            # 发送文字 + 网格布局的合成图片
            yield event.chain_result([
                Plain(result_text),
                Image.fromFileSystem(composite_path)
            ])
            # 清理临时文件
            cleanup_temp_file(composite_path)
        else:
            # 如果没有图片或合成失败，只发送文字
            yield event.plain_result(result_text + "\n(图片资源未配置)")
    
    @filter.command("tq非酋指数")
    async def unlucky_index(self, event: AstrMessageEvent):
        """非酋指数 - 查看非酋评级"""
        user_id = self._get_user_id(event)
        
        total_pulls = self.luck_tracker.get_total_pulls(user_id)
        if total_pulls == 0:
            yield event.plain_result("📊 非酋指数评测 📊\n\n你还没有抽过卡，快去抽几发吧！")
            return
        
        thresholds = self.config.get("luck_index", {}).get("unlucky_thresholds", [])
        rating, message, pulls_since_sss = self.luck_tracker.evaluate_unlucky(user_id, thresholds)
        sss_rate = self.luck_tracker.get_sss_rate(user_id)
        
        result_text = format_unlucky_index(rating, message, pulls_since_sss, total_pulls, sss_rate)
        yield event.plain_result(result_text)
    
    @filter.command("tq欧皇指数")
    async def lucky_index(self, event: AstrMessageEvent):
        """欧皇指数 - 查看欧皇评级"""
        user_id = self._get_user_id(event)
        
        total_pulls = self.luck_tracker.get_total_pulls(user_id)
        if total_pulls == 0:
            yield event.plain_result("📊 欧皇指数评测 📊\n\n你还没有抽过卡，快去抽几发吧！")
            return
        
        thresholds = self.config.get("luck_index", {}).get("lucky_thresholds", [])
        rating, message, sss_count, window = self.luck_tracker.evaluate_lucky(user_id, thresholds)
        sss_rate = self.luck_tracker.get_sss_rate(user_id)
        
        result_text = format_lucky_index(rating, message, sss_count, window, total_pulls, sss_rate)
        yield event.plain_result(result_text)
    
    @filter.command("tq池列表")
    async def pool_list(self, event: AstrMessageEvent):
        """卡池列表 - 查看可用卡池"""
        user_id = self._get_user_id(event)
        current_pool = self.user_pools.get(user_id, self.config.get("default_pool", "常驻池"))
        pools = self.config.get("pools", {})
        
        result_text = format_pool_list(pools, current_pool)
        yield event.plain_result(result_text)
    
    @filter.command("tq切池")
    async def switch_pool(self, event: AstrMessageEvent):
        """切换卡池 - 切换当前使用的卡池"""
        user_id = self._get_user_id(event)
        
        # 获取目标卡池名称
        message_text = event.message_str.strip()
        # 移除指令前缀，获取卡池名称
        parts = message_text.split(maxsplit=1)
        if len(parts) < 2:
            yield event.plain_result("❌ 请指定要切换的卡池名称\n用法：/tq切池 池名\n使用 /tq池列表 查看可用卡池")
            return
        
        target_pool = parts[1].strip()
        pools = self.config.get("pools", {})
        
        if target_pool not in pools:
            yield event.plain_result(format_pool_switch_result(target_pool, False, f"卡池 {target_pool} 不存在"))
            return
        
        if not pools[target_pool].get("enabled", True):
            yield event.plain_result(format_pool_switch_result(target_pool, False, f"卡池 {target_pool} 已禁用"))
            return
        
        self.user_pools[user_id] = target_pool
        pool_desc = pools[target_pool].get("description", "")
        yield event.plain_result(format_pool_switch_result(target_pool, True, pool_desc))
    
    async def terminate(self):
        """插件销毁"""
        logger.info("边狱巴士人格抽取插件已卸载")
