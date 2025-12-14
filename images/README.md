# 图片资源目录

此目录用于存放边狱巴士人格头像图片资源。

## 图片命名规范

图片文件名需与 `identities.py` 中定义的 `image` 字段对应。

### 命名格式
```
{罪人英文名}_{人格标识}.png
```

### 示例文件名
- `yi_sang_lcb.png` - 以实玛利 LCB囚人
- `faust_lcb.png` - 浮士德 LCB囚人
- `don_quixote_lcb.png` - 堂吉诃德 LCB囚人
- `yi_sang_feather.png` - 以实玛利 刺客翎羽事务所
- `faust_7_section3.png` - 浮士德 七色协会西部支部3科

## 推荐图片规格
- 格式：PNG（透明背景）
- 尺寸：200x200 像素或 256x256 像素
- 文件大小：建议不超过 500KB

## 默认图片
如果需要设置默认占位图片（当指定人格图片不存在时显示），请创建：
- `default.png` - 默认占位图片

## 文件列表参考

完整的图片文件名列表请参考 `identities.py` 文件中各人格的 `image` 字段。
