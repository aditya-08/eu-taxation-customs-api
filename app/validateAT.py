import re

def validateAT(input):
    tin = input
    input = re.sub('[^A-Za-z0-9 ]+', '', tin)
    outInvalid = {
        "tinNumber": tin, 
        "validStructure": False,
        "validSyntax": False,
    }

    if len(input) != 9:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    else:
        return checkDigit(input)

def checkDigit(input):
    total = 0

    for c in range(0,len(input[0:8])):
        if c % 2 == 0:
            total = total + int(input[c])*1
        else:
            s = int(input[c])*2
            if s > 9:
                s = s%10 + 1
            total = total + s

    unitDigit = (100 - total) % 10

    if unitDigit == int(input[8]):
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