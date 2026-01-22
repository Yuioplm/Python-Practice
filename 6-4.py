from pathlib import Path
import shutil

src_dir = Path("source")
dst_dir = Path("backup/source")

if dst_dir.exists():
    shutil.rmtree(dst_dir)

shutil.copytree(src_dir, dst_dir)
print(f"Copied {src_dir} -> {dst_dir}")