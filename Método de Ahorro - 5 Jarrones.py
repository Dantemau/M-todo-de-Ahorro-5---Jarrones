import os
from datetime import datetime

# Ingreso monetario
ingreso_monetario = float(input("Ingrese su ingreso monetario: "))

# Cálculo de presupuestos
gastos_generales = ingreso_monetario * 0.5
inversion = ingreso_monetario * 0.2
diezmo = ingreso_monetario * 0.1
beneficiencia = ingreso_monetario * 0.1
ahorro = ingreso_monetario * 0.1

# Creación de carpeta
carpeta_ahorro = "Método de ahorro - 5 Jarrones"
carpeta_jarrones = "5 Jarrones"
carpeta_ahorro2 = os.path.join(carpeta_ahorro, carpeta_jarrones)

if os.path.exists(carpeta_ahorro2):
    print(f"La carpeta {carpeta_ahorro2} ya existe.")
else:
    try:
        os.makedirs(carpeta_ahorro2)
    except Exception as e:
        print(f"Error al crear la carpeta: {e}")

# Creación de carpeta anual
carpeta_ano = os.path.join(carpeta_ahorro2, str(datetime.now().year))
if os.path.exists(carpeta_ano):
    print(f"La carpeta {carpeta_ano} ya existe.")
else:
    try:
        os.mkdir(carpeta_ano)
    except Exception as e:
        print(f"Error al crear la carpeta: {e}")

# Pregunta si quiere incluir fecha
incluir_fecha = input("¿Desea incluir la fecha en el archivo? (s/n): ").lower()

# Creación de archivo de texto
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

mes_actual = meses[datetime.now().month - 1]
dia_semana = dias[datetime.now().weekday()]
ano_actual = datetime.now().year

archivo_mes = os.path.join(carpeta_ano, f"Presupuesto del mes de {mes_actual}.txt")
if os.path.exists(archivo_mes):
    print(f"El archivo {archivo_mes} ya existe.")
    if incluir_fecha == 's':
        with open(archivo_mes, 'r') as f:
            contenido = f.readlines()
            if contenido and contenido[-1] != '\n':
                fecha = f"{dia_semana}, {datetime.now().day} de {mes_actual} de {ano_actual}\n"
            else:
                fecha = ""
    else:
        fecha = ""
else:
    if incluir_fecha == 's':
        fecha = f"{dia_semana}, {datetime.now().day} de {mes_actual} de {ano_actual}\n"
    else:
        fecha = ""
with open(archivo_mes, 'a') as f:
    f.write(fecha)
    f.write(f'Ingreso monetario: {ingreso_monetario}\n')
    f.write(f'(50%) Gastos Generales: {gastos_generales}\n')
    f.write(f'(20%) Inversión: {inversion}\n')
    f.write(f'(10%) Diezmo: {diezmo}\n')
    f.write(f'(10%) Beneficiencia: {beneficiencia}\n')
    f.write(f'(10%) Ahorro: {ahorro}\n')
    f.write("_______________________________\n")
