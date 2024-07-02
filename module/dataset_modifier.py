import csv


def airport_dataset(route, custom_route):
    '''This function returns a copy of the "ar-airports.csv" file
    and add a new column with the elevation of each airport'''
    with open(route, encoding='utf-8') as airport_file, open(custom_route, 'w', encoding='utf-8', newline='') as custom_file:
        airport_reader = csv.reader(airport_file)
        writer = csv.writer(custom_file)

        header = next(airport_reader)
        header.append('elevation_name')
        writer.writerow(header)

        elevation = 6

        for line in airport_reader:
            if line[elevation]:
                if int(line[elevation]) <= 131:
                    line.append('bajo')
                elif 131 < int(line[elevation]) <= 903: 
                    line.append('medio')
                else:
                    line.append('alto')
            else:
                line.append('-')  
            writer.writerow(line)
            
    return custom_file


def airport_with_provs_dataset(route, custom_route):
    '''This function returns a copy of the new custom csv file "ar-airports.csv"
    and add a new column with the name of the province of each airport'''
    with open(custom_route, encoding='utf-8') as custom_file: 
        reader = csv.reader(custom_file)
        data = list(reader)    

    data[0].append('prov_name')

    municipality = 13
    city = 0
    admin_name = 5
    region_name = 10

    with open(route, encoding='utf-8') as argentina_file:
        argentina_reader = csv.reader(argentina_file)
        for i in range(1, len(data)):
            city_name = data[i][municipality] 
            argentina_file.seek(0)
            found = False
            for argentina_row in argentina_reader:
                if argentina_row[city] == city_name:
                    province_name = argentina_row[admin_name]  
                    data[i].append(province_name)
                    found = True
                    break
            if not found:   
                data[i].append(data[i][region_name])

    with open(custom_route, 'w', encoding='utf-8', newline='') as custom_file:
        writer = csv.writer(custom_file)
        writer.writerows(data)      

    return custom_file


def internet_dataset(route, custom_route):
    '''This function returns a copy of the csv file "Conectividadd_Internet.csv",
    with a two new implementations. If there is a character = "--" this function put the
    value "NO" and add a new column called "posee_conectividad". If there is at least
    one element with the value "SI" this function put the value "SI", if not put 
    the value = "NO" '''
    with open(route, encoding='utf-8') as connection_file, open(custom_route, 'w', encoding='utf-8', newline='') as custom_file:
        connection_reader = csv.reader(connection_file)
        writer = csv.writer(custom_file)

        header = next(connection_reader)
        header.append('posee_conectividad')
        writer.writerow(header)

        for line in connection_reader: ## tipo lista
            if 'SI' in line[4:13]:
                line.append('SI')
            else:
                line.append('NO')
            line = ['NO' if element == '--' else element for element in line]
            writer.writerow(line)
    
    return custom_file


def decimal_degrees_converter(campos): # ejercicio 3
    ''' This function receives a list of 2 elements, the first one is the lattitude and the second one is the longitud. After clean
     the unuseful characters and gets the useful numbers, does some operations to convert them to decimal degrees. Returns a list of
      2 elements also, in the same order, but now converted to DD. '''
    gms1 = campos[0]
    gms2 = campos[1]
    gms1 = gms1.replace('°',' ').replace('\'',' ').replace('Â','').replace('"',' ').split()
    gms2 = gms2.replace('°',' ').replace('\'',' ').replace('Â','').replace('"',' ').split()

    dd1 = (int(gms1[0]) + (int(gms1[1])/60) + int(gms1[2])/3600)
    dd2 = (int(gms2[0]) + (int(gms2[1])/60) + int(gms2[2])/3600)
    if (gms1[3] == 'S'): dd1 = '-' + str(dd1)
    if (gms2[3] == 'O'): dd2 = '-' + str(dd2)
    campos[0] = dd1
    campos[1] = dd2
    return campos


def lakes_dataset(route, custom_route): 
    ''' This function returns a copy of the file "lagos_arg.csv" but with some modifications. New columns, which indicate the lattitud
    and longitud in DMS(Degrees, Minutes and Seconds) and DD(Decimal Degrees) are added, and the "Coordenadas" one is replaced.
    Also add a new column which indicate the size of the lake in km².
    Lakes with a surface area less than or equal to 17 km² will be classified as "chico".
    Lakes with a surface area greater than 17 km² and less than or equal to 59 km² will be classified as "medio".
    Lakes with a surface area greater than 59 km² will be classified as "grande". '''
    with open(route) as lakes_file, open(custom_route, 'w', newline='') as custom_file:
        lakes_reader = csv.reader(lakes_file)
        writer = csv.writer(custom_file)

        header = next(lakes_reader)
        header[5] = 'Latitud GMS'
        header = header + ['Longitud GMS','Latitud GD','Longitud GD','Sup TamaÃ±o']
        writer.writerow(header)

        surface = 2
        coordinates = 5
        for line in lakes_reader:
        
            fields = line[coordinates].split()
            line[5] = fields[0]
            line = line + [fields[1]]

            fields = decimal_degrees_converter(fields)

            line = line + [fields[0],fields[1]]
            #-----------------------------------------
            if line[surface]:
                if int(line[surface]) <= 17:
                    line.append('chico')
                elif 17 < int(line[surface]) <= 59: 
                    line.append('medio')
                else:
                    line.append('grande')
            else:
                line.append('-')  

            writer.writerow(line) 

    return custom_file


def census_dataset(route, custom_route):
    ''' This function returns a copy of the file "c2022_tp_c_resumen_adaptado.csv" but with some modifications.
    The string "///" and the character "-" are replaced by '0'. Also, a new column is added in order to indicate
    the percentage of homeless people.'''
    
    with open(route, encoding='utf-8') as poblation_file, open(custom_route, 'w', encoding='utf-8', newline='') as custom_file:
        poblation_reader = csv.reader(poblation_file)
        writer = csv.writer(custom_file)

        header = next(poblation_reader)
        header.append('Porcentaje de población en situación de calle')
        writer.writerow(header)

        homeless_people = 4
        people = 1

        for line in poblation_reader:
            line = ['0' if element == '///' or element == '-' else element for element in line]
        
            line.append('% '+str(int(line[homeless_people])/int(line[people])*100))
            writer.writerow(line)
            
    return custom_file