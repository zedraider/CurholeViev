$header = @"
# CurholeView - Martingale Strategy Simulator

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Python GUI application** for simulating Martingale betting strategy with real-time visualization.
"@

$content = Get-Content README.md -Raw
$newContent = $header + "`n`n" + $content
$newContent | Out-File README.md -Encoding UTF8

## Features
- 🎯 Martingale strategy simulation with customizable parameters
- 📊 Real-time profit/loss charts using matplotlib
- ⚡ Multi-threaded batch simulations
- 💾 Export results to CSV
- 🎨 Tkinter-based user interface

## Requirements
- Python 3.8+
- matplotlib
- tkinter (included with Python)

## Installation
```bash
pip install matplotlib
```

## Usage
```bash
python curholeview.py
```

## Project Structure
- \`curholeview.py\` - Main application file
- \`requirements.txt\` - Python dependencies
- \`tests/\` - Unit tests

## Testing
```bash
# Run tests
pytest tests/

# Code formatting
ruff format .
ruff check .
```

## License
MIT