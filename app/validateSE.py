
#640823-3234
#640883-3231
#610321-3499
#19640823-3234
#19640883-3231
#19640883+3231
def validateSE(input):  
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False, 
        "validSyntax": False,
    }
    tin1 = input.replace("-","")
    tin = tin1.replace("+","")
    length = len(tin)

    if not tin.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif not (length == 10 or length == 12):
        outInvalid["message"] = "Invalid length"
        return outInvalid
    elif length == 10:
        if int(tin[2:3]) > 13:
            #return('month error')
            outInvalid["message"] = "3rd and 4th character must be in the range 1...12"
            return outInvalid
        # 0-31 or 61-91
            #return('days error')
            outInvalid["message"] = "5th and 6th character must be in the range 1...31 or 61...91"
            return outInvalid
        else:
            res=checkDigit(tin)
            res["tinNumber"] = input
            return res
    elif length == 12:
        if  not (int(tin[0:2]) == 18 or int(tin[0:2]) == 19 or int(tin[0:2]) == 20):
            # return('eeror')
            outInvalid["message"] = "1st and 2nd character must be 18 or 19 or 20"
            return outInvalid
        elif not (int(tin[4:6]) > 1 and int(tin[4:6]) < 12):
            # return(error)
            outInvalid["message"] = "5th and 6th character must be in the range 1...12"
            return outInvalid
        # 0-31 or 61-91
        elif ((int(tin[6:8])>31 and int(tin[6:8])<61) or int(tin[6:8])>91):
            # return('error')
            outInvalid["message"] = "7th and 8th character must be in the range 1...31 or 61...91"
            return outInvalid
        else:
            res=checkDigit(tin)
            res["tinNumber"] = input
            return res
         

def addDigit(num):
    sum=0
    temp=num
    while num > 0:
        rem = num % 10
        sum += rem
        num //=10
    return sum

def checkDigit(tin):
    outInvalidSyntax = {
        "tinNumber": tin, 
        "validStructure": True, 
        "validSyntax": False,
    }
    out = {
        "tinNumber": tin, 
        "validStructure": True, 
        "validSyntax": True,
    }
    print('in check digit')
    sum=0
    if len(tin) == 10:
        sum=sum+addDigit(int(tin[0])*2)
        sum=sum+addDigit(int(tin[1])*1)
    sum=sum+addDigit(int(tin[2])*2)
    sum=sum+addDigit(int(tin[3])*1)
    sum=sum+addDigit(int(tin[4])*2)
    sum=sum+addDigit(int(tin[5])*1)
    sum=sum+addDigit(int(tin[6])*2)
    sum=sum+addDigit(int(tin[7])*1)
    sum=sum+addDigit(int(tin[8])*2)

    if len(tin) == 12:
        sum=sum+addDigit(int(tin[9])*1)
        sum=sum+addDigit(int(tin[10])*2)
        print(sum)
        unitDigit = 10 - sum % 10
        if unitDigit == 10:
            unitDigit = 0
        print(unitDigit)
        if int(tin[11]) == unitDigit:
        # return('goog result')
            print('in out..')
            return out
        else:
        # return ('bad syntax')
            outInvalidSyntax["message"] = "Check Digit failed"
            return outInvalidSyntax

    unitDigit = 10 - sum % 10
    if unitDigit == 10:
        unitDigit = 0
    if int(tin[9]) == unitDigit:
        # return('goog result')
        return out
    else:
        # return ('bad syntax')
        outInvalidSyntax["message"] = "Check Digit failed"
        return outInvalidSyntax

    return outInvalidSyntax

# validateSE('640823-3234')
# validateSE('640823-323')