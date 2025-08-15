import random

class PasswordGenerator:
    def __init__(self, lenght=8, use_uppercase=True, use_numbers=True, use_special_chars=True):
        self.lenght = lenght
        self.use_uppercase = use_uppercase
        self.use_numbers = use_numbers
        self.use_special_chars = use_special_chars

    def generator(self):
        characters = "abcdefghijklmnopqrstuvwxyz"
        if self.use_uppercase:
            characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.use_numbers:
            characters += "0123456789"
        if self.use_special_chars:
            characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/"
        
        password = ''.join(random.choice(characters) for _ in range(self.lenght))
        return password
    

if __name__ == "__main__":
    jebo = PasswordGenerator()
    print("Generovane heslo: " + jebo.generator())
