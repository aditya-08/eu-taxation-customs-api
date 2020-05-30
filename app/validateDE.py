
def validateDE(input):
    tin = input.replace("/","")
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
        "validSyntax": False,
    }

    val = checkDigitCount(tin[0:9])

    if len(tin) != 11:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not tin.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif int(tin[0]) == 0:
        outInvalid["message"] = "1st character can never be 0"
        return outInvalid

    val = checkDigitCount(tin[0:10])
    
    if not ((val["duplicate"] == 1 and val["triple"] == 0) or (val["duplicate"] == 0 and val["triple"] == 1)):
        outInvalid["message"] = "One and only one mandatory duplicate or triple value"
        return outInvalid
    
    checkSum2 = checkDigit2(tin)
    checkSum3 = checkDigit3(tin)

    if val["triple"] == 1 and checkSum3 == True:
        return({
            "tinNumber": input, 
            "validStructure": True,
            "validSyntax" : True
        })
    elif val["duplicate"] == 1 and checkSum2 == True:
        return({
            "tinNumber": input, 
            "validStructure": True,
            "validSyntax" : True
        })
    else:
        return({
            "tinNumber": input, 
            "validStructure": True,
            "validSyntax" : False,
            "message": "Check failed"
        })
    

def checkDigit3(tin):
    X = (((int(tin[0]) + 10) % 10) * 2)%11

    Y = (int(tin[1]) + X) % 10
    if Y == 0:
        Y = 10
    Y = (Y * 2) % 11

    in1 = tin[2:10]
    for x in in1:
        Y = (Y + int(x)) % 10
        if Y == 0:
            Y = 10
        Y = (Y * 2) % 11
    Z = 11 - Y

    if Z == 10:
        Z = 0

    if Z == int(tin[10]):
        return True
    else:
        return False

def checkDigit2(tin):
    X = ((int(tin[0]) % 10) * 2)%11

    Y = (int(tin[1]) + X) % 10
    if Y == 0:
        Y = 10
    Y = (Y * 2) % 11

    in1 = tin[2:10]
    for x in in1:
        Y = (Y + int(x)) % 10
        if Y == 0:
            Y = 10
        Y = (Y * 2) % 11
    Z = 11 - Y

    if Z == 10:
        Z = 0

    if Z == int(tin[10]):
        return True
    else:
        return False


def checkDigitCount(input):
    countDuplicate = 0
    countTriple = 0
    string = input
    duplicates = {}
    for char in string:
        if char in duplicates:
            duplicates[char] += 1
        else:
            duplicates[char] = 1
        i = 0

    for key, value in duplicates.items():
        if value == 2:
            print(value)
            countDuplicate = countDuplicate + 1
        elif value == 3:
            countTriple = countTriple + 1    
    
    return({
        "duplicate": countDuplicate,
        "triple": countTriple
    })
