from pathlib import Path

base_dir = Path("source")
backup_root = Path("backup")

file_path = base_dir / "data" / "sample.txt"

relative_path = file_path.relative_to(base_dir)
backup_path = backup_root / relative_path

print(backup_path)
