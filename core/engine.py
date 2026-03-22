import threading
from core.parser import LogParser
from core.analyzer import Analyzer
from core.storage import Storage
from core.logger import logger

class BeruEngine:
    def __init__(self, log_file, config):
        self.parser = LogParser(log_file)
        self.analyzer = Analyzer(config)
        self.storage = Storage()
        self.threads = []
        self.thread_limit = config.get("thread_limit")

    def worker(self, line):
        parsed = self.parser.parse(line)
        alerts = self.analyzer.analyze(parsed)

        for a in alerts:
            self.storage.add(a, parsed)

    def run(self):
        active = []

        for line in self.parser.read_lines():
            t = threading.Thread(target=self.worker, args=(line,))
            t.start()
            active.append(t)

            if len(active) >= self.thread_limit:
                for th in active:
                    th.join()
                active = []

        for th in active:
            th.join()

        logger.log("INFO", "Analysis complete")
        return self.storage.all()
