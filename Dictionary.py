# Dictionary
scores = {
    "John": 85,
    "Roman": 92,
    "Seth": 75,
    "Dean": 67
}
grades = {}
for score in scores:
    if scores[score] in range(91,101):
        grades[score] = "Outstanding"
    elif scores[score] in range(81,91):
        grades[score] = "Exceeds Expectations"
    elif scores[score] in range(71, 81):
        grades[score] = "Acceptable"
    else:
        grades[score] = "Fail"
print(grades)
