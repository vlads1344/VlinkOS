@echo off
title VlinkOS Terminal
cls
echo [SYSTEM] Starting VlinkOS Kernel...
:: Переходим в папку, где лежит сам батник
cd /d "%~dp0"
:: Запускаем ядро
py main.py
pause