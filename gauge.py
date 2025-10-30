def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    print(gauge(percent))
def convert(f):
    x, y = f.split("/")
    return int(x) * 100 // int(y)
def gauge(p):
    if p <=1:
        return "E"
    elif p>=99:
        return "F"
    else: 
        return f"{p}%"
if __name__ == "__main__":
    main()