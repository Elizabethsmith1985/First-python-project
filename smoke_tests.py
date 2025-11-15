from csv_clean import clean_csv 
import os
import csv
INPUT = "utilities/messy.csv"
OUTPUT = "utilities/tmp_cleaned.csv"
clean_csv(INPUT, OUTPUT)
print("running smoke tests...")
with open (OUTPUT, newline="") as f:
    reader = csv.reader(f)
    header = next(reader, None)
    assert header == ["name", "age", "location"], f"Bad header: {header}"
    rows = list(reader)
    for r in rows
        assert any(c.strip() for c in r), f"Empty row found: {r}"
    for r in rows:
        assert len(r) == 3, f"Row has wrong number of columns: {r}"
    for r in rows:
        assert all(c.strip() for c in r), f"Missing vallue not filled: {r}"
    for r in rows:
        assert r[0] == r[0].title(), f"Name not title-cased: {r}"
        assert r[2] == r[2].title(), f"location not title-cased: {r}"
print("All smoke tests passed.")