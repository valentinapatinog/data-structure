class Heroe:
    def __init__(self, nombre_del_heroe, mundo_al_que_pertenece):
        self.nombre = nombre_del_heroe
        self.mundo = mundo_al_que_pertenece
        self.poderes = []
        self.creadores = []
        
        
    def obtener_poderes(self):
        los_poderes = ''
        for poder in self.poderes:
            los_poderes = los_poderes + ' ' + poder
        los_poderes
        
    def agregar_poder(self, nuevo_poder):
        self.poderes.append(nuevo_poder)
        
    def agregar_creador(self, nuevo_creador):
        self.creadores.append(nuevo_creador)
        
class superhero:
    def __init__(self):
        self.superheroes = []
        
    def mostrar_menu_general(self):
        print ("Bienvenido usuario, seleccione una opción del menu: ")
        while True:
            try:
                menu_option = int(input('1. Encontrar un super heroe \n2. Eliminar superheroe \n3. Superheroe con mayor cantidad de super poderes \n4. Superheroe con menor cantidad de super poderes \n5. Mostrar todos los superheroes del sistema \n6. Salir\n\n'))
                if menu_option < 1 or menu_option > 6:
                    print ("Opción incorrecta")
                elif menu_option == 1:
                    self.__buscar_superheroe()
                elif menu_option == 2:
                    self.__eliminar_superheroe()
                elif menu_option == 3:
                    self.__encontrar_superheroe_con_mayor_cantidad_de_poderes()
                elif menu_option == 4:
                    self.__()
                elif menu_option == 5:
                    self.__unite_lists()
                elif menu_option == 6:
                    break
            except ValueError:
                print ("Error en la opción indicada")
    def __buscar_superheroe(self):
        nombre_heroe_a_buscar = input("Nombre del superhéroe que deseas buscar: ")
        encontrado = False
        for superhero in self.superheroes:
            if superhero.nombre == nombre_heroe_a_buscar:
                print("Superpoderes: " + superhero.obtener_poderes())
            encontrado = True
            break
        if not encontrado:
            desea_agregarlo = input("No se encontró el superhéroe. ¿Deseas añadirlo? (s/n) ")
        if desea_agregarlo == "s":
            self.__agregar_superheroe(nombre_heroe_a_buscar)
        elif desea_agregarlo == "n":
            print("No se añadirá ningún superhéroe, si desea vuelva pronto")
        else:
            print("Lo que ingresó no es válido. Por favor ingrese 's' o 'n'.")
                        
    def __agregar_superheroe(self, nombre_heroe_a_agregar):
        mundo = input('A que mundo pertenece: ')
        nuevo_heroe = Heroe(nombre_heroe_a_agregar, mundo)
        
        cantidad_de_poderes = int(input("Ingrese la cantidad de poderes que tiene el superheroe: "))
        for i in range (cantidad_de_poderes):
            poder = input("Ingrese el nombre del poder del superheroe: ")
            nuevo_heroe.agregar_poder(poder)

        cantidad_de_creadores = int(input("Ingrese la cantidad de creadores que tiene el superheroe: "))
        for i in range (cantidad_de_creadores):
            creador = input("¿Cuál es el nombre del creador?: ")
            nuevo_heroe.agregar_creador(creador)
            
        self.superheroes.append(nuevo_heroe)       
     
    def __eliminar_superheroe(self):
        nombre_heroe_a_eliminar = input("Nombre del superhéroe que deseas eliminar: ")
        encontrado = False
        for superhero in self.superheroes:
            if superhero.nombre == nombre_heroe_a_eliminar:
                self.superheroes.remove(superhero)
            print("El superhéroe " + nombre_heroe_a_eliminar + " ha sido eliminado.")
            encontrado = True
            break
        if not encontrado:
            print("No se encontró el superhéroe " + nombre_heroe_a_eliminar)


    def __encontrar_superheroe_con_mayor_cantidad_de_poderes(self):
        if(len(self.superheroes) > 0):
            heroe_con_mas_poderes_encontrado_hasta_el_momento = self.superheroes[0]
            for heroe in self.superheroes:
                if(len(heroe.poderes) > len(heroe_con_mas_poderes_encontrado_hasta_el_momento.poderes)):
                    heroe_con_mas_poderes_encontrado_hasta_el_momento = heroe
                    
            print(f"El nombre del superhéroe con más poderes es: {heroe_con_mas_poderes_encontrado_hasta_el_momento.nombre}, que tiene {len(heroe_con_mas_poderes_encontrado_hasta_el_momento.poderes)} poderes")
        else:
            print('No hay heroes por el momento')
#corregir 
#8. método que devuelva el nombre del superhéroe que tiene menor cantidad de superpoderes
    def __encontrar_superheroe_con_menor_cantidad_de_poderes(self):
        least = 100
        auxiliar_list = self.marvel_superheroes_list + self.dc_superheroes_list
        for superhero in auxiliar_list:
            # Valida si es una lista o un String
            if type(superhero[1]) == str:
                length = 1
            else:
                length = len(superhero[1])
            print(length)

            if length < least:
                least = len(superhero[1])
                name = superhero[0]
        print(f"El nombre del superhéroe con menos poderes es: {name}")
#corregir
    def unite_lists(self):
        self.marvel_universe.extend(self.dc_universe)
        print("Lista unida")
        print(self.marvel_universe)


