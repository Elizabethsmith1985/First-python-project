from utilities.text_clean import clean_text
from utilities.csv_clean import clean_csv
from utilities.city_counts import count_cities
from utilities.duplicate_finder import find_duplicates_from_csv, find_duplicates_from_list
import os
import csv
INPUT = "utilities/messy.csv"
OUTPUT = "utilities/tmp_cleaned.csv"
clean_csv(INPUT, OUTPUT)
print("Running smoke tests...")
with open (OUTPUT, newline="") as f:
    reader = csv.reader(f)
    header = next(reader, None)
    assert header == ["name", "age", "location"], f"Bad header: {header}"
    rows = list(reader)
    for r in rows:
        assert any(c.strip() for c in r), f"Empty row found: {r}"
    for r in rows:
        assert len(r) == 3, f"Row has wrong number of columns: {r}"
    for r in rows:
        assert all(c.strip() for c in r), f"Missing vallue not filled: {r}"
    for r in rows:
        assert r[0] == r[0].title(), f"Name not title-cased: {r}"
        assert r[2] == r[2].title(), f"location not title-cased: {r}"
print("All smoke tests passed.")
print("Running extra tests...")
# Test: cleaned.csv should exist and not be empty
assert os.path.exists(OUTPUT), "Output file missing."
print("Test: Names are title-cased...OK")
with open(OUTPUT, newline="") as f:
    reader = csv.reader(f)
    next(reader) #skip header
    for row in reader:
        assert row[0] == row[0].title(), f"Name not title-cased:{row}"
#test: Locations are title-cased
print("Test: Locations are title-cased...", end="")
with open(OUTPUT, newline="") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for row in reader:
        assert row[2] == row[2].title(), f"Location not title-cased: {row}"
print ("OK")
# Test: Missing values filled with 'Unknown'
print("Test: Missing values filled...", end="")
with open(OUTPUT, newline="") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for row in reader:
        for cell in row:
            assert cell.strip() != "", f"Blank value found: {row}"
print ("OK")
# Test: ages are valid or 'unknown'
print ("Test: Ages are valid...", end="")
with open(OUTPUT, newline="") as f:
    reader = csv.reader (f)
    next(reader)
    for row in reader:
        age = row[1].strip()
        assert age == "Unknown" or age.isdigit(), f"Invalid age found: {row}"
print("OK")
print("Running text_clean tests...")
# create a small messy text file
with open("utilities/messy.txt", "w", encoding="utf-8") as f:
    f.write("   hello. \n")
    f.write("this  is   my  messy text\n")
clean_text("utilities/messy.txt", "utilities/cleaned.txt")
with open("utilities/cleaned.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]
assert lines == ["hello", "this is my messy text"], f"Unexpected cleaned text: {lines}"
print("Text-clean tests passed!")
print("Running city_counts tests...")
counts = count_cities("utilities/cleaned.csv")
assert counts == {"Nyc": 1, "La": 2, "Seattle": 2, "Chickamauga": 2, "Bend": 1, "Sandy River": 1, "Chicago": 1}
f"Unexpected city counts: {counts}"
print ("city_counts tests passed!")
print("Running duplicate_finder tests...")
test_names = {"Bob", "Bob", "Thomas", "Thomas", "Bob", "Alice"}
result = find_duplicates_from_csv("utilities/cleaned.csv")
print("DEBUG duplicate result from CSV:", result)
assert result == {"Bob: 3", "Thomas: 2"}, f"Unexpected result: {result}"
# no duplicates test 
no_dup_names = ["Alice", "Charlie", "Candice"]
no_dup_result = find_duplicates_from_list(no_dup_names)
print("DEBBUG no_result:", no_dup_result)
assert no_dup_result == {}, f"Expected no duplicates, got: {no_dup_result}"
print ("duplicate_finder tests passed!")