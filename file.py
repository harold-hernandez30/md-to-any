import os
from supported_files import SupportedFiles

class File:
    def __init__(self, parent_dir, filename, is_dir):
        self._filename = filename
        self._is_dir = is_dir
        self._files = []
        self._content = ""
        if not is_dir:
            return
        

        new_parent_dir = parent_dir + "/" + filename
        files = os.listdir(new_parent_dir)
        for file in files:
            if os.path.isdir(new_parent_dir + "/" + file) and not SupportedFiles.is_directory_excluded(file):
                self._files.append(File(new_parent_dir, file, True))
                print(f"dir: {file}")
            elif SupportedFiles.is_content_file_supported(file):
                self._files.append(File(new_parent_dir, file, False))
                self._populate_content(new_parent_dir + "/" + file)
        self.is_root = False

    def _populate_content(self, file_path):

        with open(file_path, 'r') as file:
            line = file.readline()
            
            while line:
                self._content += line
                line = file.readline()
        
        print(f"content: {self._content}")

    def __repr__(self):
        if self._files:

            for file in self._files:
                if self._is_dir:
                    return f"/{file._filename}"
                else:
                    return f"{file._filename}"
        else:
            return self._filename


