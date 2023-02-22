"""
Q. 03-03. Defina una lista llamada n_list con valores de [10,20,30]. Utilice la funcion map y lambda
para imprimir los resultados de duplicar, triplicar y cuadruplicar los objetos de la lista

ejemplo: mapped_numbers = list(map(lambda x:x*2+3, numbers))
"""

n_list = [10, 20, 30]

dup_list = list(map(lambda dup: dup*2, n_list))
trip_list = list(map(lambda trip: trip*3, n_list))
cuad_list = list(map(lambda cuad: cuad*4, n_list))

print (f"""
************************************************

        lista original:  {n_list}            
       lista duplicada:  {dup_list}     
      lista triplicada:  {trip_list}     
   lista cuadruplicada:  {cuad_list}    

************************************************* 
""")

