import sqlite3

def validateFI(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
        "validSyntax": False,
    }

    if len(input) != 11:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input[0:6].isnumeric():
        outInvalid["message"] = "1st six characters must be numeric"
        return outInvalid
    elif not input[7:10].isnumeric():
        outInvalid["message"] = "8th, 9th and 10th characters must be numeric"
        return outInvalid
    elif not input[6] in ['+','-','A']:
        outInvalid["message"] = "7th character can be +,- or A"
        return outInvalid
    elif int(input[0:2]) < 1 or int(input[0:2]) > 31:
        outInvalid["message"] = "1st two character must be in the range 1...31"
        return outInvalid
    elif int(input[2:4]) < 1 or int(input[2:4]) > 12:
        outInvalid["message"] = "3rd and 4th must be in the range 1...12"
        return outInvalid
    else:
        return checkDigit(input)
    
def checkDigit(input):
    con = sqlite3.connect("finland.db")
    c = con.cursor()

    num = int(input[0:6] + input[7:10])
    mod31 = str(num % 31)

    m = (mod31,)
    res = c.execute('select val from MapDataFI where mod31 = ?',  m).fetchone()[0]

    if res == input[10]:  
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