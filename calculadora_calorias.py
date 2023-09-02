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

ligero_desayuno = manzana + pera + platano
medio_desayuno = tostada + cereales + yogur
pesado_desayuno = huevo + bacon + salchichas

ligero_comida = ensalada + sopa + pasta
medio_comida = pollo + pescado + arroz
pesado_comida = carne + patatas + legumbres

ligero_cena = sopa + verduras + pescado
medio_cena = pollo + pescado + arroz
pesado_cena = carne + patatas + legumbres

def mostrar_menu_principal():
    print("Menú principal:\n1.Desayuno\n2.Comida\n3.Cena\n4.Salir")
    opcion = int(input("Elije una opción: "))
    return opcion

def mostrar_comida(tipo_comida):
    if tipo_comida == 1:
        print("Elegiste Desayuno...")
    elif tipo_comida == 2:
        print("Elegiste Comida...")
    elif tipo_comida == 3:
        print("Elegiste Cena...")

def mostrar_grupos_alimentos(tipo_comida):
    if tipo_comida == 1:  # Desayuno
        print("Ligera: Manzana, Pera, Plátano")
        print("Media: Tostada, Cereales, Yogur")
        print("Pesada: Huevo, Bacon, Salchichas")
    elif tipo_comida == 2:  # Comida
        print("Ligera: Ensalada, Sopa, Pasta")
        print("Media: Pollo, Pescado, Arroz")
        print("Pesada: Carne, Patatas, Legumbres")
    elif tipo_comida == 3:  # Cena
        print("Ligera: Sopa, Verduras, Pescado")
        print("Media: Pollo, Pescado, Arroz")
        print("Pesada: Carne, Patatas, Legumbres")

def mostrar_ligera_media_pesada():
    print("Menú de opciones:\n1.Ligera\n2.Media\n3.Pesada")
    opcion = int(input("Elije una opción: "))
    return opcion

def mostrar_opcion_ligera_media_pesada(opcion_comida):
    if opcion_comida == 1:
        print("Elegiste Ligera...")
    elif opcion_comida == 2:
        print("Elegiste Media...")
    elif opcion_comida == 3:
        print("Elegiste Pesada...")

def calcular_calorias(tipo_comida, opcion_comida):
    if tipo_comida == 1:  # Desayuno
        if opcion_comida == 1:
            return ligero_desayuno
        elif opcion_comida == 2:
            return medio_desayuno
        else:
            return pesado_desayuno
    elif tipo_comida == 2:  # Comida
        if opcion_comida == 1:
            return ligero_comida
        elif opcion_comida == 2:
            return medio_comida
        else:
            return pesado_comida
    elif tipo_comida == 3:  # Cena
        if opcion_comida == 1:
            return ligero_cena
        elif opcion_comida == 2:
            return medio_cena
        else:
            return pesado_cena

if __name__ == '__main__':
    
    total_calorias = 0
    contador_comidas = 0

    while True:
        #Mostrar menu
        #Ejemplo: 1. Desayuno
        comida_principal = mostrar_menu_principal()
        print('\n')
        
        #Salir si el usuario elige 4
        if comida_principal == 4:
            break
        
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
        opcion_comida = mostrar_ligera_media_pesada()
        print("*" * 50)
        mostrar_opcion_ligera_media_pesada(opcion_comida)
        
        #Calcular calorias de acuerdo a opcion de comida y tipo de comida
        #Ejemplo: Calorías totales: 180
        total_calorias += calcular_calorias(comida_principal, opcion_comida)
        
        #Mostrar total de comidas
        contador_comidas += 1
        
        print(f"Has comido {contador_comidas} veces")
        
        # Mensajes preventivos de acuerdo a numero de comidas
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
    if total_calorias <= 1500:
        print("Tu elección es saludable")
    else:
        print("Elección excede calorías recomendadas")
