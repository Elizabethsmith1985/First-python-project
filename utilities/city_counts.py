import csv
def count_cities(input_file):
    with open(input_file, newline='')as f:
       reader = csv.reader(f)
       next(reader) # skip header row
       city_counts = {}
       for row in reader:
           city = row[2].strip()
           if city in city_counts:
               city_counts[city] += 1
           else:
               city_counts[city] = 1
    return city_counts
if __name__ == "__main__":
    input_name = input("Input csv filename: ").strip()
    results = count_cities(input_name)
    for city, count in results.items():
        print(city, ":", count)