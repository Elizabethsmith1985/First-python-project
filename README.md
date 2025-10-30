#  Utilities - Python Basics

Small, clean command_line utilities that show input conversion output formatting, and basic control flow.

These scripts are intentionally simple on the surface but demonstrate: 
- Parsing strings into numeric values
- Cleaning and converting input formats
- Performing calculations
- Providing clear printed output

---

## 1) Tip calculator ('utilities/tip.py') 
Parses dollar amounts (like $12.50) and percentages (like 15%) to calculates tip precisely. 
Run:
python3 utilities/tip.py

## 2) Fuel Fraction to Percentage ('utilities/convert.py')
Converts fuel fractions like 3/4, 1/2, and 99/100 into a percentage.
Run:
python3 utilities/convert.py

## 3) Fuel Gauge Display ('utilities/gauge.py')
Displays E (Empty), F (Full), or a percentage for intermediate fuel levels.
Run:
python3 utilities/gauge.py

### Folder Structure
FIRST-PYTHON-PROJECT
| 
|-Utilities
|   |-tip.py
|   |-convert.py
|.  |-gauge.py
|
|-README