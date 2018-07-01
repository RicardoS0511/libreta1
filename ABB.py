class Contacto:
	def __init__(self,apellido,nombre,telefono,email):
		self.apellido=apellido
		self.nombre=nombre
		self.telefono=telefono
		self.email=email
class Nodo:
	def __init__(self):
		self.data=None
		self.hijoIzquierdo=None
		self.hijoDerecho=None
        self.nodo=None
def ambos(self):
    return self.left and self.rigth
class arbolAbb:
 	def __init__ (self):
 		self.raiz = None
 		self.tamano= 0
 	def longitud(self):
 		return self.tamano
 	def ambos(self):
 		return self.left and self.rigth
    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)
    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre
        return not (self.hijoDerecho or self.hijoIzquierdo)
 	def insertar(self, contacto, root):
 		if self.root == None:
 			nodito = nodo(contacto)
 			self.root=nodito
 		else:
 			if self.root.data.telefono > self.contacto.telefono:
 				if self.head.left == None:
 					self.head.data=nodito
 				else:
 					insertar(contacto, root.left)
 			if self.root.data.telefono <  self.contacto.telefono:
 				if self.head.rigth == None:
 					self.head.data=nodito
 				else:
 					insertar(contacto, root.rigth)
 		self.tamano=self.tamano+1
 			

 	def buscar(self, nombre,telefono, nodo):#nodo = root y element es un objeto de tipo contacto
 		if self.nombre==nodo.data.nombre:
 			return  nodo
 		elif self.telefono<nodo.data.telefono:
 			if self.nombre==nodo.left.data.nombre:
 				return nodo
 			elif nodo.left!=None:
 				self.buscar(nombre,telefono,nodo.rigth)
 		elif self.telefono>nodo.data.telefono:
 			if nombre ==nodo.rigth.data.nombre:
 				return nodo
 			elif nodo.rigth!=None:
 				self.buscar(nombre,telefono,nodo.rigth)
 	def obtener(self,element,nodo):
 		if not nodo:
 			return None
 		elif nodo.element == element:
 			return nodo
 		elif element < nodo.element:
 			return self.obtener(element,nodo.left)
 		else:
 			return self.obtener(element,nodo.rigth)
    def empalmar(self):
        if self.esHoja():
            if self.esHijoIzquierdo():
             self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                self.hijoDerecho.padre = self.padre
    def remover(self,nodoActual):
         if nodoActual.esHoja(): #hoja
           if nodoActual == nodoActual.padre.hijoIzquierdo:
               nodoActual.padre.hijoIzquierdo = None
           else:
               nodoActual.padre.hijoDerecho = None
         elif nodoActual.tieneAmbosHijos(): #interior
           suc = nodoActual.encontrarSucesor()
           suc.empalmar()
           nodoActual.clave = suc.clave
           nodoActual.cargaUtil = suc.cargaUtil

         else: # este nodo tiene un (1) hijo
           if nodoActual.tieneHijoIzquierdo():
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave,
                                    nodoActual.hijoIzquierdo.cargaUtil,
                                    nodoActual.hijoIzquierdo.hijoIzquierdo,
                                    nodoActual.hijoIzquierdo.hijoDerecho)
           else:
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave,
                                    nodoActual.hijoDerecho.cargaUtil,
                                    nodoActual.hijoDerecho.hijoIzquierdo,
                                    nodoActual.hijoDerecho.hijoDerecho)

    def eliminar(self, element, nodo):
 		if self.tamano > 1:
 			nodo = self.obtener(element,self.root)
 			if nodo:
 				self.remover(nodo)
 				self.tamano = self.tamano-1
 			else:
 				raise KeyError("Este elemento no esta en el alrbol")
 		elif self.tamano == 1 and self.root.element == element:
 			self.root = None
 			self.tamano = self.tamano - 1
 		else:
 			raise KeyError("Este elemento no esta en el alrbol")