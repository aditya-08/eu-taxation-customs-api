import sqlite3

def validateCY(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
        "validSyntax": False,
    }

    if len(input) != 9:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input[0:8].isnumeric():
        outInvalid["message"] = "1st eight characters must be numeric"
        return outInvalid
    elif not input[8].isalpha():
        outInvalid["message"] = "9th character must be letter"
        return outInvalid
    else:
        return checkSum(input)

def checkSum(input):
    conn = sqlite3.connect('cyprus.db')
    c = conn.cursor()
    total = 0

    for i in range(0, len(input[0:8])):
        if i % 2:
            total = total + int(input[i])
        else:
            m = (int(input[i]),)
            res = c.execute('select val from MapDataCY where num = ?',  m).fetchone()[0]
            total = total + int(res)
    result = chr(total % 26 + 65)

    if result == input[8]:
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
