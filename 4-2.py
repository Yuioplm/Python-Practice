import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s [%(levelname)s] %(message)s"
)

try:
    with open("sample.txt", "r", encoding="utf-8") as f:
        data = f.read()
    logging.info("ファイル読み込み成功")
except Exception as e:
    logging.error(f"ファイル読み込み失敗: {e}")
