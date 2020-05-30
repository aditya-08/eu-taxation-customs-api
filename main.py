from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

from app.schemas import TIN
from app.customize import fastapi_title, fastapi_description, fastapi_version
from app.validateCodeIT import validateCodeIT
from app.validateTinES import validateTinES
from app.validateGB import validateGB
from app.validateSE import validateSE
from app.validateSI import validateSI
from app.validateSK import validateSK
from app.validateRO import validateRO
from app.validatePT import validatePT
from app.validatePL import validatePL
from app.validateNL import validateNL
from app.validateMT import validateMT
from app.validateLU import validateLU
from app.validateLT import validateLT
from app.validateLV import validateLV
from app.validateIE import validateIE
from app.validateHU import validateHU
from app.validateGR import validateGR
from app.validateDE import validateDE
from app.validateFR import validateFR
from app.validateFI import validateFI
from app.validateEE import validateEE
from app.validateDK import validateDK
from app.validateCZ import validateCZ
from app.validateCY import validateCY
from app.validateHR import validateHR
from app.validateBG import validateBG
from app.validateBE import validateBE
from app.validateAT import validateAT

class TinBase(BaseModel):
    tinNumber: str
    validStructure: bool
    validSyntax: bool
    countryCode: str

app = FastAPI(
    title=fastapi_title,
    description=fastapi_description,
    version=fastapi_version,
)

@app.middleware("http")
async def add_no_cache_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-cache"
    return response

@app.get("/tin")
async def welcome():
    return ({
        "message": "EU TAX API"
        })

@app.get("/tin/validate",response_model=TinBase)
async def validate_TIN(countryCode: str, tinNumber: str):
    """
    Validates structure and syntax of Tax Identity Number
    """
    checkCountry(countryCode)

    #Remove space
    tinNumber = tinNumber.replace(" ","")

    if countryCode == 'IT':
        result = validateCodeIT(tinNumber)
    elif countryCode == 'ES':
        if len(tinNumber) < 9:
            n = 9 - len(tinNumber)
            # Add leading zeros
            tinNumber = tinNumber.rjust(n + len(tinNumber),'0')
        result = validateTinES(tinNumber)
    elif countryCode == 'UK':
        result = validateGB(tinNumber)
    elif countryCode == 'SE':
        result = validateSE(tinNumber)
    elif countryCode == 'SI':
        result = validateSI(tinNumber)
    elif countryCode == 'SK':
        result = validateSK(tinNumber)
    elif countryCode == 'RO':
        result = validateRO(tinNumber)
    elif countryCode == 'PT':
        result = validatePT(tinNumber)
    elif countryCode == 'PL':
        result = validatePL(tinNumber)
    elif countryCode == 'NL':
        result = validateNL(tinNumber)
    elif countryCode == 'MT':
        if len(tinNumber) < 8:
            n = 8 - len(tinNumber)
            # Add leading zeros
            tinNumber = tinNumber.rjust(n + len(tinNumber),'0')
        result = validateMT(tinNumber)
    elif countryCode == 'LU':
        result = validateLU(tinNumber)
    elif countryCode == 'LT':
        result = validateLT(tinNumber)
    elif countryCode == 'LV':
        result = validateLV(tinNumber)
    elif countryCode == 'IE':
        result = validateIE(tinNumber)
    elif countryCode == 'HU':
        result = validateHU(tinNumber)
    elif countryCode == 'GR':
        result = validateGR(tinNumber)
    elif countryCode == 'DE':
        result = validateDE(tinNumber)
    elif countryCode == 'FR':
        result = validateFR(tinNumber)
    elif countryCode == 'FI':
        result = validateFI(tinNumber)
    elif countryCode == 'EE':
        result = validateEE(tinNumber)
    elif countryCode == 'DK':
        result = validateDK(tinNumber)
    elif countryCode == 'CZ':
        result = validateCZ(tinNumber)
    elif countryCode == 'CY':
        result = validateCY(tinNumber)
    elif countryCode == 'HR':
        result = validateHR(tinNumber)
    elif countryCode == 'BG':
        result = validateBG(tinNumber)
    elif countryCode == 'BE':
        result = validateBE(tinNumber)
    elif countryCode == 'AT':
        result = validateAT(tinNumber)

    # results = {"countryCode": countryCode, 
    #         "tinNumber": tinNumber, 
    #         "validStructure": True, 
    #         "validSyntax": True}z

    result["countryCode"] = countryCode
    return result


# @app.post("/tin/validate")
# async def validate_TIN(tin: TIN):
#     checkCountry(tin.countryCode)
#     if tin.countryCode == 'IT':
#         validateCodeIT(tin.tin)
#     elif tin.countryCode == 'ES':
#         n = 9 - len(tin.tin)
#         # Add leading zeros
#         tin.tin = tin.tin.rjust(n + len(tin.tin),'0')
#         validateTinES(tin.tin,tin.foreigner)
    # return tin

def checkCountry(countryCode):
    validCountryCode=['AT','BE','BG','CY','CZ','DE','DK','EE','EL','ES','FI','FR','GR','HR','HU','IE','IT','LT','LU','LV','MT','NL','PL','PT','RO','SE','SI','SL','SK','UK']
    for i in range(len(validCountryCode)):
        if countryCode == validCountryCode[i]:
            return True
    
    raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':100, 
                            'errorMessage': 'Invalid Country Code',
                            'countryCode': countryCode
                            }
                        )


# handler = Mangum(app, enable_lifespan=False)