from pathlib import Path

base_dir = Path("Documents")
backup_root = Path("backup")

file_path = base_dir / "work" / "report.txt"

relative_path = file_path.relative_to(base_dir)
backup_path = backup_root / relative_path

print(f"Original: {file_path}")
print(f"Relative: {relative_path}")
print(f"Backup: {backup_path}")
