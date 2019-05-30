
import argparse  

#Colores
rd='\033[1;31m'
gr='\033[1;32m'
xx='\033[0m'

# Parse the target options 
parser = argparse.ArgumentParser() 
parser.add_argument("-c", "--cadenita", help="Cadena a descifrar")

args = parser.parse_args() 

if args.cadenita:
	cadena = args.cadenita
else:
	print "\n"+rd+"El argumento: [-c|--cadena], es obligatorio\n"+xx
	exit()


if __name__ == "__main__":
	
	Cero =[]
	Uno = []
	Dos = ["a","b","c"]
	Tres = ["d","e","f"]
	Cuatro = ["g","h","i"]
	Cinco = ["j","k","l"]
	Seis = ["m","n","o"]
	Siete = ["p","q","r","s"]
	Ocho = ["t","u","v"]
	Nueve = ["w","x","y","z"]
	
	ListadoArrays = Cero,Uno,Dos,Tres,Cuatro,Cinco,Seis,Siete,Ocho,Nueve
	Contador = 0
	LastDigito = 99
	Mensaje = ""
	
	for c in range(len(cadena)):
		
		if LastDigito != cadena[c] and LastDigito != 99:
			
			if ord(LastDigito) > 49 and ord(LastDigito) < 58:
				a = ListadoArrays [int(LastDigito)]
				Mensaje += a[Contador-1]
			else:
				Mensaje += LastDigito
			Contador = 0
					
		if ord(cadena[c]) > 49 and ord(cadena[c]) < 58:
			Contador += 1
			LastDigito = cadena[c]
		else:
			LastDigito = cadena[c]
			
print "\nEl mensaje ha quedado: "+gr+str(Mensaje)
