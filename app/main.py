from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from customize import fastapi_title
from validateCodeIT import validateCodeIT
from validateTinES import validateTinES

app = FastAPI(title=fastapi_title)

class TIN(BaseModel):
    countryCode: str
    tin: str
    foreigner: bool = None

@app.get("/")
async def welcome():
    return "Welcome to European Customs and Taxation API"
@app.post("/tin/validate")
async def validate_TIN(tin: TIN):
    checkCountry(tin.countryCode)
    if tin.countryCode == 'IT':
        validateCodeIT(tin.tin)
    elif tin.countryCode == 'ES':
        n = 9 - len(tin.tin)
        # Add leading zeros
        tin.tin = tin.tin.rjust(n + len(tin.tin),'0')
        validateTinES(tin.tin,tin.foreigner)
    return tin

def checkCountry(countryCode):
    validCountryCode=['AT','BE','BG','CY','CZ','DK','EE','EL','ES','FI','FR','HR','HU','IE','IT','LT','LU','LV','MT','NL','PL','PT','RO','SE','SL','SK','UK']
    for i in range(len(validCountryCode)):
        if countryCode == validCountryCode[i]:
            return True
    
    raise HTTPException(status_code=400, 
                        detail={
                            'errorCode':100, 
                            'errorMessage': 'Invalid Country'
                            }
                        )
