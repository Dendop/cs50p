def main():
    utext = input("Your text: ")
    converted_text = convert(utext)

    print(converted_text)

def convert(utext):
    converted_text = utext.replace(":)", "🙂").replace(":(", "🙁")
    return converted_text

if __name__ == "__main__":
    main()