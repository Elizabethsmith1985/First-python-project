import csv

def count_cities(csv_filename):
    city_counts = {}
    with open(csv_filename, newline="", encoding="utf-8")as f:
        reader = csv.reader(f)
        next (reader) #  Skip header row
        for row in reader:
            if len(row) >3:
               continue
            name, age, location = [cell.strip() for cell in row]
            if not location:
                continue
            if location in city_counts:
                city_counts[location] += 1
            else:
               city_counts[location] = 1
    return city_counts

def main():
    counts = count_cities("utilities/cleaned.csv")
    for city, count in counts.items():
        print(f"{city}: {count}")

if __name__ == "__main__":
    main()