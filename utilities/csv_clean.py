import csv
import sys
def clean_csv(input_file, output_file):
    cleaned_rows = [] 
    with open(input_file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
                    if not any(row):
                         continue
                    cleaned = [cell.strip() for cell in row]
        cleaned_rows.append(cleaned)
    with open(output_file, 'w', newline='') as f:
         writer = csv.writer(f)
         writer.writerows(cleaned_rows)
if __name__ == "__main__":
        if len(sys.argv) == 3:
         input_name, output_name = sys.argv[1], sys.argv[2]
        else:
         input_name = input("Input csv filename: ").strip()
output_name = input("Output csv filename: ").strip()
clean_csv(input_name, output_name)
print("csv cleaned and saved.")