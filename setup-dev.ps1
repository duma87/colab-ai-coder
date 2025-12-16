@echo off
REM Development setup script for Colab AI Coder (Windows)

setlocal enabledelayedexpansion

echo.
echo 🚀 Colab AI Coder - Development Setup (Windows)
echo ================================================

REM Check Python version
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set python_version=%%i
echo ✓ Python version: %python_version%

REM Create virtual environment
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat
echo ✓ Virtual environment activated

REM Install dependencies
echo 📦 Installing dependencies...
cd backend
pip install -e \".[dev]\" -q
pip install pre-commit -q
cd ..

REM Setup pre-commit hooks
echo 🔧 Setting up pre-commit hooks...
pre-commit install

REM Run tests
echo 🧪 Running tests...
cd backend
pytest tests/ --cov=src --cov-report=term -q
cd ..

echo.
echo ✅ Setup complete!
echo.
echo Next steps:
echo 1. Activate environment: venv\Scripts\activate.bat
echo 2. Start dev server: cd backend ^&^& uvicorn src.main:app --reload\n 3. Open notebook: notebooks/qwen-assistant.ipynb\n 4. Or run tests: pytest backend/tests/ -v\necho.\n\nendlocal\n