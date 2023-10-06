# tworzenie pliku CSV

import chardet
#pip instal chardet - wydanie komendy w terminalu i instaluje pakiet chardet

file_path = 'test.log'

with open(file_path, 'rb') as file: # musi być RB
    raw_data = file.read()

print(raw_data) # nie mamy polskich liter bo brak kodowania w odczycie

result = chardet.detect(raw_data)
print(result) # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

kodowanie = result['encoding']
confidence = result['confidence']
print(kodowanie, confidence) # utf-8 0.99 - pewność wykrycia kodowania





