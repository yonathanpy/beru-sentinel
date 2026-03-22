import sys
from core.engine import BeruEngine
from core.config import Config
from core.logger import logger

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <logfile>")
        return

    config = Config()
    engine = BeruEngine(sys.argv[1], config)

    logger.log("INFO", "Starting Beru Sentinel")
    results = engine.run()

    for key, values in results.items():
        print(f"\n[{key}] ({len(values)})")
        for v in values[:3]:
            print(v["raw"][:120])

if __name__ == "__main__":
    main()
