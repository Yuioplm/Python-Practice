import csv

excellent = 0
passed = 0
failed = 0

with open("scores.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        score = int(row["score"])
        if score >= 80:
            excellent += 1
        elif score >= 60:
            passed += 1
        else:
            failed += 1

print(f"Excellent : {excellent}")
print(f"Passed : {passed}")
print(f"Failed : {failed}")