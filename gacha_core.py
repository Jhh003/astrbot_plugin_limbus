# -*- coding: utf-8 -*-
"""
抽卡核心逻辑模块

包含概率计算、保底机制、抽取算法等核心功能。
可复用于其他抽卡类游戏插件。
"""
import random
from typing import Optional


class GachaCore:
    """抽卡核心引擎"""
    
    def __init__(
        self,
        rarity_rates: dict[str, float],
        pity_rates: Optional[dict[str, float]] = None,
        pity_enabled: bool = True,
        pity_guarantee_rarity: str = "SS"
    ):
        """
        初始化抽卡引擎
        
        Args:
            rarity_rates: 稀有度概率配置，如 {"SSS": 2.9, "SS": 12.8, "S": 81.7}
            pity_rates: 保底时的概率配置，如 {"SSS": 2.98, "SS": 97.02}
            pity_enabled: 是否开启保底机制
            pity_guarantee_rarity: 保底最低稀有度
        """
        self.rarity_rates = rarity_rates
        self.pity_rates = pity_rates or {}
        self.pity_enabled = pity_enabled
        self.pity_guarantee_rarity = pity_guarantee_rarity
        
        # 按概率从高到低排序稀有度
        self.rarity_order = sorted(rarity_rates.keys(), key=lambda x: rarity_rates[x])
    
    def determine_rarity(self, is_pity: bool = False) -> str:
        """
        根据概率决定本次抽取的稀有度
        
        Args:
            is_pity: 是否为保底抽取
            
        Returns:
            抽取到的稀有度
        """
        rand = random.uniform(0, 100)
        
        if is_pity and self.pity_enabled and self.pity_rates:
            # 保底时使用保底概率
            cumulative = 0
            for rarity in self.rarity_order:
                if rarity in self.pity_rates:
                    cumulative += self.pity_rates[rarity]
                    if rand < cumulative:
                        return rarity
            # 默认返回保底最低稀有度
            return self.pity_guarantee_rarity
        else:
            # 普通抽取
            cumulative = 0
            for rarity in self.rarity_order:
                cumulative += self.rarity_rates[rarity]
                if rand < cumulative:
                    return rarity
            # 默认返回最低稀有度
            return self.rarity_order[-1]
    
    def draw_single(
        self,
        pool: list[dict],
        is_pity: bool = False,
        fallback_pool: Optional[list[dict]] = None
    ) -> dict:
        """
        执行单次抽取
        
        Args:
            pool: 当前卡池（按稀有度分组的人格列表）
            is_pity: 是否为保底抽取
            fallback_pool: 当对应稀有度池为空时的备用池
            
        Returns:
            抽取到的人格信息字典
        """
        selected_rarity = self.determine_rarity(is_pity)
        
        # 从对应稀有度的池中筛选
        rarity_pool = [item for item in pool if item.get("rarity") == selected_rarity]
        
        if rarity_pool:
            return random.choice(rarity_pool)
        
        # 如果对应稀有度池为空，使用备用池
        if fallback_pool:
            return random.choice(fallback_pool)
        
        # 最后兜底，从整个池随机选
        return random.choice(pool) if pool else {}
    
    def draw_multiple(
        self,
        pool: list[dict],
        count: int = 10,
        pity_position: int = 10,
        fallback_pool: Optional[list[dict]] = None
    ) -> list[dict]:
        """
        执行多次抽取（带保底机制）
        
        Args:
            pool: 当前卡池
            count: 抽取次数
            pity_position: 保底触发位置（第几抽触发保底）
            fallback_pool: 备用池
            
        Returns:
            抽取到的人格信息列表
        """
        results = []
        for i in range(count):
            # 在指定位置触发保底
            is_pity = self.pity_enabled and ((i + 1) == pity_position)
            results.append(self.draw_single(pool, is_pity=is_pity, fallback_pool=fallback_pool))
        return results
    
    @staticmethod
    def count_by_rarity(results: list[dict]) -> dict[str, int]:
        """
        统计抽取结果中各稀有度的数量
        
        Args:
            results: 抽取结果列表
            
        Returns:
            各稀有度的数量统计
        """
        count = {}
        for item in results:
            rarity = item.get("rarity", "unknown")
            count[rarity] = count.get(rarity, 0) + 1
        return count
    
    @staticmethod
    def filter_by_rarity(results: list[dict], rarity: str) -> list[dict]:
        """
        筛选指定稀有度的结果
        
        Args:
            results: 抽取结果列表
            rarity: 目标稀有度
            
        Returns:
            筛选后的结果列表
        """
        return [item for item in results if item.get("rarity") == rarity]


