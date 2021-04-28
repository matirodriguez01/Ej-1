class email:
    __idCuenta = ''
    __dominio = ''
    __tipodominio = ''
    __contraseña = ''

    def __init__(self, id, dom, tipodomi, contra):
        self.__idCuenta = id
        self.__dominio = dom
        self.__tipodominio = tipodomi
        self.__contraseña = contra

    def __str__(self):
        return ""+self.__idCuenta+"@"+self.__dominio+"."+ self.__tipodominio+""

    def retornaDominio (self):
        return self.__dominio

    def modificarContra (self, contravieja):
        if contravieja == self.__contraseña:
            self.__contraseña == input('Ingrese su contraseña nueva;')

        else:
            print('La contraseña ingresada no corresponde con la almacenada en nuestro sistema')

