from Tipos import *
from Colas import Cola

MIN = 1
MAX = 10000
NULO = None

class NodoArbol:
    def __init__(self):
        self.datos: TipoElemento = None
        self.HI: PosicionArbol = None
        self.HD: PosicionArbol = None
        self.FE: int = 0
        
PosicionArbol = NodoArbol

class ArbolAVL:
    def Crear(self, avTipoClave: TipoDatosClave, alSize: int) -> Resultado:
        '''Crea el árbol vacio'''
        if  MAX < alSize < MIN:
            return Resultado.CError
        elif alSize >= MIN and alSize <= MAX:
            self.raiz = NULO
            self.q_items = 0
            self.TDatoDeLaClave = avTipoClave
            self.size = alSize
            return Resultado.OK
        
    def EsVacio(self) -> bool:
        '''Control de árbol vacío'''
        return self.raiz == NULO
    
    def EsLleno(self) -> bool:
        '''Control de árbol lleno'''
        return self.q_items == self.size
    
    def RamaNula(P: PosicionArbol) -> bool:
        '''Control de rama nula (Controla si apunta a una posición None)'''
        return P == NULO
    
    def Recuperar(self, P: PosicionArbol) -> TipoElemento:
        '''Recupera un TipoElemento de la posición P'''
        if not self.RamaNula(P):
            return P.datos
        else:
            return TipoElemento()
        
    def PreOrden(self) -> str:
        '''Recorrido Pre-Orden recursivo'''
        def PreOrd(P: PosicionArbol):
            '''Proceso que lee en preorden'''
            if self.RamaNula(P):
                S += '.'
            else:
                S += P.datos.ArmarString()
                PreOrd(P.HI)
                PreOrd(P.HD)
        
        S = ''
        PreOrd(self.raiz)
        return S
    
    def InOrden(self) -> str:
        '''Recorrido IN-Orden recursivo'''
        def InOrd(P: PosicionArbol):
            '''Proceso que lee en preorden'''
            if self.RamaNula(P):
                S += ''
            else:
                InOrd(P.HI)
                S += P.datos.ArmarString()
                InOrd(P.HD)
                
        S = ''
        InOrd(self.raiz)
        return S
    
    def PostOrden(self) -> str:
        '''Recorrido Post-Orden recursivo'''
        def PostOrd(P: PosicionArbol):
            '''Proceso que lee postorden'''
            if self.RamaNula(P):
                S += ''
            else:
                PostOrd(P.HI)
                PostOrd(P.HD)
                S += P.datos.ArmarString()
                
        S = ''
        PostOrd(self.raiz)
        return S
    
    def anchura(self) -> str:
        '''Recorre el árbol por niveles'''
        s = ''
        x = TipoElemento()
        q: PosicionArbol
        if not self.EsVacio():
            c = Cola()
            c.crear(TipoDatosClave.CADENA, self.size)
            x.valor2 = self.raiz
            c.encolar(x)
            
            while not c.esVacia():
                x = c.recuperar()
                c.desencolar()
                q = x.valor2
                s += q.datos.ArmarString()
                #Si no es nulo, se encola el hijo izquierdo
                if not self.RamaNula(q.HI):
                    x.valor2 = q.HI
                    c.encolar(x)
                
                #Si no es nulo, se encola el hijo derecho
                if not self.RamaNula(q.HD):
                    x.valor2 = q.HD
                    c.encolar(x)
                    
        return s

    def crearNodo(self, x: TipoElemento) -> PosicionArbol:
        p = PosicionArbol()
        p.datos = x
        p.HI = NULO
        p.HD = NULO
        p.FE = 0
        return p

    def R_II(N: PosicionArbol, N1: PosicionArbol):
        '''Rotación por desbalanceo izquierdo simple'''
        
        # Rotación
        N.HI = N1.HD
        N1.HD = N
        
        # Se acomoda el factor de equilibrio
        if N1.FE == -1:
            N1.FE = 0
            N.FE = 0
        else:
            N1.FE = 1
            N.FE = -1
            
        # Se retorna la nueva raíz
        N = N1
        
    def R_DD(N: PosicionArbol, N1: PosicionArbol):
        '''Rotación por desbalanceo derecho simple'''
        
        # Rotación
        N.HD = N1.HI
        N1.HI = N
        
        # Se acomoda el factor de equilibrio
        if N1.FE == 1:
            N1.FE = 0
            N.FE = 0
        else:
            N1.FE = -1
            N.FE = 1
            
        # Se retorna la nueva raíz
        N = N1

    def R_ID(N: PosicionArbol, N1:PosicionArbol):
        '''Rotación por desbalanceo doble izquierdo-derecho'''
        N2 = N1.HD
        
        # 1er rotación
        N.HI = N2.HD
        N2.HD = N
        
        # 2da rotación
        N1.HD = N2.HI
        N2.HI = N1
        
        # Se acomoda el factor de equilibrio
        if N2.FE == -1:
            N.FE = 1
        else:
            N.FE = 0

        if N2.FE == 1:
            N1.FE = -1
        else:
            N1.FE = 0
            
        # El factor de equilibrio de N2 siempre es cero
        N2.FE = 0
        
        # Se retorna la nueva raíz
        N = N2
        
    def R_DI(N: PosicionArbol, N1:PosicionArbol):
        '''Rotación por desbalanceo doble derecho-izquierdo'''
        N2 = N1.HI
        
        # 1er rotación
        N.HD = N2.HI
        N2.HI = N
        
        # 2da rotación
        N1.HI = N2.HD
        N2.HD = N1
        
        # Se acomoda el factor de equilibrio
        if N2.FE == -1:
            N1.FE = 1
        else:
            N1.FE = 0
            
        if N2.FE == 1:
            N.FE = -1
        else:
            N.FE = 0
            
        # El factor de equilibrio de N2 siempre es cero
        N2.FE = 0
        
        # Se retorna la nueva raíz
        N = N2

    def insertar(self, x: TipoElemento) -> Resultado:
        '''Función que inserta un nodo en un árbol binario balanceado'''
        def inserta(r: PosicionArbol, bh: bool):
            '''Proceso recursivo que inserta la clave'''
            nonlocal inserto
            if self.RamaNula(r):
                r = self.crearNodo(x)
                bh = True
                inserto = True
            elif x.clave < r.datos.clave:
                inserta(r.HI, bh)
                if bh:
                    if r.FE == 1:
                        r.FE = 0
                        bh = False
                    elif r.FE == 0:
                        r.FE = -1
                    elif r.FE == -1:
                        N1 = r.HI
                        if N1.FE <= 0:
                            self.R_II(r, N1)
                        else:
                            self.R_DD(r, N1)
                        bh = False
            elif x.clave > r.datos.clave or x.clave == r.datos.clave:
                inserta(r.HD, bh)
                if bh:
                    if r.FE == -1:
                        r.FE = 0
                        bh = False
                    elif r.FE == 0:
                        r.FE = 1
                    elif r.FE == 1:
                        N1 = r.HD
                        if N1.FE >= 0:
                            self.R_DD(r, N1)
                        else:
                            self.R_DI(r, N1)
                        bh = False
        
        inserto = False
        if x.TipoDatoClave(x.clave) != self.TDatoDeLaClave:
            return Resultado.ClaveIncompatible
        elif self.EsLleno:
            return Resultado.Llena
        else:
            bh = False
            inserta(self.raiz, bh)
        
            if inserto:
                self.q_items += 1
                return Resultado.OK
            else:
                return Resultado.CError
            
    def equilibrar_I(self, N: PosicionArbol, bh:bool):
        '''Al borrar un nodo por la izquierda entonces crece la derecha '''
        nonlocal bh
        if N.FE == -1:
            N.FE = 0
        elif N.FE == 0:
            N.FE = 1
            bh = False
        elif N.FE == 1:
            N1 = N.HD
            if N1.FE >= 0:
                if N1.FE == 0:
                    bh = False
                self.R_DD(N, N1)
            else:
                self.R_DI(N, N1)
                
    def equilibrar_D(self, N:PosicionArbol, bh:bool):
        '''Al borrar un nodo por la derecha entonces crece la izquierda'''
        nonlocal bh
        if N.FE == 1:
            N.FE = 0
        elif N.FE == 0:
            N.FE = -1
            bh = False
        elif N.FE == -1:
            N1 = N.HI
            if N1.FE <= 0:
                if N1.FE == 0:
                    bh = False
                self.R_II(N, N1)
            else:
                self.R_ID(N, N1)
                
    def eliminar(self, x:TipoElemento) -> Resultado:
        def elimina(r: PosicionArbol, bh: bool):
            q: PosicionArbol
            
            def B_N_R(p: PosicionArbol, bh: bool):
                '''Busca el nodo para reemplazar todo a la izquierda'''
                if p.HI != NULO:
                    B_N_R(p.HI, bh)
                    if bh:
                        self.equilibrar_I(p, bh)
                else:
                    nonlocal q
                    q.datos = p.datos
                    q = p
                    p = p.HD
                    bh = True
                    
            if not self.RamaNula(r):
                if x.clave < r.datos.clave:
                    elimina(r.HI, bh)
                    if bh:
                        self.equilibrar_I(r, bh)
                elif x.clave > r.datos.clave:
                    elimina(r.HD, bh)
                    if bh:
                        self.equilibrar_D(r, bh)
                        