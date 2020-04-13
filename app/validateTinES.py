from fastapi import HTTPException
import sqlite3

def validateTinES(input,foreigner):
    print(foreigner)
    # checkC9(input)
    if foreigner == True:
        checkPositionF(input)
        checkC1F(input[0])
        checkDigitESF(input)
        return True
    else:
        checkPosition(input)
        checkDigitES(input)
        return True

def checkC9(input):
    if not input[8].isalpha():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':301, 
                            'errorMessage': '9th character must be a letter',
                            'tin': input
                            }
                        )

def checkPosition(input):
    if not input[0].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':202, 
                            'errorMessage': '1st character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[1].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':203, 
                            'errorMessage': '2nd character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[2].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':204, 
                            'errorMessage': '3rd character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[3].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':205, 
                            'errorMessage': '4th character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[4].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':206, 
                            'errorMessage': '5th character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[5].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':207, 
                            'errorMessage': '6th character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[6].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':208, 
                            'errorMessage': '7th character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[7].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':209, 
                            'errorMessage': '8th character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[8].isalpha():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':301, 
                            'errorMessage': '9th character must be a letter',
                            'tin': input
                            }
                        )
     
    return True 

def checkDigitES(input):
    conn = sqlite3.connect('spain.db')
    c = conn.cursor()

    print(int(input[0:8]))
    mod23 = (int(input[0:8]) % 23) + 1
    print(mod23)
    m = (mod23,)
    res = c.execute('SELECT checkDigit from RefDigitES WHERE dig=?', m)

    if res.fetchone()[0] == input[8]:
        return True
    else:
        raise HTTPException(status_code=400, 
                            detail={
                            'errorCode':301, 
                            'errorMessage': 'Check Digit - failed',
                            'tin': input
                            }
                        ) 

def checkPositionF(input):
    if not len(input) == 9:
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':202, 
                            'errorMessage': 'Incorrect Length',
                            'tin': input
                            }
                        )
    if not input[0].isalpha():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':202, 
                            'errorMessage': '1st character must be a letter',
                            'tin': input
                            }
                        )
    if not input[1].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':203, 
                            'errorMessage': '2nd character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[2].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':204, 
                            'errorMessage': '3rd character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[3].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':205, 
                            'errorMessage': '4th character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[4].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':206, 
                            'errorMessage': '5th character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[5].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':207, 
                            'errorMessage': '6th character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[6].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':208, 
                            'errorMessage': '7th character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[7].isdigit():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':209, 
                            'errorMessage': '8th character must be a numeric',
                            'tin': input
                            }
                        )
    if not input[8].isalpha():
        raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':301, 
                            'errorMessage': '9th character must be a letter',
                            'tin': input
                            }
                        )
     
    return True 

def checkC1F(input):
    valid = ['X','Y','Z','K','L','M']
    output=False

    for i in range(len(valid)):
        if input == valid[i]:
            output=True
        
    if output == False:
        raise HTTPException(status_code=400, 
                            detail={
                                'errorCode':218, 
                                'errorMessage': '1st character must be X, Y, Z, K, L or M',
                                'tin': input
                                }
                            ) 

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
    print(mod23)
    m = (mod23,)
    res = c.execute('SELECT checkDigit from RefDigitES WHERE dig=?', m).fetchone()[0]
    print(res)
    print(input[8])

    if res == input[8]:
        return True
    else:
        raise HTTPException(status_code=400, 
                            detail={
                            'errorCode':301, 
                            'errorMessage': 'Check Digit - failed',
                            'tin': input
                            })
  