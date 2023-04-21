class TupleList:
    def_ init_(self):
        self.countries_list = []
        self.country_name = ""
        self.population = 0
        Self.continent = ""

    #Funcion que solicita al usuario de paises a crear 
     def total_coutries (self):
        print ('Ingresa la informacion')
        print ('=========================================')

        while True:
            try:
                number_countries = int (input('Cantidad a añadir:'))
                for country in range (number_countries):
                    self.country_name = input(':')
            except ValueError:
                print ('>> Error en el tipo de dato suministrado ')