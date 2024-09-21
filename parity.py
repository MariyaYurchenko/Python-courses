def main():
    try:
        num = int(input("?: x = "))     
        if is_even(num):
            parity = "even"
        else:
            parity = "odd"
        print(f"{num} is {parity} integer number.")
    
    except ValueError:
        print("Exception: user input is not an integer number.")

def is_even(x):
    return (x % 2 == 0)

main()