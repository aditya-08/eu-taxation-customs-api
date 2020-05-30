
def validateGR(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
    }

    if len(input) != 9:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    else:
        return({
            "tinNumber": input, 
            "validStructure": True, 
            })
