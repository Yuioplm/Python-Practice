from pathlib import Path

base = Path("C:/Backup")
data_dir = base / "data"
data_dir.mkdir(parents=True, exist_ok=True)

print(data_dir)
