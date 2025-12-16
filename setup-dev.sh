#!/bin/bash
# Development setup script for Colab AI Coder

set -e

echo "🚀 Colab AI Coder - Development Setup"
echo "======================================"

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate
echo "✓ Virtual environment activated"

# Install dependencies
echo "📦 Installing dependencies..."
cd backend
pip install -e ".[dev]" -q
pip install pre-commit -q
cd ..

# Setup pre-commit hooks
echo "🔧 Setting up pre-commit hooks..."
pre-commit install

# Run tests
echo "🧪 Running tests..."
cd backend
pytest tests/ --cov=src --cov-report=term -q
cd ..

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Activate environment: source venv/bin/activate"
echo "2. Start dev server: cd backend && uvicorn src.main:app --reload"
echo "3. Open notebook: notebooks/qwen-assistant.ipynb"
echo "4. Or run tests: pytest backend/tests/ -v"
echo ""
