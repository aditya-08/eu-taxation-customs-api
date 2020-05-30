
def validateNL(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False, 
        "validSyntax": False,
    }
    if not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif len(input) != 9:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    else:
        return checkDigit(input)

def checkDigit(input):
    sum = int(input[0])*9 + int(input[1])*8 + int(input[2])*7 + int(input[3])*6 + int(input[4])*5 + int(input[5])*4 + int(input[6])*3 + int(input[7])*2
    module = sum % 11
    if int(input[8]) == module:
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

