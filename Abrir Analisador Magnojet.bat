@echo off
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (
  ".venv\Scripts\python.exe" -m analisador_magnojet --interface
) else (
  python -m analisador_magnojet --interface
)
if errorlevel 1 pause
