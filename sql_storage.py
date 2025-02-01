
from storage import Storage
import sqlite3
import hashlib

class SQLiteStorage(Storage):
    TABLE_FILES = "files"

    def __init__(self):
        super().__init__()
        self._cursor = None


    def start(self):
        self._connection = sqlite3.connect("vault.db")
        self._cursor  = self._connection.cursor()
        self._create_table(SQLiteStorage.TABLE_FILES)

    def _check_table_exists(self, table_name):
         # Use a parameterized query for safety and fetch the result
        self._cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    
        return self._cursor.fetchone() is not None

    def _create_table(self, table_name):
        
        if self._check_table_exists(SQLiteStorage.TABLE_FILES) is None:
            self._cursor.execute(f"Create TABLE {table_name} (hash TEXT, path TEXT, filename TEXT, content TEXT)")
            if self._check_table_exists(SQLiteStorage.TABLE_FILES) != None:
                print(f"Table '{table_name}' created")

        self._connection.commit()

    def add(self, table_name, file):
        hash = hashlib.sha256(file.content.encode('utf-8')).hexdigest()
        self._cursor.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?)", (hash, file.location, file.filename, file.content))
        self._connection.commit()


    def update(self):
        pass

    def delete(self):
        pass

    def get(self):
        return super().get()


    def end(self):
        self._connection.close()