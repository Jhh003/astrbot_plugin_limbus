# -*- coding: utf-8 -*-
"""
边狱巴士（Limbus Company）人格数据文件
此文件包含所有可抽取的人格信息和图片路径配置

图片资源说明：
1. 图片需放置在 images/{罪人英文名}/ 目录下
2. 图片命名格式：{罪人英文名}-{人格标识}.webp 或 .jpg
3. 例如：Yi_Sang/Yi_Sang-LCB.jpg, Faust/Faust-LCB.jpg
"""

# 稀有度等级定义
RARITY_SSS = "SSS"  # 000 人格 (3星)
RARITY_SS = "SS"    # 00 人格 (2星)
RARITY_S = "S"      # 0 人格 (1星)

# 稀有度对应的抽取概率（百分比）
RARITY_RATES = {
    RARITY_SSS: 2.9,   # 2.9% 概率抽到 SSS(000) 人格
    RARITY_SS: 12.8,   # 12.8% 概率抽到 SS(00) 人格
    RARITY_S: 81.7,    # 81.7% 概率抽到 S(0) 人格
}

# 十连保底概率（第10次必为00或00以上）
PITY_RATES = {
    RARITY_SSS: 2.98,   # 保底时000概率2.98% (实际游戏中约为2.9%/97.4% ≈ 2.98%)
    RARITY_SS: 97.02,   # 保底时00概率97.02% (实际游戏中约为94.5%/97.4% ≈ 97.02%)
}

# 图片资源目录路径（相对于插件目录）
IMAGES_DIR = "images"

# 默认占位图片（当人格图片不存在时使用）
DEFAULT_IMAGE = "default.png"

# 罪人列表
SINNERS = [
    "李箱",        # Yi Sang
    "浮士德",      # Faust
    "堂吉诃德",    # Don Quixote
    "良秀",        # Ryoshu
    "默尔索",      # Meursault
    "鸿璐",        # Hong Lu
    "希斯克利夫",  # Heathcliff
    "以实玛利",    # Ishmael
    "罗佳",        # Rodion
    "辛克莱",      # Sinclair
    "格里高尔",    # Gregor
    "奥提斯",      # Outis
]

