import csv
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def count_csv(csv_path):
    logging.info("Start processing CSV")

    result = {
        "Excellent" : 0,
        "Pass" : 0,
        "Fail" : 0
    }

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

    except Exception as e:
        logging.error(f"Error while processing CSV: {e}")
        raise

    logging.info("CSV processing completed successfully") 
    return result

def main():
    logging.info("処理開始")

    result = count_csv("scores.csv")

    logging.info(f"Result: {result}")
    print(result)

    logging.info("処理完了")

if __name__ == "__main__":
    main()