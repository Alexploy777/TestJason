@echo off
chcp 65001 > nul
:: Проверяем, запущен ли .bat с правами администратора
fltmc >nul 2>&1 || (
    echo Запуск от имени администратора...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit
)
cd /d "%~dp0"
echo Регистрация и запуск COM-сервера...
python keyboard_com.py --register
start /min python keyboard_com.py
