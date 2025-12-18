import csv
def find_duplicates_from_list(names):
    """
    Take a list of names and return a dictionary of duplicates and their counts.
    """
    counts = {}
    for name in names:
        name = str(name).strip()
        if not name:
            continue
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1
    duplicates = {name: count for name, count in counts.items() if count > 1}
    return  duplicates
def find_duplicates_from_csv(filename):
    """
    read a csv file, extract names from comlumn 6 (index 5), and return a dictionary of duplicates and their counts.
    """
    names = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader, None) # skip header row
        for row in reader:
            if not row:
                continue
            if len(row) > 5: raw_name = row[5]
            else:
                raw_name = row[0] 
            names.append(raw_name)
    return find_duplicates_from_list(names)
if __name__ == "__main__":
    filename = "utilities/cleaned.csv"
    dups = find_duplicates_from_csv(filename)
    print("duplicates dictionary:", dups)
    for name, count in dups.items():
        print(f"{name}: {count}")