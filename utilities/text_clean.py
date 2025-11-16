def clean_text(input_file, output_file):
    cleaned_lines = [] 
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            stripped = line.strip()
            if not stripped: 
                continue
            normalized = " ".join(stripped.split())
            normalized = "".join(ch for ch in normalized if ch.isalnum() or ch.isspace())
            cleaned_lines.append(normalized)
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in cleaned_lines:
            f.write(line + "\n")
if __name__ == "__main__":
   input_name = input("Input text filename: ").strip()
   output_name = input("Output text filename: ").strip()
   clean_text(input_name, output_name)
print("Text cleaned and saved.")