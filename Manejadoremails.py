import csv

from Clasemail import email

class manejadoremail:

    __listacorreos = [ ]

    def __init__(self):
        self.__listacorreos = []

    def agregarmail(self, mailnuevo):
        self.__listacorreos.append(mailnuevo)

    def crearlista(self):
        archivo = open('Emails.csv')
        reader = csv.reader(archivo,delimiter = ',')
        for fila in reader:
            lista1 = fila[0].split("@")  # lista1 [0] = id del correo // lista1 [1] = dom.tipodom
            lista2 = lista1[1].split(".")  # lista2 [0] = dom // lista2 [1] = tipodom
            mailnuevo = email(lista1[0], lista2[0], lista2[1])
            self.agregarmaill(mailnuevo)
        archivo.close()

    def busquedamails (self,dom):
        cont = 0
        for email in self.__listacorreos:
            if email.getdominio() == dom:
                cont += 1
        return cont











