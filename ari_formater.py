def arithmetic_arranger(problems, show_answers=False):
    arranged_problems = ""
    
    # Lists to store the lengths of each number in the problem
    first_number_lengths = []
    second_number_lengths = []
    
    # Loop through each problem to collect lengths of numbers
    for each in problems:
        split_each = each.split()
        first_number_lengths.append(len(split_each[0]))
        second_number_lengths.append(len(split_each[2]))
        
        # Construct the formatted strings for the first number
        arranged_problems += f"{split_each[0]:>{len(split_each[2])}}    "
    arranged_problems += "\n"  # Add a newline to move to the next line
    
    # Loop through each problem to construct formatted strings for the operator and second number
    for each in problems:
        split_each = each.split()
        
        # Construct the formatted strings for the operator and second number
        arranged_problems += f"{split_each[1]} {split_each[2]:>{len(split_each[0])}}    "
    
    arranged_problems += "\n"  # Add a newline before the line of dashes
    
    # Calculate the maximum length of all numbers in the problems
    max_length_all = max(max(first_number_lengths), max(second_number_lengths))
    
    # Construct the line of dashes
    arranged_problems += "-" * (max_length_all + 2)  # Add a line of dashes
    
    print(arranged_problems)
    return problems

def main():
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

if __name__ == "__main__":
    main()
