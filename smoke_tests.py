from utilities.csv_clean import clean_csv
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