#Exercise 10: Is it  even?
#Marionne Jizella E. Centeno
def is_even(number):
    """
    Function to check if a number is even.
    Returns True if even, False if odd.
    """
    return number % 2 == 0

def main():
    print("Welcome to the 'Is it Even?' Checker!")
    
    while True:
        user_input = input("Enter a number (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Validate input
        if not user_input.isdigit() and not (user_input.startswith('-') and user_input[1:].isdigit()):
            print("Please enter a valid integer.")
            continue
        
        number = int(user_input)
        
        if is_even(number):
            print(f"{number} is EVEN ✅")
        else:
            print(f"{number} is ODD ❌")

if __name__ == "__main__":
    main()
