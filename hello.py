def main():
    name = input("Hello, what is your name? ").strip().title()
    hello(name)

    x = round(float(input("x = ")),1)
    print(f"{square_input(x):.2f}")

    y = round(float(input("y = ")),1)
    print(f"{add_input(x, y):.2f}")
    print(f"{div_input(x, y):.2f}")
    
def add_input(x, y): # Add input values
    print("x + y = ", end="")
    return x + y

    print(f"{x + y:,}")

def div_input(x, y):    # Divide input values
    print("x / y = ", end="")
    return x / y

def hello(to = "world"):    
    print("\"Nice\" to meet you", to, sep = ", ", end = ". ")
    print(f"I mean it, {to}. You seem very \"nice\".")

def square_input(x): # Calculate square of input value
    print("The square of x is ", end="")
    return pow(x, 2)

main()

