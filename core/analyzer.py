from collections import defaultdict
from core.patterns import PatternLibrary

class Analyzer:
    def __init__(self, config):
        self.patterns = PatternLibrary()
        self.ip_hits = defaultdict(int)
        self.config = config

    def analyze(self, parsed):
        alerts = []

        ip = parsed["ip"]
        raw = parsed["raw"]

        if ip:
            self.ip_hits[ip] += 1
            if self.ip_hits[ip] > self.config.get("bruteforce_threshold"):
                alerts.append("BRUTE_FORCE")

        alerts.extend(self.patterns.match(raw))

        if parsed["length"] > self.config.get("max_line_length"):
            alerts.append("LONG_PAYLOAD")

        return alerts
