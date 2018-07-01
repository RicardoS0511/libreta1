"""
from lista import*
from ABB import*
from hash import*
from AVL import*
"""
def main():
	opcion=opcion
	print("********************************")
	print("Bienvenido a tu agenda (:")
	print("Elija su estructura favorita c;")
	print("1.Lista")
	print("2. Arbol binario de busqueda")
	print("3. Hash")
	print("4. AVL")
	print("********************************")

	if opcion==1:
		from lista import*

	if opcion==2:
		from ABB import*

	if opcion==3:
		from hash import*

	if opcion==4:
		from AVL import*


if __name__ == "__main__":main()