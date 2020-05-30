
def validatePL(input):
    if len(input) == 10:
        return validatePL10(input)
    else:
        return validatePL11(input)

def validatePL11(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False, 
        "validSyntax": False,
    }
    if not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif len(input) != 11:
        outInvalid["message"] = "Invalid length"
        return outInvalid
    else:
        return checkDigit11(input)

def validatePL10(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False, 
        "validSyntax": False,
    }
    if not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif len(input) != 10:
        outInvalid["message"] = "Invalid length"
        return outInvalid
    else:
        return checkDigit10(input)
    

def checkDigit10(input):
    sum = int(input[0])*6 + int(input[1])*5 + int(input[2])*7 + int(input[3])*2 + int(input[4])*3 + int(input[5])*4 + int(input[6])*5 + int(input[7])*6 + int(input[8])*7
    module = sum % 11

    if int(input[9]) == module:
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
            "message": "Check Digit failed"
        })

def checkDigit11(input):
    sum = int(input[0])*1 + int(input[1])*3 + int(input[2])*7 + int(input[3])*9 + int(input[4])*1 + int(input[5])*3 + int(input[6])*7 + int(input[7])*9 + int(input[8])*1 + int(input[9])*3
    module = sum % 10
    checkDigit = 10 - module
    print(input[10])
    print(checkDigit)

    if int(input[10]) == checkDigit:
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
            "message": "Check Digit failed"
        })