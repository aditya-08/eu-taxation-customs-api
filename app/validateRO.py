
def validateRO(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False, 
    }
    if len(input) != 13:
        outInvalid["message"] = "Invalid length"
        return outInvalid
    elif not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif int(input[0]) < 1:
        print(input[0])
        outInvalid["message"] = "1st character must be greater than 0"
        return outInvalid
    elif not (int(input[3:5]) > 1 and int(input[3:5]) < 13):
        outInvalid["message"] = "5th and 6th character must be in the range 1...12"
        return outInvalid
    elif int(input[5:7]) > 31:
        outInvalid["message"] = "6th and 7th character must be in the range 01...31"
        return outInvalid
    elif not (int(input[7:9]) > 0 and int(input[7:9]) <48) or int(input[7:9]) == 51  or int(input[7:9]) == 52:
        outInvalid["message"] = "8th and 9th character must be in the range 01...47 or 51 or 52"
        return outInvalid
    else:
        return({
            "tinNumber": input, 
            "validStructure": True, 
        }) 
