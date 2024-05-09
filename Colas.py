from Tipos import *

MIN = 1
MAX = 2000
NULO = None

class NodoCola:
    def __init__(self):
        self.datos: TipoElemento = None
        self.prox: PosicionCola = None
        
PosicionCola = NodoCola

class Cola:
    def crear(self, avTipoClave: TipoDatosClave, alSize: int) -> Resultado:
        '''Crea la cola vacía'''
        if  MAX < alSize < MIN:
            return Resultado.CError
        elif alSize >= MIN and alSize <= MAX:
            self.inicio: PosicionCola = NULO
            self.fin: PosicionCola = NULO
            self.q_items: int = 0
            self.TDatoDeLaClave: TipoDatosClave = avTipoClave
            self.size: int = alSize
            return Resultado.OK
        
    def esVacia(self) -> bool:
        '''Control de cola vacía'''
        return self.inicio == NULO
    
    def esLlena(self) -> bool:
        '''Control de cola llena'''
        return self.q_items == self.size
    
    def encolar(self, x: TipoElemento) -> Resultado:
        '''Agrega items a la cola'''
        if x.TipoDatoClave(x.clave) != self.TDatoDeLaClave:
            return Resultado.ClaveIncompatible
        elif self.esLlena():
            return Resultado.Llena
        else:
            q = PosicionCola()
            q.prox = NULO
            if self.esVacia():
                self.inicio = q
            else:
                self.fin.prox = q
            q.datos = x
            self.fin = q
            self.q_items += 1
            return Resultado.OK

    def desencolar(self) -> Resultado:
        '''Elimina un item de la cola. Siempre del final'''
        if self.esVacia():
            return Resultado.Vacia
        else:
            q = self.inicio
            self.inicio = self.inicio.prox
            self.q_items -= 1
            del q
            return Resultado.OK
        
    def recuperar(self) -> TipoElemento:
        if not self.esVacia():
            return self.inicio.datos
        else:
            return TipoElemento()