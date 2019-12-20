from enigma import Enigma
from reflector import Reflector
from rotor import Rotor
import sys
from config import ROTORS_COUNT, MAX_LEN


def main():
    try:
        file = open(sys.argv[1], "rb")
    except IndexError:
        print("Set file as argv[1]")
        return

    rotors = []
    for _ in range(ROTORS_COUNT):
        rotors.append(Rotor())
        
    enigma = Enigma(rotors, Reflector())
    print("*********")
    print(enigma)
    print("*********")
    print("*********")
    print()
    print()

    enc_file_name = "enc_" + sys.argv[1] 
    dec_file_name = "dec_" + sys.argv[1] 
    enc_file = open(enc_file_name, "wb")

    while True:
        # считывается MAX_LEN символов из файла
        buf = file.read(MAX_LEN)
        if(not len(buf)):
            file.close()
            enc_file.close()
            break
        else:
            enc_str = enigma.encryptStr(buf)
            enc_file.write(enc_str)


    enc_file = open(enc_file_name, "rb")    
    dec_file = open(dec_file_name, "wb")
    
    enigma.reset()
    while True:
        buf = enc_file.read(MAX_LEN)
        if(not len(buf)):
            enc_file.close()
            dec_file.close()
            break
        else:
            dec_str = enigma.encryptStr(buf)
            dec_file.write(dec_str)
    
if __name__ == "__main__":
    main()