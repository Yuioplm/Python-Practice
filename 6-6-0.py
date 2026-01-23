from pathlib import Path
from datetime import datetime, timedelta
import logging

logging.basicConfig(
    filename="scan.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def scan_recent_files(base_dir):
    logging.info(f"Scan start: {base_dir}")

    border_date = datetime.now() - timedelta(days=30)
    logging.info(f"Border date: {border_date}")

    count = 0

    for path in base_dir.rglob("*"):
        if not path.is_file():
            continue

        last_modified = datetime.fromtimestamp(path.stat().st_mtime)

        if last_modified >= border_date:
            logging.info(f"TARGET : {path}")
            count += 1
        else:
            logging.info(f"SKIP   : {path}")
    
    logging.info(f"Target files count: {count}")
    logging.info("Scan finished")

def main():
    base = Path.home() / "Documents"
    scan_recent_files(base)

if __name__ == "__main__":
    main()