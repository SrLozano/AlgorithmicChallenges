def firstNotRepeatingCharacter(s):
    
    '''
    We strore each different char of the string in a dictionary where the number stored
    represents the number of ocurrences of the char in the array. After that we just need 
    to iterate the string, look up the character in the dictionary and if it only appears 
    once we hace found the firstNotRepeatingCharacter.
    '''
    
    dictionary = {}

    for element in s:
        if element in dictionary:
            dictionary[element] = dictionary[element] + 1
        else:
            dictionary[element] = 1

    for element in s:
        if dictionary[element] == 1:
            return element

    return '_' 


while(1):
    print("Welcome to our firstNotRepeatingCharacter calculator")
    a = input("Enter a string ")
    if len(a) != 0:
        result = firstNotRepeatingCharacter(a)
        print("The fisrt not repeating character is: " + str(result))
        print("")
    else:
        print("The string can not be empty")
            