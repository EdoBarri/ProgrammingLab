def sum_csv(file_name):
    # Inizializzo una lista vuota per salvare i valori
    values = []
    risultato = 0
    # Apro e leggo il file, linea per linea
    my_file =open (file_name, 'r')
    for line in my_file:
         # Faccio lo split di ogni riga sulla virgola
        elements = line.split(',')
        # Se NON sto processando l’intestazione...
        if elements[0] != 'Date':
        # Setto la data e il valore
            #date = elements[0]
            value = float(elements[1])  # Convert value to a float
        # Aggiungo alla lista dei valori questo valore
            values.append(value)
        # Sommo i valori
    risultato = sum(values)
    return risultato

#a = sum_csv('prova.csv')
#print("Il risultato è: {}".format(a))
