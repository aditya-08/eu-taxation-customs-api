
def validateFR(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
        "validSyntax": False,
    }

    if len(input) != 13:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif not (input[0] in ['0','1','2','3']):
        outInvalid["message"] = "1st character must be 0, 1, 2 or 3"
        return outInvalid
    else:
        return checkDigit(input)

def checkDigit(input):
    mod511 = int(input[0:10]) % 511
    if mod511 == int(input[10:13]):
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