
def validateSK(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False, 
        "validSyntax": False,
    }
    if not (len(input) == 10 or len(input) == 9):
        outInvalid["message"] = "Invalid length"
        return outInvalid
    elif not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif ((int(input[2:4])>12 and int(input[2:4])<51) or int(input[2:4])>62):
        outInvalid["message"] = "3rd and 4th character must be in the range 01...12 or 51...61"
        return outInvalid
    elif int(input[4:6])>31:
        outInvalid["message"] = "5th and 6th character must be in the range 01...31"
        return outInvalid
    # elif int(input[6:8])>9:
    #     outInvalid["message"] = "7th and 8th character must be in the range 01...09"
    #     return outInvalid
    else:
        return checkDigit(input)
        
def checkDigit(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": True, 
        "validSyntax": False,
        }
    out = {
        "tinNumber": input, 
        "validStructure": True, 
        "validSyntax": True,
        }
    if int(input[0:2]) < 54 and len(input) == 9:
        return out
    elif int(input[0:2]) > 54 and len(input) == 10:
        return out
    else:
        return outInvalid