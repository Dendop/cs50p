def arithmetic_arranger(problems, show_answers=False):
    arranged_problems = ""
    for each in problems:
        split_each = each.split()
        first_number = split_each[0]
        operator = split_each[1]
        second_number = split_each[2]
        
        # Calculate the length of the longest number (either first_number or second_number)
        max_length = max(len(first_number), len(second_number))
        
        # Construct the formatted strings
        arranged_problems += f"{first_number:>{max_length + 1}}"
        arranged_problems += "    "  # Add 4 spaces to separate each set
        
    arranged_problems += "\n"  # Add a newline to move to the next line
    
    for each in problems:
        split_each = each.split()
        first_number = split_each[0]
        operator = split_each[1]
        second_number = split_each[2]
        
        # Construct the formatted strings for operator and second number
        arranged_problems += f"{operator} {second_number:>{len(second_number)}}"
        arranged_problems += "    "  # Add 4 spaces to separate each set
        
    print(arranged_problems)
    return problems

def main():
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

if __name__ == "__main__":
    main()
