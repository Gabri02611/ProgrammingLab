class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name
    def get_data(self):
        values = []
        list = []
        try:
            my_file = open(self.name)
        except:
            raise ExamException('Errore: file non leggibile')
        for line in my_file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip() 
            if elements[0] != 'date':
                list = [elements[0] ,elements[1]]
                values = values + [list]
        my_file.close()
        i = 0 
        for elem in values:
            totale = elem[0].split(',')
            data = totale[0].split('-')
            try:
                annata = int(data[0])
            except:
                raise ExamException("Errore: timestamp dell'anno non valido")
            if i == 0:
                anno = data[0]
            mese = 0
            i = i +1
            if anno != data[0]:
                raise ExamException("Errore: timestamp non ordinato")
            if i < 10 :
                mese = data[1].strip('0')
            else:
                mese = data[1]
            try:
                mese = int(mese)
            except:
                raise ExamException("Errore: timestamp del mese non valido")
            if i != mese :
                raise ExamException("Errore: timestamp non ordinato")
            if i == 12:
                i=0
        return(values)
def detect_similar_monthly_variations(time_series, years):
    try:
        anno1 = int(years[0])
    except:
        raise ExamException("Errore il valore ", years[0], "non è valido")
    try:
        anno2 = int(years[1])
    except:
        raise ExamException("Errore il valore ", years[1], "non è valido")
    check1 = False
    check2 = False
    for elem in time_series:
        val = elem[0].split('-')
        anno = int(val[0])
        if(years[0] == int(val[0])):
            check1 = True
        if (years[1] == int(val[0])):
            check2 = True
    if (check1 == False):
        raise ExamException('Errore: la seguente data non è presente nel file: {}', format(years[0]))
    if (check2 == False):
        raise ExamException('Errore: la seguente data non è presente nel file: {}', years[1])
    if (abs(years[0] - years[1]) != 1):
        raise ExamException("Errore: le annate non sono consecutive ")
    anno1 = years[0]
    anno2 = years[1]
    #print("anno1:" ,anno1)
    #print("anno2:", anno2)
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    for elem in time_series:
        valori = elem[0].split('-')
        try:
            valint = int(elem[1])
        except Exception as e:
            print("Errore: non è possibile trasformare in intero il seguente valore: ", elem[1])
            print("Ho ricevuto il seguente messaggio d'errore: ", format(e))
        #print(valori[0])
            valint = False
        if anno1 == int(valori[0]):
            lista1.append(valint)
        if anno2 == int(valori[0]):
            lista2.append(valint)
    for i in range (0, len(lista1)-1):
        if lista1[i] == False:
            lista3.append(lista1[i])
        else:
            lista3.append(abs(lista1[i]-lista1[i+1]))
    for i in range (0, len(lista2)-1):
        if lista2[i] == False:
            lista4.append(lista2[i])
        else:
            lista4.append(abs(lista2[i]-lista2[i+1]))
    for i in range(0, 11):
        check  = False
        if(abs(lista3[i] - lista4[i]) <= 2):
            check = True
            lista5.append(check)
        else:
            check = False
            lista5.append(check)
    return(lista5)
class ExamException(Exception):
    pass

