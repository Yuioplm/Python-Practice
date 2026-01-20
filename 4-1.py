import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.info("処理開始")
logging.info("CSV出力完了")
logging.info("result.csv 出力完了")
