import csv
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def count_csv(csv_path):
    logging.info("CSV処理を開始")

    result = {
        "Excellent" : 0,
        "Pass" : 0,
        "Fail" : 0
    }

    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for i, row in enumerate(reader, start=1):
                try:
                    score = int(row["score"])

                    if score < 0 or score > 100:
                        logging.warning(
                            f"Invalid score detected (row {i}): {score}"
                        )
                        continue
                    elif score == 100:
                        logging.warning(f"Perfect score detected (row {i}): 100")
                        result["Excellent"] += 1
                        continue

                    if score >= 80:
                        result["Excellent"] += 1
                    elif score >= 60:
                        result["Pass"] += 1
                    else:
                        result["Fail"] += 1
                
                except ValueError:
                    logging.warning(
                        f"Score is not a number (row {i}): {row['score']}"
                    )
                    continue

    except Exception as e:
        logging.error(f"Fatal error: {e}")
        raise

    logging.info("CSV processing finished successfylly")
    
    return result

def main():
    logging.info("Processing start")

    result = count_csv("scores.csv")

    logging.info(f"集計結果: {result}")
    print(result)

    logging.info("Processing finished")

if __name__ == "__main__":
    main()