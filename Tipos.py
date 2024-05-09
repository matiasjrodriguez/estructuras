from enum import Enum

cTab = chr(9)

class Resultado(Enum):
    '''Retorno de las funciones de manejo de estructuras'''
    OK=1
    CError=2
    Llena=3
    Vacia=4
    PosicionInvalida=5
    Otro=6
    ClaveIncompatible=7
    ClaveDuplicada=8

class TipoDatosClave(Enum):
    '''Tipo de datos soportados por la clave'''
    NUMERO=1
    CADENA=2
    OTROS=3

class TipoElemento:
    '''Datos a guardar dentro de las estructuras'''
    def __init__(self, clave='', valor1='', valor2=None):
        self.clave = clave
        self.valor1 = valor1
        self.valor2 = valor2
        
    def ArmarString(self) -> str:
        try:
            sv = str(self.clave)
            sv += cTab + str(self.valor1)
            return sv
        except:
            return ''                 
    
    def TipoDatoClave(self, clave) -> TipoDatosClave:
        '''Evalua el valor de la clave y retorna el tipo de dato'''
        print('hasta acá funciona')
        if isinstance(clave, (int, float, complex)):
            return TipoDatosClave.NUMERO
        elif isinstance(clave, str):
            return TipoDatosClave.CADENA
        else:
            return TipoDatosClave.OTROS
