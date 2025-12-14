# -*- coding: utf-8 -*-
"""
边狱巴士（Limbus Company）人格抽取插件

功能：
- 单抽：模拟单次人格抽取
- 十连：模拟十连抽取

使用指令：
- /tq单抽 或 /tq抽卡 - 进行单次抽取
- /tq十连 - 进行十连抽取
"""
import os
import random
from pathlib import Path

from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api.message_components import Image, Plain
from astrbot.api import logger

from .identities import (
    IDENTITIES,
    RARITY_RATES,
    RARITY_SSS,
    RARITY_SS,
    RARITY_S,
    IMAGES_DIR,
    DEFAULT_IMAGE,
    get_identities_by_rarity,
    get_rarity_display,
)


@register("astrbot_plugin_limbus", "Jhh003", "边狱巴士人格抽取插件，支持单抽和十连", "1.0.0")
class LimbusGachaPlugin(Star):
    """边狱巴士人格抽取插件"""
    
    def __init__(self, context: Context):
        super().__init__(context)
        # 获取插件目录路径
        self.plugin_dir = Path(__file__).parent
        self.images_dir = self.plugin_dir / IMAGES_DIR
        
    async def initialize(self):
        """插件初始化"""
        logger.info("边狱巴士人格抽取插件初始化完成")
        # 检查图片目录是否存在
        if not self.images_dir.exists():
            logger.warning(f"图片目录不存在: {self.images_dir}，请创建并添加图片资源")
            self.images_dir.mkdir(parents=True, exist_ok=True)
    
    def _get_image_path(self, image_name: str) -> str | None:
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
    
    def _draw_single(self) -> dict:
        """
        执行单次抽取
        
        Returns:
            抽取到的人格信息字典
        """
        # 根据概率确定稀有度
        # SSS: 0-3, SS: 3-15, S: 15-100
        rand = random.uniform(0, 100)
        
        # 按照从稀有到常见的顺序检查
        if rand < RARITY_RATES[RARITY_SSS]:
            # 0 <= rand < 3 -> SSS (3%)
            selected_rarity = RARITY_SSS
        elif rand < RARITY_RATES[RARITY_SSS] + RARITY_RATES[RARITY_SS]:
            # 3 <= rand < 15 -> SS (12%)
            selected_rarity = RARITY_SS
        else:
            # 15 <= rand < 100 -> S (85%)
            selected_rarity = RARITY_S
        
        # 从对应稀有度的人格池中随机选择
        pool = get_identities_by_rarity(selected_rarity)
        if pool:
            return random.choice(pool)
        
        # 如果对应池为空，从所有人格中随机选择
        return random.choice(IDENTITIES)
    
    def _draw_multiple(self, count: int) -> list:
        """
        执行多次抽取
        
        Args:
            count: 抽取次数
            
        Returns:
            抽取到的人格信息列表
        """
        return [self._draw_single() for _ in range(count)]
    
    def _format_result(self, identity: dict) -> str:
        """
        格式化单个抽取结果
        
        Args:
            identity: 人格信息字典
            
        Returns:
            格式化的结果字符串
        """
        rarity_display = get_rarity_display(identity["rarity"])
        return f"【{identity['sinner']}】{identity['name']}\n稀有度: {rarity_display}"
    
    @filter.command("tq单抽")
    async def gacha_single(self, event: AstrMessageEvent):
        """边狱巴士单抽 - 模拟单次人格抽取"""
        result = self._draw_single()
        
        # 构建结果消息
        result_text = f"🎰 边狱巴士人格抽取 🎰\n\n{self._format_result(result)}"
        
        # 尝试获取图片
        image_path = self._get_image_path(result["image"])
        
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
        results = self._draw_multiple(10)
        
        # 统计稀有度
        rarity_count = {RARITY_SSS: 0, RARITY_SS: 0, RARITY_S: 0}
        for r in results:
            rarity_count[r["rarity"]] += 1
        
        # 构建结果消息
        result_lines = ["🎰 边狱巴士十连抽取 🎰\n"]
        result_lines.append(f"统计: ★★★×{rarity_count[RARITY_SSS]} | ★★×{rarity_count[RARITY_SS]} | ★×{rarity_count[RARITY_S]}\n")
        result_lines.append("=" * 20 + "\n")
        
        for i, result in enumerate(results, 1):
            result_lines.append(f"{i}. {self._format_result(result)}\n")
        
        result_text = "\n".join(result_lines)
        
        # 收集存在的图片
        images = []
        for result in results:
            image_path = self._get_image_path(result["image"])
            if image_path:
                images.append(Image.fromFileSystem(image_path))
        
        if images:
            # 如果有图片，发送文字和所有图片
            chain = [Plain(result_text)] + images
            yield event.chain_result(chain)
        else:
            # 如果没有图片，只发送文字
            yield event.plain_result(result_text + "\n(图片资源未配置)")
    
    async def terminate(self):
        """插件销毁"""
        logger.info("边狱巴士人格抽取插件已卸载")
