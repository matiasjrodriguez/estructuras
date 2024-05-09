from Tipos import *
import numpy

MIN = 1
MAX = 2000
NULO = 0

class NodoLista:
    def __init__(self, datos: TipoElemento = None, ante = None, prox = None):
        self.datos = datos
        self.ante: PosicionLista = ante
        self.prox: PosicionLista = prox
        
PosicionLista = NodoLista

def SetLength(size):
    posiciones = []
    nodo_vacio = NodoLista()
    for _ in range(size):
        posiciones.append(nodo_vacio)
    
    return numpy.array(posiciones)

class Lista:
    
    ### Métodos indispensables para el final ###
    
    def crear(self, avTipoClave: TipoDatosClave, alSize: int) -> Resultado:
        '''Crea la lista vacía'''
        if MAX > alSize > MIN:
            # La posición 0 no la usamos pero la tenemos en cuenta
            
            self.cursor = SetLength(alSize+1)
            # Encadenamiento de libres
            for Q in range(MIN, alSize-1): 
                self.cursor[Q].prox = Q+1
            self.cursor[alSize].prox = NULO
            self.libre = MIN
            self.inicio = NULO
            self.final = NULO
            self.q_items = 0
            self.TDatoDeLaClave = avTipoClave
            self.size = alSize
            return Resultado.OK
        else:
            return Resultado.CError

    def esVacia(self) -> bool:
        '''Control de lista vacía'''
        return self.inicio == NULO
    
    def esLlena(self) -> bool:
        '''Control de lista llena'''
        return self.size == self.q_items
    
    def validarPosicion(self, p: PosicionLista) -> bool:
        '''Valida la posicion de la lista'''
        encontre = False
        if not self.esVacia():
            q = self.inicio
            while q != NULO and not encontre:
                if q == p:
                    encontre = True
                else:
                    q = self.cursor[q].prox
        
        return encontre
    
    def agregar(self, x: TipoElemento) -> Resultado:
        '''Agrega un item al final de la lista'''
        if x.TipoDatoClave(x.clave) != self.TDatoDeLaClave:
            return Resultado.ClaveIncompatible
        elif self.esLlena():
            return Resultado.Llena
        else:
            q = self.libre
            self.libre = self.cursor[self.libre].prox
            self.cursor[q].datos = x
            self.cursor[q].prox = NULO
            self.cursor[q].ante = self.final
            if self.esVacia():
                self.inicio = q
            else:
                self.cursor[self.final].prox = q
            self.final = q
            self.q_items += 1 
            return Resultado.OK
        
    def insertar(self, x: TipoElemento, p: PosicionLista) -> Resultado:
        '''Inserta un item entre el inicio y el final de la lista'''
        if x.TipoDatoClave(x.clave) != self.TDatoDeLaClave:
            return Resultado.ClaveIncompatible
        elif self.esLlena():
            return Resultado.Llena
        else:       
            if self.validarPosicion(p):
                q = self.libre
                self.libre = self.cursor[self.libre].prox
                self.cursor[q].datos = x
                self.cursor[q].prox = p
                self.cursor[q].ante = self.cursor[p].ante          
                self.cursor[p].ante = q
                if p == self.inicio:
                    self.inicio = q
                else:
                    self.cursor[self.cursor[q].ante].prox = q
                self.q_items += 1
                return Resultado.OK
            else:
                return Resultado.PosicionInvalida
     
     
    def actualizar(self, x: TipoElemento, p: PosicionLista) -> Resultado:
        '''Cambia un item dentro de la lista'''
        if x.TipoDatoClave(x.clave) != self.TDatoDeLaClave:
            return Resultado.ClaveIncompatible
        elif self.validarPosicion(p):
            self.cursor[p].datos = x
            return Resultado.OK
        else:
            return Resultado.PosicionInvalida
        
    def eliminar(self, p: PosicionLista) -> Resultado:
        '''Elimina un elemento de cualquier posición de la lista.'''
        if self.esVacia():
            return Resultado.Vacia
        else:
            if self.validarPosicion(p):
                q = p
                if self.inicio == p == self.final:
                    # Único elemento en la lista. Se vuelve a crear la lista vacía
                    self.crear(self.TDatoDeLaClave, self.size)
                elif p == self.inicio:
                    # Se elimina el primer elemento. Cambia el inicio
                    self.inicio = self.cursor[self.inicio].prox
                    self.cursor[self.inicio].ante = NULO
                elif p == self.final:
                    # Se elimina el último elemento. Cambia el final
                    self.final = self.cursor[self.final].ante
                    self.cursor[self.final].prox = NULO
                else:
                    # Se elimina cualquier otro elemento que no es el inicio ni el final
                    self.cursor[self.cursor[p].ante].prox = self.cursor[p].prox
                    self.cursor[self.cursor[p].prox].ante = self.cursor[p].ante

                self.cursor[q].prox = self.libre
                self.q_items -= 1
                return Resultado.OK
            else:
                return Resultado.PosicionInvalida
            
    ### Métodos extra ###
            
if __name__ == '__main__':
    l1 = Lista()
    l1.crear(TipoDatosClave.NUMERO, 5)

