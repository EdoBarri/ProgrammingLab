class ExamException(Exception):
    pass

class CSVFile:

    def __init__(self, name):

        # Setto il nome del file
        self.name = name


    def get_data(self):
        # Provo ad aprire il file e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False


        if not self.can_read:
            raise ExamException('File inesistente o illeggibile')



        else:
            # Inizializzo una lista vuota per salvare tutti i dati
            data = []

            # Apro il file
            my_file = open(self.name, 'r')

            # Leggo il file linea per linea
            for line in my_file:

                # Faccio lo split di ogni linea sulla virgola
                elements = line.split(',')

                # Posso anche pulire il carattere di newline
                # dall'ultimo elemento con la funzione strip():
                elements[-1] = elements[-1].strip()

                # p.s. in realta' strip() toglie anche gli spazi
                # bianchi all'inizio e alla fine di una stringa.

                # Se NON sto processando l'intestazione...
                if elements[0] != 'date':

                    # Aggiungo alla lista gli elementi di questa linea
                    data.append(elements)

            # Chiudo il file
            my_file.close()

            # Quando ho processato tutte le righe, ritorno i dati
            return data

class CSVTimeSeriesFile(CSVFile):
    def get_data(self):

        raw_data = super().get_data()

        if raw_data is None:

            return None



        time_series_data = []

        last_date = None

        dates_seen = set()



        for item in raw_data:

            try:

                date, passengers = item[0], int(item[1])
                year, month = date.split('-')

                if int(year)<1949 or int(year)>1960 or int(month)<=0 or int(month)>12:
                    continue

                if int(passengers) < 0:

                    continue


                if date in dates_seen:

                    raise ExamException('Date duplicate')

                dates_seen.add(date)



                if last_date and date <= last_date:

                    raise ExamException('Date non ordinate')

                last_date = date



                time_series_data.append([date, passengers])

            except ValueError:

                continue

            except IndexError:

                continue

        
        return time_series_data


def compute_increments(time_series, first_year, last_year):
    if not time_series:
        raise ExamException("Errore, lista valori vuota")
    # Verifica che first_year e last_year siano presenti nei dati
    years = {data[0][:4] for data in time_series}
    if first_year not in years or last_year not in years:
        raise ExamException("Estremi dell'intervallo non validi")
    # Dizionario per memorizzare la media dei passeggeri per ogni anno
    yearly_average = {}

    # Calcolo la media dei passeggeri per ogni anno
    for data in time_series:
        year = data[0][:4]
        if year < first_year or year > last_year:
            continue
        if year not in yearly_average:
            yearly_average[year] = []
        yearly_average[year].append(data[1])

    # Calcolo delle medie
    for year in yearly_average:
        yearly_average[year] = sum(yearly_average[year]) / len(yearly_average[year])

    ## Calcolo degli incrementi
    increments = {}
    sorted_years = sorted(yearly_average.keys())
    for i in range(len(sorted_years) - 1):
        year = sorted_years[i]
        next_year = sorted_years[i + 1]
        if year in yearly_average and next_year in yearly_average:
            increments[f"{year}-{next_year}"] = round(yearly_average[next_year] - yearly_average[year], 1)

    return increments