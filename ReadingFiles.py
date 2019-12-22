# Reading file in one shoot
print("Reading file in one shoot\n")

with open("text_example.txt", "r") as f:
    data = f.read()
    print(data)
f.close()

# Reading file line by line
print("Reading file line by line\n")

f = open("text_example.txt", "r")
for line in f:
    print(line, end="")

f.close()