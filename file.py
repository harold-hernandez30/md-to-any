import os
from supported_files import SupportedFiles

class File:
    def __init__(self, parent_dir, filename, is_dir):
        self._filename = filename
        self._is_dir = is_dir
        self._files = []
        full_path = os.path.join(parent_dir, filename)
        if not is_dir:
            content = self._read_content(parent_dir + "/" + filename)
            self.persist(content)
            return
        

        
        files = os.listdir(full_path)
        for file in files:
            if os.path.isdir(os.path.join(full_path, file)) and not SupportedFiles.is_directory_excluded(file):
                self._files.append(File(full_path, file, True))
                print(f"dir: {file}")
            elif SupportedFiles.is_content_file_supported(file):
                new_file = File(full_path, file, False)
                self._files.append(new_file)
        self.is_root = False
        

    def persist(self, content):
        print(f"PERSISTING: {content}")
            

            

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
                    return f"/{file._filename}"
                else:
                    return f"{file._filename}"
        else:
            return self._filename


