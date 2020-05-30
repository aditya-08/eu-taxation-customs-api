import sqlite3
from fastapi import HTTPException

def checkDigitIT(input):
    conn = sqlite3.connect('italy.db')
    c = conn.cursor()
    added = 0

    for i in range(len(input)-1):
        t=(input[i],)
        if (i + 1)  % 2 == 0:
            result = c.execute('SELECT valueEven FROM CheckDigitIT WHERE app=?', t)
        else:
            result = c.execute('SELECT valueOdd FROM CheckDigitIT WHERE app=?', t)
        added = added + int(result.fetchone()[0])
    mod26 = added % 26
    m = (mod26,)
    res = c.execute('SELECT checkDigit from RefDigitIT WHERE dig=?', m)
    if res.fetchone()[0] == input[15]:
        return True
    else:
        return False 


def checkCode(input):
    conn = sqlite3.connect('italy.db')
    c = conn.cursor()
    # print(input)

    t = (input,)
    result = c.execute('SELECT * FROM CodeList WHERE code=?', t)
    count = len(result.fetchall())
    # print(count)

    if count > 0:
        return True
    else:
        return False

#print(checkCode('M291'))

def checkC9(input):
    valid=['A','B','C','D','E','H','L','M','P','R','S','T']
    output=False

    for i in range(len(valid)):
        if input == valid[i]:
            output=True
            break

    return output
           

#print(checkC9('1'))

def checkC10C11(input):
    val =int(input)

    if val >= 1 and val <= 31:
        return True
    elif val >=41 and val <=71:
        return True
    else:
        return False

#print(checkC10C11(40))

def checkLength(input):
    if len(input) == 16:
        return True
    else:
        return False


def checkPosition(input):
    if not input[0].isalpha():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':202, 
                            'errorMessage': '1st character must be a letter'
                            }
                        )
    if not input[1].isalpha():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':203, 
                            'errorMessage': '2nd character must be a letter'
                            }
                        )
    if not input[2].isalpha():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':204, 
                            'errorMessage': '3rd character must be a letter'
                            }
                        )
    if not input[3].isalpha():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':205, 
                            'errorMessage': '4th character must be a letter'
                            }
                        )
    if not input[4].isalpha():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':206, 
                            'errorMessage': '5th character must be a letter'
                            }
                        )
    if not input[5].isalpha():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':207, 
                            'errorMessage': '6th character must be a letter'
                            }
                        )
    if not input[6].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':208, 
                            'errorMessage': '7th character must be a numeric'
                            }
                        )
    if not input[7].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':209, 
                            'errorMessage': '8th character must be a numeric'
                            }
                        )
    if not input[8].isalpha():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':210, 
                            'errorMessage': '9th character must be a letter'
                            }
                        )
    if not input[9].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':211, 
                            'errorMessage': '10th character must be a numeric'
                            }
                        )
    if not input[10].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':212, 
                            'errorMessage': '11th character must be a numeric'
                            }
                        )
    if not input[11].isalpha():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':213, 
                            'errorMessage': '12th character must be a letter'
                            }
                        )
    if not input[12].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':214, 
                            'errorMessage': '13th character must be a numeric'
                            }
                        )
    if not input[13].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':215, 
                            'errorMessage': '14th character must be a numeric'
                            }
                        )
    if not input[14].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':216, 
                            'errorMessage': '15th character must be a numeric'
                            }
                        )
    if not input[15].isalpha():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':217, 
                            'errorMessage': '16th character must be a letter'
                            }
                        )
           
    return True

#print(checkLength('DMLPRY77D15H501F'))
#print(checkPosition('DMLPRY77D15H501F'))

def validateCodeIT(input):
    if checkLength(input) == False:
        # raise HTTPException(status_code=400, 
        #                 detail={
        #                     'errorCode':200, 
        #                     'errorMessage': 'Incorrect Length'
        #                     }
        #                 )
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "Incorrect Length"            
            })   
    elif not input[0].isalpha():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "1st character must be a letter"            
            })
    elif not input[1].isalpha():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "2nd character must be a letter"            
            })
    elif not input[2].isalpha():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "3rd character must be a letter"            
            })
    elif not input[3].isalpha():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "4th character must be a letter"            
            })
    elif not input[4].isalpha():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "5th character must be a letter"            
            })
    elif not input[5].isalpha():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "1st character must be a letter"            
            })
    elif not input[6].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "7th character must be a numeric"            
            })
    elif not input[7].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "8th character must be a numeric"            
            })
    elif not input[8].isalpha():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "9th character must be a letter"            
            })
    elif not input[9].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "10th character must be a numeric"            
            })
    elif not input[10].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "11th character must be a numeric"            
            })
    elif not input[11].isalpha():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "12th character must be a letter"            
            })
    elif not input[12].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "13th character must be a numeric"            
            })
    elif not input[13].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "14th character must be a numeric"            
            })
    elif not input[14].isdigit():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "15th character must be a numeric"            
            })
    elif not input[15].isalpha():
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "16th character must be a letter"            
            }) 
    elif checkC9(input[8]) == False:
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "Incorrect Length"            
            })
        # raise HTTPException(status_code=400, 
        #                 detail={
        #                     'errorCode':218, 
        #                     'errorMessage': '9th character must represent a month'
        #                     }
        #                 ) 
    elif checkC10C11(input[9:10]) == False:
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "Incorrect Length"            
            })
        # raise HTTPException(status_code=400, 
        #                 detail={
        #                     'errorCode':219, 
        #                     'errorMessage': '8th and 9th must be day of month()1...31 for men,41...71 for women'
        #                     }
        #                 ) 
    elif checkCode(input[11:15]) == False:
        return({
            "tinNumber": input, 
            "validStructure": False, 
            "validSyntax": False,
            "message": "12th to 15th - incorrect place of birth"            
            })
        # raise HTTPException(status_code=400, 
        #                 detail={
        #                     'errorCode':220, 
        #                     'errorMessage': '12th to 15th - incorrect place of birth'
        #                     }
        #                 )
    elif checkDigitIT(input) == False:
        return({
            "tinNumber": input, 
            "validStructure": True, 
            "validSyntax": False,
            "message": "Check Digit failed"            
            })
        # raise HTTPException(status_code=400, 
        #                 detail={
        #                     'errorCode':221, 
        #                     'errorMessage': 'Check Digit failed'
        #                     }
        #                 ) 
    else:
        return({
            "tinNumber": input, 
            "validStructure": True, 
            "validSyntax": True            
            })

# print(validateCodeIT('DMLPRY77D15H501F'))
# print(validateCodeIT('DMLPRY77D15H501F'))