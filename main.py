import math

def quadratic_calculator(a: int, b: int, c: int):
    discriminant = (b**2 - 4*a*c)

    if a != 0 and discriminant >= 0:  #The coefficient of the x^2 term, a, must be non-zero & discriminant must be none-negative
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)

        return x1, x2
    return None

def main():
    try:
        value_a = float(input("\nEnter the value of a:    "))
        value_b = float(input("Enter the value of b:    "))
        value_c = float(input("Enter the value of c:    "))
    except ValueError:
        print("Please enter a valid coefficient.\n")
    else:
        roots = quadratic_calculator(value_a, value_b, value_c)

        if roots is not None:
            print(f"\nThe roots of the equation are: {roots[0]:.2f}, {roots[1]:.2f}\n")
        else:
            print("Please enter coefficients of a proper quadratic equation!\n")


if __name__ == "__main__":
    print("Quadratic Calculator")
    print(f"{'-'*30}\nA quadratic equation takes the form: ax^2+bx+c=0; where a, b, c are coefficients.\n")

    is_running = True
    while is_running:
        main()
        user_prompt = input("Continue? Y/N: \n")
        if user_prompt.lower() != 'y':
            is_running = False