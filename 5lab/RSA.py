from algoritms import Algorithms
import struct
import sys

class RSA():

    def __init__(self, bit_count=512):
        
        self.bit_count = bit_count
        self.e , self.d, self.n = self.generate_keys()


    # e - открытый ключ
    # d - закрытый ключ
    # n - модуль
    def generate_keys(self):
        
        p = Algorithms.simple_number(self.bit_count)
        q = Algorithms.simple_number(self.bit_count)
        n = p * q
        phi = (p - 1) * (q - 1)
        e, d = Algorithms.find_e_d(phi)


        #print("p - выбранное простое число №1:", p)
        #print("q - выбранное простое число №2:", q)
        #print("n = p * q:", n)
        #print("Функция Эйлера: phi = (p1 - 1) * (p2 - 1) = ", phi)
        #print("e - показатель степени, нечетное число, без общих делителей с phi:", e)
        #print("d - закрытый ключ:", d)

        #print("size n:", sys.getsizeof(n), "bytes")
        #print("e*d mod phi:", e*d % phi)
        publicKey = n
        privateKey = d
        RSA.writeKeys(publicKey, privateKey)
        return e, d, n

    def writeKeys(public, private):
        with open('public.pem', "wb") as pub:
            pub.write(public.save_pkcs1('PEM'))

        with open('private.pem', "wb") as pub:
            pub.write(private.save_pkcs1('PEM'))

    def encrypt(self, filename_read, filename_write):
        
        with open(filename_read, "rb") as fr, open(filename_write, "w") as fw:
            data = fr.read()
            for item in data:
                print(item)
                new_item = pow(item, self.e, self.n)
                fw.write(str(new_item) + "\n") 

    def decrypt(self, filename_read, filename_write):
        with open(filename_read, "r") as fr, open(filename_write, "wb") as fw:
            
            line = fr.readline()
            while line:
                num = int(line)
                byte = pow(num, self.d, self.n)
                fw.write(struct.pack('B', byte)) 
                line = fr.readline()

