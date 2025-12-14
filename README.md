# 边狱巴士人格抽取插件

AstrBot 的边狱巴士（Limbus Company）人格抽取模拟插件。

## 功能特性

- 🎲 **单抽模式**：模拟单次人格抽取
- 🎰 **十连模式**：模拟十连抽取
- 🖼️ **头像展示**：抽取后显示人格头像图片（需自行添加图片资源）
- ⭐ **稀有度系统**：
  - ★★★ (000/SSS): 3% 概率
  - ★★ (00/SS): 12% 概率
  - ★ (0/S): 85% 概率

## 使用方法

### 指令列表

| 指令 | 说明 |
|------|------|
| `/limbus单抽` | 进行单次人格抽取 |
| `/limbus抽卡` | 单抽的别名指令 |
| `/limbus十连` | 进行十连抽取 |

## 安装

1. 将此插件放置到 AstrBot 的插件目录
2. 重启 AstrBot 或热重载插件

## 图片资源配置

插件支持显示人格头像图片，但图片资源需要自行添加。

### 添加图片步骤

1. 在插件目录下的 `images/` 文件夹中添加图片文件
2. 图片文件名需与 `identities.py` 中定义的 `image` 字段对应

### 图片命名规范

```
{罪人英文名}_{人格标识}.png
```

例如：
- `yi_sang_lcb.png` - 以实玛利 LCB囚人
- `faust_lcb.png` - 浮士德 LCB囚人
- `don_quixote_w3.png` - 堂吉诃德 W协会3科

### 推荐图片规格

- 格式：PNG（透明背景）
- 尺寸：200x200 或 256x256 像素
- 文件大小：建议不超过 500KB

### 默认图片

如需设置默认占位图片（当指定人格图片不存在时显示），请创建 `images/default.png` 文件。

## 自定义人格池

如需添加或修改人格，请编辑 `identities.py` 文件：

```python
# 人格数据格式
{
    "name": "人格名称",
    "sinner": "罪人名称",
    "rarity": RARITY_SSS,  # 稀有度：RARITY_SSS / RARITY_SS / RARITY_S
    "image": "图片文件名.png"
}
```

## 支持

- [AstrBot 帮助文档](https://astrbot.app)
- [插件开发文档](https://docs.astrbot.app/dev/star/plugin-new.html)

## 许可证

MIT License
