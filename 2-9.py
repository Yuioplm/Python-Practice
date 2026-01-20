scores = [45, 80, 72, 90]

excellent = 0
passed = 0
failed = 0

for score in scores:
    if score >= 80:
        excellent += 1
    elif score >= 60:
        passed += 1
    else:
        failed += 1

print(f"Excellent : {excellent}")
print(f"Pass : {passed}")
print(f"Fail : {failed}")
