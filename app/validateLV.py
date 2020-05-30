
def validateLV(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
    }
    if len(input) != 11:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif int(input[0:2]) == 0 or int(input[0:2]) > 32:
        outInvalid["message"] = "1st and 2nd character must be in the range 01...32"
        return outInvalid
    elif int(input[0:2]) < 32:
        if int(input[2:4]) == 0 or int(input[2:4]) > 12:
            outInvalid["message"] = "4th and 5th character must be in the range 01...12"
            return outInvalid
        elif int(input[6:7]) > 2:
            outInvalid["message"] = "7th character must be in the range 0...2"
            return outInvalid
        else:
            return({
                "tinNumber": input, 
                "validStructure": True,
                })
    else:
        return({
            "tinNumber": input, 
            "validStructure": True,
            })