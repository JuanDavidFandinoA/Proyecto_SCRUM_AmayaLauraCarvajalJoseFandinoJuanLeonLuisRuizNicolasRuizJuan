from funcionesGlobales import *
from menu_administrador import*
from menu_usuarios import*

datosUsuarios = leerJson("usuarios")

while True:
    datosUsuarios= leerJson("usuarios")
    opc = usuario_o_admin()
    if opc == 1:
        if contraseña_admin():
            menu_administrador()
    elif opc == 2:
        datosUsuarios = login(datosUsuarios)
        if datosUsuarios==None:
            datosUsuarios=leerJson("usuarios")
    elif opc== 0:
        print("Gracias por ingresar a knowledge jungle ")
        print("¡Vuelva Pronto a aprender")
        break
    else:
        print("Ingresa un valor valido")

    guardarJson("usuarios",datosUsuarios)