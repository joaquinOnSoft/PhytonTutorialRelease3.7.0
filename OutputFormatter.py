# formatted string literal
year = 1977
event = 'was born'

print(f'I {event} in {year}')

# str.format() examples
yes = 54
no = 34
yes_percentage = yes / (yes + no)
no_percentage = no / (yes + no)

print("{:-6} YES votes {:2.2%}".format(yes, yes_percentage))
print("{:-6} NO votes {:2.2%}".format(no, no_percentage))

# str() and repr()
message = 'Hello World!'
print(str(message))
print(repr(message))