class LuckTracker:
    """运气追踪器，用于计算非酋/欧皇指数"""
    
    def __init__(self, max_history: int = 500):
        """
        初始化运气追踪器
        
        Args:
            max_history: 保存的最大抽卡历史记录数
        """
        self.max_history = max_history
        # 用户抽卡历史：{user_id: [稀有度列表]}
        self.user_history: dict[str, list[str]] = {}
    
    def record_pull(self, user_id: str, rarity: str) -> None:
        """
        记录一次抽卡结果
        
        Args:
            user_id: 用户ID
            rarity: 抽取到的稀有度
        """
        if user_id not in self.user_history:
            self.user_history[user_id] = []
        
        self.user_history[user_id].append(rarity)
        
        # 限制历史记录长度
        if len(self.user_history[user_id]) > self.max_history:
            self.user_history[user_id] = self.user_history[user_id][-self.max_history:]
    
    def record_pulls(self, user_id: str, results: list[dict]) -> None:
        """
        记录多次抽卡结果
        
        Args:
            user_id: 用户ID
            results: 抽取结果列表
        """
        for item in results:
            self.record_pull(user_id, item.get("rarity", "unknown"))
    
    def get_pulls_since_last_sss(self, user_id: str) -> int:
        """
        获取用户距离上次抽到SSS的抽数
        
        Args:
            user_id: 用户ID
            
        Returns:
            距离上次SSS的抽数，如果从未抽到则返回总抽数
        """
        history = self.user_history.get(user_id, [])
        if not history:
            return 0
        
        # 从后往前查找最近的SSS
        for i, rarity in enumerate(reversed(history)):
            if rarity == "SSS":
                return i
        
        # 从未抽到SSS
        return len(history)
    
    def get_sss_count_in_window(self, user_id: str, window: int = 10) -> int:
        """
        获取用户最近N抽中SSS的数量
        
        Args:
            user_id: 用户ID
            window: 统计窗口大小
            
        Returns:
            窗口内SSS的数量
        """
        history = self.user_history.get(user_id, [])
        if not history:
            return 0
        
        recent = history[-window:] if len(history) >= window else history
        return sum(1 for r in recent if r == "SSS")
    
    def get_total_pulls(self, user_id: str) -> int:
        """
        获取用户总抽卡次数
        
        Args:
            user_id: 用户ID
            
        Returns:
            总抽卡次数
        """
        return len(self.user_history.get(user_id, []))
    
    def get_sss_rate(self, user_id: str) -> float:
        """
        获取用户的SSS出率
        
        Args:
            user_id: 用户ID
            
        Returns:
            SSS出率百分比
        """
        history = self.user_history.get(user_id, [])
        if not history:
            return 0.0
        
        sss_count = sum(1 for r in history if r == "SSS")
        return (sss_count / len(history)) * 100
    
    def evaluate_unlucky(
        self,
        user_id: str,
        thresholds: list[dict]
    ) -> tuple[str, str, int]:
        """
        评估用户的非酋指数
        
        Args:
            user_id: 用户ID
            thresholds: 评价标准列表，按阈值从高到低排序
            
        Returns:
            (评级, 调侃文案, 距离上次SSS的抽数)
        """
        pulls_since_sss = self.get_pulls_since_last_sss(user_id)
        
        for config in thresholds:
            if pulls_since_sss >= config.get("threshold", 0):
                return (
                    config.get("rating", "普通"),
                    config.get("message", ""),
                    pulls_since_sss
                )
        
        return ("普通", "运气尚可", pulls_since_sss)
    
    def evaluate_lucky(
        self,
        user_id: str,
        thresholds: list[dict]
    ) -> tuple[str, str, int, int]:
        """
        评估用户的欧皇指数
        
        Args:
            user_id: 用户ID
            thresholds: 评价标准列表，按SSS数量从高到低排序
            
        Returns:
            (评级, 调侃文案, 窗口内SSS数量, 窗口大小)
        """
        for config in thresholds:
            window = config.get("window", 10)
            threshold = config.get("threshold", 0)
            sss_count = self.get_sss_count_in_window(user_id, window)
            
            if sss_count >= threshold:
                return (
                    config.get("rating", "普通"),
                    config.get("message", ""),
                    sss_count,
                    window
                )
        
        return ("普通", "运气普通", 0, 10)
    
    def clear_user_history(self, user_id: str) -> None:
        """
        清除用户的抽卡历史
        
        Args:
            user_id: 用户ID
        """
        if user_id in self.user_history:
            del self.user_history[user_id]
