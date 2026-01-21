import csv
import logging

# ===== Logging 設定 =====
logging.basicConfig(
    filename="process.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def count_csv(csv_path):
    result = {
        "Excellent" : 0,
        "Pass" : 0,
        "Fail" : 0
    }

    logging.info(f"Read CSV: {csv_path}")

    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                score = int(row["score"])

                if score >= 80:
                    result["Excellent"] += 1
                elif score >= 60:
                    result["Pass"] += 1
                else:
                    result["Fail"] += 1

        logging.info(f"Count finished")

    except Exception as e:
        logging.error(f"Error: {e}")
        raise

    return result

def main():
    logging.info("Process start")

    result = count_csv("scores.csv")

    for k, v in result.items():
        logging.info(f"{k} : {v}")
        print(f"{k} : {v}")

    logging.info("Process end")

if __name__ == "__main__":
    main()