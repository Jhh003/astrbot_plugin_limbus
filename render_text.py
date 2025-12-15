# -*- coding: utf-8 -*-
"""
文字排版模块

负责抽卡结果的文字格式化和排版。
"""
from typing import Optional

from .identities import get_rarity_display


# 稀有度排序权重（用于排序显示）
RARITY_WEIGHT = {
    "SSS": 3,
    "SS": 2,
    "S": 1,
}


def format_single_result(identity: dict, show_rarity: bool = True) -> str:
    """
    格式化单个抽取结果
    
    Args:
        identity: 人格信息字典
        show_rarity: 是否显示稀有度
        
    Returns:
        格式化的结果字符串
    """
    rarity_display = get_rarity_display(identity.get("rarity", ""))
    sinner = identity.get("sinner", "未知")
    name = identity.get("name", "未知")
    
    if show_rarity:
        return f"【{sinner}】{name} ({rarity_display})"
    return f"【{sinner}】{name}"


def format_single_pull_result(identity: dict) -> str:
    """
    格式化单抽结果（完整信息）
    
    Args:
        identity: 人格信息字典
        
    Returns:
        格式化的结果字符串
    """
    rarity_display = get_rarity_display(identity.get("rarity", ""))
    return f"🎰 边狱巴士人格抽取 🎰\n\n【{identity.get('sinner', '未知')}】{identity.get('name', '未知')}\n稀有度: {rarity_display}"


def format_statistics(rarity_count: dict[str, int]) -> str:
    """
    格式化稀有度统计信息
    
    Args:
        rarity_count: 各稀有度的数量统计
        
    Returns:
        格式化的统计字符串，如 "★★★×1 | ★★×3 | ★×6"
    """
    parts = []
    # 按权重从高到低排序
    for rarity in sorted(rarity_count.keys(), key=lambda x: RARITY_WEIGHT.get(x, 0), reverse=True):
        count = rarity_count[rarity]
        if count > 0:
            parts.append(f"{get_rarity_display(rarity)}×{count}")
    
    return " | ".join(parts) if parts else "无统计"


def format_ten_pull_result(
    results: list[dict],
    rarity_count: dict[str, int],
    high_star_rarity: str = "SSS",
    pool_name: Optional[str] = None
) -> str:
    """
    格式化十连抽取结果（精简版）
    
    只显示高星（SSS）的详细信息，低星简写。
    
    Args:
        results: 抽取结果列表
        rarity_count: 各稀有度的数量统计
        high_star_rarity: 被视为"高星"的稀有度
        pool_name: 当前卡池名称
        
    Returns:
        格式化的结果字符串
    """
    lines = []
    
    # 第一行：标题
    if pool_name:
        lines.append(f"🎰 边狱巴士十连抽取 🎰\n【{pool_name}】")
    else:
        lines.append("🎰 边狱巴士十连抽取 🎰")
    
    # 第二行：统计
    lines.append(f"统计：{format_statistics(rarity_count)}")
    
    # 第三行：分割线
    lines.append("─" * 18)
    
    # 高星详细信息
    high_star_results = [r for r in results if r.get("rarity") == high_star_rarity]
    
    if high_star_results:
        lines.append(f"🌟 {get_rarity_display(high_star_rarity)} 人格：")
        for result in high_star_results:
            lines.append(f"  • 【{result.get('sinner', '未知')}】{result.get('name', '未知')}")
    
    # 低星简写
    low_star_count = sum(v for k, v in rarity_count.items() if k != high_star_rarity)
    if low_star_count > 0:
        lines.append(f"\n其余{low_star_count}个为★★/★人格")
    
    return "\n".join(lines)


def format_unlucky_index(
    rating: str,
    message: str,
    pulls_since_sss: int,
    total_pulls: int,
    sss_rate: float
) -> str:
    """
    格式化非酋指数结果
    
    Args:
        rating: 评级
        message: 调侃文案
        pulls_since_sss: 距离上次SSS的抽数
        total_pulls: 总抽卡次数
        sss_rate: SSS出率
        
    Returns:
        格式化的结果字符串
    """
    lines = [
        "📊 非酋指数评测 📊",
        "─" * 18,
        f"评级：{rating}",
        f"距离上次★★★：{pulls_since_sss}抽",
        f"总计抽卡：{total_pulls}次",
        f"★★★出率：{sss_rate:.2f}%",
        "─" * 18,
        f"💬 {message}"
    ]
    return "\n".join(lines)


def format_lucky_index(
    rating: str,
    message: str,
    sss_count: int,
    window: int,
    total_pulls: int,
    sss_rate: float
) -> str:
    """
    格式化欧皇指数结果
    
    Args:
        rating: 评级
        message: 调侃文案
        sss_count: 窗口内SSS数量
        window: 统计窗口大小
        total_pulls: 总抽卡次数
        sss_rate: SSS出率
        
    Returns:
        格式化的结果字符串
    """
    lines = [
        "📊 欧皇指数评测 📊",
        "─" * 18,
        f"评级：{rating}",
        f"最近{window}抽★★★数：{sss_count}个",
        f"总计抽卡：{total_pulls}次",
        f"★★★出率：{sss_rate:.2f}%",
        "─" * 18,
        f"💬 {message}"
    ]
    return "\n".join(lines)


def format_pool_list(pools: dict[str, dict], current_pool: str) -> str:
    """
    格式化卡池列表
    
    Args:
        pools: 所有卡池配置
        current_pool: 当前使用的卡池名称
        
    Returns:
        格式化的卡池列表字符串
    """
    lines = [
        "🎱 可用卡池列表 🎱",
        "─" * 18,
    ]
    
    for pool_name, pool_config in pools.items():
        if pool_config.get("enabled", True):
            marker = "✓" if pool_name == current_pool else "○"
            desc = pool_config.get("description", "")
            lines.append(f"{marker} {pool_name}")
            if desc:
                lines.append(f"    {desc}")
    
    lines.append("─" * 18)
    lines.append(f"当前卡池：{current_pool}")
    lines.append("使用 /tq切池 池名 切换卡池")
    
    return "\n".join(lines)


def format_pool_switch_result(pool_name: str, success: bool, message: str = "") -> str:
    """
    格式化卡池切换结果
    
    Args:
        pool_name: 目标卡池名称
        success: 是否切换成功
        message: 附加消息
        
    Returns:
        格式化的结果字符串
    """
    if success:
        return f"✅ 已切换到卡池：{pool_name}\n{message}" if message else f"✅ 已切换到卡池：{pool_name}"
    return f"❌ 切换失败：{message}" if message else f"❌ 切换失败：卡池 {pool_name} 不存在"
