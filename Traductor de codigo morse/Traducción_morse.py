def texto_a_morse (texto):
    
    texto = texto.upper ()

    diccionario_morse = { 
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    } #Diccionario de texto a código morse

    traduccion_a_morse = [] #Lista para guardar la traducción

    for letra in texto:
        if letra in diccionario_morse:
            traduccion_a_morse.append(diccionario_morse[letra])
        elif letra == " ":
            traduccion_a_morse.append(" ")
        else:
            traduccion_a_morse.append(letra)
    
    return ' '.join (traduccion_a_morse) #Une la lista con la traducción, para que sea un texto legible

def morse_a_texto (morse):
    
    codigo_letra = morse.split (" ")

    diccionario_texto = {
        '.-': 'a', '-...': 'b', '-.-.': 'c','-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g',
        '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n',
        '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u',
        '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z',
    } #Diccionario de morse a texto

    traduccion_a_texto = []

    for codigo in codigo_letra:
        if codigo in diccionario_texto:
            traduccion_a_texto.append (diccionario_texto[codigo])
        elif codigo == "":
            traduccion_a_texto.append (" ")
        else:
            traduccion_a_texto.append (codigo)
    
    return ''.join (traduccion_a_texto)

print ("Bienvenid@ al traductor de código morse")

def main ():
    while True:
        print ("\n¿Que deseas hacer?")
        print ("\n1) Traducir de texto a morse.")
        print ("2) Traducir de morse a texto.")
        print ("3) Salir del programa")
        eleccion = input ("Seleccione la opción que desea realizar (1, 2, 3): ")
        if eleccion == "1":
            texto = input ("\nIngresa el texto a traducir: ")
            morse = texto_a_morse (texto)
            print ("\nLa traducción a morse es:", morse)
        elif eleccion == "2":
            print ("\nNOTA: Registre el codigo agregando un espacio al final de cada combinación")
            morse = input ("Ingresa el código morse a traducir: ")
            texto = morse_a_texto (morse)
            print ("\nLa traducción a texto es:", texto)
        elif eleccion == "3":
            break
        else:
            print ("La opción seleccionada no se encuentra, intenta nuevamente")

main()