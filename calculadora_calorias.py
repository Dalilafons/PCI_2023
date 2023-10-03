ensalada = 15
sopa = 18
pasta = 20
pollo = 24
pescado = 27
arroz = 30
carne = 36
patatas = 38
legumbres = 40
verduras = 42
huevo = 45
tostada = 34
bacon = 23
salchichas = 45
manzana = 10
pera = 8
platano = 7
cereales = 9
yogur = 11

ligero_desayuno = [manzana, pera, platano]
medio_desayuno = [tostada , cereales , yogur]
pesado_desayuno = [huevo , bacon , salchichas]

ligero_comida = [ensalada , sopa , pasta]
medio_comida = [pollo , pescado , arroz]
pesado_comida = [carne , patatas , legumbres]

ligero_cena = [sopa , verduras , pescado]
medio_cena = [pollo , pescado ,arroz]
pesado_cena = [carne , patatas ,legumbres]

def mostrar_menu_principal():
    print("Menú principal:\n1.Desayuno\n2.Comida\n3.Cena\n4.Salir")
    opcion = int(input("Elije una opción: "))
    return opcion

def mostrar_comida(tipo_comida):
    """
    Esta función recibe un numero 1-3  e imprime el tipo de comida al que corrresponde.
    Si recibe 1, imprime "Elegiste Desayuno".
    Si recibe 2, imprime "Elegiste Comida".
    Si recibe 3, imprime "Elegiste Cena".

    Args:
        tipo_comida (int): tipo de comida

    Return:
        None
    """
    #Validar entrada
    if ((tipo_comida >=1) and (tipo_comida <=3)):
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
    Esta función recibe un numero 1-3  e imprime los alimentos si es ligera, media o pesada.
    Si recibe 1, imprime:
    Ligera: Manzana, Pera, Plátano
    Media: Tostada, Cereales, Yogur
    Pesada: Huevo, Bacon, Salchichas
    
    Args:
        tipo_comida (int): tipo de comida

    Return:
        None
    """
    #Validar entrada
    if ((tipo_comida>=1) and (tipo_comida<=3)):
        if tipo_comida == 1:  # Desayuno
            print("Ligera: Manzana, Pera, Plátano")
            print("Media: Tostada, Cereales, Yogur")
            print("Pesada: Huevo, Bacon, Salchichas")
        elif tipo_comida == 2:  # Comida
            print("Ligera: Ensalada, Sopa, Pasta")
            print("Media: Pollo, Pescado, Arroz")
            print("Pesada: Carne, Patatas, Legumbres")
        else:#Cena
            print("Ligera: Sopa, Verduras, Pescado")
            print("Media: Pollo, Pescado, Arroz")
            print("Pesada: Carne, Patatas, Legumbres")
    else:
        print("Error, el valor que ingresaste no existe.")

def mostrar_ligera_media_pesada():
    print("Menú de opciones:\n1.Ligera\n2.Media\n3.Pesada")
    opcion = int(input("Elije una opción: "))
    return opcion

def mostrar_opcion_ligera_media_pesada(opcion_comida):
    """
    Esta función recibe un numero 1-3  e imprime si elegiste ligera, media o pesada.
    Si elegiste 1, imprime "Elegiste ligera"
    Si elegiste 2, imprime "Elegiste Media"
    Si elegiste 3, imprime "Elegiste Pesada"

    Args:
        opcion_comida (int): opcion de comida

    Return:
        None
    """
    #Validar entrada
    if ((opcion_comida >= 1) and (opcion_comida <=3)):
        if opcion_comida == 1:
            print("Elegiste Ligera...")
        elif opcion_comida == 2:
            print("Elegiste Media...")
        else:
            print("Elegiste Pesada...")
    else:
        print("Error, el valor que ingresaste no existe.")

def calcular_calorias(tipo_comida, opcion_comida):
    """
    Esta función recibe tipo de comida 1-3 y opcion de comida 1-3.
    Si el tipo de comida es 1 y opcion de comida es 1.

    Args:
        opcion_comida (int): opción de comida
        tipo_comida (int): tipo de comida

    Return:
        ligero_desayuno
    """
    #Validar entrada
    if ((tipo_comida>=1) and (tipo_comida<=3)):
        if tipo_comida == 1:  # Desayuno
            if opcion_comida == 1: #Desayuno ligero
                total_ligero = 0
                for ligero in ligero_desayuno:
                    total_ligero += ligero
                return total_ligero
            elif opcion_comida == 2:#Desayuno medio
                total_medio = 0
                for medio in medio_desayuno:
                    total_medio += medio
                return total_medio
            else:#Desayuno pesado
                total_pesado = 0
                for pesado in pesado_desayuno:
                    total_pesado += pesado
                return total_pesado
        elif tipo_comida == 2:  #Comida
            if opcion_comida == 1: #Comida ligera
                total_ligero = 0
                for ligero in ligero_comida:
                    total_ligero += ligero
                return total_ligero
            elif opcion_comida == 2:#Comida media
                total_medio = 0
                for medio in medio_comida:
                    total_medio += medio
                return total_medio
            else:#Comida pesado
                total_pesado = 0
                for pesado in pesado_comida:
                    total_pesado += pesado
                return total_pesado
            
        elif tipo_comida == 3:  #Cena
            if opcion_comida == 1: #Cena ligera
                total_ligero = 0
                for ligero in ligero_cena:
                    total_ligero += ligero
                return total_ligero
            elif opcion_comida == 2:#Cena media
                total_medio = 0
                for medio in medio_cena:
                    total_medio += medio
                return total_medio
            else:#Cena pesada
                total_pesado = 0
                for pesado in pesado_cena:
                    total_pesado += pesado
                return total_pesado
    else:
        print("Error, el valor que ingresaste no existe.")

if __name__ == '__main__':
    
    total_calorias = 0
    contador_comidas = 0

    #Bievenida
    while True:
        
        #Mostrar menu
        #Ejemplo: 1. Desayuno

        comida_principal = mostrar_menu_principal()
        print('\n')

        #Salir si el usuario elige 4 o un numero diferente de 1,2 o 3.
        if (comida_principal == 4):
                print("Elegiste salir")
                break
        while((comida_principal >= 4) or (comida_principal <1 )):
                print("Debes de elegir, desayuno, comida o cena!!!")
                comida_principal= mostrar_menu_principal()
       
        #Mostrar comida (Desayuno, Comida, Cena)
        # Ejemplo: Elegiste Desayuno...
        print("*" * 50)
        mostrar_comida(comida_principal)

        #Mostrar tipos de alimentos indicados por comida (Desayuno, Comida, Cena)
        #Ejemplo: Ligera: Manzana, Pera, Plátano
        mostrar_grupos_alimentos(comida_principal)
        print("*" * 50)

        #Mostrar opcion de acuerdo a comida (desayuno, comida, cena) y tipo (ligera, media, pesada)
        # Ejemplo: Elegiste Ligera... 
        # eleccion = mostrar_ligera_media_pesada()
        opcion_comida = mostrar_ligera_media_pesada()
        print("*" * 50)
        while((opcion_comida >= 4) or (opcion_comida < 1)):
            print("Debes de elegir, ligera, media o pesada!!!")
            opcion_comida = mostrar_ligera_media_pesada()
        
        #Mostrar opcion de la comida que elegiste
        mostrar_opcion_ligera_media_pesada(opcion_comida)
    
        #Mostrar total de comidas
        if (opcion_comida>=1 and opcion_comida<=3):
            contador_comidas += 1
            total_calorias += calcular_calorias(comida_principal, opcion_comida)
            #Calcular calorias de acuerdo a opcion de comida y tipo de comida
            #Ejemplo: Calorías totales: 180
        print(f"Has comido {contador_comidas} veces")
        
        #Mensajes preventivos de acuerdo a numero de comidas
        if contador_comidas < 3:
            print("Debes comer al menos 3 veces al día")
        elif contador_comidas == 3:
            print("Número de comidas recomendadas")
            #  Reducir calorías en 20%
            total_calorias *= 0.8
        else:
            # Aumentar calorías en 10%
            total_calorias *= 1.1
            print("Advertencia, número de comidas mayor a 3")

        print(f"Total de calorías: {total_calorias}")
        print("*" * 50)
        print('\n')
    #Mostrar si eleecion es saludable o excede las calorias recomendadas
    if  total_calorias > 0 and  total_calorias <= 1500:
        print("Tu elección es saludable")
    elif total_calorias > 1500:
        print("Elección excede calorías recomendadas")
