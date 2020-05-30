def validateBG(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
        "validSyntax": False,
    }

    if len(input) != 10:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif int(input[2:4])<1 or (int(input[2:4])>12 and int(input[2:4])<21) or (int(input[2:4])>32 and int(input[2:4])<41) or int(input[2:4])>52:
        outInvalid["message"] = "3rd and 4th must be in the range 1...12, 21...32, 41...52"
        return outInvalid
    elif int(input[4:6])<1 or int(input[4:6])>31:
            outInvalid["message"] = "5th and 6th character must be in the range 01...31"
            return outInvalid
    else:
        return checkDigit(input)

def checkDigit(input):
    total = 0

    total = int(input[0])*2 + int(input[1])*4 + int(input[2])*8 + int(input[3])*5 + int(input[4])*10 + int(input[5])*9 + int(input[6])*7 + int(input[7])*3 + int(input[8])*6
    mod11 = total % 11

    if mod11 == 10:
        mod11 = 0
    
    
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
