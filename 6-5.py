from pathlib import Path
import shutil
import logging

logging.basicConfig(
    filename="backup.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def backup_directory(src_dir :Path, dst_dir :Path):
    logging.info(f"Backup start: {src_dir} -> {dst_dir}")

    try:
        if not src_dir.exists():
            raise NotADirectoryError(f"Source not found: {src_dir}")

        if dst_dir.exists():
            shutil.rmtree(dst_dir)
            logging.info(f"Existing backup removeed: {dst_dir}")
        
        shutil.copytree(src_dir, dst_dir)
        logging.info("Backup completed successfully")
        logging.info(f"Backup target: {dst_dir}")
    
    except Exception as e:
        logging.error(f"Backup failed: {e}")
        raise

def main():
    logging.info("=== Backup process started ===")

    src = Path("output/source")
    dst = Path("output/backup/source")

    backup_directory(src, dst)
    logging.info("=== Backup process finished ===")

if __name__ == "__main__":
    main()