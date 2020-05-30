
def validateLU(input):
    outInvalid = {
        "tinNumber": input, 
        "validStructure": False,
        "validSyntax": False 
    }
    if len(input) != 13:
        outInvalid["message"] = "Invalid Length"
        return outInvalid
    elif not input.isnumeric():
        outInvalid["message"] = "TIN must be numeric"
        return outInvalid
    elif int(input[4:6]) == 0 or int(input[4:6]) > 12:
        outInvalid["message"] = "5th and 6th character must be in the range 01...12"
        return outInvalid
    elif int(input[6:8]) == 0 or int(input[6:8]) > 31:
        outInvalid["message"] = "7th and 8th character must be in the range 01...31"
        return outInvalid
    elif checkDigit12(input) != 0:
        outInvalid["validStructure"] = True
        outInvalid["message"] = "Invalid check digit C12"
        return outInvalid
    elif checkDigit13(input) != 0:
        outInvalid["validStructure"] = True
        outInvalid["message"] = "Invalid check digit C13"
        return outInvalid
    else:
        return({
        "tinNumber": input, 
        "validStructure": True,
        "validSyntax": True 
        })

def checkDigit12(input):
    i = 0
    sum = 0
    for c in input[0:12:1]:
        # print(c)
        num = int(c)
        if i % 2 == 0:
            num = num * 2
            if num > 9:
                num = addDigit(num)
            sum = sum + num
        else:
            sum = sum + num
        i = i + 1
        # print(num)
    
    modulo = sum % 10
    return modulo

def addDigit(num):
    sum=0
    temp=num
    while num > 0:
        rem = num % 10
        sum += rem
        num //=10
    return sum

def checkDigit13(input):
    D = [
        [0,1,2,3,4,5,6,7,8,9],
        [1,2,3,4,0,6,7,8,9,5],
        [2,3,4,0,1,7,8,9,5,6],
        [3,4,0,1,2,8,9,5,6,7],
        [4,0,1,2,3,9,5,6,7,8],
        [5,9,8,7,6,0,4,3,2,1],
        [6,5,9,8,7,1,0,4,3,2],
        [7,6,5,9,8,2,1,0,4,3],
        [8,7,6,5,9,3,2,1,0,4],
        [9,8,7,6,5,4,3,2,1,0]
        ]
    P = [
        [0,1,2,3,4,5,6,7,8,9],
        [1,5,7,6,2,8,3,0,9,4],
        [5,8,0,3,7,9,6,1,4,2],
        [8,9,1,6,0,4,3,5,2,7],
        [9,4,5,3,1,2,6,8,7,0],
        [4,2,8,6,5,7,9,3,0,1],
        [2,7,9,3,8,0,6,4,1,5],
        [7,0,4,6,9,1,3,2,5,8]
        ]
    c = 0
    l = len(input) - 1
    i = 0
    sum = 0

    while l >= 0:
        if l == 11:
            l = l - 1
            continue
        x = i % 8
        y = P[x][int(input[l])]
        c = D[c][y]
        sum = sum + c
        l = l - 1
        i = i + 1

    return (sum%10)

# checkDigit13('1893120105732')
# checkDigit12('1893120105732')

