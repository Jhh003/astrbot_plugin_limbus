# -*- coding: utf-8 -*-
"""
图片渲染模块

负责抽卡结果的图片合成和布局。
"""
import os
import tempfile
from typing import Optional

from PIL import Image as PILImage


def create_grid_composite(
    image_paths: list[str],
    rows: int = 2,
    cols: int = 5,
    spacing: int = 5,
    target_height: Optional[int] = None,
    background_color: tuple[int, int, int] = (255, 255, 255)
) -> Optional[str]:
    """
    将多张图片按网格布局合成一张图片
    
    Args:
        image_paths: 图片路径列表
        rows: 行数
        cols: 每行列数
        spacing: 图片之间的间距（像素）
        target_height: 目标图片高度，None表示使用原始高度
        background_color: 背景颜色 (R, G, B)
        
    Returns:
        合成图片的临时文件路径，如果失败则返回 None
    """
    if not image_paths:
        return None
    
    # 加载并处理所有图片
    images = []
    for path in image_paths:
        if path and os.path.exists(path):
            try:
                img = PILImage.open(path)
                # 转换为RGBA模式以支持透明背景
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
                images.append(img)
            except (IOError, OSError):
                continue
    
    if not images:
        return None
    
    # 确定单个图片的尺寸
    if target_height:
        # 按目标高度缩放所有图片
        resized_images = []
        for img in images:
            ratio = target_height / img.height
            new_width = int(img.width * ratio)
            img = img.resize((new_width, target_height), PILImage.Resampling.LANCZOS)
            resized_images.append(img)
        images = resized_images
    
    # 计算单个图片的尺寸（取最大值保证对齐）
    cell_width = max(img.width for img in images)
    cell_height = max(img.height for img in images)
    
    # 计算总尺寸
    total_width = cols * cell_width + (cols - 1) * spacing
    total_height = rows * cell_height + (rows - 1) * spacing
    
    # 创建背景图片
    composite = PILImage.new('RGB', (total_width, total_height), background_color)
    
    # 按网格布局放置图片
    for idx, img in enumerate(images):
        if idx >= rows * cols:
            break
        
        row = idx // cols
        col = idx % cols
        
        x = col * (cell_width + spacing)
        y = row * (cell_height + spacing)
        
        # 居中放置图片
        offset_x = (cell_width - img.width) // 2
        offset_y = (cell_height - img.height) // 2
        
        # 将RGBA图片粘贴到RGB背景上
        if img.mode == 'RGBA':
            bg = PILImage.new('RGB', img.size, background_color)
            bg.paste(img, mask=img.split()[3])  # 使用alpha通道作为mask
            composite.paste(bg, (x + offset_x, y + offset_y))
        else:
            composite.paste(img, (x + offset_x, y + offset_y))
    
    # 保存为临时文件
    temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    composite.save(temp_file.name, 'PNG')
    temp_file.close()
    
    return temp_file.name


def create_horizontal_composite(
    image_paths: list[str],
    spacing: int = 5,
    target_height: Optional[int] = None,
    background_color: tuple[int, int, int] = (255, 255, 255)
) -> Optional[str]:
    """
    将多张图片横向排列合成一张图片（兼容旧版）
    
    Args:
        image_paths: 图片路径列表
        spacing: 图片之间的间距（像素）
        target_height: 目标图片高度，None表示使用原始高度
        background_color: 背景颜色 (R, G, B)
        
    Returns:
        合成图片的临时文件路径，如果失败则返回 None
    """
    if not image_paths:
        return None
    
    # 加载所有图片
    images = []
    for path in image_paths:
        if path and os.path.exists(path):
            try:
                img = PILImage.open(path)
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
                images.append(img)
            except (IOError, OSError):
                continue
    
    if not images:
        return None
    
    # 统一高度
    if target_height:
        max_height = target_height
    else:
        max_height = max(img.height for img in images)
    
    # 调整所有图片为相同高度
    resized_images = []
    for img in images:
        if img.height != max_height:
            ratio = max_height / img.height
            new_width = int(img.width * ratio)
            img = img.resize((new_width, max_height), PILImage.Resampling.LANCZOS)
        resized_images.append(img)
    
    # 计算总宽度
    total_width = sum(img.width for img in resized_images) + spacing * (len(resized_images) - 1)
    
    # 创建背景图片
    composite = PILImage.new('RGB', (total_width, max_height), background_color)
    
    # 依次粘贴图片
    x_offset = 0
    for img in resized_images:
        if img.mode == 'RGBA':
            bg = PILImage.new('RGB', img.size, background_color)
            bg.paste(img, mask=img.split()[3])
            composite.paste(bg, (x_offset, 0))
        else:
            composite.paste(img, (x_offset, 0))
        x_offset += img.width + spacing
    
    # 保存为临时文件
    temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    composite.save(temp_file.name, 'PNG')
    temp_file.close()
    
    return temp_file.name


def cleanup_temp_file(file_path: Optional[str]) -> bool:
    """
    清理临时文件
    
    Args:
        file_path: 临时文件路径
        
    Returns:
        是否成功清理
    """
    if file_path and os.path.exists(file_path):
        try:
            os.unlink(file_path)
            return True
        except (IOError, OSError):
            return False
    return False
