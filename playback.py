def main():
   utext = input("Your text: ")
   modified_text = "" #initialize empty string

   for char in utext:
      if ord(char) == 32:
         char = "..."
      modified_text += char #if the character is not 32(space) then we just print character withou change

    
    
   print(modified_text)
   


if __name__ == "__main__":
   main()