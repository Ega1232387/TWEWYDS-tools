import os
import re
from tww_text import dic
from tww_utils import to_hex


#to get all of the font data (symbols, their IDs and lengths)
def unpack(original, tbl):
    with open(original, "rb") as file:
        filesize = os.path.getsize(original)
        with open(tbl, "w", encoding="utf8") as file1:
            for i in range(filesize):
                a = file.read(1)
                numb = int(a.hex(), 16)
                symb = hex(i)[2:].zfill(4).upper()
                symb = "".join(reversed([symb[i:i + 2].upper() for i in range(0, 4, 2)]))
                if symb in dic.keys():
                    file1.write("❄".join([symb, str(numb), dic[symb]]) + "\n")
                else:
                    file1.write("❄".join([symb, str(numb)]) + "\n")

#to pack the font data back
def pack(tbl, final):
    with open(tbl, encoding="utf8") as file:
        with open(final, "wb") as file1:
            f = [i.rstrip("\n") for i in file.readlines()]
            for i in f:
                if "❄" in i:
                    ii = hex(int(i.split("❄")[1]))[2:].zfill(2).upper()
                    file1.write(bytes.fromhex(ii))


#unpack("F:/udav/twewyds/font/in_works/0002/Grp_Font.bin_2.bin_1.bin", "0002.txt")
#unpack("F:/udav/twewyds/font/in_works/0008/Grp_Font.bin_8.bin_1.bin", "0008.txt")


#pack("0002.txt", "Grp_Font.bin_2.bin_1.bin")
#pack("0008.txt", "Grp_Font.bin_8.bin_1.bin")
