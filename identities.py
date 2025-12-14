# -*- coding: utf-8 -*-
"""
边狱巴士（Limbus Company）人格数据文件
此文件包含所有可抽取的人格信息和图片路径配置

图片资源说明：
1. 图片需放置在 images/ 目录下
2. 图片命名格式建议：{罪人英文名}_{人格英文名}.png
3. 例如：yi_sang_base.png, faust_base.png
"""

# 稀有度等级定义
RARITY_SSS = "SSS"  # 000 人格 (3星)
RARITY_SS = "SS"    # 00 人格 (2星)
RARITY_S = "S"      # 0 人格 (1星)

# 稀有度对应的抽取概率（百分比）
RARITY_RATES = {
    RARITY_SSS: 3.0,   # 3% 概率抽到 SSS 人格
    RARITY_SS: 12.0,   # 12% 概率抽到 SS 人格
    RARITY_S: 85.0,    # 85% 概率抽到 S 人格
}

# 图片资源目录路径（相对于插件目录）
IMAGES_DIR = "images"

# 默认占位图片（当人格图片不存在时使用）
DEFAULT_IMAGE = "default.png"

# 罪人列表
SINNERS = [
    "以实玛利",  # Yi Sang
    "浮士德",    # Faust
    "堂吉诃德",  # Don Quixote
    "良秀",      # Ryōshū
    "默尔索",    # Meursault
    "鸿璐",      # Hong Lu
    "希斯克利夫", # Heathcliff
    "以扫",      # Ishmael
    "罗佳",      # Rodya
    "辛克莱",    # Sinclair
    "奥提斯",    # Outis
    "桂",        # Gregor
]

