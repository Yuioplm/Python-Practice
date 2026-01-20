import csv

def count_scores(csv_path):
    result = {
        "Excellent" : 0,
        "Pass" : 0,
        "Fail" : 0
    }

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
    return result

def write_result_csv(result, output_path):
    rows = []
    for key, value in result.items():
        rows.append({
            "category" : key,
            "count" : value
        })
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["category", "count"]
        )
        writer.writeheader()
        writer.writerows(rows)

def main():
    result = count_scores("scores.csv")
    write_result_csv(result, "result.csv")

if __name__ == "__main__":
    main()