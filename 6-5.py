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
            logging.e