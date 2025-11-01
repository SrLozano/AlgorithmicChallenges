def firstDuplicate(a):

    '''
    We store each different number of the array in a dictionary, where each
    position is set to 1 if there is at least one ocurrence of that number.
    As soon as we detect that one number is already stored at the dictionary 
    we have already detected firstDuplicate. 
    '''

    dictionary = {}

    for element in a:
        if element in dictionary:
            return element
        else:
            dictionary[element] = 1
    return -1

while(1):
    print("Welcome to our first duplicate calculator")
    print("Please insert a list of numbers, whenever you want to stop just select number -1")
    condition = True
    a = []
    while(condition):
        number_introduced = int(input("Enter a number "))
        if number_introduced == -1:
            condition = False
            if len(a) != 0:
                result = firstDuplicate(a)
                print("The result is: " + str(result))
                print("")
            else:
                print("The list can not be empty")
        else:
            print("The number has been inserted")
            a.append(number_introduced)