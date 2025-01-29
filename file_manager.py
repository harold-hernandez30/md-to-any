from file import File

class FileManager:
    def __init__(self, full_path_directory):

        self._main = File(full_path_directory, '', True)
