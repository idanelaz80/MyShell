@echo off
if "%~2"=="back" goto back

python "%~dp0cd.py" "%~1"
exit /b

:back
echo %~1