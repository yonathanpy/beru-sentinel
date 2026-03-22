import re

class LogParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_lines(self):
        with open(self.file_path, "r", errors="ignore") as f:
            for line in f:
                yield line.strip()

    def parse(self, line):
        ip = self._extract_ip(line)
        method = self._extract_method(line)

        return {
            "raw": line,
            "ip": ip,
            "method": method,
            "length": len(line)
        }

    def _extract_ip(self, line):
        match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
        return match.group(0) if match else None

    def _extract_method(self, line):
        match = re.search(r'(GET|POST|PUT|DELETE)', line)
        return match.group(0) if match else None
