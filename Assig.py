import random
# Function name: removeExsistingCharacters
# input : username (String) & characterList (String)
# output : characterList after removing all username characters
def removeExsistingCharacters(username, characterList):
    # x is a consecutive characters inside username string 
    for x in username:
        characterList = characterList.replace(x, "")
    
    return characterList
# Function name: generate_password
# input : username (String) 
# output : Generated password
def generate_password(username):
    # Define the possible characters that could be in the password
    # calling to function removeExsistingCharacters to remove lower case letters present in username
    lowercase = removeExsistingCharacters(username, "abcdefghijklmnopqrstuvwxyz")
    # calling to function removeExsistingCharacters to remove upper case letters present in username 
    uppercase = removeExsistingCharacters(username, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # calling to function removeExsistingCharacters to remove special characters present in username
    specialChars = removeExsistingCharacters(username, "!@#$%^&*()-+")
    # calling to function removeExsistingCharacters to remove digits present in username            
    digits = removeExsistingCharacters(username, "0123456789")

    # Make sure the password has at least one of each type of character
    # choose one single character from each list
    password = [random.choice(lowercase), random.choice(uppercase), random.choice(specialChars), random.choice(digits)]
    # now the password contains 4 characters
    
    # Fill the rest of the password size with random choices from all the characters
    
    # loop from 4 to 8 times to add n random different characters
    # passLimit is a random counter from 4 to 8
    passLimit = random.randint(4,8)
    for i in range(passLimit):
        # choose one random character from all lists
        randomChar = random.choice(lowercase + uppercase + specialChars + digits)
        # make sure that the random chosen character doesn't exist in my password
        while (randomChar in password):
            randomChar = random.choice(lowercase + uppercase + specialChars + digits)
        # after exiting the while loop add the random chosen character into your password    
        password.append(randomChar)

    # Join the characters into a single string and return it
    # Password is a list of characters
    # ''.join(password) concat the characters from the list to one single string
    return ''.join(password)


username = input("enter username: ")
print(generate_password(username))