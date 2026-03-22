class PatternLibrary:
    def __init__(self):
        self.patterns = {
            "SQLI": ["select", "union", "insert", "drop", "--"],
            "XSS": ["<script>", "onerror=", "alert("],
            "LFI": ["../", "/etc/passwd"],
        }

    def match(self, raw):
        results = []
        low = raw.lower()

        for name, plist in self.patterns.items():
            for p in plist:
                if p in low:
                    results.append(name)
                    break

        return results
