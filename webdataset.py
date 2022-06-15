import json, os
import shutil
import tarfile

def json_decode(number):
    file_es = './Pictogramas/indexpictograms.es.json'
    file_en = "./Pictogramas/indexpictograms.en.json"
    jsonfile_es = open(file_es,'r', encoding='utf-8')
    json_data_es = json.load(jsonfile_es)
    jsonfile_en = open(file_en,'r', encoding='utf-8')
    json_data_en = json.load(jsonfile_en)
    print(json_data_es[number])
    print(json_data_en[number])
    file_name = "my_images/"+number+".json"
    data ={}
    #data[number] = json_data_es[number]
    data[number] = json_data_en[number]
    with open(file_name, 'w') as file:
        json.dump(data, file)
        
 
        
def getNamePicto():
    i = 0
    data = []
    data_path ="./Pictogramas/pictogramas/"
    for r, d, f in os.walk(data_path):
        for file in f:
            if '.png' in file:                
                json_decode(file.split("_")[0])                
                shutil.copyfile(data_path+file, "my_images/"+file.split("_")[0]+".png")
                i = i+1
    print("Count file: ",i)
        
        
if __name__ == '__main__':                 
   #json_decode("9854")   
   getNamePicto()
     
   #python -m tarfile -c webdataset.tar .\my_images\
   