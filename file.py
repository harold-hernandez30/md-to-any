import os
from supported_files import SupportedFiles
from sql_storage import SQLiteStorage

class File:
    def __init__(self, parent_dir, filename, is_dir, storage):
        self.filename = filename
        self.location = parent_dir
        self._is_dir = is_dir
        self._files = []
        self._storage = storage
        self.content = ""
        full_path = os.path.join(parent_dir, filename)
        if not is_dir:
            self.content = self._read_content(os.path.join(parent_dir, filename))
            return
        

        
        files = os.listdir(full_path)
        for file in files:
            if os.path.isdir(os.path.join(full_path, file)) and not SupportedFiles.is_directory_excluded(file):
                self._files.append(File(full_path, file, True, storage))
            elif SupportedFiles.is_content_file_supported(file):
                new_file = File(full_path, file, False, storage)
                self._files.append(new_file)
                self.persist(new_file)
        self.is_root = False
        

    def persist(self, file):
        self._storage.add(SQLiteStorage.TABLE_FILES, file)

            
    def _read_content(self, file_path):

        content = ""

        with open(file_path, 'r') as file:
            line = file.readline()
            
            while line:
                content += line
                line = file.readline()
        
        return content

    def __repr__(self):
        if self._files:

            for file in self._files:
                if self._is_dir:
                    return f"/{file.filename}"
                else:
                    return f"{file.filename}"
        else:
            return self.filename


