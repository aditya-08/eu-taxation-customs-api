from pydantic import BaseModel

class TIN(BaseModel):
    countryCode: str
    tin: str
    foreigner: bool = None