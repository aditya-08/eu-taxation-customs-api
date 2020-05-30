
def validateCZ(input):
    tin = input.replace("/","")
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
    }

    if not (len(tin) == 10 or len(tin) == 9):
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not tin.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid 
    elif len(tin) == 9:
        if (int(input[2:4])>12 and int(input[2:4])<51) or int(input[2:4])>62 or int(input[2:4])<1:
            outInvalid["message"] = "3rd and 4th character must be in the range 01...12 or 51...61"
            return outInvalid
        elif int(input[4:6])<1 or int(input[4:6])>31:
            outInvalid["message"] = "5th and 6th character must be in the range 01...31"
            return outInvalid
        else:
            return({
                "tinNumber": input, 
                "validStructure": True, 
                })
    elif len(tin) == 10:
        if int(input[2:4])<1 or (int(input[2:4])>12 and int(input[2:4])<21) or (int(input[2:4])>32 and int(input[2:4])<51) or (int(input[2:4])>62 and int(input[2:4])<71) or int(input[2:4])>82:
            outInvalid["message"] = "3rd and 4th character must be in the range 01...12 or 21...32 or 51...62 or 71..82"
            return outInvalid
        elif int(input[4:6])<1 or int(input[4:6])>31:
            outInvalid["message"] = "5th and 6th character must be in the range 01...31"
            return outInvalid
        else:
            return({
                "tinNumber": input, 
                "validStructure": True, 
                })

print(validateCZ('685229/444'))