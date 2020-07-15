import random

# A function do shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

uppercaseLetter1 = chr(random.randint(65, 90))  # Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))
lowercaseLetter3 = chr(random.randint(97, 122))
digit1 = str(random.randint(0, 9))
digit2 = str(random.randint(0, 9))

# Generate password using all the characters, in random order
password = uppercaseLetter1 + lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + digit1 + digit2
password = shuffle(password)

# Output
print(password)
