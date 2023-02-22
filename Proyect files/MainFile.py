import datetime
import pandas as pd
import matplotlib.pyplot as plt

# 1. Obtenga la fecha en la que se ejecuta el script
# Estas tres líneas muestran la fecha actual del sistema
now = datetime.datetime.now()
print("Current date and time ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

"""
Para ambos archivos:
Cree un DataFrame para cada escuela, con el formato de nombre “nombrecolegio_curso”
que reúna los datos de las columnas: school, sex, age, address, Pstatus, guardian,
traveltime, studytime, failures, paid, internet, health, absences, G1,G2,G3
"""

# Importar los dos csv
df_mat = pd.read_csv("student-mat.csv", sep=';')
df_por = pd.read_csv("student-por.csv", sep=';')

"""Verifique que no haya data valor nulo"""
# Eliminar valores NaN en caso de haber
if df_mat.isnull().values.any():
    df_mat.dropna

if df_por.isnull().values.any():
    df_por.dropna

# Verifico antes de dividir los dataframes
# Para no tener que repetir el proceso 4 veces

# Obtener los datos de cada escuela del dataframe df_mat
gp_mat = df_mat[df_mat['school'] == 'GP']
ms_mat = df_mat[df_mat['school'] == 'MS']

# Obtener los datos de cada escuela del dataframe df_por
gp_por = df_por[df_por['school'] == 'GP']
ms_por = df_por[df_por['school'] == 'MS']

""" Para cada escuela muestre un gráfico circular(pastel)
donde se evidencie el porcentaje de estudiantes hombres y mujeres de cada curso"""

# Porcentaje de hombres y mujeres del curso matematicas en GP
fig, ax = plt.subplots()
gp_mat_sex_graph = gp_mat.sex.value_counts().plot \
    (kind='pie', labels=['Hombres', 'Mujeres'], title="Porcentaje de hombres y mujeres del curso matematicas en GP")
gp_mat_sex_graph.plot  # Muestra la grafica

# Porcentaje de hombres y mujeres del curso matematicas en MS
fig, ax = plt.subplots()
ms_mat_sex_graph = ms_mat.sex.value_counts().plot \
    (kind='pie', labels=['Hombres', 'Mujeres'], title="Porcentaje de hombres y mujeres del curso matematicas en MS")
ms_mat_sex_graph.plot  # Muestra la grafica

# Porcentaje de hombres y mujeres del curso portuges en GP
fig, ax = plt.subplots()
gp_por_sex_graph = gp_por.sex.value_counts().plot \
    (kind='pie', labels=['Hombres', 'Mujeres'], title="Porcentaje de hombres y mujeres del curso portuges en GP")
gp_por_sex_graph.plot  # Muestra la grafica

# Porcentaje de hombres y mujeres del curso portuges en MS
fig, ax = plt.subplots()
ms_por_sex_graph = ms_por.sex.value_counts().plot \
    (kind='pie', labels=['Hombres', 'Mujeres'], title="Porcentaje de hombres y mujeres del curso portuges en MS")
ms_por_sex_graph.plot  # Muestra la grafica

"""Para cada escuela muestre un gráfico de barras
donde se muestre la cantidad de estudiantes que tienen la misma edad"""

# Grafica de edades del curso matematicas en GP
fig, ax = plt.subplots()
gp_mat_age = gp_mat.groupby("age").size().plot(kind="bar", title="Grafica de edades del curso matematicas en GP")
plt.show()

# Grafica de edades del curso matematicas en MS
fig, ax = plt.subplots()
ms_mat_age = ms_mat.groupby("age").size().plot(kind="bar", title="Grafica de edades del curso matematicas en MS")
plt.show()

# Grafica de edades del curso portugues en GP
fig, ax = plt.subplots()
gp_por_age = gp_por.groupby("age").size().plot(kind="bar", title="Grafica de edades del curso portugues en GP")
plt.show()

# Grafica de edades del curso portuges en MS
fig, ax = plt.subplots()
ms_por_age = ms_por.groupby("age").size().plot(kind="bar", title="Grafica de edades del curso portuges en MS")
plt.show()

""" Muestre el promedio de las edades de cada curso de cada escuela """

# Almacenar en ms/gp_mat_promage el promedio de edades del curso de matematicas de la escuela MS y GP respectivamente
ms_mat_promage = ms_mat['age'].mean()
gp_mat_promage = gp_mat['age'].mean()

# Almacenar en ms/gp_por_promage el promedio de edades del curso de matematicas de la escuela MS y GP
ms_por_promage = ms_por['age'].mean()
gp_por_promage = gp_por['age'].mean()

# Imprimir el promedio de las edades de cada curso de cada escuela

print(f"""
***************************************************************
El promedio de edades del curso mat de la escuela MS fue: {round(ms_mat_promage, 2)}
***************************************************************
El promedio de edades del curso mat de la escuela GP fue: {round(gp_mat_promage, 2)}
***************************************************************
El promedio de edades del curso por de la escuela MS fue: {round(ms_por_promage, 2)}
***************************************************************
El promedio de edades del curso por de la escuela GP fue: {round(ms_por_promage, 2)}
***************************************************************
""")

""" Muestre el promedio de las notas G1, G2, G3 de cada curso de cada escuela """

# Almacenar en ms_mat_promn el promedio de notas del curso mat de la escuela MS
ms_mat_promg1 = ms_mat['G1'].mean()
ms_mat_promg2 = ms_mat['G2'].mean()
ms_mat_promg3 = ms_mat['G3'].mean()

# Almacenar en gp_mat_promn el promedio de notas del curso mat de la escuela GP
gp_mat_promg1 = gp_mat['G1'].mean()
gp_mat_promg2 = gp_mat['G2'].mean()
gp_mat_promg3 = gp_mat['G3'].mean()

# Almacenar en ms_por_promn el promedio de notas del curso portugues de la escuela MS
ms_por_promg1 = ms_por['G1'].mean()
ms_por_promg2 = ms_por['G2'].mean()
ms_por_promg3 = ms_por['G3'].mean()

# Almacenar en gp_mat_promn el promedio de notas del curso portuges de la escuela GP
gp_por_promg1 = ms_por['G1'].mean()
gp_por_promg2 = gp_por['G2'].mean()
gp_por_promg3 = gp_por['G3'].mean()

# Imprimir los promedios
print(f"""
*********************************************************
El promedio de notas del curso mat de la escuela MS fue:
para G1: {ms_mat_promg1}
para G2: {ms_mat_promg2}
para G3: {ms_mat_promg3}
*********************************************************
El promedio de notas del curso mat de la escuela GP fue:
para G1: {ms_mat_promg1}
para G2: {ms_mat_promg2}
para G3: {ms_mat_promg3}
*********************************************************
El promedio de notas del curso por de la escuela MS fue:
para G1: {ms_por_promg1}
para G2: {ms_por_promg2}
para G3: {ms_por_promg3}
*********************************************************
El promedio de notas del curso por de la escuela GP fue:
para G1: {ms_por_promg1}
para G2: {ms_por_promg2}
para G3: {ms_por_promg3}

""")

"""Grafique el promedio de las notas en un gráfico de barras horizontal"""

# Ciclo for para imprimir las graficas de las notas del curso de matematicas,
# de la escuela MS, del periodo G1, G2 y G3
aux_mat_ms = ("G1", "G2", "G3")
for n in aux_mat_ms:
    fig, ax = plt.subplots()
    ms_mat.groupby(n).size().plot(kind="barh", title=f"Notas del curso de matematicas, escuela MS, periodo {n} ")
    plt.show()

# Ciclo for para imprimir las graficas de las notas del curso de matematicas,
# de la escuela GP, del periodo G1, G2 y G3
aux_mat_gp = ("G1", "G2", "G3")
for n in aux_mat_gp:
    fig, ax = plt.subplots()
    ms_mat.groupby(n).size().plot(kind="barh", title=f"Notas del curso de matematicas, escuela GP, periodo {n} ")
    plt.show()

# Ciclo for para imprimir las graficas de las notas del curso de portugues,
# de la escuela MS, del periodo G1, G2 y G3
aux_por_ms = ("G1", "G2", "G3")
for n in aux_por_ms:
    fig, ax = plt.subplots()
    ms_mat.groupby(n).size().plot(kind="barh", title=f"Notas del curso de portuges, escuela MS, periodo {n} ")
    plt.show()

# Ciclo for para imprimir las graficas de las notas del curso de portugues,
# de la escuela GP, del periodo G1, G2 y G3
aux_por_gp = ("G1", "G2", "G3")
for n in aux_por_gp:
    fig, ax = plt.subplots()
    ms_mat.groupby(n).size().plot(kind="barh", title=f"Notas del curso de portuges, escuela GP, periodo {n} ")
    plt.show()

"""
Halle el valor máximo de las ausencias y considere dicho valor como el total de clases del curso,
de manera que pueda sacar un porcentaje de asistencia para cada estudiante"""

# Encontrar el máximo de ausencias -> Max ausencias = total de clases

tot_clases_mat_ms = ms_mat['absences'].max()  # total de clases de mat-ms
tot_clases_mat_gp = gp_mat['absences'].max()  # total de clases de mat-gp

tot_clases_por_ms = ms_por['absences'].max()  # total de clases de por-ms
tot_clases_por_gp = gp_por['absences'].max()  # total de clases de por-gp

# guardar las asistencias en un vector para mat-ms
asistencia_mat_ms = []

for i in ms_mat['absences']:
    asistencia_mat_ms.append(i)

# guardar las asistencias en un vector para mat-gp
asistencia_mat_gp = []
for i in gp_mat['absences']:
    asistencia_mat_gp.append(i)

# guardar las asistencias en un vector para por-ms
asistencia_por_ms = []
for i in ms_por['absences']:
    asistencia_por_ms.append(i)

# guardar las asistencias en un vector para por-gp
asistencia_por_gp = []
for i in gp_por['absences']:
    asistencia_por_gp.append(i)

# Encontrar el porcentaje de asistencias

# para mat-ms
porcentaje_mat_ms = []
for i in range(0, len(ms_mat.index)):
    absences_mat_ms = round((-(asistencia_mat_ms[i] / tot_clases_mat_ms) * 100 + 100), 2)
    porcentaje_mat_ms.append(absences_mat_ms)

# para mat-gp
porcentaje_mat_gp = []
for i in range(0, len(gp_mat.index)):
    absences_mat_gp = round((-(asistencia_mat_gp[i] / tot_clases_mat_gp) * 100 + 100), 2)
    porcentaje_mat_gp.append(absences_mat_gp)

# para por-ms
porcentaje_por_ms = []
for i in range(0, len(ms_por.index)):
    absences_por_ms = round((-(asistencia_por_ms[i] / tot_clases_por_ms) * 100 + 100), 2)
    porcentaje_por_ms.append(absences_por_ms)

# para por-gp
porcentaje_por_gp = []
for i in range(0, len(gp_por.index)):
    absences_por_gp = round((-(asistencia_por_gp[i] / tot_clases_por_gp) * 100 + 100), 2)
    porcentaje_por_gp.append(absences_por_gp)

# Los porcentajes de asistencias de cada estudiante estan guardados en las variables
# porcentaje_por_gp, porcentaje_por_ms
# porcentaje_mat_gp, porcentaje_mat_ms


"""Obtener promedio de notas de cada estudiante"""

# almacenar notas para mat_ms.
mat_ms_nota1 = []
mat_ms_nota2 = []
mat_ms_nota3 = []

for i in ms_mat['G1']:
    mat_ms_nota1.append(i)
    for o in ms_mat['G2']:
        mat_ms_nota2.append(o)
        for u in ms_mat['G3']:
            mat_ms_nota3.append(u)

# almacenar notas para mat_gp.
mat_gp_nota1 = []
mat_gp_nota2 = []
mat_gp_nota3 = []

for i in gp_mat['G1']:
    mat_gp_nota1.append(i)
    for o in gp_mat['G2']:
        mat_gp_nota2.append(o)
        for u in gp_mat['G3']:
            mat_gp_nota3.append(u)

# almacenar notas para por_ms.
por_ms_nota1 = []
por_ms_nota2 = []
por_ms_nota3 = []

for i in ms_por['G1']:
    por_ms_nota1.append(i)
    for o in ms_por['G2']:
        por_ms_nota2.append(o)
        for u in ms_por['G3']:
            por_ms_nota3.append(u)

# almacenar notas para por_gp.
por_gp_nota1 = []
por_gp_nota2 = []
por_gp_nota3 = []

for i in gp_por['G1']:
    por_gp_nota1.append(i)
    for o in gp_por['G2']:
        por_gp_nota2.append(o)
        for u in gp_por['G3']:
            por_gp_nota3.append(u)

# obtener promedio de notas para mat_ms
mat_ms_notafinal = []
for i in range(0, len(ms_mat.index)):
    mat_ms_nota = round((mat_ms_nota1[i] + mat_ms_nota2[i] + mat_ms_nota3[i]) / 3, 2)
    mat_ms_notafinal.append(mat_ms_nota)

# obtener promedio de notas para mat_gp
mat_gp_notafinal = []
for i in range(0, len(gp_mat.index)):
    mat_gp_nota = round((mat_gp_nota1[i] + mat_gp_nota2[i] + mat_gp_nota3[i]) / 3, 2)
    mat_gp_notafinal.append(mat_gp_nota)

# obtener promedio de notas para por_ms
por_ms_notafinal = []
for i in range(0, len(ms_por.index)):
    por_ms_nota = round((por_ms_nota1[i] + por_ms_nota2[i] + por_ms_nota3[i]) / 3, 2)
    por_ms_notafinal.append(por_ms_nota)

# obtener promedio de notas para mat_gp
por_gp_notafinal = []
for i in range(0, len(gp_mat.index)):
    por_gp_nota = round((por_gp_nota1[i] + por_gp_nota2[i] + por_gp_nota3[i]) / 3, 2)
    por_gp_notafinal.append(por_gp_nota)

"""
Cree una nueva columna llamada “extra”
Cree una nueva columna llamada “approved”
"""


# Almacenar en nuevas listas, los alumnos aprobados, reprobados y los extras


# Funcion para encontrar los alumnos aprobados y sus extras
def aprobados(porcentaje, notafinal):
    extra = []
    approved = []
    for i in range(0, len(notafinal)):
        a = porcentaje[i]
        n = notafinal[i]
        if (a < 80):
            approved.append(0)
            extra.append(None)
        elif (a > 80 and n < 10):
            approved.append(0)
            extra.append(None)
        elif (a > 80 and n >= 10 and n <= 15):
            approved.append(1)
            extra.append(1)
        elif (a > 80 and n > 15):
            approved.append(1)
            extra.append(0)
    return extra, approved


# almacenar los extras y los alumnos aprobados en las listas
# utilizando la funcion creada

# para mat_ms
mat_ms_extra, mat_ms_approved = aprobados(porcentaje_mat_ms, mat_ms_notafinal)

# para mat_gp
mat_gp_extra, mat_gp_approved = aprobados(porcentaje_mat_gp, mat_gp_notafinal)

# para por_ms
por_ms_extra, por_ms_approved = aprobados(porcentaje_por_ms, por_ms_notafinal)

# para por_gp
por_gp_extra, por_gp_approved = aprobados(porcentaje_por_gp, por_gp_notafinal)

"""Añadir las columnas al DataFrame"""
"""Para el curso de matematicas"""

aprobados_matematicas_gp = pd.DataFrame(mat_gp_approved)
extras_matematicas_gp = pd.DataFrame(mat_gp_extra)

# para ms_mat, insertar approved
ms_mat.insert(33, 'approved', mat_ms_approved, allow_duplicates=False)

# para ms_mat, insertar extras
ms_mat.insert(34, 'extra', mat_ms_extra, allow_duplicates=False)

# para gp_mat, insertar approved
gp_mat.insert(33, 'approved', aprobados_matematicas_gp, allow_duplicates=False)

# para ms_mat, insertar extras
gp_mat.insert(34, 'extra', extras_matematicas_gp, allow_duplicates=False)


df_mat_final = pd.merge(ms_mat, gp_mat,  how="outer")
#print(d3)

#Grafica pastel del porcentaje de aprobados y reprobados del curso de matematicas
fig, ax = plt.subplots()
colores = ["#EE6055", "#60D394"]
mat_approved_graph = df_mat_final.approved.value_counts().plot \
    (kind='pie',
     labels=['Aprobados', 'Reprobados'],
     title="Grafica de aprobados y reprobados del curso de matematicas",
     autopct="%0.1f %%",
     colors=colores)

mat_approved_graph.plot  # Muestra la grafica

"""Añadir las columnas al DataFrame"""
"""Para el curso de Portuges"""

aprobados_portugues_gp = pd.DataFrame(por_gp_approved)
extras_portugues_gp = pd.DataFrame(por_gp_extra)

# para ms_mat, insertar approved
ms_por.insert(33, 'approved', por_ms_approved, allow_duplicates=False)

# para ms_mat, insertar extras
ms_por.insert(34, 'extra', por_ms_extra, allow_duplicates=False)

# para gp_mat, insertar approved
gp_por.insert(33, 'approved', aprobados_portugues_gp, allow_duplicates=False)

# para ms_mat, insertar extras
gp_por.insert(34, 'extra', extras_portugues_gp, allow_duplicates=False)


df_por_final = pd.merge(ms_por, gp_por,  how="outer")
#print(d3)

#Grafica pastel del porcentaje de aprobados y reprobados del curso de Portugues
fig, ax = plt.subplots()
colores = ["#EE6055", "#60D394"]
por_approved_graph = df_por_final.approved.value_counts().plot \
    (kind='pie',
     labels=['Aprobados', 'Reprobados'],
     title="Grafica de aprobados y reprobados del curso de Portugues",
     autopct="%0.1f %%",
     colors=colores)

por_approved_graph.plot  # Muestra la grafica


"""Imprimir porcentaje de asistencia para cada alumno de cada curso de cada escuela"""

# Porcentaje de asistencia para los alumnos MS del curso de mat
estudiante = 1
print("""     Porcentajes de asistencias para los alumnos del colegio MS, del curso de Matematicas""")
for i in range(len(porcentaje_mat_ms)):
    print(f"""*************************************************************************************
              Estudiante {estudiante}, su porcentaje de asistencia fue: {porcentaje_mat_ms[i]}
              ************************************************************************************
    """)
    estudiante += 1

# Porcentaje de asistencia para los alumnos GP del curso de mat
estudiante = 1
print("""     Porcentajes de asistencias para los alumnos del colegio GP, del curso de Matematicas""")
for i in range (len(porcentaje_mat_gp)):
    print(f"""*************************************************************************************
              Estudiante {estudiante}, su porcentaje de asistencia fue: {porcentaje_mat_gp[i]}
              ************************************************************************************
    """)
    estudiante += 1

# Porcentaje de asistencia para los alumnos MS del curso de Portugues
estudiante = 1
print("""     Porcentajes de asistencias para los alumnos del colegio MS, del curso de Portugues""")
for i in range (len(porcentaje_por_ms)):
    print(f"""************************************************************************************
              Estudiante {estudiante}, su porcentaje de asistencia fue: {porcentaje_por_ms[i]}
              ************************************************************************************
    """)
    estudiante += 1

# Porcentaje de asistencia para los alumnos GP del curso de Portugues
estudiante = 1
print("""     Porcentajes de asistencias para los alumnos del colegio MS, del curso de Portugues""")
for i in range (len(porcentaje_por_gp)):
    print(f"""*************************************************************************************
              Estudiante {estudiante}, su porcentaje de asistencia fue: {porcentaje_por_gp[i]}
              ***************************************************************
    """)
    estudiante += 1

"""Generar un archivo en formato csv con nombre: “Resultado + Fecha en la que se ejecuta el script”,
 este archivo debe quedar en la carpeta donde se encuentren los datos originales y el archivo de Python"""

df_mat_final.to_csv(f'Resultado_Matematicas {now.strftime("%Y-%m-%d")}', sep=";")
df_por_final.to_csv(f'Resultado_Portuges {now.strftime("%Y-%m-%d")}', sep=";")

plt.show(block=True)  # Comando para poder mostrar las graficas, sin esto, no funcionan
