#aqui importamos todas las librerias necesarias
import datetime
#contact data
#almacenar datos: nombre, apellido, fecha nac, adress, comuna, mail, rut, cantidad de hijos por afiliado, fecha de nacimiemnto de hijos de afiliados,
#  edad de los hijos del afiliado y del afiliado 
def nombre_afiliado():
   ingrese_nombre = input("nombre del afiliado",)
   ingrese_apellido = input("nombre del apellido",)
   
   ingrese_direccion = input("direccion del afiliado",)
   ingrese_comuna = input("comuna del afiliado",)
   ingrese_mail = input("mail del afiliado",)
   ingrese_rut = input("rut del afiliado",)
   ingrese_numero_de_hijos = input("numero de hijos del afiliado",)
   array_data = [ingrese_nombre, ingrese_apellido,  ingrese_direccion, ingrese_comuna, ingrese_mail, ingrese_rut, ingrese_numero_de_hijos]
   #calculo de fecha
   fecha_nacimiento = '30-01-12'
   convert_fecha_nacimiento_date = datetime.datetime.strptime(fecha_nacimiento, '%d-%m-%y').date()
   #datetime.date(2012, 1, 30)
   ano_nacimiento = convert_fecha_nacimiento_date.year
   print(ano_nacimiento)
   return array_data


   #invocando funcion
nombre_afiliado()
  

 #queda pendiente remplazar variables para funcion de calculos  
 #


