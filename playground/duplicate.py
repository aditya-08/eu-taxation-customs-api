def checkDuplicate(input):
    countDuplicate = 0
    countTriple = 0
    string = input
    duplicates = {}
    for char in string:
        if char in duplicates:
            duplicates[char] += 1
        else:
            duplicates[char] = 1
        i = 0

    for key, value in duplicates.items():
        if value == 2:
            print(value)
            countDuplicate = countDuplicate + 1
        elif value == 3:
            countTriple = countTriple + 1    
    return({
        "duplicate": countDuplicate,
        "triple": countTriple
    })

print(checkDuplicate('2225537189'))