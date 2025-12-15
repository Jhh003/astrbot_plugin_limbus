# 边狱巴士人格抽取插件

AstrBot 的边狱巴士（Limbus Company）人格抽取模拟插件。

## 功能特性

- 🎲 **单抽模式**：模拟单次人格抽取
- 🎰 **十连模式**：模拟十连抽取（2行5列网格布局）
- 🖼️ **头像展示**：抽取后显示人格头像图片（需自行添加图片资源）
- ⭐ **稀有度系统**：
  - ★★★ (000/SSS): 2.9% 概率
  - ★★ (00/SS): 12.8% 概率
  - ★ (0/S): 81.7% 概率
- 🎯 **十连保底**：第10次必出00或00以上
- 📊 **运气指数**：非酋/欧皇指数评测系统
- 🎱 **多卡池支持**：支持常驻池和罪人专属池切换
- ⚙️ **高度可配置**：通过 config.yaml 自定义概率、卡池等

## 使用方法

### 指令列表

| 指令 | 说明 |
|------|------|
| `/tq单抽` | 进行单次人格抽取 |
| `/tq抽卡` | 单抽的别名指令 |
| `/tq十连` | 进行十连抽取 |
| `/tq非酋指数` | 查看非酋评级（距离上次★★★的抽数） |
| `/tq欧皇指数` | 查看欧皇评级（最近★★★出率） |
| `/tq池列表` | 查看可用卡池列表 |
| `/tq切池 池名` | 切换到指定卡池 |

### 十连展示效果

十连结果采用精简展示：
- 第一行：标题
- 第二行：统计（★★★×N | ★★×N | ★×N）
- 分割线
- 仅显示★★★的详细信息
- 其余低星简写为"其余X个为★★/★人格"
- 图片采用2行5列网格布局

## 安装

1. 将此插件放置到 AstrBot 的插件目录
2. 重启 AstrBot 或热重载插件

## 配置说明

插件支持通过 `config.yaml` 文件进行配置，无需修改代码即可调整参数。

### 配置文件位置

`config.yaml` 位于插件根目录。

### 可配置项

```yaml
# 稀有度概率配置 (%)
rarity_rates:
  SSS: 2.9     # 000 人格概率
  SS: 12.8     # 00 人格概率
  S: 81.7      # 0 人格概率

# 十连保底配置
pity:
  enabled: true           # 是否开启十连保底
  guarantee_rarity: "SS"  # 保底最低稀有度
  pity_rates:             # 保底时的概率分布
    SSS: 2.98
    SS: 97.02

# 卡池配置
pools:
  常驻池:
    enabled: true
    description: "包含所有可抽取人格"
    filter: null
  
  李箱专属池:
    enabled: true
    description: "只包含李箱的人格"
    filter:
      type: "sinner"
      value: "李箱"

# 默认卡池
default_pool: "常驻池"

# 图片布局配置
image:
  ten_pull_layout:
    rows: 2           # 行数
    cols: 5           # 每行列数
    spacing: 5        # 间距
    target_height: 120  # 图片高度
```

## 图片资源配置

插件支持显示人格头像图片，但图片资源需要自行添加。

### 添加图片步骤

1. 在插件目录下的 `images/` 文件夹中添加图片文件
2. 图片文件名需与 `identities.py` 中定义的 `image` 字段对应

### 图片命名规范

```
{罪人英文名}/{罪人英文名}-{人格标识}.webp
```

例如：
- `Yi_Sang/Yi_Sang-LCB.jpg` - 李箱 LCB囚人
- `Faust/Faust-LCB.jpg` - 浮士德 LCB囚人
- `Don_Quixote/Don_Quixote-W.webp` - 堂吉诃德 W公司

### 推荐图片规格

- 格式：PNG/WebP/JPG
- 尺寸：建议 120x120 或更大
- 文件大小：建议不超过 500KB

### 默认图片

如需设置默认占位图片（当指定人格图片不存在时显示），请创建 `images/default.png` 文件。

## 模块结构

插件采用模块化设计，便于维护和扩展：

```
astrbot_plugin_limbus/
├── main.py          # 主插件入口
├── identities.py    # 人格数据池
├── gacha_core.py    # 抽卡核心逻辑
├── render_text.py   # 文字排版模块
├── render_image.py  # 图片合成模块
├── config.yaml      # 配置文件
└── images/          # 图片资源目录
```

## 自定义人格池

如需添加或修改人格，请编辑 `identities.py` 文件：

```python
# 人格数据格式
{
    "name": "人格名称",
    "sinner": "罪人名称",
    "rarity": RARITY_SSS,  # 稀有度：RARITY_SSS / RARITY_SS / RARITY_S
    "image": "罪人英文名/罪人英文名-标识.webp"
}
```

## 支持

- [AstrBot 帮助文档](https://astrbot.app)
- [插件开发文档](https://docs.astrbot.app/dev/star/plugin-new.html)

## 许可证

MIT License
