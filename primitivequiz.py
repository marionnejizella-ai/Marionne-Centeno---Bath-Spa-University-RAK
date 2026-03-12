#Exercise 4: Primitive Quiz
#Marionne Jizella E. Centeno

score = 0

print("Welcome to the Primitive Data Types Quiz!")
print("----------------------------------------")

# Question 1
answer = input("1. Which primitive type stores whole numbers? ")
if answer.lower() == "int":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is int.\n")

# Question 2
answer = input("2. Which primitive type stores decimal numbers? ")
if answer.lower() == "float":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is float.\n")

# Question 3
answer = input("3. Which primitive type stores text? ")
if answer.lower() == "string" or answer.lower() == "str":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is string (str).\n")

# Question 4
answer = input("4. Which primitive type stores True or False values? ")
if answer.lower() == "boolean" or answer.lower() == "bool":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is boolean (bool).\n")

# Question 5
answer = input("5. What function is used to check the data type of a variable in Python? ")
if answer.lower() == "type":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is type().\n")

# Final Score
print("----------------------------------------")
print("Quiz Finished!")
print("Your Score:", score, "/ 5")

if score == 5:
    print("Excellent! You know primitive types very well!")
elif score >= 3:
    print("Good job! Keep practicing.")
else:
    print("You should study primitive types more.")