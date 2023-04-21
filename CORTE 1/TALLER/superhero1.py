class Superhero:
    def _init_(self):
        self.marvel_superheroes_list = []
        self.dc_superheroes_list = []
        self.superheroe_name = ""
        self.superheroe_powers = []
        self.superheroe_creators = []
    
    def menu(self):
        # >>> Objetos de prueba <<<
        self.marvel_superheroes_list.append(("Spider-Man", ["Telaraña", "Pelear", "Invisibilidad"], ["Steve Ditko " , "Stan Lee "]))
        self.marvel_superheroes_list.append(("Super-man", ["Volar", "Velocidad"],["Stan Lee"]))
        self.marvel_superheroes_list.append(("Hulk", ["Dinamo kinesis","Super fuerzas"], ["Stan Lee", "Jack Kirby"]))
        self.dc_superheroes_list.append(("Batman", ["Conducir rápido", "Esconderse en la noche"], ["Bob Kane", "Bill Finger"]))
        self.dc_superheroes_list.append(("Mujer maravilla", ["Super fuerza, Invisibilidad"], ["William Mouton"]))
        while True:
            try:
                opciones = {
                    '1': ('Agregar superheroes', self.get_data),
                    '2': ('Ver poderes superheroe', self.get_superhero_powers),
                    '3': ('Eliminar superheroe', self.delete_superhero),
                    '4': ('Superheroe mayor cantidad de superpoderes', self.greater_powers),
                    '5': ('Superheroe menor cantidad de superpoderes', self.least_powers),
                    '6': ('Unir lista DC y lista Marvel', self.join_lists),
                    '7': ('Info testeo', self.test)
                }
                print(" >>> Menú superhéroes <<<")
                for clave in opciones:
                    print(f"[{clave}] {opciones[clave][0]}")
                print(f"[{len(opciones) + 1}] Salir")
                opcion = input("Opción: ")

                if int(opcion) != len(opciones) + 1 and opcion in opciones:
                    opciones[opcion][1]()
                else:
                    print("Mensaje salida")
                    break
            except ValueError:
                print(" ¡Error!: Debe ingresar un número")
    
    def get_data(self):
        while True:
            try:
                print(" >>> Ingrese la siguiente información: <<<")
                superhero_world = int(input("Mundo al que pertenecen los superhores: \n[1] DC\n[2] Marvel\n[3] Salir\n"))
                if superhero_world == 1 or superhero_world == 2:
                    num_superheroes = int(input("Cantidad de superheroes: "))
                    for superheroe in range(num_superheroes):
                        print(f" >>> {superheroe + 1} <<< ")
                        self.superheroe_name = str(input("Nombre del superheroe: "))
                        # title(): Pone las primeras letras de cada palabra en mayúscula
                        # split(): Separa las palabras
                        self.superheroe_powers = input("Poderes:  (separados por una coma)\n").title().split(", ")
                        
                        # Validar si es sólo 1 elemento, en el caso de que sí, volver un String
                        if len(self.superheroe_powers) == 1:
                            self.superheroe_powers = self.superheroe_powers[0]

                        self.superheroe_creators = input("Creadores: (separados por coma)\n").title().split(", ")
                        if len(self.superheroe_creators) == 1:
                            self.superheroe_creators = self.superheroe_creators[0]
                        
                        # Agregar a la lista, dependiendo si es de DC o Marvel
                        if superhero_world == 1:
                            self.dc_superheroes_list.append((self.superheroe_name, self.superheroe_powers, self.superheroe_creators))
                        elif superhero_world == 2:
                            self.marvel_superheroes_list.append((self.superheroe_name, self.superheroe_powers, self.superheroe_creators))
                else:
                    break
            except ValueError:
                print(" ¡Error!: debe ingresar un número")
    
    def get_superhero_powers(self):
        found = False
        self.superheroe_name = input("Ingrese el nombre del superheroe: ")
        auxiliar_list = self.marvel_superheroes_list + self.dc_superheroes_list
        for superhero in auxiliar_list:
            if self.superheroe_name in superhero:
                # Imprime la lista de poderes
                found = True
                print(f"Poderes: {superhero[1]}")
        
        if not found:
            print("No pudimos encontrar ese superheroe")
            selection = input("¿Desea añadir un nuevo superheroe?\n[1] Sí\n[2] No\n")
            if selection == '1':
                self.get_data()



    def delete_superhero(self):
        self.superheroe_name = input("Ingrese el nombre del superheroe: ")
        for superhero in self.marvel_superheroes_list:
            if self.superheroe_name == superhero[0]:
                print(f"Se eliminó {self.superheroe_name} de la lista de superheroes Marvel")
                self.marvel_superheroes_list.remove(superhero)

        for superhero in self.dc_superheroes_list:
            if self.superheroe_name == superhero[0]:
                print(f"Se eliminó {self.superheroe_name} de la lista de superheroes DC")
                self.dc_superheroes_list.remove(superhero)
        

    def greater_powers(self):
        greater = 0
        auxiliar_list = self.marvel_superheroes_list + self.dc_superheroes_list
        for superhero in auxiliar_list:
            # Valida si es una lista o un String
            if type(superhero[1]) == str:
                length = 0
            else:
                length = len(superhero[1])

            if length > greater:
                greater = len(superhero[1])
                name = superhero[0]
        print(f"El nombre del superhéroe con más poderes es: {name}")
    
    def least_powers(self):
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
    
    def join_lists(self):
        joined_list = self.marvel_superheroes_list + self.dc_superheroes_list
        print(" >>> Lista unida <<<")
        print(joined_list)

    def test(self):
        print("Superheroes Marvel")
        for marvel_superhero in self.marvel_superheroes_list:
            print("------------------------------------")
            print(f"Nombre: {marvel_superhero[0]}")
            print(f"Poderes: {marvel_superhero[1]}")
            print(f"Creadores: {marvel_superhero[2]}")
        print("=======================================")
        print("Superheroes DC")
        for dc_superhero in self.dc_superheroes_list:
            print("------------------------------------")
            print(f"Nombre: {dc_superhero[0]}")
            print(f"Poderes: {dc_superhero[1]}")
            print(f"Creadores: {dc_superhero[2]}")