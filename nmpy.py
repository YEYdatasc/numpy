#numpy


import numpy as np

x=np.array([4,5,6,7])
print(x)
print(type(x))
print(x.shape)
print(x.size)
print(x.ndim)
print(x.nbytes)
print(x.dtype)

y=np.array([[1,2,3],[4,5,6]])
print(y)
print(type(y))
print(y.shape)
print(y.size)
print(y.ndim)  # kaç satır ve kaç sütunsa onu gösterir. burda 1 satır 1 stun ile çalıştığı için 2 olarak output aldık.
print(y.nbytes) #hafızadaki alanı gösterir.
print(y.dtype)

#3 boyutlu array oluşturmak
z=np.array([[[1,2],[3,4]],[[1,2],[3,4]]])
print(z.shape)   #çıkrısı 2 adet 2*2 matrix oluştuuğunu anlatır.(2 2 2 )
print(z.ndim)

#veri tipleri-saved(),load() 

x=np.array([3,4.0,5])
print(x)
print(x.dtype)

import numpy as np
x=np.array([3,4.0,5])
print(x)
print(x.dtype)

x=np.array([3,4,5], dtype=np.int)
print(x)
print(x.dtype)

y=np.array([3,4,5], dtype=np.float)
print(y)
print(y.dtype)

z=np.array([3,4,5], dtype=np.complex)
print(z)

x=np.array([1.2,2.7,3.8], dtype= np.int)
print(x)
print(x.dtype)

x=np.array([1,2,3,4], dtype=np.float)
print(x)
print(x.dtype)

x=np.array(x, dtype=complex)
print(x)
print(x.dtype)                     #veri tipini değiştirme 

x=x.astype(np.complex)
print(x)
print(x.dtype)
#yukarıda görüldüüğü gibi astype methodu ile de veri tipinin cinsi değiştirilebilir.

x1=np.array([1,2,3], dtype=int)
x2=np.array([5.2,2.8,4.9], dtype=np.float)
print(x1+x2)
print((x1+x2).dtype)

x=np.sqrt(np.array([-1,9,4], dtype=np.float))
print(x)
print(x.dtype)           # float ile çalışında birinci terim "non" döndü

x=np.sqrt(np.array([-1,9,4], dtype=np.complex))
print(x)
print(x.dtype)           # complex sayı ile yazılınca 1. terim karmaşık sayı olarak output verdi

print(x.real)
print(x.imag)  #gerçek ve sanal kısım ayrı ayrı olarak gösterildi.
#gömülü fonksiyonlarI, ones, zeros  
import numpy as np
x=np.array([3,9,8])
print(x)
print(type(x)) 

#np.zeros ve np.ones

x1= np.zeros(4)
print(x1)

y1= np.ones(4)
print(y1)
print(y1.dtype)

x2=np.zeros((2,3,4), dtype=np.int)     #2 tane 3 satır 4 sütunluk matrix üretir
print(x2)
y2=np.ones((3,2))
print(y2)
#np.full()
x=np.full((2,3),10)
print(x)
print(x.dtype)
y=10.0*np.ones((2,3))
z=10.0+np.zeros((2,3))
print(y)
print(z)
#np.empty()
x=np.empty((2,2))
print(x)
x.fill(3)
print(x)

#np.eye()

x=np.eye(4)  #♦birim matrix oluşturur
print(x)
y=np.eye(5,4)
print(y)

x=np.eye(6)
print(x)
print()
y=np.eye(6, k=1)
print(y)                 #diagonal:çaprazlamasına gelen 1leredenir
print()                  # k=1 diagonali bir birim yukarı, -2 ise iki birim aşağı taşır
z=np.eye(6, k=-2)
print(z)

x=np.identity(5) 
print(x)

#np.diag()

x=np.diag([4,7,11,3])     #listede verilen ifadeleri çaprazlamasına(diagonale) yerleştirir.
print(x)
#np.arange()     [0,10]

x=np.arange(10)
print(x)                #0 dan 10 a kadar(10 dahil değil) 


y=np.arange(4,9)         # 4 den 9'a kadar 9 dahil değil
print(y)

z=np.arange(3,23,4)
print(z)                 # 3 den 23'e kadar 4 attırarak sıralanır.

#np.linspace

x=np.linspace(0,15,10)
print(x)                #tek boyutlu bir array oluşturur, arangeden farkı son terim aralığa dahldir.3. ifade(10) burada kaç terim yazılacagını söyler 

y=np.linspace(0,15,14)     #NŞA'da oluşturulan linspace 50 elemanlıdır, 3. terim girilmediği sürece
print(y)

z=np.linspace(0,15, endpoint=False)
print(z)                             #endpoint komutu ile 15 listeye alınmaz.

#np.reshape()

x=np.arange(20)
print(x)

y=np.reshape(x,(4,5))
print(y)                # 4 satır 5 sütundan oluşan matrix oluşturur. 

x=np.arange(32)
print(x)
y=np.reshape(x,(2,4,4))  #2 tane 4*4 matrix döndürür.
print(y)

x=np.linspace(0,19,20)
print(x)

y=np.reshape(x, (2,10))
print(y)

z=np.linspace(0,19,20).reshape(2,10)
print(z)

## random.random [0,1)
import numpy as  np
x=np.random.random((2,3))   # 2satır 3 sütun matrix üretir.
print(x)
#random.randint
x=np.random.randint(3,12, size=(3,2))
print(x)

#NDArray değiştirmek, insert, append 
x=np.arange(5)
print(x)
print(x[0])
print(x[1])
print(x[2])
print(x[-1])

