from pathlib import Path
from datetime import datetime, timedelta
import shutil
import logging
import csv
import sys

# ==========================
# 設定
# ==========================
SOURCE_DIR = Path.home() / "Documents"
SCRIPT_DIR = Path(__file__).parent
BACKUP_ROOT = SOURCE_DIR / "backup"
LOG_DIR = SCRIPT_DIR / "logs"
CSV_PATH = SCRIPT_DIR / "backup_list.csv"

BORDER_DATE = datetime.now() - timedelta(days=30)

# ==========================
# ログ設定
# ==========================
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "backup.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# ==========================
# バックアップ処理
# ==========================
def backup_files(src_dir :Path, backup_root :Path):
    logging.info("=== Backup Start ===")