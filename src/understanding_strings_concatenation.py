# Trabajndo en listas
print("\n\t Hoy toca trabajar con listas \n".upper())

# Vamos a crear una lista de puros strings con nombres 
magicians = ['harry', 'ron', 'hermione', 'snape']
print(magicians)

print(magicians[0], magicians[1], magicians[2], magicians[3])
# print(magicians[0], magicians[1], magicians[2], magicians[3])

#CICLO FOR
print("\n\t Ciclo For \n".upper())

for magician in magicians: 
    print(magician)

# A esto se le llama looping

# Ahora vamos a imprimri un mensaje para cada mago
print("\n")
for magician in magicians: 
    print(f"{magician.title()} ese fue un gran hechizo.")
    print(f"No puedo esperar a ver el siguiente hechizo, {magician.upper()}")
    print("\n")
print("Gracias a todos. Fue un gran espectaculo.")
# Combinacion o Concatenacion de STRING
first_name = 'charly'
last_name = "mercury"
full_name = first_name + " " + last_name
print(full_name.title())

print("Hola".upper(), "Carlos" + " " +"Tovar", first_name.title()+" "+last_name.title())

message = "Hola, " +full_name.title() + "!"
print(message)

# WHITE SPACES

"""
    White Space se refiere a cualquier String
    (caracter) que no se imprime, es decir,
    un espacio (" "), tabuladores (\t) y 
    finales de linea (\n).

    LOs White Spaces se utilizan comunmente para
    organizar las salidas d etextos a usuario
    de tal manera que sea mas amigable de leer
    o ver para los usuarios.
"""
print("Python")
print("\tPython")
print("\t\tPython")
print("Lenguajes: \n Python \n C \n JavaScript")

# F-String

famous_person = "charly mercury"
message = f"{famous_person} una ves dijo: Python es amor."
print(message)

qoute = "Python is in the air"
message_2= f"{famous_person} una ves dijo {qoute}"
print(message_2)