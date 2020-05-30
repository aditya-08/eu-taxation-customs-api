def validateHR(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
        "validSyntax": False,
    }

    if len(input) != 11:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    else:
        return checkDigit(input)

def checkDigit(input):
    total = 0
    for c1 in range(0,len(input[0:10])):
        if c1 == 0:
            total = (int(input[c1]) + 10) % 10
        else:
            total = (int(input[c1]) + total) % 10

        if total == 0:
            total = 10
        total = (total * 2) % 11
    
    if total == 1:
        checkDigit = 1
    else:
        checkDigit = 11 - total

    if checkDigit == int(input[10]):
        return({
            "tinNumber": input, 
            "validStructure": True, 
            "validSyntax": True,
            })
    else:
        return({
            "tinNumber": input, 
            "validStructure": True, 
            "validSyntax": False,
            "message": 'Check Digit - failed'
            })