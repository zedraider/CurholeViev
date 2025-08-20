# CurholeView — Martingale Simulator

## Program Description

CurholeView is a Martingale strategy simulator designed to analyze and test one of the most well-known betting management strategies in gambling games. The program allows modeling gaming sessions with various parameters, visualizing results, and saving them for further analysis.

## Key Features

### 1. Martingale Strategy Simulation
- **Basic Principle**: After each loss, the bet amount increases by a specified factor, and after a win, it returns to the base bet
- **Flexible Configuration**: Users can modify the bet multiplier, maximum bet limit, win probability, and other parameters
- **Automatic Simulation**: The program can run thousands of rounds automatically with a specified delay

### 2. Bankroll and Savings Management
- **Initial Deposit**: Setting the starting bank for simulation
- **Withdrawals**: Ability to withdraw a fixed amount or percentage of the deposit after a win
- **Savings Account**: Separate account for accumulated funds that doesn't participate in betting

### 3. Results Visualization
- **Bankroll Change Charts**: Visual display of bank dynamics during simulation
- **Bet Size Charts**: Tracking changes in bet sizes based on results
- **Savings Chart**: Visualization of the growth of the savings account

### 4. Data Operations
- **Save Results**: Export simulation results to CSV file
- **Load Data**: Import previously saved simulations for analysis or continuation
- **Data Format**: Structured format with information about each round

### 5. Settings and Personalization
- **Presets**: Three ready-made profiles (Classic, Aggressive, Conservative)
- **Color Themes**: Five color schemes for the interface (light, dark, blue, green, pink)
- **Language Support**: Russian and English interface languages

## Technical Specifications

### System Requirements
- Operating System: Windows, macOS, Linux
- Python 3.6 or higher
- Dependencies: tkinter, matplotlib, numpy

### Program Architecture
- Multithreading: The main simulation process runs in a separate thread to prevent UI blocking
- Update Queue: Using a queue for safe UI updates from another thread
- Event-Driven Approach: Handling user interface events

## Program Usage

### Launch
1. Make sure Python 3.6 or higher is installed on your computer
2. Install the required dependencies: `pip install tkinter matplotlib numpy`
3. Launch the program: `python ready.py`

### Basic Operations

#### 1. Simulation Configuration
- **Deposit**: Enter the initial deposit amount
- **Max Bet**: Set the maximum bet limit (0 for no limit)
- **Multiplier**: Factor by which the bet increases after a loss
- **Delay**: Interval between rounds in seconds
- **Win Probability**: Percentage chance of winning in each round
- **Withdraw on Win**: Fixed amount to be withdrawn after each win
- **Withdraw % from Deposit**: Percentage of the current deposit to be withdrawn
- **Only on Win (percentage)**: Withdraw percentage only on a win

#### 2. Simulation Control
- **Start**: Begin a new simulation with the specified parameters
- **Stop**: Stop the current simulation
- **Reset**: Reset the simulation to its initial state
- **Fast Simulation**: Enable mode without delay between rounds for quick modeling

#### 3. Working with Results
- **Save CSV**: Export simulation results to a CSV file
- **Load CSV**: Import previously saved results

#### 4. Interface Configuration
- **Presets**: Choose one of the ready-made configurations (Classic, Aggressive, Conservative)
- **Theme**: Change the interface color scheme
- **Language**: Switch between Russian and English languages

## Program Interface

### Left Panel
- **Parameters**: Simulation settings
- **Control**: Simulation control buttons
- **Status**: Current simulation status (round number, deposit amount, current bet, savings size)

### Right Panel
- **Charts**: Three graphs showing:
  1. Deposit dynamics
  2. Bet sizes by round
  3. Growth of the savings account

### Menu
- **File**: Exit the program
- **Settings**: Configure presets and theme
- **Language**: Change interface language
- **Help**: About the program

## Martingale Strategy

