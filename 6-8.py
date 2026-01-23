from pathlib import Path
from datetime import datetime, timedelta
import shutil
import logging

logging.basicConfig(
    filename="backup.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def backup_recent_file(src_dir :Path, backup_root :Path, days: int = 30):
    logging.info("=== Backup Start ===")
    logging.info(f"Source: {src_dir}")
    logging.info(f"BackupRoot: {backup_root}")

    border_date = datetime.now() - timedelta(days=days)
    logging.info(f"BorderDate: {border_date}")

    success = 0
    skipped = 0

    try:
        if not src_dir.exists():
            raise FileNotFoundError(f"Source directory not found: {src_dir}")
        
        for path in src_dir.rglob("*"):
            if not path.is_file():
                continue
            
            last_modified = datetime.fromtimestamp(path.stat().st_mtime)
            if last_modified < border_date:
                continue

            relative_path = path.relative_to(src_dir)
            dst_path = backup_root / relative_path
            dst_path.parent.mkdir(parents=True, exist_ok=True)

            try:
                shutil.copy2(path, dst_path)
                logging.info(f"SUCCESS: {path}")
                success += 1

            except Exception as e:
                logging.warning(f"SKIPPED: {path}")
                skipped += 1
    
    except Exception as e:
        logging.error(f"FATAL: {e}")
        raise

    logging.info(f"SUMMARY: Success={success}, Skipped={skipped}")
    logging.info("=== Backup End ===")

def main():
    src = Path("output/source")
    backup_root = Path("output/backup")

    backup_recent_file(src, backup_root)

if __name__ == "__main__":
    main()