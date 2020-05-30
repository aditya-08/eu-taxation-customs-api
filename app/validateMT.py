

def validateMT(input):
    if len(input) == 9:
        return validateMT9(input)
    else:
        return validateMT8(input)

def validateMT9(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False, 
    }
    print(input)
    if len(input) != 9:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif not(int(input[0:2]) == 22 or int(input[0:2]) == 33 or int(input[0:2]) == 44 or int(input[0:2]) == 55 or int(input[0:2]) == 66 or int(input[0:2]) == 77 or int(input[0:2]) == 88):
        outInvalid["message"] = "1st and 2nd character can only take the values 11, 22, 33, 44, 55, 66, 77 or 88"
        return outInvalid
    else:
        return({
            "tinNumber": input,
            "validStructure": True,
        })

def validateMT8(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False, 
    }
    if len(input) != 8:
        outInvalid["message"] = "Invalid Length"
    elif not input[0:7].isnumeric():
        outInvalid["message"] = "1st seven characters must be numeric"
        return outInvalid
    elif not input[7].isalpha():
        outInvalid["message"] = "8th characters must be a letter"
        return outInvalid
    elif not (input[7] == 'M' or input[7] == 'G' or input[7] == 'A' or input[7] == 'P' or input[7] == 'L' or input[7] == 'H' or input[7] == 'B' or input[7] == 'Z'):
        outInvalid["message"] = "8th characters must be M, G, A, P, L, H, B or Z"
        return outInvalid
    elif (input[7] == 'A' or input[7] == 'P') and int(input[0:7]) >= 1:
        return({
            "tinNumber": input,
            "validStructure": True,
        }) 
    elif int(input[0:5]) >= 1 and int(input[0:5]) <= 32000 and int(input[5:7]) > 0 and int(input[5:7]) <=99 and (input[7] == 'M' or input[7] == 'G' or input[7] == 'L' or input[7] == 'H' or input[7] == 'B' or input[7] == 'Z'):
        return({
            "tinNumber": input,
            "validStructure": True,
            })
    else:
        outInvalid["message"] = "Invalid TIN"
        return outInvalid