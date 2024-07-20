import re

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        print("Error: Too many problems.")
    
    
    operators = []
    
    for each in problems:
        element = each.split()
        operators.append(element[1])
        
        if(re.search("[/]", each) or re.search("[*]", each)):
            print("Error: Operator must be '+' or '-' .")
            
        
        
        
        #QUICK CHECK FOR LENGHT OF NUMBERS
        for i in element:
            if len(i) > 4:
                print("Error: Numbers cannot be more than four digits.")
        
        #assing numbers 
        first_number = element[0]
        second_number = element[2]
    #CHECK FOR OPERATORS
    #for i in operators:
        #if i == '/' or i == '*':
            #print("Error: Operator must be '+' or '-' .")
         
        
        
        
    
def main():
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    
if __name__ == "__main__":
    main()
