import csv

def openCsv(filePath):
    try:
        with open(filePath,'r',encoding='iso-2022-jp') as csvfile:

            reader=csv.reader(csvfile)

            s=''
            for row in reader:
                s +=','.join(row)
                s +='\r\n'
                
        return s

    except FileNotFoundError as e:
        print(e)
    except csv.excel as e:
        print(e)
        