# 人格数据列表
# 格式：{"name": 人格名称, "sinner": 罪人名称, "rarity": 稀有度, "image": 图片文件名}
# 注：图片文件名为占位符，用户需自行添加对应图片资源
IDENTITIES = [
    # === SSS 稀有度人格 (000) ===
    # 以实玛利
    {"name": "LCB囚人", "sinner": "以实玛利", "rarity": RARITY_SSS, "image": "yi_sang_lcb.png"},
    {"name": "刺客翎羽事务所", "sinner": "以实玛利", "rarity": RARITY_SSS, "image": "yi_sang_feather.png"},
    {"name": "七色协会东部支部4科", "sinner": "以实玛利", "rarity": RARITY_SSS, "image": "yi_sang_7_section4.png"},
    
    # 浮士德
    {"name": "LCB囚人", "sinner": "浮士德", "rarity": RARITY_SSS, "image": "faust_lcb.png"},
    {"name": "七色协会西部支部3科", "sinner": "浮士德", "rarity": RARITY_SSS, "image": "faust_7_section3.png"},
    {"name": "流血狂欢骑士团", "sinner": "浮士德", "rarity": RARITY_SSS, "image": "faust_bloodfiesta.png"},
    
    # 堂吉诃德
    {"name": "LCB囚人", "sinner": "堂吉诃德", "rarity": RARITY_SSS, "image": "don_quixote_lcb.png"},
    {"name": "石灰工坊", "sinner": "堂吉诃德", "rarity": RARITY_SSS, "image": "don_quixote_shi.png"},
    {"name": "W协会3科", "sinner": "堂吉诃德", "rarity": RARITY_SSS, "image": "don_quixote_w3.png"},
    
    # 良秀
    {"name": "LCB囚人", "sinner": "良秀", "rarity": RARITY_SSS, "image": "ryoshu_lcb.png"},
    {"name": "七色协会东部支部4科", "sinner": "良秀", "rarity": RARITY_SSS, "image": "ryoshu_7_section4.png"},
    {"name": "流血狂欢骑士团", "sinner": "良秀", "rarity": RARITY_SSS, "image": "ryoshu_bloodfiesta.png"},
    
    # 默尔索
    {"name": "LCB囚人", "sinner": "默尔索", "rarity": RARITY_SSS, "image": "meursault_lcb.png"},
    {"name": "石灰工坊", "sinner": "默尔索", "rarity": RARITY_SSS, "image": "meursault_shi.png"},
    {"name": "刺客翎羽事务所", "sinner": "默尔索", "rarity": RARITY_SSS, "image": "meursault_feather.png"},
    
    # 鸿璐
    {"name": "LCB囚人", "sinner": "鸿璐", "rarity": RARITY_SSS, "image": "hong_lu_lcb.png"},
    {"name": "流血狂欢骑士团", "sinner": "鸿璐", "rarity": RARITY_SSS, "image": "hong_lu_bloodfiesta.png"},
    {"name": "七色协会西部支部4科", "sinner": "鸿璐", "rarity": RARITY_SSS, "image": "hong_lu_7_section4.png"},
    
    # 希斯克利夫
    {"name": "LCB囚人", "sinner": "希斯克利夫", "rarity": RARITY_SSS, "image": "heathcliff_lcb.png"},
    {"name": "石灰工坊", "sinner": "希斯克利夫", "rarity": RARITY_SSS, "image": "heathcliff_shi.png"},
    {"name": "七色协会西部支部3科", "sinner": "希斯克利夫", "rarity": RARITY_SSS, "image": "heathcliff_7_section3.png"},
    
    # 以扫
    {"name": "LCB囚人", "sinner": "以扫", "rarity": RARITY_SSS, "image": "ishmael_lcb.png"},
    {"name": "七色协会南部支部4科", "sinner": "以扫", "rarity": RARITY_SSS, "image": "ishmael_7_section4.png"},
    {"name": "刺客翎羽事务所", "sinner": "以扫", "rarity": RARITY_SSS, "image": "ishmael_feather.png"},
    
    # 罗佳
    {"name": "LCB囚人", "sinner": "罗佳", "rarity": RARITY_SSS, "image": "rodya_lcb.png"},
    {"name": "流血狂欢骑士团", "sinner": "罗佳", "rarity": RARITY_SSS, "image": "rodya_bloodfiesta.png"},
    {"name": "七色协会东部支部4科", "sinner": "罗佳", "rarity": RARITY_SSS, "image": "rodya_7_section4.png"},
    
    # 辛克莱
    {"name": "LCB囚人", "sinner": "辛克莱", "rarity": RARITY_SSS, "image": "sinclair_lcb.png"},
    {"name": "石灰工坊", "sinner": "辛克莱", "rarity": RARITY_SSS, "image": "sinclair_shi.png"},
    {"name": "七色协会南部支部4科", "sinner": "辛克莱", "rarity": RARITY_SSS, "image": "sinclair_7_section4.png"},
    
    # 奥提斯
    {"name": "LCB囚人", "sinner": "奥提斯", "rarity": RARITY_SSS, "image": "outis_lcb.png"},
    {"name": "七色协会西部支部3科", "sinner": "奥提斯", "rarity": RARITY_SSS, "image": "outis_7_section3.png"},
    {"name": "W协会3科", "sinner": "奥提斯", "rarity": RARITY_SSS, "image": "outis_w3.png"},
    
    # 桂
    {"name": "LCB囚人", "sinner": "桂", "rarity": RARITY_SSS, "image": "gregor_lcb.png"},
    {"name": "刺客翎羽事务所", "sinner": "桂", "rarity": RARITY_SSS, "image": "gregor_feather.png"},
    {"name": "流血狂欢骑士团", "sinner": "桂", "rarity": RARITY_SSS, "image": "gregor_bloodfiesta.png"},
    
    # === SS 稀有度人格 (00) ===
    {"name": "南部夜叉刘氏事务所", "sinner": "以实玛利", "rarity": RARITY_SS, "image": "yi_sang_liu.png"},
    {"name": "迪耶奇协会", "sinner": "浮士德", "rarity": RARITY_SS, "image": "faust_dieci.png"},
    {"name": "迪耶奇协会", "sinner": "堂吉诃德", "rarity": RARITY_SS, "image": "don_quixote_dieci.png"},
    {"name": "N协会大剑", "sinner": "良秀", "rarity": RARITY_SS, "image": "ryoshu_n_corp.png"},
    {"name": "迪耶奇协会", "sinner": "默尔索", "rarity": RARITY_SS, "image": "meursault_dieci.png"},
    {"name": "南部夜叉刘氏事务所", "sinner": "鸿璐", "rarity": RARITY_SS, "image": "hong_lu_liu.png"},
    {"name": "N协会大锤", "sinner": "希斯克利夫", "rarity": RARITY_SS, "image": "heathcliff_n_corp.png"},
    {"name": "南部夜叉刘氏事务所", "sinner": "以扫", "rarity": RARITY_SS, "image": "ishmael_liu.png"},
    {"name": "N协会大剑", "sinner": "罗佳", "rarity": RARITY_SS, "image": "rodya_n_corp.png"},
    {"name": "南部夜叉刘氏事务所", "sinner": "辛克莱", "rarity": RARITY_SS, "image": "sinclair_liu.png"},
    {"name": "迪耶奇协会", "sinner": "奥提斯", "rarity": RARITY_SS, "image": "outis_dieci.png"},
    {"name": "N协会大锤", "sinner": "桂", "rarity": RARITY_SS, "image": "gregor_n_corp.png"},
    
    # === S 稀有度人格 (0) ===
    {"name": "雅格布事务所", "sinner": "以实玛利", "rarity": RARITY_S, "image": "yi_sang_yageob.png"},
    {"name": "雅格布事务所", "sinner": "浮士德", "rarity": RARITY_S, "image": "faust_yageob.png"},
    {"name": "雅格布事务所", "sinner": "堂吉诃德", "rarity": RARITY_S, "image": "don_quixote_yageob.png"},
    {"name": "雅格布事务所", "sinner": "良秀", "rarity": RARITY_S, "image": "ryoshu_yageob.png"},
    {"name": "雅格布事务所", "sinner": "默尔索", "rarity": RARITY_S, "image": "meursault_yageob.png"},
    {"name": "雅格布事务所", "sinner": "鸿璐", "rarity": RARITY_S, "image": "hong_lu_yageob.png"},
    {"name": "雅格布事务所", "sinner": "希斯克利夫", "rarity": RARITY_S, "image": "heathcliff_yageob.png"},
    {"name": "雅格布事务所", "sinner": "以扫", "rarity": RARITY_S, "image": "ishmael_yageob.png"},
    {"name": "雅格布事务所", "sinner": "罗佳", "rarity": RARITY_S, "image": "rodya_yageob.png"},
    {"name": "雅格布事务所", "sinner": "辛克莱", "rarity": RARITY_S, "image": "sinclair_yageob.png"},
    {"name": "雅格布事务所", "sinner": "奥提斯", "rarity": RARITY_S, "image": "outis_yageob.png"},
    {"name": "雅格布事务所", "sinner": "桂", "rarity": RARITY_S, "image": "gregor_yageob.png"},
]


def get_identities_by_rarity(rarity: str) -> list:
    """根据稀有度获取人格列表"""
    return [i for i in IDENTITIES if i["rarity"] == rarity]


def get_all_identities() -> list:
    """获取所有人格列表"""
    return IDENTITIES


def get_rarity_display(rarity: str) -> str:
    """获取稀有度显示文本"""
    display_map = {
        RARITY_SSS: "★★★ (000)",
        RARITY_SS: "★★ (00)",
        RARITY_S: "★ (0)",
    }
    return display_map.get(rarity, rarity)
