# Variables individuales para cada alimento.
ENSALADA = 15
SOPA = 18
PASTA = 20
POLLO = 24
PESCADO = 27
ARROZ = 30
CARNE = 36
PATATAS = 38
LEGUMBRES = 40
VERDURAS = 42
HUEVO = 45
TOSTADA = 34
BACON = 23
SALCHICHAS = 45
MANZANA = 10
PERA = 8
PLATANO = 7
CEREALES = 9
YOGUR = 11

# Listas anidadas para desayunos, comidas, y cenas.
desayunos = [
    [MANZANA, PERA, PLATANO],      # ligero
    [TOSTADA, CEREALES, YOGUR],    # medio
    [HUEVO, BACON, SALCHICHAS]     # pesado
]

comidas = [
    [ENSALADA, SOPA, PASTA],       # ligero
    [POLLO, PESCADO, ARROZ],       # medio
    [CARNE, PATATAS, LEGUMBRES]    # pesado
]

cenas = [
    [SOPA, VERDURAS, PESCADO],     # ligero
    [POLLO, PESCADO, ARROZ],       # medio
    [CARNE, PATATAS, LEGUMBRES]    # pesado
]

# Para más detalles sobre las listas en Python, 
# consulte: https://docs.python.org/3/tutorial/introduction.html#lists


def mostrar_menu_principal():
    """Muestra el menu principal y toma la opcion del usuario.

    Return:
        int: Opcion seleccionada por el usuario.
    """
    print("Menu principal:\n1.Desayuno\n2.Comida\n3.Cena\n4.Salir")
    opcion = int(input("Elije una opcion: "))
    return opcion

def mostrar_comida(tipo_comida):
    """
    Esta funcion recibe un numero 1-3  e 
    imprime el tipo de comida al que corrresponde.
    Si recibe 1, imprime "Elegiste Desayuno".
    Si recibe 2, imprime "Elegiste Comida".
    Si recibe 3, imprime "Elegiste Cena".

    Args:
        tipo_comida (int): tipo de comida

    Return:
        None
    """
    # Validar entrada
    if ((tipo_comida >= 1) and (tipo_comida <= 3)):
        if tipo_comida == 1:
            print("Elegiste Desayuno...")
        elif tipo_comida == 2:
            print("Elegiste Comida...")
        else:
            print("Elegiste Cena...")
    else:
        print("Error, el valor que ingresaste no existe.")

def mostrar_grupos_alimentos(tipo_comida):
    """
    Esta funcion recibe un numero 1-3  e imprime 
    los alimentos si es ligera, media o pesada.
    Si recibe 1, imprime:
    Ligera: Manzana, Pera, Plátano
    Media: Tostada, Cereales, Yogur
    Pesada: Huevo, Bacon, Salchichas
    
    Args:
        tipo_comida (int): tipo de comida

    Return:
        None
    """
    # Validar entrada
    if ((tipo_comida >= 1) and (tipo_comida <= 3)):
        if tipo_comida == 1:  # Desayuno
            print("Ligera: Manzana, Pera, Platano")
            print("Media: Tostada, Cereales, Yogur")
            print("Pesada: Huevo, Bacon, Salchichas")
        elif tipo_comida == 2:  # Comida
            print("Ligera: Ensalada, Sopa, Pasta")
            print("Media: Pollo, Pescado, Arroz")
            print("Pesada: Carne, Patatas, Legumbres")
        else:  # Cena
            print("Ligera: Sopa, Verduras, Pescado")
            print("Media: Pollo, Pescado, Arroz")
            print("Pesada: Carne, Patatas, Legumbres")
    else:
        print("Error, el valor que ingresaste no existe.")

def mostrar_ligera_media_pesada():
    """Muestra el menu para elegir el tipo de comida 
    y toma la opcion del usuario.

    Return:
        int: Opcion seleccionada por el usuario.
    """
    print("Menu de opciones:\n1.Ligera\n2.Media\n3.Pesada")
    opcion = int(input("Elije una opción: "))
    return opcion