x[2]=200
print(x)
#x[row,column]
x=np.arange(12).reshape(3,4)
print(x[0,0])
print(x[1,2])
x[0,0]=100   
print(x)
x=np.arange(6)
print(x)
y=np.delete(x,[0,1])  #yeni oluşturulan arrayde  silme işlmei yaptı #tek boyutluda yapıldı 
print(y)
print(x) 
# axis= 0 row- satır, axis=1 column- sütun 
x=np.arange(16).reshape(4,4)
print(x)

x=np.delete(x,1,axis=0)   #• x in 1. indexini silmek istiyorum, satırını silmek isyotrum(yani satır)7
print(x)

x=np.delete(x, [0,2], axis=1)
print(x)                       # 0. ve 2.'ci sütunlarını silmek istiyorum.
#np.append

x=np.arange(5)
print(x)
x=np.append(x,100)   #x'e 100 ü ekledik.
print(x)
x=np.append(x,[200,300]) # x'e 200 ve 300'ü ekledik.
print(x) 

########
x=np.arange(9).reshape(3,3)
print(x)
x=np.append(x,[[100,200,300]], axis=0)
print(x)

x= np.append(x,[[10],[20],[30],[40]], axis=1)
print(x)

#np.insert ara noktalara dizi eklemek için kullanılır. > np.insert(ndarray,index, element,axis)

x=np.arange(5)
print(x)
x=np.insert(x,0,10)   # 10'u 0. indexe koy.
print(x)

x=np.insert(x,2,[10,20])  # 
print(x)

x=np.arange(9).reshape(3,3)
print(x)
x=np.insert(x,1,[100,200,300], axis=0)
print(x)

x=np.insert(x,0,[10,20,30,40],axis=1)
print(x)

#np.stack 

x=np.arange(3)
print(x)

y=np.arange(9).reshape(3,3)
print(y)
z=np.vstack((x,y))   # vstack=vertical stack= dikey iliştirme 
print(z)

t=np.hstack((x,y))   # yatay iliştime horizontal stack
print(t)

#slicing-copy()

ndarray[start:end], ndarray[start],ndarray[start:],ndarray[:end]

import numpy as np
x=np.arange(10)
print(x[2:6])
print(x[4:])

x=np.arange(25).reshape(5,5)
print(x)
y=x[0:3,1:4]     # 0. satırdan 3.satıra; 1. sütundan 4.sütüuna kadar
print(y)
t=x[::]         # x matrixini aynen alır    
print(t)  

v= x[:,3:]       # satırlarının tamamnını al sütunları 3 den sonrasını al 
print(v)       

x=np.arange(9).reshape(3,3)
print(x)

y=x[1:2,0:2]     # x matrixini parçalar 
print(y)     
y[0,0]=100
print(y)
print(x)


x=np.arange(16).reshape(4,4)
print(x)
print()
y=np.copy(x[0:3,1:3])     #copy methodunu kullanarak birbirinden farklı 2 farklı ndarray oluşturduk.
print(y)

print(np.shares_memory(x,y)  # yukarıda oluşturulan 2 farklı nd array memory methodu ile kontrol edildi.(false döndü))
y[0,0]=100
print(y)
print(x) 

z= x[1:2,1:2].copy()
print(z)

x=np.linspace(1,21,11)
print(x)
y=np.array([2,4,7])
print(x[y])           # x arrayının içinden y arayini kullanarak 2. 4. ve 7. elemanlara erişildi.

#başka bir ndarray yardımı ile sliceing yapma 
x=np.arange(25).reshape(5,5)
print(x)
y=np.array([1,2])
print(y) 
print(x[y,:])    # x arrayinin içinden 1. ve 2. indexdeki satırı al ve tüm sütunları al 
print(x[:,y])    # x arayindeki tüm satılarları al, sadece 1. ve 2. sütunu al 

x=np.arange(25).reshape(5,5)
y=np.array([1,2])
z=x[y,:] 
print(z)
z[0,0]=100
print()
print(z)  
print(x)         
#fancy indexing = bir nd arrayin alt kümesine başka bir nd array yardımı ile ulaşılyorsa

#boolean indexing 
x=np.arange(10)
print(x)
print()
print(x[x % 2 ==0])
  
z=x[(x % 2== 0) ]    #ayrı oluşturlan aray orijianl arrayi değiştirmiyor.
print(z)
print(x)

x=np.random.randint(10,size=10)
y=np.random.randint(10,size=10)
print(x)
print(y)
print(x>y)
print(type(x>y))
print((x>y).dtype)  #true ya da false ile dönülen veri tipleri "boolean" olarak değerlendirilir.

x=np.linspace(1,21,11)
print(x)
mask=(x % 3==0)
print(mask)
print(type(mask))

#set operaitons 
x=np.array([2,5,3,6,9])
y=np.array([6,1,8,7,3])

print(np.intersect1d(x,y))   #ortak olan elemanaları çağıran fonksiyon
print(np.setdiff1d(x,y))   #[2 5 9 ]   (x de olup y de olmaanlar)
print(np.setdiff1d(y,x))   #[1 7 8 ]   (y de olup x de olmayanlar)


print(np.union1d(x,y))    # her ikisinde olan elemanları gönderdi

print(np.in1d(x,y))       #x içerisinde olan elemanlar y arrayinin de içinde var mı sırasıyla kontrol ederek true ya da false döndürür

#element-wise, array-wise

x=np.random.randint(1,10,size=(5,))
print(x)
y=np.random.randint(1,10,size=(5,))
print(y)
print(x+y)
print(np.add(x,y))

#istatistik fonksiyonlar,broadcasting

x=np.random.randint(1,10,size=(8,))
print(x)
print(x.mean())
print(np.median(x))
print(x.std())











