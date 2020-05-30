from zeep import Client

def callVatService(countryCode, vatNumber):
    client = Client('https://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl')
    result = client.service.checkVat(countryCode,vatNumber)

    return result

print(callVatService('GB', 31800554))