def mostrar_opcion_ligera_media_pesada(opcion_comida):
    """
    Esta funcion recibe un numero 1-3  
    e imprime si elegiste ligera, media o pesada.
    Si elegiste 1, imprime "Elegiste ligera"
    Si elegiste 2, imprime "Elegiste Media"
    Si elegiste 3, imprime "Elegiste Pesada"

    Args:
        opcion_comida (int): opcion de comida

    Return:
        None
    """
    # Validar entrada
    if ((opcion_comida >= 1) and (opcion_comida <= 3)):
        if opcion_comida == 1:
            print("Elegiste Ligera...")
        elif opcion_comida == 2:
            print("Elegiste Media...")
        else:
            print("Elegiste Pesada...")
    else:
        print("Error, el valor que ingresaste no existe.")

def calcular_cal(tipo_comida, opcion_comida):
    """
    Esta funcion recibe tipo de comida 1-3 y 
    opcion de comida 1-3.

    Si el tipo de comida es 1 y opcion de comida es 1.

    Args:
        opcion_comida (int): opción de comida
        tipo_comida (int): tipo de comida

    Return:
        ligero_desayuno
    """
    # Validar entrada
    if ((tipo_comida >= 1) and (tipo_comida <= 3)):
        comidas_dict = {
        1: desayunos,
        2: comidas,
        3: cenas
        }

        # Para más detalles sobre diccionarios, 
        # https://docs.python.org/3/tutorial/datastructures.html#dictionaries

        comidas_elegidas = comidas_dict[tipo_comida]
        total = sum(comidas_elegidas[opcion_comida - 1])
        return total
    else:
        print("Error, el valor que ingresaste no existe.")

if __name__ == '__main__':
    
    total_calorias = 0
    contador_comidas = 0

    # Bievenida
    while True:
        
        # Mostrar menu
        comida_principal = mostrar_menu_principal()
        print('\n')

        # Salir si el usuario elige 4 o un numero diferente de 1,2 o 3.
        if (comida_principal == 4):
                print("Elegiste salir")
                break
        
        while((comida_principal >= 4) or (comida_principal < 1)):
                print("Debes de elegir, desayuno, comida o cena!!!")
                comida_principal= mostrar_menu_principal()
       
        # Mostrar comida (Desayuno, Comida, Cena)
        # Ejemplo: Elegiste Desayuno...
        print("*" * 50)
        mostrar_comida(comida_principal)

        # Mostrar tipos de alimentos indicados
        #  por comida (Desayuno, Comida, Cena)
        # Ejemplo: Ligera: Manzana, Pera, Plátano
        mostrar_grupos_alimentos(comida_principal)
        print("*" * 50)

        # Mostrar opcion de acuerdo a comida 
        # (desayuno, comida, cena) y tipo (ligera, media, pesada)
        # Ejemplo: Elegiste Ligera... 
        # eleccion = mostrar_ligera_media_pesada()
        opcion_comida = mostrar_ligera_media_pesada()
        print("*" * 50)

        while((opcion_comida >= 4) or (opcion_comida < 1)):
            print("Debes de elegir, ligera, media o pesada!!!")
            opcion_comida = mostrar_ligera_media_pesada()
        
        # Mostrar opcion de la comida que elegiste
        mostrar_opcion_ligera_media_pesada(opcion_comida)
    
        # Mostrar total de comidas
        if (opcion_comida >= 1 and opcion_comida <= 3):
            contador_comidas += 1
            total_calorias += calcular_cal(comida_principal, opcion_comida)
            # Calcular calorias de acuerdo a opcion de comida 
            # y tipo de comida.
            # Ejemplo: Calorías totales: 180
        print(f"Has comido {contador_comidas} veces")
        
        # Mensajes preventivos de acuerdo a numero de comidas
        if contador_comidas < 3:
            print("Debes comer al menos 3 veces al dia")
        elif contador_comidas == 3:
            print("Numero de comidas recomendadas")
            #  Reducir calorías en 20%
            total_calorias *= 0.8
        else:
            # Aumentar calorías en 10%
            total_calorias *= 1.1
            print("Advertencia, numero de comidas mayor a 3")

        print(f"Total de calorias: {total_calorias}")
        print("*" * 50)
        print('\n')
    # Mostrar si eleecion es saludable o excede las calorias recomendadas
    if  total_calorias > 0 and  total_calorias <= 1500:
        print("Tu eleccion es saludable")
    elif total_calorias > 1500:
        print("Eleccion excede calorias recomendadas")
