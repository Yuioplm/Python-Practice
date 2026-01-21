import csv

with open("scores.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        name = row["name"]
        score = int(row["score"])

        if score >= 80:
            print(f"{name} : Excellent")
        elif score >= 60:
            print(f"{name} : Pass")
        else:
            print(f"{name} : Fail")
