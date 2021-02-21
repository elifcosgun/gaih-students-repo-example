#En başta teker teker yazmamak için birden yüze asal sayıları hesaplayan minik bir kod yazdım.
#Kod iç içe for döngüsüyle kontrol ettiği sayıyı birden kendisine kadar bölüp kalanına bakıyor
#Kalan hiçbir zaman sıfır olmuyorsa asal sayı listesine ekliyor
#Aşağıda da sıfırdan listenin uzunluğunun bir eksiği arasında random bir değer alıp bu değerin
#indexindeki değeri iki boyutlu arraye atıyor

#Question 1
import random

myList = []
for x in range(100):
    control = False
    for y in range(2, x + 1):
        if y == x:  #Sayı kendine kadar ulaşıp breaklenmediyse asaldır
            myList.append(x)
            break
        if x % y == 0:  #asal sayı değildir
            #bir sonraki sayıyı kontrole geçer
            break



ran = random.randint(1,len(myList))
matList = [[None for x in range(3)] for x in range(3)]
for i in range(3):
  for j in range (3):
      ran = random.randint(0,len(myList)-1)
      matList[i][j] = myList[ran]

print(matList)
