@echo off
chcp 65001 >nul
echo ==========================================
echo 🔧 WSL 修复和 APK 打包工具
echo ==========================================
echo.
:: 检查 WSL 是否可用
wsl --version >nul 2>&1
if errorlevel 1 (
    echo ❌ WSL 未安装，请先安装 WSL
    echo 在 PowerShell(管理员) 执行：wsl --install
    pause
    exit /b 1
)
echo ✅ WSL 已安装
:: 询问是否要修复 WSL
echo.
set /p repair="是否要修复/重置 WSL Ubuntu? (Y/N): "
if /i "%repair%"=="Y" (
    echo.
    echo 🔄 正在卸载旧的 Ubuntu...
    wsl --unregister Ubuntu-24.04
    echo ⏳ 等待 3 秒...
    timeout /t 3 /nobreak >nul
    echo 📥 正在安装 Ubuntu-24.04...
    wsl --install -d Ubuntu-24.04
    echo ⏳ 等待 WSL 初始化...
    timeout /t 10 /nobreak >nul
)
echo.
echo 🚀 开始在 WSL 中执行打包...
echo ⏰ 预计需要 30-60 分钟
echo.
:: 在 WSL 中执行打包脚本
wsl -d Ubuntu-24.04 -- bash -c "cd /mnt/c/Users/Administrator/aipywork/CayhBYUGkawrGZR2LVmrJ && bash build_apk.sh"
if errorlevel 1 (
    echo.
    echo ❌ 打包失败，请查看上方错误信息
) else (
    echo.
    echo 🎉 打包成功！APK 文件在 bin 目录中
)
echo.
pause
