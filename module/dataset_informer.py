import csv

def without_repeated(route, index):
    '''This function returns a list without repeteated elements'''
    with open(route, encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        type_list = []

        for line in reader:
            type_list.append(line[index])

    new_list = set(type_list)
    return new_list


def choose_elevation_menu():
    '''This function is a menu to choose the elevation 
    of the airport. Returns the value entered'''

    print("""Ingrese el tipo de elevacion de aeropuerto que quiere visualizar
         1._ Bajo
         2._ Medio
         3._ Alto
         """)
    
    while True:
        elevation = (input())
        if elevation in ["1", "2", "3"]:
            break
        else:
            print("Ingresaste un valor incorrecto, ingresa un valor entre 1-3")
            continue
    return elevation


def airports_by_elevation(route):
    elevation = choose_elevation_menu()
    print(f"Aeropuertos de elevacion {elevation}")

    with open(route, encoding= 'utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        type_list = []

        for line in reader:
            if elevation == "1":
                if(line[23] == "bajo"):
                    type_list.append(line[3])
            elif elevation == "2":
                if(line[23] == "medio"):
                    type_list.append(line[3])
            else:
                if(line[23] == "alto"):
                    type_list.append(line[3])

    return type_list


def choose_minor_or_major():
    '''This function is a menu to choose between
    minor or major. Returns the value entered'''

    print('''Deseas filtrarlo por : 
          a_ Mayor
          b_ menor''')
    
    while True:
        minor_or_major = (input())
        if minor_or_major in ["a", "b"]:
            break
        else:
            print("Ingresaste un valor incorrecto, ingresa 'a' o 'b'")
            continue
    return minor_or_major


def airports_by_entered_value(route):
    '''This function returns the airports names according to the entered
    value and the airport elevation. If is minor or major add to the list'''
    value = int(input('Ingrese un valor de elevacion: '))
    minor_or_major = choose_minor_or_major()
    
    with open(route, encoding='utf-8') as file:
        reader = csv.reader(file)
        header, data = next(reader), list(reader)
    
    elevation = 6
    airport_name = 3
    result_list = []

    if minor_or_major == 'a':
        print(f'Los aeropuertos con mayor elevacion segun el valor ingresado "{value}" son: ')

        for line in data:
            if line[elevation]:
                if int(line[elevation]) > value:
                    result_list.append(line[airport_name]) 

        return result_list
    else:
        print(f'Los aeropuertos con menor elevacion segun el valor ingresado "{value}" son: ')

        for line in data:
            if line[elevation]:
                if int(line[elevation]) < value:
                    result_list.append(line[airport_name]) 

        return result_list


def replace_vowels(text):
    ''' This function replaces accented vowels with normal vowels '''
    import string
    characters = ('á','é','í','ó','ú')
    for character in characters:
        if not(character in string.ascii_letters):
            match character:
                case 'á': text = text.replace('á','a')
                case 'é': text = text.replace('é','e')
                case 'í': text = text.replace('í','i')
                case 'ó': text = text.replace('ó','o')
                case 'ú': text = text.replace('ú','u')
                case _: continue
    return text


def aiport_printer(airport_route, census_route, value, minor_or_major):
    '''This function print provinces and airports according to an entered value'''
    prov_name = 24
    population = 1
    airport_name = 3

    if minor_or_major == 'a':
        with open(airport_route, encoding='utf-8') as airport_file, open(census_route, encoding='utf-8') as census_file:
            airport_reader = csv.reader(airport_file)
            census_reader = csv.reader(census_file)

            next(airport_reader)

            for airport_line in airport_reader:
                province_airport = airport_line[prov_name]
                census_file.seek(0)
                next(census_reader)
                next(census_reader)
                for census_line in census_reader:
                    if province_airport.lower() in census_line[0].lower(): 
                        if int(census_line[population]) > value:
                            print(f'Provincia : {province_airport}; Aeropuerto : {airport_line[airport_name]}')  
                        break
    else:
        with open(airport_route, encoding='utf-8') as airport_file, open(census_route, encoding='utf-8') as census_file:
            airport_reader = csv.reader(airport_file)
            census_reader = csv.reader(census_file)

            next(airport_reader)

            for airport_line in airport_reader:
                province_airport = airport_line[prov_name]
                census_file.seek(0)
                next(census_reader)
                next(census_reader)
                for census_line in census_reader:
                    if province_airport.lower() in census_line[0].lower(): 
                        if int(census_line[population]) < value:
                            print(f'Provincia : {province_airport}; Aeropuerto : {airport_line[airport_name]}')  
                        break


def lakes_printer(lakes_route, census_route, value, minor_or_major):
    '''This function print provinces and lakes according to an entered value'''
    province_lake1 = 1
    population = 1
    lake_name = 0

    if minor_or_major == "a":
        with open(lakes_route, encoding='utf-8') as lakes_file, open(census_route, encoding='utf-8') as census_file:
            lakes_reader = csv.reader(lakes_file)
            census_reader = csv.reader(census_file)

            next(lakes_reader)

            for lake_line in lakes_reader:
                province_lake = lake_line[province_lake1]
                census_file.seek(0)
                next(census_reader)
                next(census_reader)
                for census_line in census_reader:
                    if province_lake.lower() in census_line[0].lower(): 
                        if int(census_line[population]) > value: 
                            print(f'Provincia : {province_lake}; Aeropuerto : {lake_line[lake_name]}')  
                        break
    else:
        with open(lakes_route, encoding='utf-8') as lakes_file, open(census_route, encoding='utf-8') as census_file:
            lakes_reader = csv.reader(lakes_file)
            census_reader = csv.reader(census_file)

            next(lakes_reader)

            for lake_line in lakes_reader:
                province_lake = lake_line[province_lake1]
                census_file.seek(0)
                next(census_reader)
                next(census_reader)
                for census_line in census_reader:
                    if province_lake.lower() in census_line[0].lower(): 
                        if int(census_line[population]) < value: 
                            print(f'Provincia : {province_lake}; Aeropuerto : {lake_line[lake_name]}')  
                        break


def type_connections_printer(connection_route, census_route, value, minor_or_major):
    '''This function print provinces and a list of 
     connectivity types according to an entered value'''
    province_column = 0
    population_column = 1

    if minor_or_major == 'a':
        with open(connection_route, encoding='utf-8') as connection_file, open(census_route, encoding='utf-8') as census_file:
            connection_reader = csv.reader(connection_file)
            census_reader = csv.reader(census_file)

            header = next(connection_reader)
            header_list = list(header)
            dataset_list = list(connection_reader)

            province_column = 0
            population_column = 1
        
            next(census_reader)
            next(census_reader)
            for census_line in census_reader:
                type_list = []
                connection_file.seek(0) 
                next(connection_reader)  
                
                population = census_line[population_column]
                province = census_line[province_column]
                province_without_accents = replace_vowels(province)

                #Realizo chequeos ya que son las mismas provincias pero en los datasets no coinciden
                if province_without_accents == 'Ciudad Autonoma de Buenos Aires':
                    province_without_accents = 'CABA'
                if province_without_accents == 'Tierra del Fuego, Antartida e Islas del Atlantico Sur':
                    province_without_accents = 'TIERRA DEL FUEGO'

                for data in dataset_list:
                    if province_without_accents.lower() in data[0].lower(): 
                        if int(population) > value:
                            for i, item in enumerate(data):
                                if item == 'SI':  
                                    type_list.append(header_list[i])
                if type_list:
                    new_list = set(type_list)  
                    print(f'Lista de conectividades de la provincia {province_without_accents} es {new_list}')
                else:
                    print(f'No hay ningun tipo de conectividad en la provincia {province_without_accents} segun los valores ingresados')
    else:
        with open(connection_route, encoding='utf-8') as connection_file, open(census_route, encoding='utf-8') as census_file:
            connection_reader = csv.reader(connection_file)
            census_reader = csv.reader(census_file)

            header = next(connection_reader)
            header_list = list(header)
            dataset_list = list(connection_reader)

            province_column = 0
            population_column = 1
        
            next(census_reader)
            next(census_reader)
            for census_line in census_reader:
                type_list = []
                connection_file.seek(0) 
                next(connection_reader)  

                population = census_line[population_column]
                province = census_line[province_column]
                province_without_accents = replace_vowels(province)

                #Realizo chequeos ya que son las mismas provincias pero en los datasets no coinciden
                if province_without_accents == 'Ciudad Autonoma de Buenos Aires':
                    province_without_accents = 'CABA'
                if province_without_accents == 'Tierra del Fuego, Antartida e Islas del Atlantico Sur':
                    province_without_accents = 'TIERRA DEL FUEGO'

                for data in dataset_list:
                    if province_without_accents.lower() in data[0].lower(): 
                        if int(population) < value:
                            for i, item in enumerate(data):
                                if item == 'SI':  
                                    type_list.append(header_list[i])
                if type_list:
                    new_list = set(type_list)  
                    print(f'Lista de conectividades de la provincia {province_without_accents} es {new_list}')
                else:
                    print(f'No hay ningun tipo de conectividad en la provincia {province_without_accents} segun los valores ingresados')


def printer(airport_route, lakes_route, connection_route, census_route):
    '''This function prints all the airports, lakes and 
    connectivity types according to an entered value'''
    value = int(input("Ingrese un valor"))
    minor_or_major = choose_minor_or_major()

    aiport_printer(airport_route, census_route, value, minor_or_major)
    lakes_printer(lakes_route, census_route, value, minor_or_major)
    type_connections_printer(connection_route, census_route, value, minor_or_major)


def inform_connectivity_types(route): #inciso 9
    """ This function reports the different types of connectivity contained in the 'Connectividad_Internet.csv' file'"""
    with open(route, encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)[4:13]
        for element in header:
            print(element, end=' ')


def connectivity_types_per_city(connectionroute): #inciso 10
    """ This function reports the amount of cities with each type of connectivity """
    counter = {'ADSL':0 ,'CABLEMODEM':0 ,'DIALUP':0,'FIBRAOPTICA':0,'SATELITAL':0,'WIRELESS':0,'TELEFONIAFIJA':0,'3G':0,'4G':0}
    with open(connectionroute, encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for line in reader:
            for elem in line:
                if(elem in counter):
                    if (line[elem] == 'SI'):
                        counter[elem] = counter[elem] + 1
        print(counter)


def remove_accent(word):
    '''This function returns the word without accent'''
    accents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
               'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
    word_without_accent = ''.join([accents.get(letter, letter) for letter in word])
    return word_without_accent


def airports_in_capitals (route1, route2):
    '''This function returns a dict with the airports in the capital of each province'''
    capital = 6
    city = 0
    municipality = 13
    name = 3
    with open(route1, encoding = 'utf-8') as capitals_file, open (route2, encoding = 'utf-8') as airports_file:
        reader = csv.reader(capitals_file)
        next (reader)
        capitals_list = []
        for line in reader:
                if line[capital] == 'admin':
                        city_without_accent = remove_accent(line[city])
                        capitals_list.append(city_without_accent)
        reader = csv.reader (airports_file)
        next(reader)
        airports_dict = {}
        for line in reader:
                city_without_accent = remove_accent(line[municipality])
                if city_without_accent in capitals_list:
                        if city_without_accent not in airports_dict:
                                airports_dict[city_without_accent] = []
                        airports_dict[city_without_accent].append(line[name])
    return airports_dict


def menu2():
    ''' This function is a menu to choose the surface of the lakes'''
    print ('''Ingrese la superficie de lagos que desea visualizar (ingresar palabra en minuscula):
            1) Chico
            2) Medio
            3) Grande
            ''')
    while True:
        surface = (input())
        if surface == 'chico' or surface == 'medio' or surface == 'grande':
            break
        else:
            print ('Ingresaste mal la superficie, ingrese una de las 3 sugeridas')
            continue
    return surface


def lakes_by_surface(route):
    '''This function returns a list with the lakes of one category (little, medium or big)'''
    size = 9
    name = 0
    surface = menu2()
    with open (route, encoding = 'utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        lakes_list = []
        for line in reader:
            if line[size] == surface:
                lakes_list.append(line[name])
    return lakes_list


def street_situation (route):
    '''This function returns a list of tuples with the five jurisdictions with the largest homeless pupulation'''
    jurisdiction = 0
    percent = 13
    with open (route, encoding = 'utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        next(reader)
        jurisdiction_dict = {}
        for line in reader:
            jurisdiction_dict[line[jurisdiction]] = line[percent]
        list_ordered = sorted (jurisdiction_dict.items(), key = lambda x: x[1], reverse = True)
        max_5 = list_ordered[:5]
    return max_5


def population_gap (route):
    '''This function returns a tuple with the name and the population gap of the jurisdiction
       in wich the gap is largest'''
    jurisdiction = 0
    male_population = 5
    female_population = 9
    max_difference = -1
    with open (route, encoding = 'utf-8') as file:
        reader = csv.reader(file)
        next (reader)
        next (reader)
        for line in reader:
            difference = abs(int(line[male_population]) - int(line[female_population]))
            if difference > max_difference:
                max_difference = difference
                tuple = (line[jurisdiction], difference)
    return tuple


def replace_vowels(text):
    """ Esta funcion remplaza las vocales con tilde por vocales normales. """
    import string
    characters = ('á','é','í','ó','ú')
    for character in characters:
        if not(character in string.ascii_letters):
            match character:
                case 'á': text = text.replace('á','a')
                case 'é': text = text.replace('é','e')
                case 'í': text = text.replace('í','i')
                case 'ó': text = text.replace('ó','o')
                case 'ú': text = text.replace('ú','u')
                case _: continue
    return text


def province_with_optical_fiber(connection_route,census_route): # Inciso 11. Los datos de buenos aires estan mal.Consultar.
    """ This function reports provinces that all its cities has optical fiber """
    with open(census_route, encoding = 'utf-8') as census_file:
        censusreader = csv.reader(census_file)
        datacensus = list(censusreader)

    with open(connection_route, encoding ='utf-8') as connection_file:
        connectionreader = csv.reader(connection_file)

        # Analizo solo la ciudad autonoma de buenos aires para no poner tantos if como si analizara junto a las demas provincias
        province = 'Ciudad Autónoma de Buenos Aires'
        counter = [0,0] # primera pos el total y segunda pos las que tienen fibra optica
        connection_file.seek(1)
        for connectionline in connectionreader:
            if (connectionline[0] == 'Ciudad Autónoma de Buenos Aires' or connectionline[0] == 'CABA'):
                counter[0] += 1
                if (connectionline[7] == 'SI'):
                    counter[1] += 1
        if (counter[0] == counter[1]): print(f'En {province} todas sus ciudades poseen fibra optica.')
        # print(counter,province)

        # Analizo todas las demas provincias
        for i in range(3, len(datacensus)):
            province = datacensus[i][0]
            counter = [0,0] # primera pos el total y segunda pos las que tienen fibra optica
            connection_file.seek(1)
            for connectionline in connectionreader:
                if (replace_vowels(connectionline[0].lower()) in replace_vowels(province.lower())):
                    counter[0] += 1
                    if (connectionline[7] == 'SI'):
                        counter[1] += 1
            if (counter[0] == counter[1]): print(f'En {province} todas sus ciudades poseen fibra optica.')
            # print(counter,province)


def capitals_with_connectivity(connection_route,argentina_route,census_route): # Inciso 12. Los datos de buenos aires estan mal y no los muestra.Consultar.
    """ This function reports the capital of each province and if they has connectivity """
    with open(census_route, encoding='utf-8') as census_file:
        censusreader = csv.reader(census_file)
        datacensus = list(censusreader)

    with open(connection_route, encoding='utf-8') as connection_file, open (argentina_route, encoding='utf-8') as argentina_file:
        connectionreader = csv.reader(connection_file)
        argentinareader = csv.reader(argentina_file)
        
        # Analizo solo buenos aires para no poner tantos if como si analizara junto a las demas provincias
        province = 'Buenos Aires'
        argentina_file.seek(1)
        for lineargentina in argentinareader:
            #print(province.lower(),lineargentina[5].lower())
            if (province.lower() == lineargentina[5].lower() and  lineargentina[6] == 'admin'):
                print('Provincia: ' + province + ' Capital: ' + lineargentina[0])
                encontre = False
                connection_file.seek(1)
                for lineconnection in connectionreader:
                    if (lineconnection[2].lower() == lineargentina[0].lower()):
                        if (lineconnection[16] == 'SI'):
                                print('Posee conectividad')
                                encontre = True
                                break
                if (encontre == False): print('Connectividad desconocida')
            #if (province.lower() == lineargentina[5].lower()):
                    #break

        # Analizo todas las demas provincias
        for i in range(4, len(datacensus)):
            province = datacensus[i][0]
            argentina_file.seek(1)
            for lineargentina in argentinareader:
                if (province == lineargentina[5]) and (lineargentina[6] == 'admin'):
                    print('Provincia: ' + province + ' Capital: ' + lineargentina[0])
                    encontre = False
                    connection_file.seek(1)
                    for lineconnection in connectionreader:
                        if (lineargentina[0] in lineconnection[2]):
                            if (lineconnection[16] == 'SI'):
                                print('Posee conectividad')
                                encontre = True
                                break
                    if (encontre == False): print('Connectividad desconocida')
                if (province == lineargentina[5]):
                    break