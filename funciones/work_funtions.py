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
   fecha_nacimiento = input("ingrese fecha nacimiento afiliado 01-01-1900",)
   convert_fecha_nacimiento_date = datetime.datetime.strptime(fecha_nacimiento, '%d-%m-%Y').date()
   #datetime.date(2012, 1, 30)
   ano_nacimiento = convert_fecha_nacimiento_date.year
   edad_afiliado = 2023 - ano_nacimiento
   print("ano de nacimiento ingresado es: ",ano_nacimiento,"\n la edad del afiliado es:", edad_afiliado)
   return ano_nacimiento


   #invocando funcion
nombre_afiliado()
  




