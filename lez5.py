class CSVFile:
    def __init__(self, name):
        self.name = name
    def get_data(self):
        values = []
        list = []
        try:
            my_file = open(self.name)
        except Exception as e:
            print("Errore: Il file che hai provato ad aprire non è valido")
            print(" Ho ricevuto il seguente messaggio di errore: {}", format(e))
        for line in my_file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip() 
            if elements[0] != 'Date':
                list = [elements[0] ,elements[1]]
                values = values + [list]
        my_file.close()
        return(values)
class NumericalCSVFile(CSVFile):
    def get_data(self):
        stringa = super().get_data()
        values = []
        for string_row in stringa:
            num_row = []
            for i,element in enumerate(string_row):
                if i == 0:
                    num_row.append(element)
                else:
                    try: 
                        num_row.append(float(element))
                    except Exception as e:
                        print("Errore nella conversione del valore {} a numerico", element)
                        break
            if len(num_row) == len(string_row):
                values.append(num_row)
        return values
                        
                
        
    
#obj= CSVFile('shampoo_sales.txt')
#print(obj.get_data())