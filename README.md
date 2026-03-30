# CurholeView — Martingale Strategy Simulator | CurholeView — симулятор стратегии Мартингейла

[English](#english) | [Русский](#russian)

---

<a name="english"></a>
## English

**Python GUI application** for simulating the Martingale betting strategy (doubling the bet after a loss) with real-time visualization.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-lightgrey.svg)

---

## ✨ Features

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

---

## 📸 Screenshots

*Screenshots can be placed here.*

---

## 📦 Requirements

- Python 3.8 or higher
- Required libraries:
  - `matplotlib`
  - `tkinter` (included with Python standard distribution)

---

## 🚀 Installation & Usage

1. **Clone the repository**

        git clone https://github.com/zedraider/CurholeViev.git
        cd CurholeViev

2. **Install dependencies**

        pip install matplotlib

3. **Run the application**

        python curholeview.py

---

## ⚙️ Simulation Parameters

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

---

## 🎮 Controls

- **Start** – begin simulation
- **Stop** – stop running simulation
- **Reset** – clear all data and reset parameters to defaults
- **Save CSV** – export results to a file
- **Load CSV** – import previously saved simulation
- **Fast simulation** – disables delay between rounds for rapid execution

---

## 📊 Batch Mode

Run a series of simulations (1 to 1000) with current parameters.  
Upon completion, a results window displays:

- Average profit
- Average number of rounds
- Number of winning / losing simulations
- Win rate percentage
- Detailed results table (final balance, savings, profit, rounds)

---

## 🎨 Themes & Language

- **Themes:** Light, Dark, Blue, Green, Pink – select from *Settings → Theme*
- **Language:** Russian or English – select from *Language* menu

---

## 🛠️ Editing Presets

From the menu *Settings → Preset settings*, you can modify the three preset profiles (Classic, Aggressive, Conservative). Changes apply for the current session.

---

## 📁 Project Structure

    CurholeViev/
    ├── curholeview.py          # main application file
    ├── requirements.txt        # dependencies (matplotlib)
    ├── requirements-dev.txt    # development dependencies
    ├── tests/                  # unit tests
    ├── .github/                # GitHub Actions configuration
    ├── dist/                   # built releases (not in repository)
    └── README.md               # this file

---

## 🧪 Testing

Install additional dependencies from `requirements-dev.txt`, then run:

    pytest tests/

Code formatting:

    ruff format .
    ruff check .

---

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for details.

---

## 👤 Author

Alexey Melnikov  
[zedraider@bk.ru](mailto:zedraider@bk.ru)  
GitHub: [@zedraider](https://github.com/zedraider)

---

_If you find this tool useful, give it a star ⭐ on GitHub!_


---

<a name="russian"></a>
## Русский

**Python GUI приложение** для моделирования стратегии Мартингейла (удвоение ставки после проигрыша) с визуализацией в реальном времени.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-lightgrey.svg)

---

## ✨ Особенности

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

---

## 🖼️ Скриншоты

*Здесь можно разместить скриншоты приложения.*

---

## 📦 Требования

- Python 3.8 или выше
- Библиотеки:
  - `matplotlib`
  - `tkinter` (входит в стандартную поставку Python)

---

## 🚀 Установка и запуск

1. **Клонируйте репозиторий**

        git clone https://github.com/zedraider/CurholeViev.git
        cd CurholeViev

2. **Установите зависимости**

        pip install matplotlib

3. **Запустите приложение**

        python curholeview.py

---

## ⚙️ Параметры симуляции

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

---

## 🎮 Управление

- **Старт** – начать симуляцию
- **Стоп** – остановить симуляцию
- **Сброс** – очистить данные и сбросить параметры к значениям по умолчанию
- **Сохранить CSV** – экспортировать результаты в файл
- **Загрузить CSV** – импортировать ранее сохранённую симуляцию
- **Быстрая симуляция** – отключает задержку между раундами

---

## 📊 Пакетный режим

Позволяет запустить серию симуляций (от 1 до 1000) с текущими параметрами.  
После завершения отображается окно со статистикой:

- Средняя прибыль
- Среднее количество раундов
- Количество выигрышных / проигрышных симуляций
- Процент выигрышных симуляций
- Таблица детальных результатов (итоговый баланс, накопления, прибыль, число раундов)

---

## 🎨 Темы и язык

- **Темы:** светлая, тёмная, синяя, зелёная, розовая – выбираются в меню *Настройки → Цветовая тема*.
- **Язык:** русский или английский – меню *Язык*.

---

## 🛠️ Редактирование пресетов

В меню *Настройки → Настройки пресетов* можно изменить параметры трёх предустановленных профилей (Классика, Агрессивная, Консервативная). Изменения сохраняются на время сеанса.

---

## 📁 Структура проекта

    CurholeViev/
    ├── curholeview.py          # основной файл приложения
    ├── requirements.txt        # зависимости (matplotlib)
    ├── requirements-dev.txt    # зависимости для разработки
    ├── tests/                  # юнит-тесты
    ├── .github/                # конфигурация GitHub Actions
    ├── dist/                   # собранные версии (не входят в репозиторий)
    └── README.md               # этот файл

---

## 🧪 Тестирование

Для запуска тестов установите дополнительные зависимости (из `requirements-dev.txt`), затем выполните:

    pytest tests/

Форматирование кода:

    ruff format .
    ruff check .

---

## 📄 Лицензия

Проект распространяется под лицензией MIT. Подробности в файле `LICENSE`.

---

## 👤 Автор

Алексей Мельников  
[zedraider@bk.ru](mailto:zedraider@bk.ru)  
GitHub: [@zedraider](https://github.com/zedraider)

---

_Если этот инструмент оказался полезен, поставьте звезду ⭐ на GitHub!_