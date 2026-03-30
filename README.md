# CurholeView — симулятор стратегии Мартингейла 🎲

[English](#english) | [Русский](#russian)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Cross-platform](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-lightgrey)](https://www.python.org/)
[![GitHub stars](https://img.shields.io/github/stars/zedraider/CurholeViev?style=social)](https://github.com/zedraider/CurholeViev/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/zedraider/CurholeViev?style=social)](https://github.com/zedraider/CurholeViev/network/members)
[![GitHub issues](https://img.shields.io/github/issues/zedraider/CurholeViev)](https://github.com/zedraider/CurholeViev/issues)
[![Tests](https://github.com/zedraider/CurholeViev/actions/workflows/python-tests.yml/badge.svg)](https://github.com/zedraider/CurholeViev/actions/workflows/python-tests.yml)

---

<a name="english"></a>
## English

**Python GUI application** for simulating the Martingale betting strategy (doubling the bet after a loss) with real-time visualization.

### ✨ Features

- **Martingale Simulation** with customizable parameters
  - Initial deposit, maximum bet limit, bet multiplier
  - Delay between rounds (for visual mode)
  - Win probability (0–100%)
  - Withdrawal options (fixed amount or percentage from deposit)
- **Simulation Modes**
  - **Step-by-step simulation** with visual feedback for each round
  - **Fast simulation** (no delay)
  - **Batch mode** – run multiple simulations in sequence for statistical analysis
- **Real-time Visualization**
  - Dynamic charts for deposit, bet size, and savings using `matplotlib`
  - Interactive plots that update during simulation
- **Data Management**
  - Export simulation results to CSV
  - Load previously saved simulations
- **Modern Interface**
  - Multiple color themes (Light, Dark, Blue, Green, Pink)
  - Bilingual support: Russian and English
  - Editable presets (Classic, Aggressive, Conservative)

### 📸 Screenshots

*Screenshots can be placed here.*

### 📦 Requirements

- Python 3.8 or higher
- Required libraries:
  - `matplotlib`
  - `tkinter` (included with Python standard distribution)

### 🚀 Installation & Usage

    # Clone the repository
    git clone https://github.com/zedraider/CurholeViev.git
    cd CurholeViev

    # Install dependencies
    pip install matplotlib

    # Run the application
    python curholeview.py

### ⚙️ Simulation Parameters

| Parameter | Description |
|-----------|-------------|
| **Deposit** | Initial bankroll amount |
| **Max bet** | Upper limit for each bet (0 = unlimited) |
| **Multiplier** | Factor by which the bet increases after a loss |
| **Delay (sec)** | Pause between rounds in visual mode |
| **Withdraw on win ($)** | Fixed amount transferred to savings on a win |
| **Withdraw % from deposit** | Percentage of current deposit transferred to savings (can be restricted to winning rounds only) |
| **Win probability (%)** | Chance of winning each round |
| **Only on win (percent)** | If enabled, percentage withdrawal applies only after a winning round |

### 🎮 Controls

- **Start** – begin simulation
- **Stop** – stop running simulation
- **Reset** – clear all data and reset parameters to defaults
- **Save CSV** – export results to a file
- **Load CSV** – import previously saved simulation
- **Fast simulation** – disables delay between rounds for rapid execution

### 📊 Batch Mode

Run a series of simulations (1 to 1000) with current parameters.  
Upon completion, a results window displays:

- Average profit
- Average number of rounds
- Number of winning / losing simulations
- Win rate percentage
- Detailed results table (final balance, savings, profit, rounds)

### 🎨 Themes & Language

- **Themes:** Light, Dark, Blue, Green, Pink – select from *Settings → Theme*
- **Language:** Russian or English – select from *Language* menu

### 🛠️ Editing Presets

From the menu *Settings → Preset settings*, you can modify the three preset profiles (Classic, Aggressive, Conservative). Changes apply for the current session.

### 📁 Project Structure

    CurholeViev/
    ├── curholeview.py          # main application file
    ├── requirements.txt        # dependencies (matplotlib)
    ├── requirements-dev.txt    # development dependencies
    ├── tests/                  # unit tests
    ├── .github/                # GitHub Actions configuration
    ├── dist/                   # built releases (not in repository)
    └── README.md               # this file

### 🧪 Testing

Install additional dependencies from `requirements-dev.txt`, then run:

    pytest tests/

Code formatting:

    ruff format .
    ruff check .

### 🤝 Contributing

Contributions are welcome! Feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add: AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure tests pass before submitting PRs.

### 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for details.

### 👤 Author

Alexey Melnikov  
[zedraider@bk.ru](mailto:zedraider@bk.ru)  
GitHub: [@zedraider](https://github.com/zedraider)

---

<a name="russian"></a>
## Русский

**Python GUI приложение** для моделирования стратегии Мартингейла (удвоение ставки после проигрыша) с визуализацией в реальном времени.

### ✨ Возможности

- **Симуляция Мартингейла** с настраиваемыми параметрами
  - Начальный депозит, максимальная ставка, множитель ставки
  - Задержка между раундами (для визуального режима)
  - Вероятность выигрыша (0–100%)
  - Снятие выигрыша (фиксированная сумма или процент от депозита)
- **Режимы работы**
  - **Пошаговая симуляция** с отображением каждого раунда
  - **Быстрая симуляция** (без задержки)
  - **Пакетный режим** – запуск нескольких симуляций подряд для статистики
- **Визуализация**
  - Графики депозита, размера ставки и накоплений в реальном времени
  - Использование `matplotlib` для интерактивных графиков
- **Управление данными**
  - Сохранение результатов в CSV
  - Загрузка ранее сохранённых симуляций
- **Интерфейс**
  - Современный дизайн с темами (светлая, тёмная, синяя, зелёная, розовая)
  - Поддержка двух языков: русский и английский
  - Редактируемые пресеты (Классика, Агрессивная, Консервативная)

### 📸 Скриншоты

*Здесь можно разместить скриншоты приложения.*

### 📦 Требования

- Python 3.8 или выше
- Библиотеки:
  - `matplotlib`
  - `tkinter` (входит в стандартную поставку Python)

### 🚀 Установка и запуск

    # Клонируйте репозиторий
    git clone https://github.com/zedraider/CurholeViev.git
    cd CurholeViev

    # Установите зависимости
    pip install matplotlib

    # Запустите приложение
    python curholeview.py

### ⚙️ Параметры симуляции

| Параметр | Описание |
|----------|----------|
| **Депозит** | Начальная сумма на счёте |
| **Макс. ставка** | Верхний предел ставки (0 = без ограничений) |
| **Множитель** | Коэффициент увеличения ставки после проигрыша |
| **Задержка (сек)** | Пауза между раундами в визуальном режиме |
| **Снимать с выигрыша (₽)** | Фиксированная сумма, которая переводится в накопления при выигрыше |
| **Снимать % с депозита** | Процент от текущего депозита, переводимый в накопления (можно ограничить только выигрышными раундами) |
| **Вероятность выигрыша (%)** | Шанс выигрыша в каждом раунде |
| **Только при выигрыше (процент)** | Если включено, процент снимается только после выигрышного раунда |

### 🎮 Управление

- **Старт** – начать симуляцию
- **Стоп** – остановить симуляцию
- **Сброс** – очистить данные и сбросить параметры к значениям по умолчанию
- **Сохранить CSV** – экспортировать результаты в файл
- **Загрузить CSV** – импортировать ранее сохранённую симуляцию
- **Быстрая симуляция** – отключает задержку между раундами

### 📊 Пакетный режим

Позволяет запустить серию симуляций (от 1 до 1000) с текущими параметрами.  
После завершения отображается окно со статистикой:

- Средняя прибыль
- Среднее количество раундов
- Количество выигрышных / проигрышных симуляций
- Процент выигрышных симуляций
- Таблица детальных результатов (итоговый баланс, накопления, прибыль, число раундов)

### 🎨 Темы и язык

- **Темы:** светлая, тёмная, синяя, зелёная, розовая – выбираются в меню *Настройки → Цветовая тема*
- **Язык:** русский или английский – меню *Язык*

### 🛠️ Редактирование пресетов

В меню *Настройки → Настройки пресетов* можно изменить параметры трёх предустановленных профилей (Классика, Агрессивная, Консервативная). Изменения сохраняются на время сеанса.

### 📁 Структура проекта

    CurholeViev/
    ├── curholeview.py          # основной файл приложения
    ├── requirements.txt        # зависимости (matplotlib)
    ├── requirements-dev.txt    # зависимости для разработки
    ├── tests/                  # юнит-тесты
    ├── .github/                # конфигурация GitHub Actions
    ├── dist/                   # собранные версии (не входят в репозиторий)
    └── README.md               # этот файл

### 🧪 Тестирование

Для запуска тестов установите дополнительные зависимости (из `requirements-dev.txt`), затем выполните:

    pytest tests/

Форматирование кода:

    ruff format .
    ruff check .

### 🤝 Участие в разработке

Приветствуются любые вклады! Смело отправляйте Pull Request.

1. Форкните проект
2. Создайте ветку (`git checkout -b feature/AmazingFeature`)
3. Зафиксируйте изменения (`git commit -m 'Add: AmazingFeature'`)
4. Отправьте в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

Пожалуйста, убедитесь, что тесты проходят перед отправкой PR.

### 📄 Лицензия

Проект распространяется под лицензией MIT. Подробности в файле `LICENSE`.

### 👤 Автор

Алексей Мельников  
[zedraider@bk.ru](mailto:zedraider@bk.ru)  
GitHub: [@zedraider](https://github.com/zedraider)

---

*Если этот инструмент оказался полезен, поставьте звезду ⭐ на GitHub!*