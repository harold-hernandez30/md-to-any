from file import File
from sql_storage import SQLiteStorage

class FileManager:
    def __init__(self, full_path_directory):
        sqliteStorage = SQLiteStorage()
        sqliteStorage.start()
        self._main = File(full_path_directory, '', True, sqliteStorage)
        sqliteStorage.end()

