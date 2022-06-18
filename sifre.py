from email import message
import keyword


alphabet =['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö'
         'p', 'q', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z']
#alfabeyi ingilizce türkçe karakterde sıralayarak bir diziye soktum 

def encryptmessage(message, key):     #şifre mesajı için boş string yazdım
    encrypted_message = " "
    
say = 0 #index değeri döndürmek için sayaç tanımladım

  str(keyword)
  for i in message: #mesaj içerisindeki harfleri if döngüsüne soktum
      if i not in alphabet :
      else:
          encrypted_message+= alphabet [(alphabet.index(i) + alphabet.index(keyword[sayac])) % len(alphabet)]
          
          sayac += 1
          
          if( sayac == len(keyword)):
              
              sayac=0 #karakter aşım hatası olmasın diye sayacı, anahtarı sıfıra eşitledm
              
              print(" sifrelenecek mesaj:" , encryptmessage)
              
              encryptmessage( "merhaba ceren0640at" , "emek")d
              
              def decryptmessage(message,key):
                  decrypted_message =" "
                  sayac= 0
                  str(key)
                  for i in message:
                      if i in message:
                          if i not in alphabet:
                              decrypted_message +=i
                     else:
                         decrypted_message += alphabet[alphabet.index(i) - alphabet.index(keyword[sayac]) % len(alphabet)]
                         
                    sayac+=1
                    if (sayac==len(key)):
                        
                            sayac=0
                            print(" şifresi kırılacak mesaj: " decryteped_message)
              
                            decryptmessage("merhaba nerec0460", "emek")
                        
      
