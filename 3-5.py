import csv

def count_csv(csv_path):
    result = {
        "Excellent" : 0,
        "Pass" : 0,
        "Fail" : 0,
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

def main():
    result = count_csv("scores.csv")

    print(f"Excellent : {result['Excellent']}")
    print(f"Pass : {result['Pass']}")
    print(f"Fail : {result['Fail']}")

if __name__ == "__main__":
    main()