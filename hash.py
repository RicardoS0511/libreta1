class Contacto:
	def __init__(self,apellido,nombre,telefono,email):
		self.apellido=apellido
		self.nombre=nombre
		self.telefono=telefono
		self.email=email
class Nodo:
  def __init__(self):
  	self.next=None
def str2num(key):
  return sum([ord(c) for c in key])
def hashstr(key,size):
  return str2num(key)%size
def get_apellido(self):
	return(self.apellido)
def get_nombre(self):
	return(self.nombre)
def get_telefono(self):
	return(self.telefono)
def get_email(self):
	return(self, email)
 
class cola:
	def __init__(self):
		self.prim=None
		self.last=None
		self.cout=0
	def insertar(self,contacto):
		if(self.prim is None):
			self.prim=self.last=contacto
			self.cout=self.cout+1
			return
		if(self.last.next is None):
			if(contacto.get_apellido()==self.prim.get_apellido()):
				self.prim=self.last=contacto
				return
			if(contacto.get_apellido()>self.prim.get_apellido()):
				primero=self.prim
				self.last=primero
				primero.next=contacto
				self.prim=contacto
				self.cout=self.cout+1
				return
			else:
				contacto.next=self.prim
				self.last=contacto
				self.cout=self.cout+1
				return
			pos=self.last
		while(pos.next is not None):
			if(contacto.get_apellido()==get_apellido()):
				contacto.next=pos.next #lo remplazo
			parent.next=contacto
			return
			if(contacto.get_apellido()<pos.get_apellido()):
				contacto.next=pos
				parent.next=contacto
				self.cout=self.cout+1
				return
			parent=pos
			pos=pos.next 
		if(contacto.get_apellido()>pos.get_apellido()):
			pos.next=contacto
			self.prim=contacto
			self.cout=self.cout+1
		else:
			parent.next=contacto
			contacto.next=pos
			self.cout=self.cout+1
class HashInsertar:
  def __init__(self,size):
    self.lista = [None]*size
    self.size= size
  def put(self,apellido, nombre, telefono, email):
    contacto=Contacto(apellido, nombre, telefono, email)
    pos = hashstr(apellido,self.size)
    if self.lista[pos] is not None:
      #Si existe esa cola, agrego
      self.lista[pos].insertar(contacto)
    else:
      #Si no existe creo una cola y agrego
      self.lista[pos]=cola()
      self.lista[pos].insertar(contacto)
  def listado(self,apellido):
    pos = hashstr(apellido,self.size)
    if self.list[pos] is not None:#si existe
      aux=self.list[pos]
    else:
      print("contacto no encontrado")
class Hash:
  def __init__(self):
    self.H_inserta=HashInsertar(10)
  def put_hash(self,apellido, nombre, telefono, email):
    self.H_inserta.put(apellido, nombre, telefono, email)
    return
  def imprimir(self,elemento):# elemento es un objeto tipo contacto
  	while True:
  		if elemento.apellido ==contacto.apellido:
  			print(contacto)
  def listado_hash(self,apellido):
    print("Busqueda de contacto",apellido)
    self.H_imprime.listado(apellido)
    return
  def eliminar(self,elemento):# elemento es un objeto tipo contacto
  	while True:
  		if elemento.apellido == contacto.next.apellido and elemento.nombre == contacto.next.nombre:
  			contacto.next=contacto.next.next
  			return contacto

H = Hash()
H.put_hash("gonzalez","rene",5959,"123@mail.cl")
H.put_hash("salazar","juan",133,"666@mail.cl")
#H.listado_hash("salazar")
#H.listado_hash("gonzalez")