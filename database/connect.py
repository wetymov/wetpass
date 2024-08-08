import sqlite3

class DataBaseConnect:
    def __init__(self, con: sqlite3.Connection):
        """Класс для подключения к базе данных и быстрого взаимодействия с ней"""
        self.con = con
        self.cur = con.cursor()

    def create_account(self, telegram_id: int):
        try:
            data = (telegram_id,)
            self.cur.execute('INSERT INTO users (telegram_id) VALUES (?)', data)
            self.con.commit()
            return True
        except:
            return False
    
    def create_notice(self, telegram_id: int, name: str, login: str, password: str, desc: str):
        try:
            data = (telegram_id, name, login, password, desc)
            self.cur.execute('INSERT INTO notes (account_id, title, note_login, note_password, desc) VALUES (?, ?, ?, ?, ?)', data)
            self.con.commit()
            return True
        except:
            return False
        
    def get_all_notice(self, telegram_id: int):
        data = (telegram_id,)
        data = self.cur.execute('SELECT * FROM notes WHERE account_id=?', data).fetchall()
        return data
    
    def get_notice(self, id:int):
        data = (id,)
        data = self.cur.execute('SELECT * FROM notes WHERE note_id=?', data).fetchone()
        return data
    

    def remove_notice(self, id: int):
        try:
            data = (id,)
            self.cur.execute('DELETE FROM notes WHERE note_id=?', data)
            self.con.commit()
            return True
        except Exception as e:
            print(e)
            return False