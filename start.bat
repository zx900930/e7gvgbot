@echo off
REM taskkill /F /IM chrome.exe
REM taskkill /F /IM chromedriver.exe
taskkill /F /IM py.exe
taskkill /F /IM python.exe
chcp 65001
cd C:\Install\XUN_Bot\
call .\venv\Scripts\activate.bat
start .\venv\Scripts\python.exe "bot.py"
exit /b