import re

def validateBE(input):
    tin = input
    input = re.sub('[^A-Za-z0-9 ]+', '', tin)
    outInvalid = {
        "tinNumber": tin, 
        "validStructure": False,
        "validSyntax": False,
    }

    if len(input) != 11:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif int(input[2:4])<0 or int(input[2:4])>12:
        outInvalid["message"] = "3rd and 4th must be in the range 0...12"
        return outInvalid
    elif int(input[4:6])<0 or int(input[4:6])>31:
        outInvalid["message"] = "5th and 6th character must be in the range 00...31"
        return outInvalid
    else:
        return checkDigit(input)

def checkDigit(input):
    mod97 = 97 - int(input[0:9]) % 97
    if mod97 == int(input[9:11]):
        return({
            "tinNumber": input, 
            "validStructure": True, 
            "validSyntax": True,
            })
    else:
        mod97 = 97 - int('2'+input[0:9]) % 97
        if mod97 == int(input[9:11]):
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
