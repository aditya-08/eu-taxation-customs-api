
def validateSI(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False, 
        "validSyntax": False,
    }

    if not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif not (int(input) < 1000000 or int(input) > 9999999):
        outInvalid["message"] = "TIN must be between 1000000 and 9999999 included"
        return outInvalid
    else:
        return checkDigit(input)

def checkDigit(input):
    sum = int(input[0])*8 + int(input[1])*7 + int(input[2])*6 + int(input[3])*5 + int(input[4])*4 + int(input[5])*3 + int(input[6])*2
    module = sum % 11
    checkDigit = 11 - module
    if int(input[7]) == checkDigit:
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

