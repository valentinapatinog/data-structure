'''
list methods
Date: 10/01/23
'''
class ListMethods:
    #Metodo inicializador de la clase
    def __init__(self):
        #Definimos una lista vacia
        self.pets= []
        #Otra forma de definir una lista vacia 
        self.vehicles = list()

    #2. Metodo para añadir elementos en la lista
    def add_list_elements(self):
        #['dog' , 'cat']
        self.pets.append('dog')
        self.pets.append('cat')
        print (self.pets)

    #3. Metodo que solicita valores al usuario
    def input_data_vehicles_list (self):
        #Variables locales: vahicles_number, vehicles_ty
        vehicles_number = int(input('¿Cuántos vehiculos?: '))
        #Recorrer la lista 
        for vehicle_item in range (vehicles_number):
            vehicle_type = input('Tipo de vehiculo:')
            #Añadimos el vehiculo a l lista
            self.vehicles.append(vehicle_type)
        #Imprimir toda la lista
        print (self.vehicles)
        #Imprimir ultimo,penultimo y antepenultimo elemento de la lista
        print (self.vehicles[-1], self.vehicles[-2],)

    #4. Extraer valores de una lista 2 hasta 4-1
    def show_collection_data_list(self):
        #Imprimir desde posicion 2 hasta 3 
        print (self.vehicles [2:4])
        #Imprimir todos los elementos de la lista 
        print (self.vehicles[:])
        #Imprimir elementos desde un indice especifico: 2 [0,1,2,..]
        print (self.vehicles[2:])
        #Imprimir elementos hasta un indice esppecifico: 2 [0,1,2]
        print (self.vehicles [:2])
        #Acceder a TODOS los elementos de 2 en 2 
        print (self.vehicles [::2])
        #Acceder a un SUBCONJUNTO de elementos de 2 en 2 
        print (self.vehicles [1:5:2])

    #iterar los elementos de una lista con for 
    def iteration_list (self):
        for item in self.vehicles:
            print (item)
        #Validar si la lista contiene un valor especifico
        if "carro".capitalize () in self.vehicles:
            print ("Si se encontró valor")
        else:
            print ("No se encontró el valor")

    #6. Añadir varios elementos al final de la lista 
    def add_elements(self):
        self.vehicles.extend(['Avion', 'Tractomula', 'Otro medio'])
        print (self.vehicles)

    #7. Añadir un elemento en posicon especifica de la lista
    def add_specific_element(self):
        self.vehicles.insert(0, 'Moto')
        print (self.vehicles)

    #8. Eliminar último elemento de la lista
    def remove_last_element (self):
        self.vehicles.pop()
        print (self.vehicles)

    #9. Eliminar elemento de posicion especifica
    def remove_specific_elements(self):
        #Primer elemento
        self.vehicles.pop (0)
        print (self.vehicles)
    
    #10. Eliminar todos los elementos de la lista 
    def remove_element_by_name(self):
        self.vehicles.clear()

    #11. Eliminar de la lista un valor especifico
    def remove_element_by_name(self):
        self.vehicles.remove ("tractomula".capitalize())
        print (self.vehicles)

    #12. Eliminar todas las coincidencias de valor en la lista
    def remove_all_match_elements(self):
        new_list = list(filter(('tractoomula')._ne_, self.vechicles))
        print (new_list)


