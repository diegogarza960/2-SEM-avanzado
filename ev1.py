# 1.1
def obtener_vocales(texto: str) -> tuple:
    """
    Acepta un texto y retorna una tupla con cada vocal encontrada en el texto.

    texto: Cadena de texto de entrada.
    return: Tupla con las vocales encontradas en el texto.
    """
    vocales = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    return tuple([letra for letra in texto if letra in vocales])


# 1.2
def ordenar_valores(val1: float, val2: float, val3: float) -> tuple:
    """
    Acepta tres valores numéricos y retorna una tupla con los valores ordenados.

    val1: Primer valor numérico.
    val2: Segundo valor numérico.
    val3: Tercer valor numérico.
    return: Tupla con los valores ordenados de menor a mayor.
    """
    return tuple(sorted([val1, val2, val3]))


# 1.3
def calcular_interes(capitall: float, tasa_interess: float) -> float:
    """
    Acepta dos datos: monto del capital y tasa de interés expresada como porcentaje.
    Retorna el monto final incorporando el interés calculado.

    capital: Monto del capital inicial.
    tasa_interes: Tasa de interés expresada como porcentaje.
    return: Monto final después de aplicar el interés.
    """
    return capitall * (1 + tasa_interess / 100)


# 1.4.  ACEPTA TRES DATOS: CAPITAL, TASA Y PERIDOS. RETORNA EL MONTO FINAL CONSIDERANDO
# INTERES SIMPLE.


def calcular_interes_simple(capitale, tasa_interess, periodos):
    """
    Calcula el monto final considerando intereses simple.

    Args:
      capital (float): El monto inicial
      tasa_interes (float): La tasa de interés en porcentaje
      periodos (int): El número de periodos

    Returns:
      float: El monto final considerando intereses simple
    """
    interes = capitale * tasa_interess / 100 * periodos
    monto_finall = capitale + interes

    return monto_finall


# 1.5.  ACEPTA 4 DATOS: CAPITAL, TASA DE INTERES ANUAL, NUMERO DE PERIODOS DE CAPITALIZACION POR AÑO,
# NUMERO DE AÑOS A MANTENER LA INVERSION SIN RETIRAR NINGUN CAPITAL.


def calcular_inversion(ccapital, tassa_interes_anual, periodoo_capitalizado, años_inversion):
    """Calcula el monto final de una inversión después de un período determinado.

    Args:
        ccapital (float): El capital inicial de la inversión.
        tassa_interes_anual (float): La tasa de interés anual como porcentaje.
        periodoo_capitalizado (int): El período de capitalización (por ejemplo, 12 para mensual).
        años_inversion (int): El número de años de la inversión.

    Returns:
        float: El monto final de la inversión.
    """

    # Convertir la tasa de interés anual a decimal
    tassa_interes_anual = tassa_interes_anual / 100

    # Calcular el monto final de la inversión
    monto_final = ccapital * \
        (1 + tassa_interes_anual /
         periodoo_capitalizado) ** (periodoo_capitalizado * años_inversion)

    return monto_final


# 1.6.  ACEPTA 2 DATOS: PESO EN KILOGRAMOS Y ESTATURA EN METROS. RETORNA LA MEDIDA DEL
# INDICE CORPORAL, EL CUAL SE OBTIENE DIVIDIENDO EL PESO ENTRE EL CUADRADO DE LA ESTATURA.


def calcular_imc(peso, estatura):
    """
    Calcula el índice de masa corporal (IMC).

    Args:
        peso (float): El peso en kilogramos.
        estatura (float): La estatura en metros.

    Returns:
        float: El IMC calculado.
    """
    return peso / (estatura ** 2)


def main():
    while True:
        print("________Menú________")
        print("1. Obtener vocales")
        print("2. Ordenar valores")
        print("3. Calcular interés")
        print("4. Calcular interés simple")
        print("5. Calcular inversión")
        print("6. Calcular IMC")
        print("7. Salir")
        opc = int(input("ingresa una opcion 1/7 :"))
        if opc >= 8 or opc <= 0:
            print("Opción inválida. Por favor, inténtelo de nuevo.")
        elif opc == 1:
            texto = input("ingresa texto :")
            vocales_encontradas = obtener_vocales(texto)
            print("Vocales encontradas:", vocales_encontradas)

        elif opc == 2:
            val1 = float(input("ingresa valor 1 :"))
            val2 = float(input("ingresa valor 2 :"))
            val3 = float(input("ingresa valor 3 :"))
            valores_ya_ordenados = ordenar_valores(val1, val2, val3)
            print("Valores ordenados:", valores_ya_ordenados)

        elif opc == 3:
            capitall = float(input("ingresa el capital :"))
            tasa_interes = float(input("ingresa la tasa :"))
            interes_calculado = calcular_interes(capitall, tasa_interes)
            print("interes calculado :", interes_calculado)

        elif opc == 4:
            capitale = float(input("ingresa el capital :"))
            tasa_interess = float(input("ingresa la tasa de interes :"))
            periodos = float(input("ingresa los periodos :"))
            monto_final = calcular_interes_simple(
                capitale, tasa_interess, periodos)
            print("interes simple calculado : ", monto_final)

        elif opc == 5:
            ccapital = float(input("ingresa el capital :"))
            tassa_interes_anual = float(
                input("ingresa la tasa de interes anual :"))
            periodoo_capitalizado = float(input("ingresa el periodo :"))
            años_inversion = float(input("ingresa los años a inversion :"))
            resultado = calcular_inversion(
                ccapital, tassa_interes_anual, periodoo_capitalizado, años_inversion)
            print("monto fin de la inversion :", resultado)

        elif opc == 6:
            peso = float(input("ingrese el peso :"))
            estatura = float(input("ingrese la estatura :"))
            imc = calcular_imc(peso, estatura)
            print("tu imc es : ", imc)

        elif opc == 7:
            confirmacion = input("¿seguro que quieres salir ? (s/n): ")
            if confirmacion.lower() == "s":
                print("bye ")
                return
            else:
                print("Volviendo al menú...")


main()
