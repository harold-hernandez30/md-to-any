import os

class File:
    def __init__(self, parent_dir, filename, is_dir):
        self._filename = filename
        self._is_dir = is_dir
        self._files = []
        if not is_dir:
            return

        new_parent_dir = parent_dir + "/" + filename
        files = os.listdir(new_parent_dir)
        for file in files:
            if os.path.isdir(new_parent_dir + "/" + file) and not file.startswith("."):
                self._files.append(File(new_parent_dir, file, True))
                print(f"dir: {file}")
            elif file.endswith('.md'):
                self._files.append(File(new_parent_dir, file, False))
                print(f"file: {file}")
        self.is_root = False

    def __repr__(self):
        if self._files:

            for file in self._files:
                if self._is_dir:
                    return f"/{file._filename}"
                else:
                    return f"{file._filename}"
        else:
            return self._filename


