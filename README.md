# 健康记录助手 - Android APP
## 📱 功能
- 用药记录（记录吃药时间和药名）
- 血压测量记录（收缩压/舒张压）
- 血糖测量记录（数值和时间）
- 拍照保存检查结果
## 🚀 GitHub Actions 打包步骤
### 1️⃣ 上传文件到 GitHub
将以下文件上传到 GitHub 仓库：
- `simple_app.py` - APP 主程序
- `buildozer.spec` - 打包配置
- `requirements.txt` - Python 依赖
- `.github/workflows/android-build.yml` - **GitHub Actions 配置**
### 2️⃣ 触发打包
1. 在仓库页面点击 **Actions** 标签
2. 左侧点击 **Build Android APK**
3. 右侧点击 **Run workflow** → 绿色按钮
### 3️⃣ 等待并下载
1. 等待 **20-30 分钟** ⏳
2. 打包完成后，点击这次运行记录
3. 在 **Artifacts** 部分下载 **health-record-apk.zip**
4. 解压得到 APK 文件，传到手机安装即可！📱
