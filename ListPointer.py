from Tipos import *

MIN = 1
MAX = 2000
NULO = None

class NodoLista:
    def __init__(self, datos: TipoElemento = None, ante = None, prox = None) -> None:
        self.datos = datos
        self.ante: PosicionLista = ante
        self.prox: PosicionLista = prox
        
PosicionLista = NodoLista
        
class Lista:
    
    ### Métodos indispensables para el final ###
    
    def crear(self, avTipoClave: TipoDatosClave, alSize: int) -> Resultado:
        '''Crea la lista vacía'''
        if  MAX > alSize > MIN:
            self.inicio: PosicionLista = NULO
            self.final: PosicionLista = NULO
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
        '''Valida la posición de la lista'''
        encontre = False
        if not self.esVacia():
            q = self.inicio
            while q != NULO and not encontre:
                if q == p:
                    encontre = True
                else:
                    q = q.prox
                    
        return encontre
    
    def agregar(self, x: TipoElemento) -> Resultado:
        '''Agrega un item al final de la lista'''
        # Controlo que el tipo de dato de la clave sea homogeneo a la lista
        if x.TipoDatoClave(x.clave) != self.TDatoDeLaClave:
            return Resultado.ClaveIncompatible
        elif self.esLlena():
            return Resultado.Llena
        else:
            q = NodoLista()
            q.datos = x
            q.prox = NULO
            q.ante = self.final
            if self.esVacia():
                # Se asigna como primer elemento de la lista
                self.inicio = q  
            else:
                # Se apunta al último elemento
                self.final.prox = q
            self.final = q
            self.q_items += 1
            return Resultado.OK
        
    def insertar(self, x: TipoElemento, p: PosicionLista) -> Resultado:
        '''Inserta un item entre el inicio y el final de la lista'''
        # Controlo que el tipo de dato de la clave sea homogeneo a la lista
        if x.TipoDatoClave(x.clave) != self.TDatoDeLaClave:
            return Resultado.ClaveIncompatible
        elif self.esLlena():
            return Resultado.Llena
        else:
            if self.validarPosicion(p):
                q = NodoLista()
                q.datos = x
                q.prox = p
                q.ante = p.ante
                if p == self.inicio:
                    self.inicio = q
                else:
                    p.ante.prox = q
                p.ante = q
                self.q_items += 1
                return Resultado.OK
            else:
                return Resultado.PosicionInvalida
            
    def actualizar(self, x: TipoElemento, p: PosicionLista) -> Resultado:
        '''Cambia un item dentro de la lista'''
        if x.TipoDatoClave(x.clave) != self.TDatoDeLaClave:
            return Resultado.ClaveIncompatible
        elif self.validarPosicion(p):
            p.datos = x
            return Resultado.OK
        else:
            return Resultado.PosicionInvalida
            
    def eliminar(self, p: PosicionLista) -> Resultado:
        '''Elimina un elemento de cualquier posicion de la lista.'''
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
                    self.inicio = self.inicio.prox
                    self.inicio.ante = NULO
                elif p == self.final:
                    # Se elimina el último elemento. Cambia el final
                    self.final = self.final.ante
                    self.final.prox = NULO
                else:
                    # Se elimina cualquier otro elemento que no es el inicio ni el final
                    p.ante.prox = p.prox
                    p.prox.ante = p.ante  
                    
                del q
                self.q_items -= 1
                return Resultado.OK
            else:
                return Resultado.PosicionInvalida
            
    ### Métodos extra ###
    
    def llenar_claves_random(self, al_size: int, rango_desde: int, rango_hasta: int) -> Resultado:
        '''Llena la lista de 0 a rango_hasta'''
        if self.crear(TipoDatosClave.NUMERO, al_size) == Resultado.OK:
            import random
            while not self.esLlena():
                x = TipoElemento()
                x.clave = rango_desde + random.randint(0, rango_hasta)
                self.agregar(x)
            return Resultado.OK
        else:
            return Resultado.CError
        