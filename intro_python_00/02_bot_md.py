def fav_animal():

    # ANSI escape codes for bold and italic
    bold_italic = "\033[1m\033[3m"  # or use "\033[1;3m"
    reset = "\033[0m"

    print(f"{bold_italic}I am asking about favourite animal :){reset} \n")
    animal = input(f"{bold_italic}Which is your favourite animal? {reset} \n")
    print(f"{bold_italic}My favourite animal is also {animal} 😊{reset}")

if __name__ == '__main__':
    fav_animal()
