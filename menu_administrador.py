from funcionesGlobales import *

def usuario_o_admin():
    print("""¡BIENVENIDO, ¿COMO DESEAS INGRESAR?
          
**************************************
          
1). Administrador
2). Usuario
0). Salir

**************************************
""")
    opcion = listaOpciones("Ingrese la opcion","Numero no valido, ingrese de nuevo",2)
    return opcion


#MENÚ DE ADMINISTRADOR
def menu_administrador():
    datosLibros = leerJson("libros")
    datosUsuarios = leerJson("usuarios")
    while True:
        print("""\n¡HOLA DE NUEVO ADMINISTRADOR!,¿QUE TE GUSTARIA HACER HOY?
**************************************
1 - Añadir libro
2 - Modificar libro
3 - Eliminar Libro
4 - Mostrar Libros
5 - Eliminar usuarios
6 - Modificar usuarios
0 - Salir""")

        opc= listaOpciones("Ingrese una opcion","Error, valor incorrecto, intentelo de nuevo",6)

        #AGREGAR UN LIBRO AL JSON "LIBROS",  NO DEVUELVE NADA
        if opc== 1:
            libros=leerJson("libros")
            nombre_agregar_libro=input("Ingresa el nombre del libro que deseas agregar: ")

            ### COMPROBACION PARA VERIFICAR QUE EL NOMBRE INGRESADO NO SE ENCUENTRE YA EN EL JSON###
            while True:
                comprobacion_nombre_libro=False
                for libro in libros["libros"]:
                    if libro["nombre"]==nombre_agregar_libro:
                        print(f"Ya se encuentra un libro de nombre: {nombre_agregar_libro}, intenta con otro libro")
                        nombre_agregar_libro=input("Ingresa el nombre del libro que deseas agregar: ")
                        comprobacion_nombre_libro=True
                if comprobacion_nombre_libro==False:
                    break
            ##################################################################
            
            edad=input("Ingresa la edad minima del libro para ser comprado")
            
        elif opc== 2:
            libros = leerJson("libros")
            opcionLibro = input("Ingrese el nombre del libro que desea modificar: ")
            for libro in libros:
                if libro["nombre"] == opcionLibro:
                    datos = modificar_libro(datosLibros)
        elif opc==3:
            datosLibros = eliminar_libro(datosLibros)
            guardarJson("libros",datosLibros)
        elif opc == 4:
            print("JOSE")
        elif opc == 5:
            print()
        elif opc== 6:
            usuarios = list(leerJson("usuarios"))
            opcionUsuarios = listaOpciones("Ingrese el documento del usuario que desea modificar","Solo se permiten numeros, intentelo de nuevo")
            for usuario in usuarios:
                if usuario["documento"] == opcionUsuarios:
                    usuarioModificado = modificar_usuarios(usuario)
                    usuarios[usuarios.index(usuario)] = usuarioModificado
            print("Documento no encontrado")
        elif opc==0:
            print("")
            break
        
def modificar_usuarios(usuario):
    print("¿Que quieres modificar?")
    print("**************************************")
    print("1). Nombre")
    print("2). Edad")
    print("3). Correo Electronico")
    print("4). Libros comprados")
    print("5). Tipo cliente")
    print("0). salir")
    opcion = listaOpciones("Ingrese la opcion deseada","Opcion no valida, intentelo de nuevo",5)
    if opcion == 1:
        usuario["nombre"] = input("Ingrese el nuevo nombre que desea: ")
    elif opcion == 2:
        usuario["edad"] = listaOpciones("Ingrese la nueva edad","Edad no valida, intentelo de nuevo",99)
    elif opcion == 3:
        usuario["email"] = input("Ingrese el nuevo correo de recuperación: ")
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    return usuario

def contraseña_admin():
    contra="admin12345"
    ingresar=input("Ingresa la contraseña: ")
    if ingresar == contra:
        return True
    else:
        print("*Contraseña incorrecta\n")
        return False

#****************** CRUD LIBROS ******************#

# C-REATE 

def Crear_libro(datos):
    None

# R-EAD 

def mostrar_libros(datos):
    None

# U-PDATE

def modificar_libro(datos):
   datos=dict(datos)
   nombre= input("ingrese el nombre del libro que desea modificar:")
   for i in range(len(datos["libros"])):
        if datos["libros"][i]["nombre"] == nombre:

            while True:
                print("¿Que te gustaria cambiar?")
                print("******************************")
                print("1). Para modificar el Nombre: ")
                print("2). Para modificar la edad: ")
                print("3). Para modificar el Autor: ")
                print("4). Para modificar la ategoria: ")
                print("5). Para modificar la Dscripcion: ")
                print("6). Para modificar la Publicacion: ")
                print("7). Para modificar el Stock: ")
                
                print("0). Para salir ")
                
                opc= int(input(" Ingrese la opcion: "))

                if opc == 1:
                    datos["libros"][i]["nombre"]= input("Ingrese el nuevo Nombre: ")
                    print(" ¡NOMRBE GUARDADO CON EXITO!")
                    print("----------------------------------")

                elif opc == 2:
                    datos["libros"][i]["edad"]= input("Ingrese la nueva Edad: ")
                    print(" ¡EDAD GUARDADA CON EXITO!")
                    print("----------------------------------")


                elif opc == 3:
                    datos["libros"][i]["autor"]= input("Ingrese el nuevo Autor:")
                    print(" ¡AUTOR GUARDADO CON EXITO!")
                    print("----------------------------------")


                elif opc == 4:
                    datos["libros"][i]["categoria"]= input("Ingrese la nueva categoria: ")
                    print(" ¡CATEGORIA GUARDADA CON EXITO!")
                    print("----------------------------------")


                elif opc == 5:
                    datos["libros"][i]["descripcion"]= input("Ingrese la nueva descripcion: ")
                    print(" ¡DESCRIPCION GUARDADO CON EXITO!")
                    print("----------------------------------")


                elif opc == 6:
                    datos["libros"][i]["publicacion"]= input("Ingrese el nuevo año de publicacion: ")
                    print(" ¡AÑO DE PUBLICACION GUARDADO CON EXITO!")
                    print("----------------------------------")


                elif opc == 7:
                    datos["libros"][i]["stock"]= input("Ingrese el nuevo Stock:")
                    print(" ¡STOCK GUARDADO CON EXITO!")
                    print("----------------------------------")
                
                elif opc == 0:
                    break
            break
        return datos   

# D-ELETE libro
def eliminar_libro(datos):
    datos = dict(datos)
    ref =input("Ingrese el nombre de el libro a eliminar: ")
    for i in range(len(datos["libros"])):
        if datos["libros"][i]["nombre"] == ref:
            opc=int(input("Esta seguro que desea eliminar este libro ( 1 ) Si ( 2 ) No "))
            if opc ==1:
                datos["libros"].pop(i)
                print("plan eliminado!")
                return datos
            elif opc ==2:
                print("Cancelado con exito")
                return datos
           
    print("plan o paquete no encontrado")
    return datos