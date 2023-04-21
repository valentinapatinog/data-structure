'''
    Data type: list practice
    Date :25/01/23
'''
#1. Declarar la clase 
class ListPractice :
    #2. Crear la funcion inicializadora de la clase 
    def __init__(self):
        #Definir las variables globales de la clase 
        self.student_name ="Valentina Patiño Giraldo"
        self.courses_list =['POO','TAD']


    #3 Funcion customizada 
    def show_info_list(self):
        #imprimir el contenido de la lista courses_list 
        print(self.courses_list)
        # Cantidad de elementos que tiene la lista
        print(len(self.courses_list))

    #4 Funcion que solicita al usuario ingresar informacion 
    def input_data_courses(self ):

        #1. Declaramos una variable a nivel de metodo
        print('ingrese la sigiente informacion:')
        #solicitud de texto
        self.student_name = input('Nombre: ')
        #Solicitud de numero entero
        courses_number = int (input('cantidad asignaturas: '))
        #Validamos si el courses_number es menor que el tamaño actual de la lista
        if courses_number <= len (self.courses_list):
            print ('>> error: cursos a incribir es menor que 2<<')
        else :
            #Solicitar nombre de las asignaturas al usuario 
            for course in range(courses_number):
                #Variabale que almacena el nombre de la signatura 
                course_name =input ('nombre asisgnatura ') 
                #Añadimos nuevoelemento al final de la lista
        if course_name in self.courses_list:
            print('Ya se encuentra registrada su asignatura')
        else:
            #Append
            self.courses_list.append(course_name)       
        # Imprimir contenido de la lista 
        print(self.courses_list)     