### Brief Description
The Martingale strategy is a betting management system where after each loss, the size of the next bet increases by a certain factor. After a win, the bet returns to its original value.

### Mathematical Principle
- Initial bet: 1 unit
- After a loss: next bet = previous bet × multiplier
- After a win: next bet = initial bet

### Risks
- **Exponential bet growth**: With a series of losses, bets grow exponentially
- **Bankroll limitation**: Even with a large bankroll, there's a risk of bankruptcy after a long losing streak
- **Bet limits**: Casinos usually have betting limits that can restrict the strategy

### Simulator Applications
The simulator allows you to:
- Test the strategy with various parameters
- Assess bankruptcy risks
- Analyze effectiveness at different win probabilities
- Optimize strategy parameters

## Development and Extension

### Project Structure
- `ready.py`: Main program file
- `config.py`: Configurations and settings (can be added to improve modularity)
- `tests/`: Tests (can be added to improve code quality)

### Possible Improvements
- Adding additional betting strategies
- Extended statistics and results analysis
- Support for other data export formats
- Web interface for remote use
- Mobile version of the application

## License

The program is distributed freely. Copyright belongs to Alexey Melnikov (zedraider@bk.ru).

## Contacts

For questions, suggestions, and bug reports, please contact the author:
- Email: zedraider@bk.ru
- Version: 2.0
- Date: 2025-08-19

---

# CurholeView — Martingale Simulator

## Описание программы

CurholeView — это симулятор стратегии Мартингейла, разработанный для анализа и тестирования одной из самых известных стратегий управления ставками в азартных играх. Программа позволяет моделировать игровые сессии с различными параметрами, визуализировать результаты и сохранять их для дальнейшего анализа.

## Основные возможности

### 1. Моделирование стратегии Мартингейла
- **Основной принцип**: После каждого проигрыша ставка увеличивается в заданное число раз, а после выигрыша возвращается к базовой ставке
- **Гибкая настройка**: Пользователь может изменять множитель ставки, максимальный размер ставки, вероятность выигрыша и другие параметры
- **Автоматическая симуляция**: Программа может проводить тысячи раундов автоматически с заданной задержкой

### 2. Управление депозитом и накоплениями
- **Начальный депозит**: Задание начального банка для симуляции
- **Снятие средств**: Возможность снимать фиксированную сумму или процент от депозита после выигрыша
- **Накопительный счет**: Отдельный счет для накопленных средств, который не участвует в ставках

### 3. Визуализация результатов
- **Графики изменения депозита**: Визуальное отображение динамики банка в течение симуляции
- **Графики размера ставок**: Отслеживание изменения размера ставок в зависимости от результатов
- **График накоплений**: Визуализация роста накопительного счета

### 4. Работа с данными
- **Сохранение результатов**: Экспорт результатов симуляции в CSV-файл
- **Загрузка данных**: Импорт ранее сохраненных симуляций для анализа или продолжения
- **Формат данных**: Структурированный формат с информацией о каждом раунде

### 5. Настройки и персонализация
- **Предустановленные конфигурации**: Три готовых профиля (Классический, Агрессивный, Консервативный)
- **Цветовые темы**: Пять цветовых схем интерфейса (светлая, темная, голубая, зеленая, розовая)
- **Языковая поддержка**: Русский и английский языки интерфейса

## Технические характеристики

### Системные требования
- Операционная система: Windows, macOS, Linux
- Python 3.6 или выше
- Зависимости: tkinter, matplotlib, numpy

### Архитектура программы
- Многопоточность: Основной симуляционный процесс работает в отдельном потоке для предотвращения блокировки UI
- Очередь обновлений: Использование очереди для безопасного обновления UI из другого потока
- Событийно-ориентированный подход: Обработка событий пользовательского интерфейса

## Использование программы

### Запуск
1. Убедитесь, что на вашем компьютере установлен Python версии 3.6 или выше
2. Установите необходимые зависимости: `pip install tkinter matplotlib numpy`
3. Запустите программу: `python ready.py`

