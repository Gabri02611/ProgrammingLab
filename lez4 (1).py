class CSVFile:
    def __init__(self, name):
        self.name = name
    def get_data(self):
        values = []
        list = []
        my_file = open(self.name)
        for line in my_file:
            elements = line.split(',')
            if elements[0] != 'Date':
                list = [elements[0] ,elements[1]]
                values = values + [list]
        my_file.close()
        return(values)

#obj= CSVFile('shampoo_sales.csv')
#print(obj.get_data())