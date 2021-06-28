
def ordenamiento(Palabra):
 alfabeto2 = {
      1:"A", 2:"Á", 3:"a", 4:"á",
     5:"B", 6:"b",
    7:"C", 8:"c",
    9:"D", 10:"d",
    11:"E", 12:"É", 13:"e", 14:"é",
    15:"F", 16:"f",
    17:"G", 18:"g",
    19:"H", 20:"h",
    21:"I", 22:"Í", 23:"i", 24:"í",
    25:"J", 26:"j",
    27:"K", 28:"k",
    29:"L", 30:"l",
    31:"M", 32:"m",
    33:"N", 34:"n",
    35:"Ñ", 36:"ñ",
    37:"O", 38:"Ó", 39:"o", 40:"ó",
    41:"P", 42:"p",
    43:"Q", 44:"q",
    45:"R", 46:"r",
    47:"S", 48:"s",
    49:"T", 50:"t",
    51:"U", 52:"Ú", 53:"u", 54:"ú",
    55:"V", 56:"v",
    57:"W", 58:"w",
    59:"X", 60:"x",
    61:"Y", 62:"y",
    63:"Z", 64:"z"}
 alfabeto = {
    "A":1, "Á":2, "a":3, "á":4,
    "B":5, "b":6,
    "C":7, "c":8,
    "D":9, "d":10,
    "E":11, "É":12, "e":13, "é":14,
    "F":15, "f":16,
    "G":17, "g":18,
    "H":19, "h":20,
    "I":21, "Í":22, "i":23, "í":24,
    "J":25, "j":26,
    "K":27, "k":28,
    "L":29, "l":30,
    "M":31, "m":32,
    "N":33, "n":34,
    "Ñ":35, "ñ":36,
    "O":37, "Ó":38, "o":39, "ó":40,
    "P":41, "p":42,
    "Q":43, "q":44,
    "R":45, "r":46,
    "S":47, "s":48,
    "T":49, "t":50,
    "U":51, "Ú":52, "u":53, "ú":54,
    "V":55, "v":56,
    "W":57, "w":58,
    "X":59, "x":60,
    "Y":61, "y":62,
    "Z":63, "z":64}

 Serial = []
 orden2 = []
 for caracter in Palabra:
           Serial.append(alfabeto[caracter])
           orden = sorted(Serial)
           
 for i in range(1,len(Palabra)+1):
         orden2.append(alfabeto2[orden[i-1]])
 return orden2

 

 
                    

datos_crudos = input('Ingrese las palabras separadas por espacio : ')
Arreglo = [d for d in datos_crudos.split()]
print(Arreglo)
index = list(range(len(Arreglo)))

for i in index: 
  print("Las letras de la palabra: ",Arreglo[i], " en orden alfabetico es el siguiente: ", ordenamiento(Arreglo[i]))
