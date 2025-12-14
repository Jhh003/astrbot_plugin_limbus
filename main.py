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
import tempfile
from pathlib import Path

from PIL import Image as PILImage

from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api.message_components import Image, Plain
from astrbot.api import logger

from .identities import (
    IDENTITIES,
    RARITY_RATES,
    PITY_RATES,
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
    
    def _create_horizontal_composite(self, image_paths: list, spacing: int = 5) -> str | None:
        """
        将多张图片横向排列合成一张图片
        
        Args:
            image_paths: 图片路径列表
            spacing: 图片之间的间距（像素）
            
        Returns:
            合成图片的临时文件路径，如果失败则返回 None
        """
        if not image_paths:
            return None
        
        # 加载所有图片
        images = []
        for path in image_paths:
            if path and os.path.exists(path):
                img = PILImage.open(path)
                # 转换为RGBA模式以支持透明背景
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
                images.append(img)
        
        if not images:
            return None
        
        # 计算合成图片的尺寸
        # 统一高度为所有图片中的最大高度
        max_height = max(img.height for img in images)
        
        # 将所有图片调整为相同高度（保持宽高比）
        resized_images = []
        for img in images:
            if img.height != max_height:
                ratio = max_height / img.height
                new_width = int(img.width * ratio)
                img = img.resize((new_width, max_height), PILImage.Resampling.LANCZOS)
            resized_images.append(img)
        
        # 计算总宽度
        total_width = sum(img.width for img in resized_images) + spacing * (len(resized_images) - 1)
        
        # 创建白色背景的合成图片
        composite = PILImage.new('RGB', (total_width, max_height), (255, 255, 255))
        
        # 依次粘贴图片
        x_offset = 0
        for img in resized_images:
            # 将RGBA图片粘贴到RGB背景上
            if img.mode == 'RGBA':
                # 创建白色背景
                bg = PILImage.new('RGB', img.size, (255, 255, 255))
                bg.paste(img, mask=img.split()[3])  # 使用alpha通道作为mask
                composite.paste(bg, (x_offset, 0))
            else:
                composite.paste(img, (x_offset, 0))
            x_offset += img.width + spacing
        
        # 保存为临时文件
        temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
        composite.save(temp_file.name, 'PNG')
        temp_file.close()
        
        return temp_file.name
    
    def _draw_single(self, is_pity: bool = False) -> dict:
        """
        执行单次抽取
        
        Args:
            is_pity: 是否为十连保底（第10次）
            
        Returns:
            抽取到的人格信息字典
        """
        rand = random.uniform(0, 100)
        
        if is_pity:
            # 十连保底：第10次必出00或00以上
            # 000: 2.9%, 00: 94.5%, 总计 97.4%（实际为100%，没有0）
            if rand < PITY_RATES[RARITY_SSS]:
                selected_rarity = RARITY_SSS
            else:
                selected_rarity = RARITY_SS
        else:
            # 普通抽取：000: 2.9%, 00: 12.8%, 0: 81.7%
            if rand < RARITY_RATES[RARITY_SSS]:
                selected_rarity = RARITY_SSS
            elif rand < RARITY_RATES[RARITY_SSS] + RARITY_RATES[RARITY_SS]:
                selected_rarity = RARITY_SS
            else:
                selected_rarity = RARITY_S
        
        # 从对应稀有度的人格池中随机选择
        pool = get_identities_by_rarity(selected_rarity)
        if pool:
            return random.choice(pool)
        
        # 如果对应池为空，从所有人格中随机选择
        return random.choice(IDENTITIES)
    
    def _draw_multiple(self, count: int) -> list:
        """
        执行多次抽取（十连带保底）
        
        Args:
            count: 抽取次数
            
        Returns:
            抽取到的人格信息列表
        """
        results = []
        for i in range(count):
            # 第10次为保底
            is_pity = (i == 9)
            results.append(self._draw_single(is_pity=is_pity))
        return results
    
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
        
        # 收集存在的图片路径
        image_paths = []
        for result in results:
            image_path = self._get_image_path(result["image"])
            if image_path:
                image_paths.append(image_path)
        
        # 创建横向排列的合成图片
        composite_path = self._create_horizontal_composite(image_paths)
        
        if composite_path:
            # 发送文字 + 横向排列的合成图片
            yield event.chain_result([
                Plain(result_text),
                Image.fromFileSystem(composite_path)
            ])
            # 清理临时文件
            try:
                os.unlink(composite_path)
            except (IOError, OSError):
                pass
        else:
            # 如果没有图片或合成失败，只发送文字
            yield event.plain_result(result_text + "\n(图片资源未配置)")
    
    async def terminate(self):
        """插件销毁"""
        logger.info("边狱巴士人格抽取插件已卸载")
