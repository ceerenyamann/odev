import re
sifrelenendizi = []
kelimeler= []
bulunanlar=[]
input= input ("Lütfen şifrelenmiş metni gir :")
def sifrecoz(message): 
    encrypted = " "
    for i in range(29):
        
        for char in message:
            value = ord(char) + 1
            valuea = value %123
            if (valuea <= 0):
                valuea= 84
                encrypted += chr(valuea)
            elif(valuea == 42):
                encrypted += chr(41)
            else:
                encrypted+= chr(valuea)
                
        message = encrypted
        sifrelenendizi.append(encrypted)
        encrypted= " "
        
def kelime_cagir(dosya_adi):
    with open(dosya_adi, 'r', encoding= 'utf-8') as input_file:
        dosya= input_file.read()
        kelime_listesi = dosya.split()
        index = 0
        while index <= 78524:
            kelimeler. append(kelime_listesi[index])
            index += 1
        return kelimeler
    
sifrecoz(input)
kelime_cagir()
for i in range(len (kelimeler)):
    for j in range (len(sifrelenendizi[j]))
    x= re.split("\s", sifrelenendizi[j])
    
    for k in range(len(x)):
        if (kelimeler[i]== x[k]):
            bulunanlar.append(kelimeler[i])
print("kırılan şifreniz :", bulunanlar)
            
        
        