### Основные операции

#### 1. Настройка параметров симуляции
- **Депозит**: Введите начальный размер депозита
- **Максимальная ставка**: Установите лимит максимальной ставки (0 для отсутствия лимита)
- **Множитель**: Коэффициент увеличения ставки после проигрыша
- **Задержка**: Интервал между раундами в секундах
- **Вероятность выигрыша**: Процентная вероятность выигрыша в каждом раунде
- **Снимать с выигрыша**: Фиксированная сумма, которая будет сниматься после каждого выигрыша
- **Снимать % от депозита**: Процент от текущего депозита, который будет сниматься
- **Только при выигрыше (процент)**: Снимать процент только при выигрыше

#### 2. Управление симуляцией
- **Старт**: Начать новую симуляцию с заданными параметрами
- **Стоп**: Остановить текущую симуляцию
- **Сброс**: Сбросить симуляцию до начального состояния
- **Быстрая симуляция**: Включение режима без задержки между раундами для быстрого моделирования

#### 3. Работа с результатами
- **Сохранить CSV**: Экспортировать результаты симуляции в CSV-файл
- **Загрузить CSV**: Импортировать ранее сохраненные результаты

#### 4. Настройка интерфейса
- **Предустановки**: Выберите одну из готовых конфигураций (Классический, Агрессивный, Консервативный)
- **Тема**: Измените цветовую схему интерфейса
- **Язык**: Переключите между русским и английским языками

## Интерфейс программы

### Левая панель
- **Параметры**: Настройки симуляции
- **Управление**: Кнопки управления симуляцией
- **Статус**: Текущее состояние симуляции (номер раунда, размер депозита, текущая ставка, размер накоплений)

### Правая панель
- **Графики**: Три графика, отображающие:
  1. Динамику депозита
  2. Размер ставок по раундам
  3. Рост накопительного счета

### Меню
- **Файл**: Выход из программы
- **Настройки**: Настройка пресетов и темы
- **Язык**: Смена языка интерфейса
- **Справка**: О программе

## Стратегия Мартингейла

### Краткое описание
Стратегия Мартингейла — это система управления ставками, при которой после каждого проигрыша размер следующей ставки увеличивается в определенное число раз. После выигрыша ставка возвращается к исходному значению.

### Математический принцип
- Начальная ставка: 1 единица
- После проигрыша: следующая ставка = предыдущая ставка × множитель
- После выигрыша: следующая ставка = начальная ставка

### Риски
- **Экспоненциальный рост ставок**: При серии проигрышей ставки растут экспоненциально
- **Ограниченность банка**: Даже с большим банком существует риск банкротства после длительной серии проигрышей
- **Лимиты ставок**: Казино обычно имеют лимиты ставок, которые могут ограничить стратегию

### Применение симулятора
Симулятор позволяет:
- Тестировать стратегию с различными параметрами
- Оценивать риски банкротства
- Анализировать эффективность при разных вероятностях выигрыша
- Оптимизировать параметры стратегии

## Разработка и расширение

### Структура проекта
- `ready.py`: Основной файл с программой
- `config.py`: Конфигурации и настройки (может быть добавлен для улучшения модульности)
- `tests/`: Тесты (может быть добавлен для улучшения качества кода)

### Возможные улучшения
- Добавление дополнительных стратегий ставок
- Расширенная статистика и анализ результатов
- Поддержка других форматов экспорта данных
- Веб-интерфейс для удаленного использования
- Мобильная версия приложения

## Лицензия

Программа распространяется в свободном доступе. Авторское право принадлежит Алексею Мельникову (zedraider@bk.ru).

## Контакты

Для вопросов, предложений и сообщений об ошибках, пожалуйста, обращайтесь к автору:
- Email: zedraider@bk.ru
- Версия: 2.0
- Дата: 2025-08-19

---