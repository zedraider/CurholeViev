@"
# CurholeView - Martingale Strategy Simulator

Python GUI application for simulating and analyzing Martingale betting strategy with real-time visualization.

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
\`\`\`bash
pip install matplotlib
\`\`\`

## Usage
\`\`\`bash
python curholeview.py
\`\`\`

## Project Structure
- \`curholeview.py\` - Main application file
- \`requirements.txt\` - Python dependencies
- \`tests/\` - Unit tests

## Testing
\`\`\`bash
# Run tests
pytest tests/

# Code formatting
ruff format .
ruff check .
\`\`\`

## License
MIT
"@ | Out-File -FilePath README.md -Encoding UTF8