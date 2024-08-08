class Template:


    def __init__(self, type: str) -> None:
        """Класс шаблонов текста"""
        self.type = type


    def get_help(self):
        self.text = """Команды и их описание, которые может выполнять этот бот.
══════════════════════════════════════
Команды, доступные всегда:
══════════════════════════════════════
/start - Приветствие, и небольшое описание возможностей бота.
/about - О разработчике.
/help - Очень трудно догадаться (выводит это сообщение).
══════════════════════════════════════
Команды, доступные для заметок:
/all - Вывод всех заметок пользователя
/downloaddata - Скачать ВСЕ данные, которые есть на сервере о пользователе
/add - Добавление в базу данных заметки
/remove - Удаление из базы данных заметки
        """
        return self.text


    def get_start(self):
        self.text = """Привет!\nЯ - бот, предназначенный для хранения паролей.
Ваш аккаунт уже создан, никто не сможет получить к нему доступ, т.к он привязан только к вашему ID в telegram
══════════════════════════════════════
Используйте команду /help, если растерялись.\n\nУдачи.
        """
        return self.text
    
    
    def get_add(self):
        self.text = """ЗАПИСЬ НОВОГО АККАУНТА
Запиши его следующим сообщением в формате
"name login password description"
"""
        return self.text
    
    
    def get_all(self):
        self.text = """Вот все ваши заметки, которые я смог найти
Чтобы показать содержимое, нажми на кнопку с интересующей заметкой
"""
        return self.text


    def get_remove(self):
        self.text = """Вот все ваши заметки, которые я смог найти
Чтобы удалить содержимое, нажми на кнопку с необходимой тебе заметкой
"""
        return self.text


    def get_empty(self):
        self.text = """У вас отсутствуют заметки, завести их можно с помощью команды /add
"""
        return self.text



    def generate(self) -> None:
        self.templates = {
            "start" : self.get_start(),
            "help" : self.get_help(),
            "add" : self.get_add(),
            "all" : self.get_all(),
            "empty" : self.get_empty(),
            "remove" : self.get_remove(),
        }


    def get(self) -> str:
        self.generate()
        return self.templates[self.type]