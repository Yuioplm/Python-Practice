from pathlib import Path
import shutil

src = Path("scores.csv")
dst_dir = Path("zz")
dst_dir.mkdir(parents=True, exist_ok=True)

dst = dst_dir / src.name
shutil.copy2(src, dst)
print(dst)