from fastapi import HTTPException
import sqlite3

def validateTinES(input):
    if not input[0].isdigit():
        result = checkPositionF(input)
        if not result["validStructure"]:
            return result
        result = checkDigitESF(input)
        if not result["validSyntax"]:
            return result
        
    else:
        result = checkPosition(input)
        if not result["validStructure"]:
            return result
        result = checkDigitES(input)
        if not result["validSyntax"]:
            return result
        
    return({
            "tinNumber": input, 
            "validStructure": True, 
            "validSyntax": True            
            })


def checkPosition(input):
    if not input[0].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '1st character must be a numeric'
            })
    if not input[1].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '2nd character must be a numeric'
            })
    if not input[2].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '3rd character must be a numeric'
            })
    if not input[3].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '4th character must be a numeric'
            })
    if not input[4].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '5th character must be a numeric'
            })
    if not input[5].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '6th character must be a numeric'
            })
    if not input[6].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '7th character must be a numeric'
            })
    if not input[7].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '8th character must be a numeric'
            })
    if not input[8].isalpha():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '9th character must be a letter'
            })
     
    return({
            "tinNumber": input, 
            "validStructure": True, 
            "validSyntax": False,
            }) 

def checkDigitES(input):
    conn = sqlite3.connect('spain.db')
    c = conn.cursor()

    print(int(input[0:8]))
    mod23 = (int(input[0:8]) % 23) + 1
    print(mod23)
    m = (mod23,)
    res = c.execute('SELECT checkDigit from RefDigitES WHERE dig=?', m)

    if res.fetchone()[0] == input[8]:
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
            "message": 'Invalid Check Digit'
            }) 

def checkPositionF(input):
    if not len(input) == 9:
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": 'Incorrect Length'
            })
    if not input[0].isalpha():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '1st character must be a letter'
            })
    if not input[1].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": 'Incorrect Length'
            })
    if not input[2].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '3rd character must be a numeric'
            })
    if not input[3].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '4th character must be a numeric'
            })
    if not input[4].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '5th character must be a numeric'
            })
    if not input[5].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '6th character must be a numeric'
            })
    if not input[6].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '7th character must be a numeric'
            })
    if not input[7].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '8th character must be a numeric'
            })
    if not input[8].isalpha():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '8th character must be a numeric'
            })
     
    return({
            "tinNumber": input, 
            "validStructure": True, 
            "validSyntax": False,
            }) 

def checkC1F(input):
    valid = ['X','Y','Z','K','L','M']
    output=False

    for i in range(len(valid)):
        if input == valid[i]:
            output=True
        
    if output == False:
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": '1st character must be X, Y, Z, K, L or M'
            })
    else:
        return({
            "tinNumber": input, 
            "validStructure": True, 
            "validSyntax": False,
            }) 

def checkDigitESF(input):
    conn = sqlite3.connect('spain.db')
    c = conn.cursor()
    replaced = input

    replaced = replaced.replace('X','0')
    replaced = replaced.replace('Y','1')
    replaced = replaced.replace('Z','2')
    replaced = replaced.replace('K','0')
    replaced = replaced.replace('L','0')
    replaced = replaced.replace('M','0')

    mod23 = (int(replaced[0:8]) % 23) + 1
    # print(mod23)
    m = (mod23,)
    res = c.execute('SELECT checkDigit from RefDigitES WHERE dig=?', m).fetchone()[0]
    # print(res)
    # print(input[8])

    if res == input[8]:
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
  