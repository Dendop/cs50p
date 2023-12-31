#assume that the user will input values in the expected formats
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    #remove $ and then convert into float
    dollars = dollars.lstrip('$')
    return float(dollars)

def percent_to_float(percent):
    #remove % adn then /100
    percent = percent.lstrip('%')
    return float(percent) / 100


if __name__ == "__main__":
    main()