# 人格数据列表
# 格式：{"name": 人格名称, "sinner": 罪人名称, "rarity": 稀有度, "image": 图片文件名}
IDENTITIES = [
    # === 李箱 (Yi Sang) ===
    {"name": "W公司3级清扫人员", "sinner": "李箱", "rarity": RARITY_SSS, "image": "Yi_Sang/Yi_Sang-W3.webp"},
    {"name": "Seven协会南部6科", "sinner": "李箱", "rarity": RARITY_SS, "image": "Yi_Sang/Yi_Sang-Seven.jpg"},
    {"name": "N公司E.G.O:凶弹", "sinner": "李箱", "rarity": RARITY_SSS, "image": "Yi_Sang/Yi_Sang-N.webp"},
    {"name": "LCE E.G.O:提灯", "sinner": "李箱", "rarity": RARITY_SS, "image": "Yi_Sang/Yi_Sang-LCE.webp"},
    {"name": "LCB罪人", "sinner": "李箱", "rarity": RARITY_S, "image": "Yi_Sang/Yi_Sang-LCB.jpg"},
    {"name": "Dieci协会南部4科", "sinner": "李箱", "rarity": RARITY_SS, "image": "Yi_Sang/Yi_Sang-Dieci.webp"},
    {"name": "绽放E.G.O:山茶花", "sinner": "李箱", "rarity": RARITY_SSS, "image": "Yi_Sang/Yi_Sang-hua_xiang.webp"},
    {"name": "裴廓德号大副", "sinner": "李箱", "rarity": RARITY_SS, "image": "Yi_Sang/Yi_Sang-da_fu.webp"},
    {"name": "脑叶公司E.G.O:庄严哀悼", "sinner": "李箱", "rarity": RARITY_SSS, "image": "Yi_Sang/Yi_Sang-ai_dao.webp"},
    {"name": "六协会南部3科", "sinner": "李箱", "rarity": RARITY_SSS, "image": "Yi_Sang/Yi_Sang-6.webp"},
    {"name": "臼齿事务所收尾人", "sinner": "李箱", "rarity": RARITY_SS, "image": "Yi_Sang/Yi_Sang-jiu_chi.webp"},
    {"name": "剑契组杀手", "sinner": "李箱", "rarity": RARITY_SSS, "image": "Yi_Sang/Yi_Sang-jian_qi.webp"},
    {"name": "环指点彩派学徒", "sinner": "李箱", "rarity": RARITY_SSS, "image": "Yi_Sang/Yi_Sang-huan_zhi.webp"},
    {"name": "黑兽-午魁首", "sinner": "李箱", "rarity": RARITY_SSS, "image": "Yi_Sang/Yi_Sang-ma.webp"},

    # === 浮士德 (Faust) ===
    {"name": "し协会东部3科", "sinner": "浮士德", "rarity": RARITY_SSS, "image": "Faust/Faust-し.webp"},
    {"name": "Zwei协会南部4科", "sinner": "浮士德", "rarity": RARITY_SS, "image": "Faust/Faust-Zwei.webp"},
    {"name": "W公司2级清扫人员", "sinner": "浮士德", "rarity": RARITY_SS, "image": "Faust/Faust-W.webp"},
    {"name": "Seven协会南部4科", "sinner": "浮士德", "rarity": RARITY_SSS, "image": "Faust/Faust-Seven.webp"},
    {"name": "LCE_E.G.O:红艳煞", "sinner": "浮士德", "rarity": RARITY_SSS, "image": "Faust/Faust-LCE.webp"},
    {"name": "LCB罪人", "sinner": "浮士德", "rarity": RARITY_S, "image": "Faust/Faust-LCB.jpg"},
    {"name": "执柄者", "sinner": "浮士德", "rarity": RARITY_SSS, "image": "Faust/Faust-N.webp"},
    {"name": "脑叶公司E.G.O:悔恨", "sinner": "浮士德", "rarity": RARITY_SSS, "image": "Faust/Faust-L.webp"},
    {"name": "脑叶公司幸存者", "sinner": "浮士德", "rarity": RARITY_SS, "image": "Faust/Faust-L2.webp"},
    {"name": "剑契组杀手", "sinner": "浮士德", "rarity": RARITY_SSS, "image": "Faust/Faust-jian_qi.webp"},
    {"name": "呼啸山庄管家", "sinner": "浮士德", "rarity": RARITY_SS, "image": "Faust/Faust-guan_jia.webp"},
    {"name": "黑兽-卯魁首", "sinner": "浮士德", "rarity": RARITY_SSS, "image": "Faust/Faust-tu.webp"},
    {"name": "多裂纹事务所代表", "sinner": "浮士德", "rarity": RARITY_SSS, "image": "Faust/Faust-duo_lie.webp"},

    # === 堂吉诃德 (Don Quixote) ===
    {"name": "し协会南部5科科长", "sinner": "堂吉诃德", "rarity": RARITY_SS, "image": "Don_Quixote/Don_Quixote-し.webp"},
    {"name": "W公司3级清扫人员", "sinner": "堂吉诃德", "rarity": RARITY_SSS, "image": "Don_Quixote/Don_Quixote-W.webp"},
    {"name": "T公司3级征收人员", "sinner": "堂吉诃德", "rarity": RARITY_SSS, "image": "Don_Quixote/Don_Quixote-T.webp"},
    {"name": "N公司中锤", "sinner": "堂吉诃德", "rarity": RARITY_SS, "image": "Don_Quixote/Don_Quixote-N.webp"},
    {"name": "LCB罪人", "sinner": "堂吉诃德", "rarity": RARITY_S, "image": "Don_Quixote/Don_Quixote-LCB.jpg"},
    {"name": "Cinq协会南部5科科长", "sinner": "堂吉诃德", "rarity": RARITY_SSS, "image": "Don_Quixote/Don_Quixote-Cinq.webp"},
    {"name": "Cinq协会东部3科", "sinner": "堂吉诃德", "rarity": RARITY_SSS, "image": "Don_Quixote/Don_Quixote-Cinq2.webp"},
    {"name": "中指幼妹", "sinner": "堂吉诃德", "rarity": RARITY_SSS, "image": "Don_Quixote/Don_Quixote-zhong_zhi.webp"},
    {"name": "脑叶公司E.G.O:以爱与憎之名", "sinner": "堂吉诃德", "rarity": RARITY_SSS, "image": "Don_Quixote/Don_Quixote-zeng_wu.webp"},
    {"name": "脑叶公司E.G.O:提灯", "sinner": "堂吉诃德", "rarity": RARITY_SS, "image": "Don_Quixote/Don_Quixote-L.webp"},
    {"name": "拉·曼却领总督", "sinner": "堂吉诃德", "rarity": RARITY_SSS, "image": "Don_Quixote/Don_Quixote-xue_tang.webp"},
    {"name": "剑契组杀手", "sinner": "堂吉诃德", "rarity": RARITY_SS, "image": "Don_Quixote/Don_Quixote-jian_qi.webp"},
    {"name": "黑兽-未", "sinner": "堂吉诃德", "rarity": RARITY_SSS, "image": "Don_Quixote/Don_Quixote-yang.webp"},

    # === 良秀 (Ryoshu) ===
    {"name": "W公司3级清扫人员", "sinner": "良秀", "rarity": RARITY_SSS, "image": "Ryoshu/Ryoshu-W.webp"},
    {"name": "Seven协会南部6科", "sinner": "良秀", "rarity": RARITY_SS, "image": "Ryoshu/Ryoshu-Seven.webp"},
    {"name": "N公司E.G.O:轻蔑，敬畏", "sinner": "良秀", "rarity": RARITY_SSS, "image": "Ryoshu/Ryoshu-N.webp"},
    {"name": "LCCB系长", "sinner": "良秀", "rarity": RARITY_SS, "image": "Ryoshu/Ryoshu-LCCB.webp"},
    {"name": "LCB罪人", "sinner": "良秀", "rarity": RARITY_S, "image": "Ryoshu/Ryoshu-LCB.jpg"},
    {"name": "脑叶公司E.G.O:赤瞳·忏悔", "sinner": "良秀", "rarity": RARITY_SSS, "image": "Ryoshu/Ryoshu-L.webp"},
    {"name": "六协会南部4科", "sinner": "良秀", "rarity": RARITY_SS, "image": "Ryoshu/Ryoshu-6.webp"},
    {"name": "良·派厨师长", "sinner": "良秀", "rarity": RARITY_SSS, "image": "Ryoshu/Ryoshu-chu_shi.webp"},
    {"name": "鸿园的流浪武者", "sinner": "良秀", "rarity": RARITY_SSS, "image": "Ryoshu/Ryoshu-dai_yv.webp"},
    {"name": "黑云会若众", "sinner": "良秀", "rarity": RARITY_SSS, "image": "Ryoshu/Ryoshu-hei_yun.webp"},
    {"name": "黑兽-卯", "sinner": "良秀", "rarity": RARITY_SSS, "image": "Ryoshu/Ryoshu-tu.webp"},
    {"name": "埃德加家族首席管家", "sinner": "良秀", "rarity": RARITY_SSS, "image": "Ryoshu/Ryoshu-ai_dejia.webp"},
    {"name": "20区圣愚", "sinner": "良秀", "rarity": RARITY_SS, "image": "Ryoshu/Ryoshu-sheng_yv.webp"},

    # === 默尔索 (Meursault) ===
    {"name": "W公司2级清扫人员", "sinner": "默尔索", "rarity": RARITY_SSS, "image": "Meursault/Meursault-W.webp"},
    {"name": "R公司第四集团军犀牛队", "sinner": "默尔索", "rarity": RARITY_SSS, "image": "Meursault/Meursault-R.webp"},
    {"name": "N公司大锤", "sinner": "默尔索", "rarity": RARITY_SSS, "image": "Meursault/Meursault-N.webp"},
    {"name": "LCB罪人", "sinner": "默尔索", "rarity": RARITY_S, "image": "Meursault/Meursault-LCB.jpg"},
    {"name": "Dieci协会南部4科科长", "sinner": "默尔索", "rarity": RARITY_SSS, "image": "Meursault/Meursault-Dieci.webp"},
    {"name": "Cinq协会西部3科", "sinner": "默尔索", "rarity": RARITY_SSS, "image": "Meursault/Meursault-Cinq.webp"},
    {"name": "中指幼弟", "sinner": "默尔索", "rarity": RARITY_SS, "image": "Meursault/Meursault-zhong_zhi.webp"},
    {"name": "死兔帮老大", "sinner": "默尔索", "rarity": RARITY_SS, "image": "Meursault/Meursault-si_tu.webp"},
    {"name": "拇指东部指挥官IIII", "sinner": "默尔索", "rarity": RARITY_SSS, "image": "Meursault/Meursault-lei_heng.webp"},
    {"name": "玫瑰扳手工坊收尾人", "sinner": "默尔索", "rarity": RARITY_SS, "image": "Meursault/Meursault-mei_gui.webp"},
    {"name": "六协会南部6科", "sinner": "默尔索", "rarity": RARITY_SS, "image": "Meursault/Meursault-6.webp"},
    {"name": "拉·曼却领王子", "sinner": "默尔索", "rarity": RARITY_SSS, "image": "Meursault/Meursault-la_manque.webp"},
    {"name": "剑契组头领", "sinner": "默尔索", "rarity": RARITY_SSS, "image": "Meursault/Meursault-jian_qi.webp"},

    # === 鸿璐 (Hong Lu) ===
    {"name": "W公司2级清扫人员", "sinner": "鸿璐", "rarity": RARITY_SS, "image": "Hong_Lu/Hong_Lu-W.webp"},
    {"name": "R公司第四集团军驯鹿队", "sinner": "鸿璐", "rarity": RARITY_SSS, "image": "Hong_Lu/Hong_Lu-R.webp"},
    {"name": "LCB罪人", "sinner": "鸿璐", "rarity": RARITY_S, "image": "Hong_Lu/Hong_Lu-LCB.jpg"},
    {"name": "K公司3级摘除人员", "sinner": "鸿璐", "rarity": RARITY_SSS, "image": "Hong_Lu/Hong_Lu-K.webp"},
    {"name": "Dieci协会南部4科", "sinner": "鸿璐", "rarity": RARITY_SSS, "image": "Hong_Lu/Hong_Lu-Dieci.webp"},
    {"name": "六协会南部5科", "sinner": "鸿璐", "rarity": RARITY_SS, "image": "Hong_Lu/Hong_Lu-6.webp"},
    {"name": "猎牙事务所收尾人", "sinner": "鸿璐", "rarity": RARITY_SS, "image": "Hong_Lu/Hong_Lu-lie_ya.webp"},
    {"name": "句点事务所代表", "sinner": "鸿璐", "rarity": RARITY_SSS, "image": "Hong_Lu/Hong_Lu-ju_dian.webp"},
    {"name": "鸿园的君主", "sinner": "鸿璐", "rarity": RARITY_SSS, "image": "Hong_Lu/Hong_Lu-jun_zhu.webp"},
    {"name": "黑云会若众", "sinner": "鸿璐", "rarity": RARITY_SS, "image": "Hong_Lu/Hong_Lu-hei_yun.webp"},
    {"name": "豆豆帮帮主", "sinner": "鸿璐", "rarity": RARITY_SSS, "image": "Hong_Lu/Hong_Lu-dou_dou.webp"},
    {"name": "吊钩事务所收尾人", "sinner": "鸿璐", "rarity": RARITY_SS, "image": "Hong_Lu/Hong_Lu-diao_gou.webp"},
    {"name": "20区圣愚", "sinner": "鸿璐", "rarity": RARITY_SSS, "image": "Hong_Lu/Hong_Lu-sheng_yv.webp"},

    # === 希斯克利夫 (Heathcliff) ===
    {"name": "し协会南部5科", "sinner": "希斯克利夫", "rarity": RARITY_SS, "image": "Heathcliff/Heathcliff-し.webp"},
    {"name": "W公司4级清扫人员-CCA", "sinner": "希斯克利夫", "rarity": RARITY_SSS, "image": "Heathcliff/Heathcliff-W.webp"},
    {"name": "Seven协会南部4科", "sinner": "希斯克利夫", "rarity": RARITY_SS, "image": "Heathcliff/Heathcliff-Seven.webp"},
    {"name": "R公司第四集团军兔子队", "sinner": "希斯克利夫", "rarity": RARITY_SSS, "image": "Heathcliff/Heathcliff-R.webp"},
    {"name": "Öufi协会南部3科", "sinner": "希斯克利夫", "rarity": RARITY_SSS, "image": "Heathcliff/Heathcliff-Öufi.webp"},
    {"name": "N公司小锤", "sinner": "希斯克利夫", "rarity": RARITY_SS, "image": "Heathcliff/Heathcliff-N.webp"},
    {"name": "LCB罪人", "sinner": "希斯克利夫", "rarity": RARITY_S, "image": "Heathcliff/Heathcliff-LCB.jpg"},
    {"name": "裴廓德号鱼叉手", "sinner": "希斯克利夫", "rarity": RARITY_SSS, "image": "Heathcliff/Heathcliff-pai_dehao.webp"},
    {"name": "脑叶公司E.G.O:狐雨", "sinner": "希斯克利夫", "rarity": RARITY_SSS, "image": "Heathcliff/Heathcliff-san.webp"},
    {"name": "狂猎", "sinner": "希斯克利夫", "rarity": RARITY_SSS, "image": "Heathcliff/Heathcliff-kang_lie.webp"},
    {"name": "句点事务所收尾人", "sinner": "希斯克利夫", "rarity": RARITY_SSS, "image": "Heathcliff/Heathcliff-ju_dian.webp"},
    {"name": "黑云会若众", "sinner": "希斯克利夫", "rarity": RARITY_SSS, "image": "Heathcliff/Heathcliff-hei_yun.webp"},
    {"name": "黑兽-酉魁首", "sinner": "希斯克利夫", "rarity": RARITY_SSS, "image": "Heathcliff/Heathcliff-ji.webp"},
    {"name": "多裂纹事务所收尾人", "sinner": "希斯克利夫", "rarity": RARITY_SS, "image": "Heathcliff/Heathcliff-duo_liewen.webp"},

    # === 以实玛利 (Ishmael) ===
    {"name": "し协会南部5科", "sinner": "以实玛利", "rarity": RARITY_SS, "image": "Ishmael/Ishmael-し.webp"},
    {"name": "Zwei协会西部3科", "sinner": "以实玛利", "rarity": RARITY_SSS, "image": "Ishmael/Ishmael-Zwei.webp"},
    {"name": "R公司第四集团军驯鹿队", "sinner": "以实玛利", "rarity": RARITY_SSS, "image": "Ishmael/Ishmael-R.webp"},
    {"name": "LCCB系长", "sinner": "以实玛利", "rarity": RARITY_SS, "image": "Ishmael/Ishmael-LCCB.webp"},
    {"name": "LCB罪人", "sinner": "以实玛利", "rarity": RARITY_S, "image": "Ishmael/Ishmael-LCB.jpg"},
    {"name": "裴廓德号船长", "sinner": "以实玛利", "rarity": RARITY_SSS, "image": "Ishmael/Ishmael-fei_dehao.webp"},
    {"name": "脑叶公司E.G.O:荡漾", "sinner": "以实玛利", "rarity": RARITY_SS, "image": "Ishmael/Ishmael-dang_yang.webp"},
    {"name": "六协会南部4科", "sinner": "以实玛利", "rarity": RARITY_SSS, "image": "Ishmael/Ishmael-6.webp"},
    {"name": "臼齿修船厂收尾人", "sinner": "以实玛利", "rarity": RARITY_SSS, "image": "Ishmael/Ishmael-jiu_chi.webp"},
    {"name": "家主候选人", "sinner": "以实玛利", "rarity": RARITY_SSS, "image": "Ishmael/Ishmael-jia_zhu.webp"},
    {"name": "黑云会副会长", "sinner": "以实玛利", "rarity": RARITY_SSS, "image": "Ishmael/Ishmael-hei_yun.webp"},
    {"name": "定事务所代表", "sinner": "以实玛利", "rarity": RARITY_SSS, "image": "Ishmael/Ishmael-ding.webp"},
    {"name": "埃德加家族管家", "sinner": "以实玛利", "rarity": RARITY_SS, "image": "Ishmael/Ishmael-ai_dejia.webp"},

    # === 罗佳 (Rodion) ===
    {"name": "Девять协会北部3科", "sinner": "罗佳", "rarity": RARITY_SSS, "image": "Rodion/Rodion-Девять.webp"},
    {"name": "Zwei协会南部5科", "sinner": "罗佳", "rarity": RARITY_SS, "image": "Rodion/Rodion-Zwei.webp"},
    {"name": "T公司2级征收人员", "sinner": "罗佳", "rarity": RARITY_SS, "image": "Rodion/Rodion-T.webp"},
    {"name": "N公司中锤", "sinner": "罗佳", "rarity": RARITY_SS, "image": "Rodion/Rodion-N.webp"},
    {"name": "LCCB系长", "sinner": "罗佳", "rarity": RARITY_SS, "image": "Rodion/Rodion-LCCB.webp"},
    {"name": "LCB罪人", "sinner": "罗佳", "rarity": RARITY_S, "image": "Rodion/Rodion-LCB.jpg"},
    {"name": "Dieci协会南部4科", "sinner": "罗佳", "rarity": RARITY_SSS, "image": "Rodion/Rodion-Dieci.webp"},
    {"name": "脑叶公司E.G.O:泪锋之剑", "sinner": "罗佳", "rarity": RARITY_SSS, "image": "Rodion/Rodion-lai_feng.webp"},
    {"name": "玫瑰扳手工坊代表", "sinner": "罗佳", "rarity": RARITY_SSS, "image": "Rodion/Rodion-mei_gui.webp"},
    {"name": "六协会南部4科科长", "sinner": "罗佳", "rarity": RARITY_SSS, "image": "Rodion/Rodion-6.webp"},
    {"name": "拉·曼却领公主", "sinner": "罗佳", "rarity": RARITY_SSS, "image": "Rodion/Rodion-la_manque.webp"},
    {"name": "黑云会若众", "sinner": "罗佳", "rarity": RARITY_SSS, "image": "Rodion/Rodion-hei_yun.webp"},
    {"name": "黑兽-巳", "sinner": "罗佳", "rarity": RARITY_SSS, "image": "Rodion/Rodion-she.webp"},

    # === 辛克莱 (Sinclair) ===
    {"name": "Девять协会北部3科", "sinner": "辛克莱", "rarity": RARITY_SSS, "image": "Sinclair/Sinclair-Девять.webp"},
    {"name": "Zwei协会西部3科", "sinner": "辛克莱", "rarity": RARITY_SS, "image": "Sinclair/Sinclair-Zwei.webp"},
    {"name": "Zwei协会南部6科", "sinner": "辛克莱", "rarity": RARITY_SS, "image": "Sinclair/Sinclair-Zwei2.webp"},
    {"name": "LCB罪人", "sinner": "辛克莱", "rarity": RARITY_S, "image": "Sinclair/Sinclair-LCB.jpg"},
    {"name": "Cinq协会南部4科科长", "sinner": "辛克莱", "rarity": RARITY_SSS, "image": "Sinclair/Sinclair-Cinq.webp"},
    {"name": "准执柄者", "sinner": "辛克莱", "rarity": RARITY_SSS, "image": "Sinclair/Sinclair-N.webp"},
    {"name": "中指幼弟", "sinner": "辛克莱", "rarity": RARITY_SSS, "image": "Sinclair/Sinclair-zhong_zhi.webp"},
    {"name": "脑叶公司E.G.O:朱符", "sinner": "辛克莱", "rarity": RARITY_SS, "image": "Sinclair/Sinclair-zhu_fu.webp"},
    {"name": "拇指东部士兵II", "sinner": "辛克莱", "rarity": RARITY_SSS, "image": "Sinclair/Sinclair-mu_zhi.webp"},
    {"name": "流浪乐队头目", "sinner": "辛克莱", "rarity": RARITY_SS, "image": "Sinclair/Sinclair-sha_chui.webp"},
    {"name": "黎明事务所收尾人", "sinner": "辛克莱", "rarity": RARITY_SSS, "image": "Sinclair/Sinclair-lin_ming.webp"},
    {"name": "臼齿修船厂收尾人", "sinner": "辛克莱", "rarity": RARITY_SS, "image": "Sinclair/Sinclair-jiu_chi.webp"},
    {"name": "剑契组杀手", "sinner": "辛克莱", "rarity": RARITY_SSS, "image": "Sinclair/Sinclair-jian_qi.webp"},
    {"name": "黑兽-酉", "sinner": "辛克莱", "rarity": RARITY_SSS, "image": "Sinclair/Sinclair-ji.webp"},

    # === 格里高尔 (Gregor) ===
    {"name": "Zwei协会南部4科", "sinner": "格里高尔", "rarity": RARITY_SSS, "image": "Gregor/Gregor-Zwei.webp"},
    {"name": "LCB罪人", "sinner": "格里高尔", "rarity": RARITY_S, "image": "Gregor/Gregor-LCB.jpg"},
    {"name": "G公司科长代理", "sinner": "格里高尔", "rarity": RARITY_SSS, "image": "Gregor/Gregor-G.webp"},
    {"name": "夜锥组队长", "sinner": "格里高尔", "rarity": RARITY_SSS, "image": "Gregor/Gregor-ye_zhui.webp"},
    {"name": "炎拳事务所幸存者", "sinner": "格里高尔", "rarity": RARITY_SSS, "image": "Gregor/Gregor-yan_quan.webp"},
    {"name": "双钩海盗团大副", "sinner": "格里高尔", "rarity": RARITY_SSS, "image": "Gregor/Gregor-shuang_gou.webp"},
    {"name": "玫瑰扳手工坊收尾人", "sinner": "格里高尔", "rarity": RARITY_SS, "image": "Gregor/Gregor-mei_gui.webp"},
    {"name": "六协会南部6科", "sinner": "格里高尔", "rarity": RARITY_SSS, "image": "Gregor/Gregor-6.webp"},
    {"name": "良·派帮厨", "sinner": "格里高尔", "rarity": RARITY_SS, "image": "Gregor/Gregor-liang.webp"},
    {"name": "拉·曼却领神父", "sinner": "格里高尔", "rarity": RARITY_SSS, "image": "Gregor/Gregor-la_manque.webp"},
    {"name": "黑云会副会长", "sinner": "格里高尔", "rarity": RARITY_SS, "image": "Gregor/Gregor-hei_yun.webp"},
    {"name": "黑兽-巳", "sinner": "格里高尔", "rarity": RARITY_SSS, "image": "Gregor/Gregor-she.webp"},
    {"name": "埃德加家族继承人", "sinner": "格里高尔", "rarity": RARITY_SSS, "image": "Gregor/Gregor-ai_dejia.webp"},

    # === 奥提斯 (Outis) ===
    {"name": "W公司3级清扫组长", "sinner": "奥提斯", "rarity": RARITY_SSS, "image": "Outis/Outis-W.webp"},
    {"name": "T公司3级强制征收人员", "sinner": "奥提斯", "rarity": RARITY_SSS, "image": "Outis/Outis-T.webp"},
    {"name": "Seven协会南部6科科长", "sinner": "奥提斯", "rarity": RARITY_SSS, "image": "Outis/Outis-Seven.webp"},
    {"name": "LCB罪人", "sinner": "奥提斯", "rarity": RARITY_S, "image": "Outis/Outis-LCB.jpg"},
    {"name": "G公司部长", "sinner": "奥提斯", "rarity": RARITY_SS, "image": "Outis/Outis-G.webp"},
    {"name": "Cinq协会南部4科", "sinner": "奥提斯", "rarity": RARITY_SS, "image": "Outis/Outis-Cinq.webp"},
    {"name": "脑叶公司E.G.O:魔弹", "sinner": "奥提斯", "rarity": RARITY_SSS, "image": "Outis/Outis-L.webp"},
    {"name": "拉·曼却领理发师", "sinner": "奥提斯", "rarity": RARITY_SSS, "image": "Outis/Outis-la_manque.webp"},
    {"name": "臼齿事务所收尾人", "sinner": "奥提斯", "rarity": RARITY_SSS, "image": "Outis/Outis-jiu_chi.webp"},
    {"name": "剑契组杀手", "sinner": "奥提斯", "rarity": RARITY_SS, "image": "Outis/Outis-jian_qi.webp"},
    {"name": "环指点彩派学徒", "sinner": "奥提斯", "rarity": RARITY_SS, "image": "Outis/Outis-huan_zhi.webp"},
    {"name": "呼啸山庄首席管家", "sinner": "奥提斯", "rarity": RARITY_SSS, "image": "Outis/Outis-hu_xiao.webp"},
    {"name": "黑兽-卯", "sinner": "奥提斯", "rarity": RARITY_SSS, "image": "Outis/Outis-tu.webp"},
]


def get_identities_by_rarity(rarity: str) -> list:
    """根据稀有度获取人格列表"""
    return [i for i in IDENTITIES if i["rarity"] == rarity]


def get_identities_by_sinner(sinner: str) -> list:
    """根据罪人获取人格列表"""
    return [i for i in IDENTITIES if i["sinner"] == sinner]


def get_all_identities() -> list:
    """获取所有人格列表"""
    return IDENTITIES


def get_rarity_display(rarity: str) -> str:
    """获取稀有度显示文本"""
    display_map = {
        RARITY_SSS: "★★★",
        RARITY_SS: "★★ ",
        RARITY_S: "★ ",
    }
    return display_map.get(rarity, rarity)
