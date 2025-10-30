def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    print(f"{percent}%")
def convert(f):
    x, y = f.split("/")
    return int(x) * 100 // int(y)
if __name__ == "__main__":
    main()