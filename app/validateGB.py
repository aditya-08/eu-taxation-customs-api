
def validateGB(input):
    if len(input) == 10:
        if not input[0].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '1st character must be a numeric'
                })
        elif not input[1].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '2nd character must be a numeric'
                })
        elif not input[2].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "validSyntax": False,
                "message": '3rd character must be a numeric'
                })
        elif not input[3].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '4th character must be a numeric'
                })
        elif not input[4].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '5th character must be a numeric'
                })
        elif not input[5].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '6th character must be a numeric'
                })
        elif not input[6].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '7th character must be a numeric'
                })
        elif not input[7].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '8th character must be a numeric'
                })
        elif not input[8].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '9th character must be a numeric'
                })
        elif not input[9].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '10th character must be a numeric'
                })
    elif len(input) == 9 or len(input) == 8:
        if not input[0].isalpha():
           return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '1st character must be a letter'
                })
        elif not input[1].isalpha():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '2nd character must be a letter'
                })
        elif not input[2].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '3rd character must be a numeric'
                })
        elif not input[3].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '4th character must be a numeric'
                })
        elif not input[4].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '5th character must be a numeric'
                })
        elif not input[5].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '6th character must be a numeric'
                })
        elif not input[6].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '7th character must be a numeric'
                })
        elif not input[7].isdigit():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '8th character must be a numeric'
                })
        elif len(input) == 9 and not input[8].isalpha():
            return({
                "tinNumber": input, 
                "validStructure": False, 
                "message": '9th character must be a character'
                })
        elif input[0] == 'D' or input[0] == 'F' or input[0] == 'I' or input[0] == 'Q' or input[0] == 'U' or input[0] == 'V':
            return({
                    "tinNumber": input, 
                    "validStructure": False, 
                    "message": '1st character must not be  D, F, I, Q, U, V'
                    })   
        elif input[1] == 'D' or input[1] == 'F' or input[1] == 'I' or input[1] == 'O' or input[1] == 'Q' or input[1] == 'U' or input[1] == 'V':
            return({
                    "tinNumber": input, 
                    "validStructure": False, 
                    "message": '2nd character must be not be  D, F, I, 0, Q, U, V'
                    })
        elif input[0:2] == 'GB' or input[0:2] == 'NK' or input[0:2] == 'TN' or input[0:2] == 'ZZ':
            return({
                    "tinNumber": input, 
                    "validStructure": False, 
                    "message": 'First two character must not be GB, NK, TN or ZZ'
                    })
        elif len(input) == 9 and input[8] == 'A':
            return({
                "tinNumber": input, 
                "validStructure": True, 
                })
        elif len(input) == 9 and input[8] == 'B':
            return({
                "tinNumber": input, 
                "validStructure": True, 
                })
        elif len(input) == 9 and input[8] == 'C':
            return({
                "tinNumber": input, 
                "validStructure": True, 
                })
        elif len(input) == 9 and input[8] == 'D':
            return({
                "tinNumber": input, 
                "validStructure": True, 
                })
        elif len(input) == 9:
            return({
                "tinNumber": input, 
                "validStructure": False,
                "message": "Last character must be A, B, C or D" 
                })       
    return({
            "tinNumber": input, 
            "validStructure": True, 
            })
    
