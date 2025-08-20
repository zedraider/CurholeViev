import threading, time, random, queue, csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class MartingaleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cur_ver = 2.1
        self.geometry("1400x700")
        self.minsize(1400, 700)
        self.maxsize(1400, 700)
        self.stop_event, self.ui_queue = threading.Event(), queue.Queue()
        self.round_index = 0
        self.bankroll = 0.0
        self.base_bet = 1.0
        self.current_bet = 1.0
        self.withdrawn_total = 0.0
        self.savings_account = 0.0
        self.max_bet_limit = 0.0
        self.results = []
        self.fast_mode = tk.BooleanVar(value=False)
        self.batch_count_var = tk.IntVar(value=10)
        self.presets = [
            {
                "name": "Classic", "mult": 2, "maxb": 20, "delay": 0.05, "withdraw_win": 0.0,
                "withdraw_percent": 0.0, "win_prob": 50.0, "percent_on_win": False
            },
            {
                "name": "Aggressive", "mult": 3, "maxb": 30, "delay": 0.05, "withdraw_win": 0.0,
                "withdraw_percent": 0.0, "win_prob": 50.0, "percent_on_win": False
            },
            {
                "name": "Conservative", "mult": 1.5, "maxb": 15, "delay": 0.05, "withdraw_win": 0.0,
                "withdraw_percent": 0.0, "win_prob": 50.0, "percent_on_win": False
            }
        ]
        self.theme = "light"
        self.theme_colors = {
            "light": {
                "bg": "#f7f7fa",
                "frame": "#f7f7fa",
                "label": "#222",
                "chart_bg": "#ffffff",
                "chart_fg": "#222",
                "preset": "#e7e7ef",
                "bank": "#0077cc",
                "bet": "#cc7700",
                "savings": "#44bbff"
            },
            "dark": {
                "bg": "#23232b",
                "frame": "#23232b",
                "label": "#696969",
                "chart_bg": "#23232b",
                "chart_fg": "#585858",
                "preset": "#33334a",
                "bank": "#44bbff",
                "bet": "#ffbb44",
                "savings": "#00ffaa"
            },
            "blue": {
                "bg": "#eaf6fb",
                "frame": "#eaf6fb",
                "label": "#1a237e",
                "chart_bg": "#e3f2fd",
                "chart_fg": "#1a237e",
                "preset": "#bbdefb",
                "bank": "#1976d2",
                "bet": "#0288d1",
                "savings": "#00bcd4"
            },
            "green": {
                "bg": "#eafaf1",
                "frame": "#eafaf1",
                "label": "#1b5e20",
                "chart_bg": "#e8f5e9",
                "chart_fg": "#1b5e20",
                "preset": "#c8e6c9",
                "bank": "#388e3c",
                "bet": "#43a047",
                "savings": "#00c853"
            },
            "pink": {
                "bg": "#fce4ec",
                "frame": "#fce4ec",
                "label": "#ad1457",
                "chart_bg": "#f8bbd0",
                "chart_fg": "#ad1457",
                "preset": "#f48fb1",
                "bank": "#d81b60",
                "bet": "#c2185b",
                "savings": "#f06292"
            }
        }
        self.lang = "ru"
        self.langs = {
            "ru": {
                "title": "CurholeView — симулятор мартингейла "f"{self.cur_ver}",
                "deposit": "Депозит:",
                "max_bet": "Макс. ставка (0=∞):",
                "multiplier": "Множитель:",
                "delay": "Задержка (сек):",
                "withdraw_win": "Снимать с выигрыша (₽):",
                "withdraw_percent": "Снимать % с депозита:",
                "win_prob": "Вероятность выигрыша (%):",
                "percent_on_win": "Зачислять на счёт накоплений только при выигрыше",
                "presets": "Пресеты",
                "classic": "Классика",
                "aggressive": "Агрессивная",
                "conservative": "Консервативная",
                "fast_sim": "Быстрая симуляция",
                "control": "Управление",
                "start": "Старт",
                "stop": "Стоп",
                "reset": "Сброс",
                "save_csv": "Сохранить CSV",
                "load_csv": "Загрузить CSV",
                "status": "Статус",
                "round": "Раунд: {}",
                "bank": "Депозит: {:.2f}",
                "bet": "Ставка: {:.2f}",
                "savings": "Счёт накоплений: {:.2f}",
                "ready": "Готово.",
                "charts": "Графики",
                "savings_chart": "График накоплений",
                "savings_title": "Счёт накоплений по раундам",
                "deposit_title": "Депозит по раундам",
                "deposit_label": "Депозит",
                "bet_title": "Размер ставки по раундам",
                "bet_label": "Ставка",
                "file": "Файл",
                "settings": "Настройки",
                "help": "Справка",
                "exit": "Выход",
                "preset_settings": "Настройки пресетов",
                "theme": "Цветовая тема",
                "about": "О программе",
                "about_text": "CurholeView — симулятор мартингейла. Автор: Алексей Мельников zedraider@bk.ru\n\nВерсия: "f"{self.cur_ver}\nДата: 2025-08-19\n\nИспользуйте на свой страх и риск!",
                "choose_theme": "Выберите цветовую тему:",
                "apply": "Применить",
                "cancel": "Отмена",
                "preset_mult": "Множитель:",
                "preset_maxb": "Макс. ставка:",
                "preset_delay": "Задержка (сек):",
                "preset_withdraw_win": "Снимать с выигрыша (₽):",
                "preset_withdraw_percent": "Снимать % с депозита:",
                "preset_win_prob": "Вероятность выигрыша (%):",
                "preset_percent_on_win": "Только при выигрыше (процент)",
                "preset_save": "Сохранить",
                "preset_cancel": "Отмена",
                "lang": "Язык",
                "choose_lang": "Выберите язык:",
                "ru": "Русский",
                "en": "English",
                "no_data": "Нет данных для сохранения.",
                "saved": "Данные сохранены в {}",
                "save_error": "Не удалось сохранить CSV: {}",
                "no_data_file": "В файле нет корректных записей.",
                "loaded": "Загружено {} записей",
                "load_error": "Не удалось загрузить CSV: {}",
                "error": "Ошибка",
                "warning": "Внимание",
                "simulating": "Идёт симуляция…",
                "stopping": "Остановка…",
                "stopped": "Остановлено",
                "finished": "Симуляция завершена",
                "incorrect_deposit": "Некорректный депозит или лимит",
                "win": "Выигрыш!",
                "lose": "Проигрыш.",
                "bank_empty": "Банкролл пуст.",
                "withdrawn": " Снято: {:.2f}",
                "percent_withdrawn": " Процент снят: {:.2f}",
                "batch_sim": "Множественные симуляции",
                "batch_count": "Количество симуляций:",
                "batch_results": "Результаты симуляций",
                "batch_avg_profit": "Средняя прибыль:",
                "batch_avg_rounds": "Среднее число раундов:",
                "batch_wins": "Выигрышных симуляций:",
                "batch_losses": "Проигрышных симуляций:",
                "totalsim": "Всего симуляций: ",
                "inidep": "Начальный депозит: "
            },
            "en": {
                "title": "CurholeView — Martingale Simulator ("f"{self.cur_ver})",
                "deposit": "Deposit:",
                "max_bet": "Max bet (0=∞):",
                "multiplier": "Multiplier:",
                "delay": "Delay (sec):",
                "withdraw_win": "Withdraw on win ($):",
                "withdraw_percent": "Withdraw % from deposit:",
                "win_prob": "Win probability (%):",
                "percent_on_win": "Add to savings only on win",
                "presets": "Presets",
                "classic": "Classic",
                "aggressive": "Aggressive",
                "conservative": "Conservative",
                "fast_sim": "Fast simulation",
                "control": "Control",
                "start": "Start",
                "stop": "Stop",
                "reset": "Reset",
                "save_csv": "Save CSV",
                "load_csv": "Load CSV",
                "status": "Status",
                "round": "Round: {}",
                "bank": "Deposit: {:.2f}",
                "bet": "Bet: {:.2f}",
                "savings": "Savings: {:.2f}",
                "ready": "Ready.",
                "charts": "Charts",
                "savings_chart": "Savings chart",
                "savings_title": "Savings by round",
                "deposit_title": "Deposit by round",
                "deposit_label": "Deposit",
                "bet_title": "Bet size by round",
                "bet_label": "Bet",
                "file": "File",
                "settings": "Settings",
                "help": "Help",
                "exit": "Exit",
                "preset_settings": "Preset settings",
                "theme": "Theme",
                "about": "About",
                "about_text": "CurholeView — Martingale simulator. Author: Alexey Melnikov zedraider@bk.ru\n\nVersion: 2.1\nDate: 2025-08-19\n\nUse at your own risk!",
                "choose_theme": "Choose theme:",
                "apply": "Apply",
                "cancel": "Cancel",
                "preset_mult": "Multiplier:",
                "preset_maxb": "Max bet:",
                "preset_delay": "Delay (sec):",
                "preset_withdraw_win": "Withdraw on win ($):",
                "preset_withdraw_percent": "Withdraw % from deposit:",
                "preset_win_prob": "Win probability (%):",
                "preset_percent_on_win": "Only on win (percent)",
                "preset_save": "Save",
                "preset_cancel": "Cancel",
                "lang": "Language",
                "choose_lang": "Choose language:",
                "ru": "Русский",
                "en": "English",
                "no_data": "No data to save.",
                "saved": "Data saved to {}",
                "save_error": "Failed to save CSV: {}",
                "no_data_file": "No valid records in file.",
                "loaded": "Loaded {} records",
                "load_error": "Failed to load CSV: {}",
                "error": "Error",
                "warning": "Warning",
                "simulating": "Simulating…",
                "stopping": "Stopping…",
                "stopped": "Stopped",
                "finished": "Simulation finished",
                "incorrect_deposit": "Incorrect deposit or limit",
                "win": "Win!",
                "lose": "Lose.",
                "bank_empty": "Bankroll empty.",
                "withdrawn": " Withdrawn: {:.2f}",
                "percent_withdrawn": " Percent withdrawn: {:.2f}",
                "batch_sim": "Batch Simulations",
                "batch_count": "Number of simulations:",
                "batch_results": "Simulation Results",
                "batch_avg_profit": "Average profit:",
                "batch_avg_rounds": "Average rounds:",
                "batch_wins": "Won simulations:",
                "batch_losses": "Lost simulations:",
                "totalsim": "Total simulations: ",
                "inidep": "Initial deposit: "
            }
        }
        self._build_ui(); self._build_menu(); self._poll_queue()

    def _build_ui(self):
        pad = {"padx": 12, "pady": 8}
        colors = self.theme_colors[self.theme]
        lang = self.langs[self.lang]
        self.configure(bg=colors["bg"])
        self.title(lang["title"])

        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.columnconfigure(0, weight=0)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

        # Левая часть (параметры, управление, статус)
        left_frame = ttk.Frame(main_frame)
        left_frame.grid(row=0, column=0, sticky="nsw")
        left_frame.columnconfigure(0, weight=1)

        top = ttk.Frame(left_frame)
        top.pack(fill=tk.X, **pad)
        top.configure(style="Top.TFrame")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Top.TFrame", background=colors["frame"])
        style.configure("Param.TLabelframe", background=colors["frame"], font=("Segoe UI", 12, "bold"))
        style.configure("Param.TLabelframe.Label", font=("Segoe UI", 12, "bold"), foreground=colors["label"])
        style.configure("Param.TLabel", background=colors["frame"], font=("Segoe UI", 11), foreground=colors["label"])
        style.configure("Param.TEntry", font=("Segoe UI", 11))
        style.configure("Param.TButton", font=("Segoe UI", 11, "bold"), padding=8)
        style.configure("Param.TCheckbutton", background=colors["frame"], font=("Segoe UI", 11), foreground=colors["label"])
        style.configure("Status.TLabel", font=("Segoe UI", 11, "bold"), foreground=colors["label"])
        style.configure("Chart.TFrame", background=colors["chart_bg"])

        param_frame = ttk.LabelFrame(top, text=lang["control"], style="Param.TLabelframe")
        param_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=8, pady=8, ipadx=8, ipady=8)

        def add_label_entry(row, text, var, default, width=12):
            ttk.Label(param_frame, text=text, style="Param.TLabel").grid(row=row, column=0, sticky=tk.W, pady=3)
            var.set(default)
            e = ttk.Entry(param_frame, width=width, textvariable=var, style="Param.TEntry")
            e.grid(row=row, column=1, sticky=tk.W, pady=3)
            return e

        self.deposit_var, self.max_bet_var = tk.StringVar(), tk.StringVar()
        self.deposit_entry = add_label_entry(0, lang["deposit"], self.deposit_var, "1000")
        self.max_bet_entry = add_label_entry(1, lang["max_bet"], self.max_bet_var, "512")

        self.multiplier_var, self.delay_var, self.withdraw_per_win_var, self.withdraw_percent_var, self.win_prob_var = [tk.DoubleVar() for _ in range(5)]
        self.multiplier_var.set(2.0)
        self.delay_var.set(0.05)
        self.withdraw_per_win_var.set(0.0)
        self.withdraw_percent_var.set(0.0)
        self.win_prob_var.set(50.0)

        def add_slider(row, col, text, var, fr, to, step=0.01):
            ttk.Label(param_frame, text=text, style="Param.TLabel").grid(row=row, column=col, sticky=tk.W, pady=3)
            frame = ttk.Frame(param_frame, style="Top.TFrame")
            frame.grid(row=row, column=col+1, sticky=tk.EW, pady=3)
            scale = ttk.Scale(frame, from_=fr, to=to, variable=var, orient=tk.HORIZONTAL)
            scale.pack(side=tk.LEFT, fill=tk.X, expand=True)
            val_label = ttk.Label(frame, text=f"{var.get():.2f}", style="Param.TLabel")
            val_label.pack(side=tk.LEFT, padx=5)
            def update_val(*_): val_label.config(text=f"{var.get():.2f}")
            var.trace_add("write", update_val)
            return scale

        add_slider(2, 0, lang["multiplier"], self.multiplier_var, 1, 10)
        add_slider(3, 0, lang["delay"], self.delay_var, 0, 1)
        add_slider(4, 0, lang["withdraw_win"], self.withdraw_per_win_var, 0, 100)
        add_slider(5, 0, lang["withdraw_percent"], self.withdraw_percent_var, 0, 100)
        add_slider(6, 0, lang["win_prob"], self.win_prob_var, 0, 100)

        self.apply_percent_on_win_var = tk.BooleanVar()
        ttk.Checkbutton(param_frame, text=lang["percent_on_win"], variable=self.apply_percent_on_win_var, style="Param.TCheckbutton").grid(row=7, column=0, columnspan=2, sticky=tk.W, pady=3)

        presets = ttk.LabelFrame(top, text=lang["presets"], style="Param.TLabelframe")
        presets.grid(row=0, column=1, sticky=tk.NSEW, padx=8, pady=8, ipadx=8, ipady=8)
        self.preset_buttons = []
        for idx, preset in enumerate(self.presets):
            # используем перевод по ключу name.lower()
            btn = ttk.Button(
                presets,
                text=lang[preset["name"].lower()] if preset["name"].lower() in lang else preset["name"],
                command=lambda i=idx: self._apply_preset_dict(self.presets[i]),
                style="Param.TButton"
            )
            btn.pack(side=tk.TOP, fill=tk.X, padx=5, pady=6)
            self.preset_buttons.append(btn)

        ttk.Checkbutton(left_frame, text=lang["fast_sim"], variable=self.fast_mode, style="Param.TCheckbutton").pack(fill=tk.X, **pad)
        
        batch_frame = ttk.LabelFrame(left_frame, text=lang["batch_sim"], style="Param.TLabelframe")
        batch_frame.pack(fill=tk.X, **pad)
        ttk.Label(batch_frame, text=lang["batch_count"], style="Param.TLabel").pack(side=tk.LEFT, padx=5, pady=5)
        batch_spinbox = ttk.Spinbox(batch_frame, from_=1, to=1000, textvariable=self.batch_count_var, width=10)
        batch_spinbox.pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(batch_frame, text=lang["start"], command=self.on_batch_start, style="Param.TButton").pack(side=tk.LEFT, padx=10, pady=5)

        btns = ttk.LabelFrame(left_frame, text=lang["control"], style="Param.TLabelframe")
        btns.pack(fill=tk.X, **pad)
        for txt, cmd in [(lang["start"], self.on_start), (lang["stop"], self.on_stop), (lang["reset"], self.on_reset), (lang["save_csv"], self.save_csv), (lang["load_csv"], self.load_csv)]:
            ttk.Button(btns, text=txt, command=cmd, style="Param.TButton").pack(side=tk.LEFT, padx=10, pady=10, ipadx=10, ipady=6)

        status = ttk.LabelFrame(left_frame, text=lang["status"], style="Param.TLabelframe")
        status.pack(fill=tk.X, **pad)
        self.status_round, self.status_bank, self.status_bet, self.status_savings, self.status_msg = [
            ttk.Label(status, text=lang["round"].format(0), style="Status.TLabel"),
            ttk.Label(status, text=lang["bank"].format(0), style="Status.TLabel"),
            ttk.Label(status, text=lang["bet"].format(0), style="Status.TLabel"),
            ttk.Label(status, text=lang["savings"].format(0), style="Status.TLabel"),
            ttk.Label(status, text=lang["ready"], style="Status.TLabel")
        ]
        for i, w in enumerate([self.status_round, self.status_bank, self.status_bet, self.status_savings, self.status_msg]):
            w.grid(row=0, column=i, sticky=tk.W, padx=(10 if i else 0, 0), pady=6)

        # Правая часть (графики депозит/ставка/накопления, фиксированный размер)
        right_frame = ttk.Frame(main_frame)
        right_frame.grid(row=0, column=1, sticky="nsew")
        right_frame.rowconfigure(0, weight=1)
        right_frame.columnconfigure(0, weight=1)

        charts = ttk.LabelFrame(right_frame, text=lang["charts"], style="Param.TLabelframe")
        charts.pack(fill=tk.BOTH, expand=False, **pad)
        charts.configure(style="Chart.TFrame")

        # --- график депозит ---
        self.fig_bankroll = Figure(figsize=(6.5, 2.0), dpi=100, facecolor=colors["chart_bg"])
        self.ax_bankroll = self.fig_bankroll.add_subplot(111)
        self.ax_bankroll.set_title(lang["deposit_title"], color=colors["chart_fg"])
        self.ax_bankroll.set_xlabel(lang["round"].split(":")[0], color=colors["chart_fg"])
        self.ax_bankroll.set_ylabel(lang["deposit_label"], color=colors["chart_fg"])
        self.ax_bankroll.tick_params(axis='x', colors=colors["chart_fg"])
        self.ax_bankroll.tick_params(axis='y', colors=colors["chart_fg"])
        self.canvas_bankroll = FigureCanvasTkAgg(self.fig_bankroll, master=charts)
        self.canvas_bankroll.get_tk_widget().pack(fill=tk.NONE, expand=False, ipadx=0, ipady=0)
        self.bank_data = []
        self.bank_line, = self.ax_bankroll.plot([], [], color=colors["bank"])

        # --- горизонтальный сепаратор между графиками ---
        sep1 = ttk.Separator(charts, orient=tk.HORIZONTAL)
        sep1.pack(fill=tk.X, padx=0, pady=12)

        # --- график ставка ---
        self.fig_bet = Figure(figsize=(6.5, 2.0), dpi=100, facecolor=colors["chart_bg"])
        self.ax_bet = self.fig_bet.add_subplot(111)
        self.ax_bet.set_title(lang["bet_title"], color=colors["chart_fg"])
        self.ax_bet.set_xlabel(lang["round"].split(":")[0], color=colors["chart_fg"])
        self.ax_bet.set_ylabel(lang["bet_label"], color=colors["chart_fg"])
        self.ax_bet.tick_params(axis='x', colors=colors["chart_fg"])
        self.ax_bet.tick_params(axis='y', colors=colors["chart_fg"])
        self.canvas_bet = FigureCanvasTkAgg(self.fig_bet, master=charts)
        self.canvas_bet.get_tk_widget().pack(fill=tk.NONE, expand=False, ipadx=0, ipady=0)
        self.bet_data = []
        self.bet_line, = self.ax_bet.plot([], [], color=colors["bet"])

        # --- горизонтальный сепаратор между графиками ---
        sep2 = ttk.Separator(charts, orient=tk.HORIZONTAL)
        sep2.pack(fill=tk.X, padx=0, pady=12)

        # --- график накоплений ---
        self.fig_savings = Figure(figsize=(6.5, 2.0), dpi=100, facecolor=colors["chart_bg"])
        self.ax_savings = self.fig_savings.add_subplot(111)
        self.ax_savings.set_title(lang["savings_title"], color=colors["chart_fg"])
        self.ax_savings.set_xlabel(lang["round"].split(":")[0], color=colors["chart_fg"])
        self.ax_savings.set_ylabel(lang["savings"].split(":")[0], color=colors["chart_fg"])
        self.ax_savings.tick_params(axis='x', colors=colors["chart_fg"])
        self.ax_savings.tick_params(axis='y', colors=colors["chart_fg"])
        self.canvas_savings = FigureCanvasTkAgg(self.fig_savings, master=charts)
        self.canvas_savings.get_tk_widget().pack(fill=tk.NONE, expand=False, ipadx=0, ipady=0)
        self.savings_data = []
        self.x_data = []
        self.savings_line, = self.ax_savings.plot([], [], color=colors["savings"])

        for i in range(4): top.columnconfigure(i, weight=1)

    def _build_menu(self):
        lang = self.langs[self.lang]
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        settings_menu = tk.Menu(menubar, tearoff=0)
        lang_menu = tk.Menu(menubar, tearoff=0)
        help_menu = tk.Menu(menubar, tearoff=0)

        file_menu.add_command(label=lang["exit"], command=self.destroy)
        settings_menu.add_command(label=lang["preset_settings"], command=self._edit_presets)
        settings_menu.add_command(label=lang["theme"], command=self._choose_theme)
        lang_menu.add_command(label=lang["ru"], command=lambda: self._set_lang("ru"))
        lang_menu.add_command(label=lang["en"], command=lambda: self._set_lang("en"))
        help_menu.add_command(label=lang["about"], command=lambda: messagebox.showinfo(
            lang["about"],
            lang["about_text"]
        ))

        menubar.add_cascade(label=lang["file"], menu=file_menu)
        menubar.add_cascade(label=lang["settings"], menu=settings_menu)
        menubar.add_cascade(label=lang["lang"], menu=lang_menu)
        menubar.add_cascade(label=lang["help"], menu=help_menu)
        self.config(menu=menubar)

    def _set_lang(self, lang_code):
        self.lang = lang_code
        for widget in self.winfo_children():
            widget.destroy()
        self._build_ui()
        self._build_menu()
        # обновить текст кнопок пресетов
        lang = self.langs[self.lang]
        for i, btn in enumerate(self.preset_buttons):
            btn.config(text=lang[self.presets[i]["name"].lower()] if self.presets[i]["name"].lower() in lang else self.presets[i]["name"])

    def _choose_theme(self):
        lang = self.langs[self.lang]
        win = tk.Toplevel(self)
        win.title(lang["theme"])
        win.grab_set()
        theme_var = tk.StringVar(value=self.theme)
        ttk.Label(win, text=lang["choose_theme"]).pack(padx=10, pady=10)
        for theme_name, theme_data in self.theme_colors.items():
            ttk.Radiobutton(win, text=theme_name.capitalize(), variable=theme_var, value=theme_name).pack(anchor=tk.W, padx=12)
        def apply_theme():
            self.theme = theme_var.get()
            for widget in self.winfo_children():
                widget.destroy()
            self._build_ui()
            self._build_menu()
        ttk.Button(win, text=lang["apply"], command=lambda: [apply_theme(), win.destroy()]).pack(pady=10)
        ttk.Button(win, text=lang["cancel"], command=win.destroy).pack(pady=2)

    def _edit_presets(self):
        lang = self.langs[self.lang]
        win = tk.Toplevel(self)
        win.title(lang["preset_settings"])
        win.grab_set()
        entries = []
        for i, preset in enumerate(self.presets):
            frame = ttk.LabelFrame(win, text=lang[preset["name"].lower()] if preset["name"].lower() in lang else preset["name"])
            frame.pack(fill=tk.X, padx=10, pady=8)
            ttk.Label(frame, text=lang["preset_mult"]).grid(row=0, column=0, sticky=tk.W, padx=5, pady=3)
            mult_var = tk.DoubleVar(value=preset["mult"])
            mult_entry = ttk.Entry(frame, textvariable=mult_var, width=10)
            mult_entry.grid(row=0, column=1, padx=5, pady=3)
            ttk.Label(frame, text=lang["preset_maxb"]).grid(row=1, column=0, sticky=tk.W, padx=5, pady=3)
            maxb_var = tk.DoubleVar(value=preset["maxb"])
            maxb_entry = ttk.Entry(frame, textvariable=maxb_var, width=10)
            maxb_entry.grid(row=1, column=1, padx=5, pady=3)
            ttk.Label(frame, text=lang["preset_delay"]).grid(row=2, column=0, sticky=tk.W, padx=5, pady=3)
            delay_var = tk.DoubleVar(value=preset.get("delay", 0.05))
            delay_entry = ttk.Entry(frame, textvariable=delay_var, width=10)
            delay_entry.grid(row=2, column=1, padx=5, pady=3)
            ttk.Label(frame, text=lang["preset_withdraw_win"]).grid(row=3, column=0, sticky=tk.W, padx=5, pady=3)
            withdraw_win_var = tk.DoubleVar(value=preset.get("withdraw_win", 0.0))
            withdraw_win_entry = ttk.Entry(frame, textvariable=withdraw_win_var, width=10)
            withdraw_win_entry.grid(row=3, column=1, padx=5, pady=3)
            ttk.Label(frame, text=lang["preset_withdraw_percent"]).grid(row=4, column=0, sticky=tk.W, padx=5, pady=3)
            withdraw_percent_var = tk.DoubleVar(value=preset.get("withdraw_percent", 0.0))
            withdraw_percent_entry = ttk.Entry(frame, textvariable=withdraw_percent_var, width=10)
            withdraw_percent_entry.grid(row=4, column=1, padx=5, pady=3)
            ttk.Label(frame, text=lang["preset_win_prob"]).grid(row=5, column=0, sticky=tk.W, padx=5, pady=3)
            win_prob_var = tk.DoubleVar(value=preset.get("win_prob", 50.0))
            win_prob_entry = ttk.Entry(frame, textvariable=win_prob_var, width=10)
            win_prob_entry.grid(row=5, column=1, padx=5, pady=3)
            percent_on_win_var = tk.BooleanVar(value=preset.get("percent_on_win", False))
            percent_on_win_cb = ttk.Checkbutton(frame, text=lang["preset_percent_on_win"], variable=percent_on_win_var)
            percent_on_win_cb.grid(row=6, column=0, columnspan=2, sticky=tk.W, padx=5, pady=3)
            entries.append((mult_var, maxb_var, delay_var, withdraw_win_var, withdraw_percent_var, win_prob_var, percent_on_win_var))
        def save():
            for i, (mult_var, maxb_var, delay_var, withdraw_win_var, withdraw_percent_var, win_prob_var, percent_on_win_var) in enumerate(entries):
                try:
                    self.presets[i]["mult"] = float(mult_var.get())
                    self.presets[i]["maxb"] = float(maxb_var.get())
                    self.presets[i]["delay"] = float(delay_var.get())
                    self.presets[i]["withdraw_win"] = float(withdraw_win_var.get())
                    self.presets[i]["withdraw_percent"] = float(withdraw_percent_var.get())
                    self.presets[i]["win_prob"] = float(win_prob_var.get())
                    self.presets[i]["percent_on_win"] = bool(percent_on_win_var.get())
                except Exception:
                    pass
                self.preset_buttons[i].config(text=lang[self.presets[i]["name"].lower()] if self.presets[i]["name"].lower() in lang else self.presets[i]["name"])
            win.destroy()
        ttk.Button(win, text=lang["preset_save"], command=save).pack(pady=10)
        ttk.Button(win, text=lang["preset_cancel"], command=win.destroy).pack(pady=2)

    def _apply_preset_dict(self, preset):
        self.multiplier_var.set(preset["mult"])
        self.max_bet_var.set(str(preset["maxb"]))
        self.delay_var.set(preset.get("delay", 0.05))
        self.withdraw_per_win_var.set(preset.get("withdraw_win", 0.0))
        self.withdraw_percent_var.set(preset.get("withdraw_percent", 0.0))
        self.win_prob_var.set(preset.get("win_prob", 50.0))
        self.apply_percent_on_win_var.set(preset.get("percent_on_win", False))

    def on_start(self):
        lang = self.langs[self.lang]
        try:
            self.bankroll = float(self.deposit_var.get()); self.max_bet_limit = float(self.max_bet_var.get())
        except ValueError:
            return messagebox.showerror(lang["error"], lang["incorrect_deposit"])
        self.base_bet = 1.0; self.current_bet = 1.0; self.round_index = 0; self.results.clear(); self._clear_plot(); self._push_point(); self.savings_account = 0.0
        self.stop_event.clear(); threading.Thread(target=self._worker_loop, daemon=True).start(); self.status_msg.configure(text=lang["simulating"])
        
    def on_batch_start(self):
        lang = self.langs[self.lang]
        try:
            deposit = float(self.deposit_var.get())
            max_bet = float(self.max_bet_var.get())
            if deposit <= 0 or max_bet < 0:
                return messagebox.showerror(lang["error"], lang["incorrect_deposit"])
        except ValueError:
            return messagebox.showerror(lang["error"], lang["incorrect_deposit"])
            
        self.batch_results = []
        self.batch_count = self.batch_count_var.get()
        
        # Запускаем симуляции в отдельном потоке
        threading.Thread(target=self._run_batch_simulations, daemon=True).start()
        self.status_msg.configure(text=f"{lang['simulating']} ({self.batch_count} {lang['batch_sim']})")

    def on_stop(self):
        lang = self.langs[self.lang]
        self.stop_event.set(); self.status_msg.configure(text=lang["stopping"])

    def on_reset(self):
        lang = self.langs[self.lang]
        self.on_stop()
        def _do_reset():
            self.bankroll = 0.0
            self.base_bet = 1.0
            self.current_bet = 1.0
            self.round_index = 0
            self.results.clear()
            self._clear_plot()
            self.savings_account = 0.0
            self.deposit_var.set("1000")
            self.max_bet_var.set("512")
            labels = [
                lang["round"].format(0),
                lang["bank"].format(0),
                lang["bet"].format(0),
                lang["savings"].format(0),
                lang["ready"]
            ]
            for lbl, t in zip([self.status_round, self.status_bank, self.status_bet, self.status_savings, self.status_msg], labels):
                lbl.configure(text=t)
        self.after(50, _do_reset)

    def _worker_loop(self):
        lang = self.langs[self.lang]
        try:
            while not self.stop_event.is_set() and self.bankroll > 0:
                bet = max(self.base_bet, self.current_bet)
                if self.max_bet_limit > 0: bet = min(bet, self.max_bet_limit)
                bet = min(bet, self.bankroll)
                if bet <= 0:
                    break
                self.round_index += 1
                lose = random.random() > self.win_prob_var.get() / 100
                self.bankroll -= bet
                msg = ""
                if lose:
                    next_bet = bet * self.multiplier_var.get()
                    if self.max_bet_limit > 0: next_bet = min(next_bet, self.max_bet_limit)
                    self.current_bet = next_bet
                    msg = lang["lose"] if self.bankroll > 0 else lang["bank_empty"]
                else:
                    self.bankroll += bet * 2
                    self.current_bet = self.base_bet
                    msg = lang["win"]
                    w = self.withdraw_per_win_var.get()
                    if w > 0 and self.bankroll >= w:
                        self.bankroll -= w
                        self.savings_account += w
                        msg += lang["withdrawn"].format(w)
                p = self.withdraw_percent_var.get() / 100.0
                if p > 0.0:
                    if (not self.apply_percent_on_win_var.get()) or (self.apply_percent_on_win_var.get() and not lose):
                        amt = round(self.bankroll * p, 2)
                        if amt > 0:
                            amt = min(amt, self.bankroll)
                            self.bankroll -= amt
                            self.savings_account += amt
                            msg += lang["percent_withdrawn"].format(amt)
                self.results.append([self.round_index, self.bankroll, bet, self.savings_account, msg])
                if not self.fast_mode.get():
                    self.ui_queue.put({"round": self.round_index, "bank": self.bankroll, "bet": self.current_bet, "savings": self.savings_account, "msg": msg})
                    time.sleep(self.delay_var.get())
        except Exception as e:
            self.ui_queue.put({"round": self.round_index, "bank": self.bankroll, "bet": self.current_bet, "savings": self.savings_account, "msg": f"{lang['error']}: {e}"})
        finally:
            final_msg = lang["stopped"] if self.stop_event.is_set() else lang["finished"]
            self.ui_queue.put({"round": self.round_index, "bank": self.bankroll, "bet": self.current_bet, "savings": self.savings_account, "msg": final_msg})

    def _run_batch_simulations(self):
        lang = self.langs[self.lang]
        
        # Получаем параметры симуляции
        deposit = float(self.deposit_var.get())
        max_bet_limit = float(self.max_bet_var.get())
        base_bet = 1.0
        multiplier = self.multiplier_var.get()
        delay = self.delay_var.get()
        withdraw_win = self.withdraw_per_win_var.get()
        withdraw_percent = self.withdraw_percent_var.get() / 100.0
        win_prob = self.win_prob_var.get() / 100.0
        apply_percent_on_win = self.apply_percent_on_win_var.get()
        
        wins = 0
        total_profit = 0.0
        total_rounds = 0
        
        for i in range(self.batch_count):
            # Инициализация симуляции
            bankroll = deposit
            current_bet = base_bet
            round_index = 0
            savings_account = 0.0
            
            # Запускаем симуляцию
            while bankroll > 0 and round_index < 10000:  # Ограничение на максимальное число раундов
                round_index += 1
                bet = max(base_bet, current_bet)
                if max_bet_limit > 0:
                    bet = min(bet, max_bet_limit)
                bet = min(bet, bankroll)
                
                if bet <= 0:
                    break
                    
                lose = random.random() > win_prob
                bankroll -= bet
                
                if lose:
                    next_bet = bet * multiplier
                    if max_bet_limit > 0:
                        next_bet = min(next_bet, max_bet_limit)
                    current_bet = next_bet
                else:
                    bankroll += bet * 2
                    current_bet = base_bet
                    wins += 1
                    
                    # Снимаем выигрыш, если настроено
                    if withdraw_win > 0 and bankroll >= withdraw_win:
                        bankroll -= withdraw_win
                        savings_account += withdraw_win
                    
                    # Снимаем процент, если настроено
                    if withdraw_percent > 0:
                        if (not apply_percent_on_win) or (apply_percent_on_win and not lose):
                            amt = round(bankroll * withdraw_percent, 2)
                            if amt > 0:
                                amt = min(amt, bankroll)
                                bankroll -= amt
                                savings_account += amt
            
            # Сохраняем результаты симуляции
            profit = bankroll + savings_account - deposit
            result_data = {
                "simulation": i + 1,
                "final_balance": bankroll,
                "savings": savings_account,
                "profit": profit,
                "rounds": round_index
            }
            self.batch_results.append(result_data)
            
            # Выводим отладочную информацию для последней симуляции
            if i == self.batch_count - 1:
                print(f"Last simulation result: {result_data}")
            
            total_profit += profit
            total_rounds += round_index
            
            # Обновляем прогресс
            if i % 10 == 0 or i == self.batch_count - 1:
                progress = (i + 1) / self.batch_count * 100
                self.ui_queue.put({
                    "progress": progress,
                    "current": i + 1,
                    "total": self.batch_count
                })
                
        # Рассчитываем статистику
        avg_profit = total_profit / self.batch_count
        avg_rounds = total_rounds / self.batch_count
        
        # Правильный расчет процента выигрышей
        # Каждый раунд может быть выигрышем или проигрышем
        # Поэтому общее количество раундов всех симуляций = self.batch_count * среднее количество раундов
        # Но для простоты и понятности, будем считать симуляцию выигрышной, если в итоге баланс + накопления > депозита
        winning_sims = 0
        for result in self.batch_results:
            if result["profit"] > 0:
                winning_sims += 1
                
        loss_sims = self.batch_count - winning_sims
        win_rate = (winning_sims / self.batch_count) * 100  # Процент симуляций, закончившихся с прибылью
        
        # Выводим отладочную информацию
        print(f"Calculated stats: avg_profit={avg_profit}, avg_rounds={avg_rounds}, winning_sims={winning_sims}, loss_sims={loss_sims}, win_rate={win_rate}")
        
        # Отображаем результаты
        self.ui_queue.put({
            "batch_complete": True,
            "avg_profit": avg_profit,
            "avg_rounds": avg_rounds,
            "wins": winning_sims,
            "losses": loss_sims,
            "win_rate": win_rate,
            "batch_count": self.batch_count,
            "deposit": deposit
        })
    
    def _poll_queue(self):
        try:
            while True: self._apply_update(self.ui_queue.get_nowait())
        except queue.Empty: pass
        self.after(50, self._poll_queue)

    def _apply_update(self, u):
        lang = self.langs[self.lang]
        
        # Обработка результатов множественных симуляций
        if u.get("batch_complete"):
            # Выводим отладочную информацию
            print("Batch results received:", u)
            
            # Получаем данные с явной проверкой типа
            try:
                avg_profit = float(u.get("avg_profit", 0))
                avg_rounds = float(u.get("avg_rounds", 0))
                wins = int(u.get("wins", 0))
                losses = int(u.get("losses", 0))
                win_rate = float(u.get("win_rate", 0))
                batch_count = int(u.get("batch_count", 0))
                deposit = float(u.get("deposit", 0))
                
                # Выводим распарсенные данные
                print(f"Parsed data: avg_profit={avg_profit}, avg_rounds={avg_rounds}, wins={wins}, losses={losses}, win_rate={win_rate}, batch_count={batch_count}, deposit={deposit}")
            except Exception as e:
                print(f"Error processing batch results: {e}")
                avg_profit = avg_rounds = win_rate = 0.0
                wins = losses = batch_count = 0
                deposit = 0.0
            
            # Создаем окно с результатами
            result_window = tk.Toplevel(self)
            result_window.title(lang["batch_results"])
            result_window.geometry("700x600")
            result_window.grab_set()
            
            # Фрейм для статистики
            stats_frame = ttk.LabelFrame(result_window, text=lang["batch_results"], padding=10)
            stats_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # Отображаем общую статистику
            stats_container = ttk.Frame(stats_frame)
            stats_container.pack(fill=tk.X, pady=10)
            
            # Левая колонка
            left_col = ttk.Frame(stats_container)
            left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
            
            # Правая колонка
            right_col = ttk.Frame(stats_container)
            right_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            
            # Отображаем статистику
            ttk.Label(left_col, text=lang["batch_avg_profit"] + f" {avg_profit:.2f}", font=("Segoe UI", 11)).pack(anchor=tk.W, pady=5)
            ttk.Label(left_col, text=lang["batch_avg_rounds"] + f" {avg_rounds:.2f}", font=("Segoe UI", 11)).pack(anchor=tk.W, pady=5)
            ttk.Label(left_col, text="Win rate: " + f"{win_rate:.2f}%", font=("Segoe UI", 11)).pack(anchor=tk.W, pady=5)
            
            ttk.Label(right_col, text=lang["batch_wins"] + f" {wins}", font=("Segoe UI", 11)).pack(anchor=tk.W, pady=5)
            ttk.Label(right_col, text=lang["batch_losses"] + f" {losses}", font=("Segoe UI", 11)).pack(anchor=tk.W, pady=5)
            ttk.Label(right_col, text=lang["totalsim"] + f"{batch_count}", font=("Segoe UI", 11)).pack(anchor=tk.W, pady=5)
            ttk.Label(right_col, text=lang["inidep"] + f"{deposit:.2f}", font=("Segoe UI", 11)).pack(anchor=tk.W, pady=5)
            
            # Создаем текстовое поле для детальных результатов
            details_frame = ttk.LabelFrame(stats_frame, text="Detailed Results", padding=10)
            details_frame.pack(fill=tk.BOTH, expand=True, pady=10)
            
            # Добавляем скроллбар
            scrollbar = ttk.Scrollbar(details_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            # Текстовое поле для результатов
            results_text = tk.Text(details_frame, height=10, width=50, yscrollcommand=scrollbar.set)
            results_text.pack(fill=tk.BOTH, expand=True)
            scrollbar.config(command=results_text.yview)
            
            # Заполняем результаты
            results_text.insert(tk.END, "Simulation #\tFinal Balance\tSavings\tProfit\tRounds\n")
            results_text.insert(tk.END, "-" * 70 + "\n")
            
            # Выводим отладочную информацию
            print(f"Total batch results to display: {len(self.batch_results)}")
            
            for result in self.batch_results:
                # Выводим отладочную информацию для каждого результата
                print(f"Processing result: {result}")
                
                results_text.insert(tk.END, 
                    f"{result['simulation']}\t\t"
                    f"{result['final_balance']:.2f}\t\t"
                    f"{result['savings']:.2f}\t\t"
                    f"{result['profit']:.2f}\t\t"
                    f"{result['rounds']}\n"
                )
            
            # Делаем текстовое поле доступным только для чтения
            results_text.config(state=tk.DISABLED)
            
            # Кнопка закрытия
            button_frame = ttk.Frame(result_window)
            button_frame.pack(fill=tk.X, pady=10)
            ttk.Button(button_frame, text=lang["apply"], command=result_window.destroy).pack(pady=5)
            
            # Обновляем статус
            self.status_msg.configure(text=lang["finished"])
            return
            
        # Обновление прогресса симуляций
        if u.get("progress"):
            progress = u.get("progress", 0)
            current = u.get("current", 0)
            total = u.get("total", 1)
            self.status_msg.configure(text=f"{lang['simulating']} ({current}/{total}) - {progress:.1f}%")
            return
            
        # Обновление обычной симуляции
        r = u.get('round', self.round_index)
        bank = u.get('bank', self.bankroll)
        bet = u.get('bet', self.current_bet)
        savings = u.get('savings', self.savings_account)
        msg = u.get('msg', '')
        try:
            self.status_round.configure(text=lang["round"].format(r))
            self.status_bank.configure(text=lang["bank"].format(bank))
            self.status_bet.configure(text=lang["bet"].format(bet))
            self.status_savings.configure(text=lang["savings"].format(savings))
            self.status_msg.configure(text=msg)
        except Exception:
            self.status_msg.configure(text=str(msg))
        self._push_point(r, bank, bet, savings)

    def _clear_plot(self):
        self.x_data.clear()
        self.bank_data.clear()
        self.bet_data.clear()
        self.savings_data.clear()
        self.bank_line.set_data([], [])
        self.bet_line.set_data([], [])
        self.savings_line.set_data([], [])
        self._rescale_axes()
        self.canvas_bankroll.draw_idle()
        self.canvas_bet.draw_idle()
        self.canvas_savings.draw_idle()

    def _push_point(self, r=None, b=None, bet=None, savings=None):
        idx = self.round_index if r is None else r
        bank = self.bankroll if b is None else b
        bet_val = self.current_bet if bet is None else bet
        savings_val = self.savings_account if savings is None else savings
        self.x_data.append(idx)
        self.bank_data.append(bank)
        self.bet_data.append(bet_val)
        self.savings_data.append(savings_val)
        self.bank_line.set_data(self.x_data, self.bank_data)
        self.bet_line.set_data(self.x_data, self.bet_data)
        self.savings_line.set_data(self.x_data, self.savings_data)
        self._rescale_axes()
        self.canvas_bankroll.draw_idle()
        self.canvas_bet.draw_idle()
        self.canvas_savings.draw_idle()

    def _rescale_axes(self):
        if not self.x_data:
            self.ax_bankroll.set_xlim(0, 1)
            self.ax_bankroll.set_ylim(0, 1)
            self.ax_bet.set_xlim(0, 1)
            self.ax_bet.set_ylim(0, 1)
            self.ax_savings.set_xlim(0, 1)
            self.ax_savings.set_ylim(0, 1)
            return
        xmin, xmax = min(self.x_data), max(self.x_data)
        # депозит
        self.ax_bankroll.set_xlim(max(0, xmin - 1), xmax + 1)
        ymin, ymax = min(self.bank_data), max(self.bank_data)
        ymin, ymax = (ymin - 1, ymax + 1) if ymin == ymax else (ymin * 0.95, ymax * 1.05)
        self.ax_bankroll.set_ylim(max(0, ymin), ymax)
        # ставка
        self.ax_bet.set_xlim(max(0, xmin - 1), xmax + 1)
        ymin, ymax = min(self.bet_data), max(self.bet_data)
        ymin, ymax = (ymin - 1, ymax + 1) if ymin == ymax else (ymin * 0.95, ymax * 1.05)
        self.ax_bet.set_ylim(max(0, ymin), ymax)
        # savings axis
        self.ax_savings.set_xlim(max(0, xmin - 1), xmax + 1)
        ymin, ymax = min(self.savings_data), max(self.savings_data) if self.savings_data else (0, 1)
        ymin, ymax = (ymin - 1, ymax + 1) if ymin == ymax else (ymin * 0.95, ymax * 1.05)
        self.ax_savings.set_ylim(max(0, ymin), ymax)

    def save_csv(self):
        lang = self.langs[self.lang]
        if not self.results:
            return messagebox.showwarning(lang["warning"], lang["no_data"])
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if path:
            try:
                with open(path, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["round", "bank", "bet", "savings", "msg"])
                    writer.writerows(self.results)
                messagebox.showinfo(lang["ready"], lang["saved"].format(path))
            except Exception as e:
                messagebox.showerror(lang["error"], lang["save_error"].format(e))

    def load_csv(self):
        lang = self.langs[self.lang]
        path = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if not path:
            return
        try:
            with open(path, newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                rows = list(reader)
            parsed = []
            for row in rows:
                if not row:
                    continue
                if row[0].strip().lower() in ("round", "раунд", "r"):
                    continue
                try:
                    r = int(row[0])
                    b = float(row[1]) if len(row) > 1 and row[1] != "" else 0.0
                    bet = float(row[2]) if len(row) > 2 and row[2] != "" else 0.0
                    savings = float(row[3]) if len(row) > 3 and row[3] != "" else 0.0
                    msg = row[4] if len(row) > 4 else ""
                    parsed.append([r, b, bet, savings, msg])
                except Exception:
                    continue
            if not parsed:
                return messagebox.showwarning(lang["warning"], lang["no_data_file"])
            self.results = parsed
            self._clear_plot()
            last_entry = None
            for r, b, bet, savings, msg in self.results:
                self._push_point(int(r), float(b), float(bet), float(savings))
                last_entry = (r, b, bet, savings)
            if last_entry:
                r, b, bet, savings = last_entry
                self.round_index = int(r)
                self.bankroll = float(b)
                self.current_bet = float(bet)
                self.savings_account = float(savings)
                self.status_round.configure(text=lang["round"].format(self.round_index))
                self.status_bank.configure(text=lang["bank"].format(self.bankroll))
                self.status_bet.configure(text=lang["bet"].format(self.current_bet))
                self.status_savings.configure(text=lang["savings"].format(self.savings_account))
            self.status_msg.configure(text=lang["loaded"].format(len(self.results)))
        except Exception as e:
            messagebox.showerror(lang["error"], lang["load_error"].format(e))


if __name__ == "__main__": MartingaleApp().mainloop()

