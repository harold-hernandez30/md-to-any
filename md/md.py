
import re
from heading import Heading

class MD:
    def __init__(self, file_content):
        self.headings = []
        self.content_lines = []
        self._populate(file_content)


    def _populate(self, file_content):
        for line in file_content.splitlines():
            if len(line) == 0:
                continue

            if line.startswith('#'):     
                match = re.search("^[#]{1,}", line)
                groups = re.split(match.group(), line)
                text_list = list(filter(lambda line: line, groups))
                if len(text_list) == 1:
                    self.headings.append(Heading(text_list[0].strip(), match.group()))
            else:
                self.content_lines.append(line) 
