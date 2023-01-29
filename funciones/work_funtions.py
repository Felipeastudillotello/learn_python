#contact data
#almacenar datos: nombre, apellido, fecha nac, adress, comuna, mail, rut, cantidad de hijos por afiliado, fecha de nacimiemnto de hijos de afiliados,
#  edad de los hijos del afiliado y del afiliado 
def nombre_afiliado():
   ingrese_nombre = input("nombre del afiliado",)
   ingrese_apellido = input("nombre del apellido",)
   ingrese_fech_nac = input("fecha de nacimiento del afiliado",)
   ingrese_direccion = input("direccion del afiliado",)
   ingrese_comuna = input("comuna del afiliado",)
   ingrese_mail = input("mail del afiliado",)
   ingrese_rut = input("rut del afiliado",)
   ingrese_numero_de_hijos = input("numero de hijos del afiliado",)
   ingrese_fech_nac_hijo = input("fecha de nacimiento de los hijo  del afiliado",) 
   edad_hijo = float(ingrese_fech_nac_hijo) - 28/1/2023
   edad_del_afiliado = float(ingrese_fech_nac) - 28/1/2023
   array_data = [ingrese_nombre, ingrese_apellido, ingrese_fech_nac, ingrese_direccion, ingrese_comuna, ingrese_mail, ingrese_rut, ingrese_numero_de_hijos, ingrese_fech_nac_hijo, edad_hijo, edad_del_afiliado ]
   return array_data
   #invocando funcion
nombre_afiliado()
 
 #queda pendiente avanzar el calculo a la fecha con date time 

