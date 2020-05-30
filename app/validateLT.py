
def validateLT(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
        "validSyntax": False 
    }
    if len(input) != 11:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif int(input[0]) == 0 or int(input[0]) > 6:
        outInvalid["message"] = "1st character can only take the value 1 to 6"
        return outInvalid
    elif int(input[3:5]) == 0 or int(input[3:5]) > 12:
        outInvalid["message"] = "4th and 5th character must be in the range 01...12"
        return outInvalid
    elif int(input[5:7]) == 0 or int(input[5:7]) > 31:
        outInvalid["message"] = "4th and 5th character must be in the range 01...31"
        return outInvalid
    else:
        return checkDigit(input)

def checkDigit(input):
    out = {
        "tinNumber": input, 
        "validStructure": True,
        "validSyntax": False 
    }
    sum = int(input[0])*1 + int(input[1])*2 + int(input[2])*3 + int(input[3])*4 + int(input[4])*5 + int(input[5])*6 + int(input[6])*7 + int(input[7])*8 + int(input[8])*9 + int(input[9])*1
    modulo11 = sum % 11
    if int(input[10]) == modulo11:
        out["validSyntax"] = True
        return out
    elif modulo11 == 10:
        sumNew = int(input[0])*3 + int(input[1])*4 + int(input[2])*5 + int(input[3])*6 + int(input[4])*7 + int(input[5])*8 + int(input[6])*9 + int(input[7])*1 + int(input[8])*2 + int(input[9])*3
        moduloNew11 = sumNew % 11
        if int(input[10]) == moduloNew11:
            out["validSyntax"] = True
            return out
        elif moduloNew11 == 10 and int(input[10]) == 0:
            out["validSyntax"] = True
            return out
        else:
            out["message"]: "Check Digit failed"
            return out
    else:
        out["message"]: "Check Digit failed"
        return out


