from pathlib import Path
import shutil


src = Path("data/test.txt")

dst_dir = Path("backup/data")
dst_dir.mkdir(parents=True, exist_ok=True)


dst = dst_dir / src.name
shutil.copy2(src, dst)

print(dst)