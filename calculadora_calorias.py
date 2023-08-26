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


total_calorias = 0
contador_comidas = 0

while True:
    print("Menú principal:\n1.Desayuno\n2.Comida\n3.Cena\n4.Salir")
    eleccion = int(input("Elije una opción: "))

    if eleccion == 4:
        break

    contador_comidas += 1

    if eleccion == 1:
        tipo_comida = 'desayuno'
    elif eleccion == 2:
        tipo_comida = 'comida'
    elif eleccion == 3:
        tipo_comida = 'cena'

    print("Menú de opciones:\n1.Ligera\n2.Media\n3.Pesada")
    opcion_comida = int(input("Elije una opción: "))

    if tipo_comida == 'desayuno':
        if opcion_comida == 1:
            total_calorias += ligero_desayuno
        elif opcion_comida == 2:
            total_calorias += medio_desayuno
        elif opcion_comida == 3:
            total_calorias += pesado_desayuno
    elif tipo_comida == 'comida':
        if opcion_comida == 1:
            total_calorias += ligero_comida
        elif opcion_comida == 2:
            total_calorias += medio_comida
        elif opcion_comida == 3:
            total_calorias += pesado_comida
    elif tipo_comida == 'cena':
        if opcion_comida == 1:
            total_calorias += ligero_cena
        elif opcion_comida == 2:
            total_calorias += medio_cena
        elif opcion_comida == 3:
            total_calorias += pesado_cena

    print(f"Has comido {contador_comidas} veces")

    if contador_comidas < 3:
        print("Debes comer al menos 3 veces al día")
    elif contador_comidas == 3:
        print("Número de comidas recomendadas")
        total_calorias *= 0.8
    else:
        total_calorias *= 1.1
        print("Advertencia, número de comidas mayor a 3")

    print(f"Total de calorías: {total_calorias}")

if total_calorias <= 1500:
    print("Tu elección es saludable")
else:
    print("Elección excede calorías recomendadas")
