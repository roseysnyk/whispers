from pathlib import Path

from whispers.utils import string_is_function, strip_string


class Php:
    def pairs(self, filepath: Path):
        for line in filepath.open("r").readlines():
            if line.startswith("define"):
                yield from self.parse_define(line)
            elif "=" in line:
                yield from self.parse_assignment(line)

    def parse_assignment(self, line: str):
        key, value = line.split("=")
        key = strip_string(key.replace("$", ""))
        value = strip_string(value.replace(";", ""))
        if not string_is_function(value):
            yield key, value

    def parse_define(self, line: str):
        line = line.replace("define(", "").replace(")", ",").split(",")
        key = strip_string(line[0])
        value = line[1].strip()
        if not string_is_function(value):
            yield key, value
