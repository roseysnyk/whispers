from pathlib import Path

from whispers.utils import string_is_function, string_is_quoted


class Javascript:
    def pairs(self, filepath: Path):
        for line in filepath.open("r").readlines():
            if line.count("=") == 1:
                yield from self.parse_assignment(line)

    def parse_assignment(self, line: str):
        key, value = line.split("=")
        value = value.replace(";", "").strip()
        if string_is_quoted(value) and not string_is_function(value):
            yield key, value
