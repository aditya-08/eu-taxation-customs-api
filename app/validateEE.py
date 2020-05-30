
def validateEE(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
        "validSyntax": False,
    }

    if len(input) != 11:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif int(input[0]) < 0 or int(input[0]) > 6:
        outInvalid["message"] = "1st character must be in the range 1...6"
        return outInvalid
    elif int(input[3:5]) < 1 or int(input[3:5]) > 12:
        outInvalid["message"] = "4th and 5th must be in the range 1...12"
        return outInvalid
    elif int(input[5:7]) < 1 or int(input[5:7]) > 31:
        outInvalid["message"] = "6th and 7th character must be in the range 1...31"
        return outInvalid
    elif int(input[7:10]) < 1 or int(input[7:10]) > 710:
        outInvalid["message"] = "8th, 9th and 10 must be in the range 001...710"
        return outInvalid
    else:
        return checkDigit(input)

def checkDigit(input):
    sum = 0

    sum = int(input[0])*1 + int(input[1])*2 + int(input[2])*3 + int(input[3])*4 + int(input[4])*5 + int(input[5])*6 + int(input[6])*7 + int(input[7])*8 + int(input[8])*9 + int(input[9])*1
    mod11 = sum % 11

    if mod11 == int(input[10]):
        return({
            "tinNumber": input, 
            "validStructure": True, 
            "validSyntax": True,
            })
    elif mod11 == 10:
        sum1 = int(input[0])*3 + int(input[1])*4 + int(input[2])*5 + int(input[3])*6 + int(input[4])*7 + int(input[5])*8 + int(input[6])*9 + int(input[7])*1 + int(input[8])*2 + int(input[9])*3
        mod11_1 = sum1 % 11
        if mod11_1 == int(input[10]):
            return({
                "tinNumber": input, 
                "validStructure": True, 
                "validSyntax": True,
                })
        elif mod11_1 == 10 and int(input[10]) == 0:
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
    else:
        return({
                "tinNumber": input, 
                "validStructure": True, 
                "validSyntax": False,
                "message": 'Check Digit - failed'
                })

