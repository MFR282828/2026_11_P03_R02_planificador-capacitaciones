# ==============================================================================
# SAGA DE REPOSITORIOS PYTHON 2026
# Repositorio: 2026_10_P03_R02_planificador-capacitaciones
# Principio 3: Funciones, parámetros y alcance de variables (Nivel: Consolidación)
# ==============================================================================


# --- FUNCIONES DE VALIDACIÓN Y ENTRADA ---

def solicitar_texto(mensaje):
    """Solicita una cadena de texto no vacía."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("  [Error] El texto no puede estar vacío. Intente de nuevo.")


def solicitar_float_positivo(mensaje):
    """Solicita un número decimal estrictamente mayor que cero."""
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = float(entrada)
            if valor > 0:
                return valor
            print("  [Error] Debe ingresar un importe numérico mayor que cero.")
        except ValueError:
            print("  [Error] Entrada no válida. Ingrese un valor numérico.")


def solicitar_entero_positivo(mensaje):
    """Solicita un número entero estrictamente mayor que cero."""
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if valor > 0:
                return valor
            print("  [Error] Debe ingresar un número entero mayor que cero.")
        except ValueError:
            print("  [Error] Entrada no válida. Ingrese un número entero.")


def solicitar_descuento(mensaje, minimo=0.0, maximo=100.0):
    """Solicita un porcentaje de descuento dentro de un rango permitido (por defecto 0 a 100)."""
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = float(entrada)
            if minimo <= valor <= maximo:
                return valor
            print(f"  [Error] El descuento debe estar entre {minimo:.0f} % y {maximo:.0f} %.")
        except ValueError:
            print("  [Error] Entrada no válida. Ingrese un porcentaje numérico.")


# --- FUNCIONES PURAS DE CÁLCULO Y EVALUACIÓN ---

def calcular_coste_bruto(coste_unitario, participantes):
    """Calcula el coste bruto multiplicando el coste por participante por la cantidad."""
    coste_bruto = coste_unitario * participantes  # Variable local
    return coste_bruto


def calcular_descuento(coste_bruto, porcentaje_descuento=0.0):
    """Calcula el importe del descuento; si no se especifica porcentaje, aplica 0.0 %."""
    importe_descuento = coste_bruto * (porcentaje_descuento / 100.0)  # Variable local
    return importe_descuento


def calcular_coste_final(coste_bruto, importe_descuento=0.0):
    """Calcula el coste neto final restando el descuento al coste bruto."""
    coste_final = coste_bruto - importe_descuento  # Variable local
    return coste_final


def calcular_coste_por_participante(coste_final, participantes):
    """Calcula el coste final individual por cada participante."""
    if participantes <= 0:
        return 0.0
    coste_individual = coste_final / participantes  # Variable local
    return coste_individual


def evaluar_presupuesto(coste_final, presupuesto):
    """
    Evalúa el coste final frente al presupuesto disponible.
    Retorna una tupla (estado, diferencia), donde diferencia positiva es saldo
    y diferencia negativa representa exceso presupuestario.
    """
    diferencia = presupuesto - coste_final  # Variable local

    if coste_final < presupuesto:
        estado = "Dentro del presupuesto"
    elif coste_final == presupuesto:
        estado = "Presupuesto utilizado al 100 %"
    else:
        estado = "Exceso presupuestario"

    return estado, diferencia


# --- FUNCIÓN DE PRESENTACIÓN Y COORDINACIÓN ---

def mostrar_resumen(
    nombre,
    coste_unitario,
    participantes,
    porcentaje_descuento,
    presupuesto,
    coste_bruto,
    importe_descuento,
    coste_final,
    coste_por_participante,
    estado,
    diferencia,
    moneda="S/"
):
    """Muestra el resumen completo de la planificación con formato tabular."""
    print("\n====================================================")
    print("       RESUMEN DE PLANIFICACIÓN DE CAPACITACIÓN     ")
    print("====================================================")
    print(f"Capacitación:                 {nombre}")
    print(f"Coste por participante:       {moneda} {coste_unitario:.2f}")
    print(f"Número de participantes:      {participantes}")
    print(f"Descuento aplicado:           {porcentaje_descuento:.2f} %")
    print(f"Presupuesto disponible:       {moneda} {presupuesto:.2f}")
    print("----------------------------------------------------")
    print(f"Coste bruto:                  {moneda} {coste_bruto:.2f}")
    print(f"Importe del descuento:       -{moneda} {importe_descuento:.2f}")
    print(f"Coste final:                  {moneda} {coste_final:.2f}")
    print(f"Coste final por participante: {moneda} {coste_por_participante:.2f}")
    print("----------------------------------------------------")

    if diferencia >= 0:
        print(f"Saldo presupuestario:         {moneda} {diferencia:.2f}")
    else:
        print(f"Exceso presupuestario:        {moneda} {abs(diferencia):.2f}")

    print(f"Estado:                       {estado}")
    print("====================================================")


def main():
    """Función principal que coordina la captura, el cálculo y el resumen."""
    print("====================================================")
    print("      PLANIFICADOR DE CAPACITACIONES (P03_R02)      ")
    print("====================================================")

    # 1. Entrada de datos validados (uso de argumentos posicionales y por nombre)
    nombre_capacitacion = solicitar_texto("Ingrese el nombre de la capacitación: ")
    coste_unitario = solicitar_float_positivo("Ingrese el coste por participante (S/): ")
    participantes = solicitar_entero_positivo("Ingrese el número de participantes: ")
    porcentaje_descuento = solicitar_descuento(
        "Ingrese el porcentaje de descuento (0-100 %): ",
        minimo=0.0,
        maximo=100.0
    )
    presupuesto = solicitar_float_positivo("Ingrese el presupuesto disponible (S/): ")

    # 2. Composición de funciones (las salidas alimentan las entradas siguientes)
    # Llamada con argumentos posicionales
    coste_bruto = calcular_coste_bruto(coste_unitario, participantes)

    # Llamada con argumentos por nombre (keyword arguments)
    importe_descuento = calcular_descuento(
        coste_bruto=coste_bruto,
        porcentaje_descuento=porcentaje_descuento
    )

    coste_final = calcular_coste_final(
        coste_bruto=coste_bruto,
        importe_descuento=importe_descuento
    )

    # Llamada con argumentos posicionales
    coste_por_participante = calcular_coste_por_participante(coste_final, participantes)

    # Llamada con argumentos por nombre
    estado_presupuesto, diferencia_presupuesto = evaluar_presupuesto(
        coste_final=coste_final,
        presupuesto=presupuesto
    )

    # 3. Presentación de resultados (aprovecha el parámetro predeterminado moneda="S/")
    mostrar_resumen(
        nombre=nombre_capacitacion,
        coste_unitario=coste_unitario,
        participantes=participantes,
        porcentaje_descuento=porcentaje_descuento,
        presupuesto=presupuesto,
        coste_bruto=coste_bruto,
        importe_descuento=importe_descuento,
        coste_final=coste_final,
        coste_por_participante=coste_por_participante,
        estado=estado_presupuesto,
        diferencia=diferencia_presupuesto
    )


if __name__ == "__main__":
    main()