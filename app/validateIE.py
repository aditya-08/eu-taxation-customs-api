import sqlite3

def validateIE(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
        "validSyntax": False 
    }
    C8 = ['X','Y','Z']
    C9 = ['J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    

    if not (len(input) != 9 or len(input) != 8):
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input[0:7].isnumeric():
        outInvalid["message"] = "First seven digit must be numeric"
        return outInvalid
    elif input[7] in C8:
        outInvalid["message"] = "8th character must be letter in the range [A-W]"
        return outInvalid
    elif len(input) == 9:
        if input[8] in C9:
            outInvalid["message"] = "9th character a letter in the range [A-I], or W"
            return outInvalid
        else:
            return checkDigit(input)
    else:
        return checkDigit(input)

def checkDigit(input):
    con = sqlite3.connect("ireland.db")
    c = con.cursor()
    str1 = "WABCDEFGHI"
    str2 = "0123456789"
    str3 = ""
    sum = 0

    if len(input) == 9:
        table = input.maketrans(str1,str2,str3)
        translated = input.translate(table)
        sum = int(translated[6])*2 + int(translated[5])*3 + int(translated[4])*4 + int(translated[3])*5 + int(translated[2])*6 + int(translated[1])*7 + int(translated[0])*8 + int(translated[8])*9
        print(sum)
        module23 = sum % 23
    else:
        sum = int(input[6])*2 + int(input[5])*3 + int(input[4])*4 + int(input[3])*5 + int(input[2])*6 + int(input[1])*7 + int(input[0])*8
        module23 = sum % 23

    m = (module23,)
    res = c.execute('SELECT alpha from MapDataIR where val=?', m).fetchone()[0]

    if res == input[7]:
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


