import csv
import string
def clean_csv(input_file, output_file, fill_value="Unknown"):
    cleaned_rows = []
    with open(input_file, newline='')as f:
        reader = csv.reader(f, skipinitialspace=True) 
        header = next(reader, None) 
        # If we have a header, clean it up. Otherwise, make a default one.
        if header:
            header = [h.strip() for h in header]
        else:
            header = ["name", "age", "location"]
        cleaned_rows.append(header)
        for row in reader:
            if not any(cell.strip() for cell in row):
                continue
            row = (row + [""] * 3)[:3]
            name, age, location = [c.strip() or fill_value for c in row]
            name = " ".join(name.split())
            location = " ".join(location.split())
            location = location.strip(string.punctuation)
            import re
            digits = re.findall(r"\d+", age)
            age = digits[0] if digits else "Unknown"
            name = name.title()
            age = age if age else fill_value
            location = location.title()
            cleaned_rows.append([name, age, location])
    with open(output_file, 'w', newline='')as f:
        writer = csv.writer(f)
        writer.writerows(cleaned_rows)
if __name__ == "__main__":
    input_name = input("Input csv filename: ").strip()
    output_name = input("Output csv filename: ").strip()
    clean_csv(input_name, output_name)
    print("csv cleaned and saved.")