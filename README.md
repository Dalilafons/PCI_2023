Algoritmo:

Entradas:
Elección de comida (desayuno, comida, cena, o salir).
Elección de grupo de alimentos (ligero, medio, pesado, muy pesado) según la comida seleccionada.

Proceso:
Presentar un menú continuamente hasta que el usuario decida salir, el menú contiene opcion de desayuno, comida, cena y salir.
Utilizando la elección del usuario (desayuno, comida, cena) mostrar tipo de alimento (ligero, medio, pesado)
Despues de elegir opcion (ligero, medio, pesado) se mostraran los alimentos y calorias correspondientes a esa opcion.
Sumar las calorías de los alimentos de la opcion correspondiente (ligero, medio pesado) para el tipo de comida seleccionado (desayuno, comida, cena)
Contar el número de veces que el usuario ha comido.
Aplicar aumentos o disminuciones al total de calorías basándose en el número de comidas.
Determinar si la cantidad total de calorías es saludable o excesiva.

Salidas:
Mensaje que muestra elección del usuario (desayuno, comida, cena) mostrado tipo de alimento (ligero, medio, pesado) y las calorías de cada alimento.
Número total de veces que el usuario ha comido.
Total de calorías consumidas.
Mensaje que indica si la elección es saludable o excede las calorías recomendadas.
Archivo "calorias.txt" con el total de calorías.


Pseudocodigo:

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


INICIAR
    total_calorias = 0
    contador_comidas = 0

    Iniciar ciclo
        imprimir menú principal (1.desayuno, 2.comida, 3.cena, 4.salir)
        leer y guardar en eleccion

        si eleccion == 4 
            terminar ciclo

        contador_comidas = contador_comidas + 1

        si eleccion == 1
            tipo_comida = 'desayuno'
        si eleccion == 2
            tipo_comida = 'comida'
        si eleccion == 3
            tipo_comida = 'cena'

	si tipo_comida == 'desayuno'        
		imprimir menu (1.ligera, 2.media, 3.pesada)
		leer y guardar en opcion_comida
	
		si opcion_comida == 1
            		total_calorias = total_calorias + ligero_desayuno
		si opcion_comida == 2
            		total_calorias = total_calorias + medio_desayuno
		si opcion_comida == 3
            		total_calorias = total_calorias + pesado_desayuno
   	si tipo_comida == 'comida'        
		imprimir menu (1.ligera, 2.media, 3.pesada)
		leer y guardar en opcion_comida
	
		si opcion_comida == 1
            		total_calorias = total_calorias + ligero_comida
		si opcion_comida == 2
            		total_calorias = total_calorias + media_comida
		si opcion_comida == 3
            		total_calorias = total_calorias + pesada_comida
	si tipo_comida == 'cena'        
		imprimir menu (1.ligera, 2.media, 3.pesada)
		leer y guardar en opcion_comida
	
		si opcion_comida == 1
            		total_calorias = total_calorias + ligera_cena
		si opcion_comida == 2
            		total_calorias = total_calorias + media_cena
		si opcion_comida == 3
            		total_calorias = total_calorias + pesada_cena	
        
        imprimir contador_comidas

        si contador_comidas < 3 
            imprimir "Debes comer al menos 3 veces al día"
        si contador_comidas == 3 
            imprimir "Numero de comidas recomendadas"
	    total_calorias = total_calorias * 0.8 
        si contador_comidas > 3
            total_calorias = total_calorias * 1.1
            imprimir "Advertencia, numero de comidas mayor a 3"

        imprimir total_calorias

    fin ciclo

    si total_calorias <= 1500
        imprimir "Tu elección es saludable"
    si no
        imprimir "Elección excede calorías recomendadas"
FIN
