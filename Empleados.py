class  Empleados():
    numero_empleados = 0 #atributo de clase


    #creador del CONSTRUCTOR
    #nombre,cargo,salario ATRIBUTOS DE INSTANCIA
    def __init__(self,nombre,cargo,salario):
        #DATOS///////////////////////////////////////////////////////
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario 
        Empleados.numero_empleados += (1) # Incrementa el contador de empleados cuando se registra
        #COMPORTAMIENTO///////////////////////////////////////////////
    def presentarse(self): #metodo de instancia
        print (f"Hola, soy {self.nombre} y mi posicion es de {self.cargo}.")

    def aumentar_salario (self, porcentaje): #metodo de instancia
        self.salario *= (1+porcentaje/100)
        print (f"Nuevo salario de {self.nombre}: {self.salario}")

    @classmethod
    def desde_string(cls, datos_empleado): #metodoo de una clase 
        nombre,cargo,salario = datos_empleado.split(",")
        return cls (nombre, cargo, float (salario))
    
    @staticmethod
    def es_festivo (dia): 
        festivo = [1, 10, 27]
        return dia in festivo

#creamos instancias de los empleados
empleado1 = Empleados ("Juan Perez", "Gerente", 5000)
empleado2 = Empleados ("Raquel Lopez", "Desarrollador", 3500)
empleado3 = Empleados ("Adamari Lopez", "Desarrollador2", 3500)

#utlizamos el metodo clase
empleado4 = Empleados.desde_string("Samuel Quiroz, UX/UI, 3000")

#comprobamos si es festivo hoy
es_festivo_hoy = Empleados.es_festivo(1)

#Utilizamos los metodos de instancia para presentarse
empleado1.presentarse()
empleado2.presentarse()
empleado3.presentarse()
empleado4.presentarse()

#aumentamos salario 
empleado1.aumentar_salario(10)


