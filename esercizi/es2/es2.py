class CSVFile ():
    def __init__(self, name):
        self.name= name

    def __repr__(self):
        return 'File "{}"'.format(self.name)

    def get_data ():
        # Inizializzo una lista vuota per salvare i valori
        dates = []
        values = []
        # Apro e leggo il file, linea per linea
        my_file = open('name', 'r')
        for line in my_file:
            # Faccio lo split di ogni riga sulla virgola
            elements = line.split(',')
            # Setto la data e il valore
            date = elements[0]
            value = elements[1]
            # Aggiungo alla lista dei valori questo valore
            dates.append (date)
            values.append(value)
            print ('{}'.format(values))
        my_file.close()
        return values

csv_file= CSVFile('prova2.csv')
print (csv_file.get_data())