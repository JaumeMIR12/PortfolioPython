class Agenda:

    def __init__(self):
        self.agenda={}

    def menu(self):
        opcion=0
        while opcion!=5:
            print("1- Carga de un contacto en la agenda")
            print("2- Listado completo de la agenda")
            print("3- Consulta ingresando el nombre de la persona")
            print("4- Modificacion del telefono y mail")
            print("5- Finalizar programa")
            opcion=int(input("QUe opcion eliges:"))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listado()
            elif opcion==3:
                self.consulta()
            elif opcion==4:
                self.modificacion()

    def cargar(self):
        nombre=input("Nombre:")
        telefono=input("Numero de telefono:")
        mail=input("Email:")
        self.agenda[nombre]=(telefono,mail)
        print("")
        
    def listado(self):
        print(" ")        
        print("Listado completo de la agenda")
        for nombre in self.agenda:
            print(nombre, self.agenda[nombre][0],self.agenda[nombre][1])
        print(" ")

    def consulta(self):
        print(" ")        
        nombre=input("Nombre que persona consultar:")
        if nombre in self.agenda:
            print(nombre," su telefono es",self.agenda[nombre][0],"y su mail es",self.agenda[nombre][1])
        else:
            print("no hay ese contacto")
        print(" ")            

    def modificacion(self):
        print(" ")        
        nombre=input("Escribe el nombre de la persona a modificar el telefono y mail:")
        if nombre in self.agenda:
            telefono=input("Escribe telefono:")
            mail=input("Escribe email:")
            self.agenda[nombre]=(telefono,mail)
        else:
            print("No existe un contaxto con ese nombre")
        print(" ")         
        

agenda=Agenda()
agenda.menu()