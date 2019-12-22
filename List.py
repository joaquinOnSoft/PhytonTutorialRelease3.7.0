#list composition
squares = [x**2 for x in range(10)]
print(squares, end="\n\n")

#list composition
points = [(x, x**2) for x in range(10)]
print(points, end="\n\n")

#list concatenation
num1 = [0, 1, 2, 3, 4]
num2 = [5, 6, 7, 8, 9]
print(num1, num2)
numbers = num1 + num2
print(numbers, end="\n\n")

#list initialization
print("numbers:", numbers)
print("numbers[0]:", numbers[0])
print("Length:", len(numbers))
print("Removing element at position 0")
del numbers[0]
print("numbers:", numbers)
print("numbers[0]:", numbers[0])
print("Length:", len(numbers), end="\n\n")

#list iteration
for num in range(1, 11):
    print(num, end=" ")
print("\n")

#Append elements to a list
numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)
