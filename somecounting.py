#Exercise 7: Some Counting
#Marionne Jizella E. Centeno
print("=== Some Counting Examples ===\n")

# 1. Count from 1 to 10
print("Counting from 1 to 10:")
for i in range(1, 11):
    print(i)

print("\n------------------")

# 2. Count even numbers from 2 to 20
print("Even numbers from 2 to 20:")
for i in range(2, 21, 2):
    print(i)

print("\n------------------")

# 3. Countdown from 10 to 1
print("Countdown from 10 to 1:")
for i in range(10, 0, -1):
    print(i)

print("\n------------------")

# 4. Sum of numbers from 1 to 10
total = 0
for i in range(1, 11):
    total += i

print("Sum of numbers from 1 to 10 =", total)

print("\n=== End of Program ===")