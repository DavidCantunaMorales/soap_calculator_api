from zeep import Client

# URL del WSDL
WSDL_URL = 'http://www.dneonline.com/calculator.asmx?WSDL'

# Crear cliente SOAP
client = Client(wsdl=WSDL_URL)

def get_soap_client():
    """
    Retorna el cliente SOAP configurado.
    """
    return client
