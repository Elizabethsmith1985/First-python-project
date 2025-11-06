import csv

def clean_csv(input_file, output_file, fill_value="Unknown"):
    cleaned_rows = [] 
    with open(input_file, newline='')as f:
        reader = csv.reader(f) 
        for row in reader:
            if all(cell.strip() == "" for cell in row):
                continue
            cleaned = [cell.strip() if cell.strip() else fill_value for cell in row]
            cleaned_rows.append(cleaned)
    with open(output_file, 'w', newline='')as f:
        writer = csv.writer(f)
        writer.writerows(cleaned_rows)
if __name__ == "__main__":
    input_name = input("Input csv filename: ").strip()
    output_name = input("Output csv filename: ").strip()
    clean_csv(input_name, output_name)
    print("csv cleaned and saved.")