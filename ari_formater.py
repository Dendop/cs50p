import re

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return("Error: Too many problems.")
    
    
    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""
    
    for each in problems:
        element = each.split()
        
        
        if(re.search("[/]", each) or re.search("[*]", each)):
            return("Error: Operator must be '+' or '-' .")
            
        
        
        
        #QUICK CHECK FOR LENGHT OF NUMBERS
        for i in element:
            if len(i) > 4:
                return("Error: Numbers cannot be more than four digits.")
        
        #assing numbers 
        first_number = element[0]
        second_number = element[2]
        operator = element[1]
        
        sum = ""
        
        if(operator == "+"):
            sum += str(int(first_number) + int(second_number))
        elif(operator == "-"):
            sum += str(int(first_number) - int(second_number))
        
        lenght = max(len(first_number), len(second_number)) + 2
        top = str(first_number).rjust(lenght)
        bottom = operator + str(second_number).rjust(lenght - 1)
        line = ""
        result = str(sum).rjust(lenght)
        for k in range(lenght):
            line += "-"
            
        if element != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += result + '    '
        else:
           first += top
           second += bottom
           lines += line
           sumx += result
           
    if show_answers:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines 
            
    return string
            
    
    
   
         
        
        
        
    
def main():
    result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    if result:
        print(result)
if __name__ == "__main__":
    main()
