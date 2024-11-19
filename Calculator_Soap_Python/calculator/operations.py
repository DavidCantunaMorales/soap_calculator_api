from calculator.client import get_soap_client

def add(a, b):
    """
    Suma dos números usando el servicio SOAP.
    """
    client = get_soap_client()
    return client.service.Add(intA=a, intB=b)

def subtract(a, b):
    """
    Resta dos números usando el servicio SOAP.
    """
    client = get_soap_client()
    return client.service.Subtract(intA=a, intB=b)

def multiply(a, b):
    """
    Multiplica dos números usando el servicio SOAP.
    """
    client = get_soap_client()
    return client.service.Multiply(intA=a, intB=b)

def divide(a, b):
    """
    Divide dos números usando el servicio SOAP.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    client = get_soap_client()
    return client.service.Divide(intA=a, intB=b)
