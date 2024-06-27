import random
import string

def generate_password(length, complexity):
    characters = ""
    

    if complexity >= 1:
        characters += string.ascii_lowercase  
    if complexity >= 2:
        characters += string.ascii_uppercase  
    if complexity >= 3:
        characters += string.digits  
    if complexity >= 4:
        characters += string.punctuation  

    if characters == "":
        print("Invalid complexity level.")
        return ""
    
    
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        complexity = int(input("Enter the complexity level (1-4):\n1. Lowercase Letters\n2. Lowercase and Uppercase Letters\n3. Lowercase, Uppercase Letters and Digits\n4. Lowercase, Uppercase Letters, Digits and Special Characters\nYour choice: "))
        
        
        password = generate_password(length, complexity)
        
        
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter valid numbers for length and complexity.")

if __name__ == "__main__":
    main()
