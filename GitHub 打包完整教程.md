# 🚀 GitHub Actions 自动打包 Android APK 完整教程
## 📋 准备工作（5 分钟）
### 1. 注册 GitHub 账号
- 打开 https://github.com
- 点击右上角 "Sign up"
- 用邮箱注册一个免费账号
### 2. 创建新仓库
1. 登录后点击右上角 "+" → "New repository"
2. 仓库名称填：`health-record-app`
3. 选择 "Public"（公开）或 "Private"（私有）都可以
4. **不要勾选** "Add a README file"
5. 点击 "Create repository"
---
## 📤 上传代码（2 种方法）
### 方法一：网页直接上传（推荐新手）
1. 在刚创建的仓库页面，点击 "uploading an existing file"
2. 把下面这些文件拖进去：
   - `main.py`
   - `buildozer.spec`
   - `requirements.txt`
   - `.github/workflows/build-apk.yml`（这个最重要！）
   
> 💡 提示：`.github` 是隐藏文件夹，需要先解压 `health-record-app-full.zip` 才能看到
3. 在底部 "Commit changes" 框里随便写点啥，比如 "Initial commit"
4. 点击绿色按钮 "Commit changes"
### 方法二：用 Git 命令（如果您会的话）
```bash
cd C:\Users\Administrator\aipywork\CayhBYUGkawrGZR2LVmrJ
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/您的用户名/health-record-app.git
git push -u origin main
```
---
## ⚙️ 开始自动打包
### 1. 触发构建
上传完成后，GitHub 会**自动开始打包**！您也可以手动触发：
1. 点击仓库顶部的 "**Actions**" 标签
2. 左侧选择 "**Build Android APK with Buildozer**"
3. 右侧点击 "**Run workflow**" 绿色按钮
4. 在下拉菜单中选择分支（main），再点击 "Run workflow"
### 2. 等待打包完成
- 第一次打包需要 **20-30 分钟**（因为要下载 Android SDK、NDK 等工具）
- 后续打包会快很多（5-10 分钟）
- 您可以看到实时日志，就像看直播一样 😄
### 3. 下载 APK
打包成功后：
1. 在 Actions 页面点击最新的那次构建记录
2. 拉到页面最底部，找到 "**Artifacts**" 区域
3. 点击 "**health-record-app-apk**" 下载
4. 下载的是一个 ZIP 文件，解压后就是 `.apk` 文件啦！
---
## 📱 安装到手机
1. 把下载的 APK 文件传到安卓手机（微信文件传输助手、QQ、数据线都行）
2. 在手机上找到这个文件，点击安装
3. 如果提示 "未知来源"，去设置里允许安装未知来源应用就行
4. 安装完成！打开就能用了！
---
## 🎯 项目文件说明
| 文件 | 作用 | 必须吗？ |
|------|------|----------|
| `main.py` | APP 主程序（健康记录功能全在这里） | ✅ 必须 |
| `buildozer.spec` | Android 打包配置 | ✅ 必须 |
| `requirements.txt` | Python 依赖列表 | ✅ 必须 |
| `.github/workflows/build-apk.yml` | GitHub 自动打包配置 | ✅ 必须 |
| `README.md` | 项目说明文档 | ❌ 可选 |
| `使用说明.md` | 中文使用指南 | ❌ 可选 |
---
## ❓ 常见问题
### Q1: 打包失败了怎么办？
**A:** 
1. 先看看错误日志（红色的部分）
2. 最常见的原因是网络问题，重新点一次 "Re-run jobs" 就好
3. 如果还是不行，检查一下 `buildozer.spec` 配置对不对
### Q2: 安装时提示 "解析包时出现问题"？
**A:** 
- 可能是手机 Android 版本太低，这个 APP 需要 Android 5.0 以上
- 或者 APK 没下载完整，重新下载一次
### Q3: 能自定义 APP 图标吗？
**A:** 
可以！在 `buildozer.spec` 里改这两行：
```ini
icon.filename = myicon.png
splash.image = splash.png
```
然后把 `myicon.png` 和 `splash.png` 一起上传到 GitHub 就行
### Q4: 打包太慢了能不能加速？
**A:** 
- 第一次慢是正常的，后面会快很多
- GitHub 免费版每月有 2000 分钟构建时间，够用的
- 如果想更快，可以考虑 GitHub Pro 或其他 CI 服务
---
## 🎉 大功告成！
现在您已经掌握了用 GitHub 免费打包 Android APP 的技能！
每次修改代码后：
1. 上传到 GitHub
2. 自动打包（或手动点一下）
3. 下载新版本的 APK
4. 安装到手机测试
是不是超级简单？！👍
---
**技术支持**: 有任何问题随时问我！