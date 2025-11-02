import re
from tww_utils import  reverse_hex

def table_to_nums(file1, file2):
    with open(file1, 'rb') as f:
        data = f.read()
        hexdata = data.hex()
        f.close()

    hx = []
    for i in range(len(hexdata) // 16):
        hexx = hexdata[16 * i:16 * (i + 1)]
        hx.append((int("".join(reverse_hex(hexx[8::])), 16) // 2))

    hx = [str(i) for i in hx]
    print(hx)

    with open(file2, "w") as f:
        f.writelines([f"{i}\n" for i in hx])
        f.close()


def nums_to_table(file1, file2):
    with open(file1, "r") as f:
        hx = [int(i.rstrip("\n")) for i in f.readlines()]
    b = 0
    new_str = ""
    for i in hx:
        a = hex((i) * 2).lstrip("0x").zfill(8)
        bh = hex(b).lstrip("0x").zfill(8)
        b += (i) * 2
        new_str += "".join(reverse_hex(bh))
        new_str += "".join(reverse_hex(a))

    nstr = bytes.fromhex(new_str)
    with open(file2, "wb") as f1:
        f1.write(nstr)


if __name__ == '__main__':
    print("0 - распаковать таблицу, 1 - запаковать")
    answ = int(input())
    if answ == 0:
        print("Введите имя таблицы")
        file1 = input()
        print("Введите имя итогового файла")
        file2 = input()
        table_to_nums(file1, file2)
    elif answ == 1:
        print("Введите имя файла")
        file1 = input()
        print("Введите имя итоговой таблицы")
        file2 = input()
        nums_to_table(file1, file2)
