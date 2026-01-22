import csv
import logging
import sys

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def count_csv(csv_path):
    logging.info(f"[count_csv] Start: {csv_path}")

    result = {
        "Excellent" : 0,
        "Pass" : 0,
        "Fail" : 0
    }

    total = 0
    skipped = 0

    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for i, row in enumerate(reader, start=1):
                total += 1
                try:
                    score = int(row["score"])

                    if score < 0 or score > 100:
                        skipped += 1
                        logging.warning(
                            f"[csv_count] Invalid score (row {i}): {score}"
                        )
                        continue

                    if score >= 80:
                        result["Excellent"] += 1
                    elif score >= 60:
                        result["Pass"] += 1
                    else:
                        result["Fail"] += 1

                except ValueError:
                    skipped += 1
                    logging.warning(
                        f"[count_csv] Non-numeric score (row {i}): {row['score']}"
                    )

    except Exception as e:
        logging.error(
            f"[count_csv] Fatal error : {e}"
        )
        raise
    
    logging.info(
        "[SUMMARY] "
        f"total={total} "
        f"excellent={result['Excellent']} "
        f"pass={result['Pass']} "
        f"fail={result['Fail']} "
        f"skipped={skipped} "
    )

    logging.info(
        f"[count_csv] Finished normally"
    )
    return result

def main():
    logging.info("Processing start")

    try:
        result = count_csv("scores.csv")
        logging.info(f"[Main] Result: {result}")
        logging.info("Processing finished normally")
        sys.exit(0)
    except Exception:
        logging.error("Processing failed")
        sys.exit(1)

if __name__ == "__main__":
    main()