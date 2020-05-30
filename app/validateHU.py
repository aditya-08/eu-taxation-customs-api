
def validateHU(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
        "validSyntax": False 
    }

    if len(input) != 10:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif int(input[0]) != 8:
        outInvalid["message"] = "1st character must be 8"
        return outInvalid
    else:
        return checkDigit(input)

def checkDigit(input):
    sum = 0

    sum = int(input[0])*1 + int(input[1])*2 + int(input[2])*3 + int(input[3])*4 + int(input[4])*5 + int(input[5])*6 + int(input[6])*7 + int(input[7])*8 + int(input[8])*9

    mod11 = sum % 11

    if mod11 == int(input[9]):
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