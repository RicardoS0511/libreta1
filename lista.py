class Contacto:
	def __init__(self,apellido,nombre,telefono,email):
		self.apellido=apellido
		self.nombre=nombre
		self.telefono=telefono
		self.email=email
class nodo:
	def __init__(self,data):
		self.next = None
		self.prev = None
		self.data= None
class lista:
	def __init__(self):
		self.head=None
		self.last=None
	def insertar(self, element):#element va a ser un objeto tipo contacto
		if self.head == None:
			self.head = element
			self.last = element
		else:
			self.element.prev=self.last
			self.last.next = element
			self.last= element
		#sistema de ordenamineto 
	def insertionSort(lista):
   		for i in range(1,len(lista)):
   			valor = lista[i]
   			posicion = i

     		while posicion>0 and lista[posicion-1]>valor:
     			if valor== self.head:
	     			lista[posicion]=lista[posicion-1]
	     			posicion = posicion-1
	     			lista[posicion]=valor
	     			self.head =  valor
	     		elif valor == self.last:
	     			lista[posicion]=lista[posicion-1]
	     			posicion = posicion-1
	     			lista[posicion]=valor
	     			self.last =  valor
	     		else:
	     			lista[posicion]=lista[posicion-1]
	     			posicion = posicion-1
	     			lista[posicion]=valor

	def buscar(self, element, aux):#element sera un objeto tipo contacto, y en aux le pasarmos la cabeza
		if self.element == self.aux.data:
			return element
		elif self.aux == self.last and self.element != self.last:
			return None
		else:
			buscar(element, aux.next)
	def eliminar(self, element, aux):
		if self.element == self.head:
			pass
		if self.element == self.last:
			pass
		if self.element == self.aux.data:
			self.aux.data.next ==self.aux.data.next.next
			self.aux.data.prev == self.data.prev.prev 
		elif self.aux == self.last and self.element!= self.last:
			return None
		else:
			eliminar(element, aux.next)
	def imprimir(self, aux):
		if self.aux!=self.last:
			print(aux)
			imprimir(aux.next)
		if self.aux == self.last:
			print(last)
			return
l=lista()
contacto= "santibanez", "ricardo", 123, "jajaja"
l.insertar(contacto)

