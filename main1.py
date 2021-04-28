from Clasemail import email

from Manejadoremails import manejadoremail

if __name__ == '__main__':
    print('Ingrese lo siguientes datos:')

    nombre = input('Nombre:')
    idCuenta = input('Id de su cuenta:')
    dominio = input('Dominio:')
    tipodom = input('Tipo de dominio:')
    contra = input('Contraseña:')

    mail = email(idCuenta,dominio,tipodom,contra)

    print(str(mail))
    print("Estimado", nombre,"te enviaremos tus mensajes a la dirección: ",mail)

    '''punto 1'''

    print('Ahora deberá cambiar la contraseña ingresada anteriormente')
    contravieja = input('Ingrese su contraseña anterior:')
    mail.modificarContra(contravieja)
    print("")
    print("Su contraseña ha sido modificada correctamente")

    '''punto 2'''

    correo = (input('Ingrese su correo electrónico:'))
    lista1 = correo.split("@")  #lista1 [0] = id del correo // lista1 [1] = dom.tipodom
    lista2 = lista1[1].split(".")  #lista2 [0] = dom // lista2 [1] = tipodom
    contra = input('Ingrese contraseña: ')
    correoobj = email(lista1[0], lista2[0], lista2[1], contra)

    if type(correoobj) == email:
        print(f'A partir del correo "{correo}", se ha creado exitosamente un objeto, cuyo identificador es c')

    '''punto 3'''

    mane = manejadoremail
    mane.crearlista()

    dom = input('Ingrese el dominio que desea buscar: ')
    print(f'Cantidad de dominios iguales a "{dom}" = {manejador.busquedamails(dom)}')

    '''punto 4'''





