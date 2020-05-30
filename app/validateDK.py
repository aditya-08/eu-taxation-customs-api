
def validateDK(input):
    tin = input.replace("-","")
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
        "validSyntax": False,
    }

    if len(tin) != 10:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not tin.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif int(input[0:2]) < 1 or int(input[0:2]) > 31:
        outInvalid["message"] = "1st and 2nd character must be in the range 1...31"
        return outInvalid
    elif int(input[2:4]) < 1 or int(input[2:4]) > 12:
        outInvalid["message"] = "3rd and 4th must be in the range 1...12"
        return outInvalid
    else:
        return checkDigit(tin,input)

def checkDigit(input,tin):

    total = 0

    total = int(input[0])*4 + int(input[1])*3 + int(input[2])*2 + int(input[3])*7 + int(input[4])*6 + int(input[5])*5 + int(input[6])*4 + int(input[7])*3 + int(input[8])*2
    mod11 = total % 11
    print(mod11)

    if mod11 == 1:
        return({
            "tinNumber": tin, 
            "validStructure": True, 
            "validSyntax": False,
            "message": 'Check Digit - failed'
            })
    elif mod11 == 0 and int(input[0]) == 0:
        return({
            "tinNumber": tin, 
            "validStructure": True, 
            "validSyntax": True,
            })
    elif int(input[9]) == (11 - mod11):
        return({
            "tinNumber": tin, 
            "validStructure": True, 
            "validSyntax": True,
            })
    else:
        return({
            "tinNumber": tin, 
            "validStructure": True, 
            "validSyntax": False,
            "message": 'Check Digit - failed'
            })


