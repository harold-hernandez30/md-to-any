
import re
from heading import Heading

class MD:
    def __init__(self, file_content):
        self.headings = self._find_headings(file_content)


    def _find_headings(self, file_content):
        headings = []
        for line in file_content.splitlines():
            if line.startswith('#'):     
                match = re.search("^[#]{1,}", line)
                groups = re.split(match.group(), line)
                text_list = list(filter(lambda line: line, groups))
                if len(text_list) == 1:
                    headings.append(Heading(text_list[0].strip(), match.group()))

        return headings

        # find top heading

        # find metadata
        # if no root heading, find multiple same-level heading

        # heading
        #  can have heading
        #   content
        # tags
        # 