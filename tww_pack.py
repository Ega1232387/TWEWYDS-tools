import os
from tww_utils import to_hex, from_hex


def unpack(name, res_dir):
    if os.path.isdir(res_dir):
        pass
    else:
        os.mkdir(res_dir)
    file = open(name, "rb")
    file_name = name.split("/")[-1]
    header = to_hex(file.read(32))
    file_count = from_hex(header[4:8])
    file.seek(32)
    file_data = []
    for i in range(file_count):
        offset = to_hex(file.read(4))
        size = to_hex(file.read(4))
        print(offset, size)
        file_data.append([from_hex(offset), from_hex(size)])

    print(file_data)

    for i in range(len(file_data)):
        data = file_data[i]
        file.seek(32 + data[0])
        with open(res_dir + file_name + "_" + str(i) + ".bin", "wb") as file1:
            file1.write(file.read(data[1]))


def pack(directory):
    dire = os.scandir(directory)
    names = [i.name for i in dire]
    names = sorted(names, key=lambda x: int(x.split(".")[1][4:]))
    point = len(names) * 8
    index = []
    data = []
    for i in range(len(names)):
        with open(directory + "/" + names[i], "rb") as file:
            size = os.stat(directory + "/" + names[i]).st_size
            f = file.read()
            fhex = to_hex(f)
            if size % 32 != 0:
                fhex += ["00"] * (((size // 32) + 1) * 32 - size)
            data += fhex
            if size == 0:
                index += ["00"] * 8
            else:
                offs_1 = hex(point)[2:].zfill(8).upper()
                offs_2 = [offs_1[i:i + 2].upper() for i in range(0, 4 * 2, 2)]
                size_1 = hex(size)[2:].zfill(8).upper()
                size_2 = [size_1[i:i + 2].upper() for i in range(0, 4 * 2, 2)]
                offs_2.reverse()
                size_2.reverse()
                index += offs_2 + size_2
                point += len(fhex)

    header1 = ["70", "61", "63", "6B"]
    header2_1 = hex(len(names))[2:].zfill(8).upper()
    header2_2 = [header2_1[i:i + 2].upper() for i in range(0, 4 * 2, 2)]
    header2_2.reverse()
    header3_1 = hex(len(data))[2:].zfill(48).upper()
    header3_2 = [header3_1[i:i + 2].upper() for i in range(0, 24 * 2, 2)]
    header3_2.reverse()
    header = header1 + header2_2 + header3_2
    print(header[0:16])
    print(header[16:])
    with open(directory + ".bin", "wb") as file1:
        file1.write(bytes.fromhex("".join(header + index + data)))

#dir = "F:/udav/twewyds/root2/Apl_Fuk/"
#for i in os.scandir(dir + "in"):
#    os.mkdir(dir + "out/" + i.name)
#    unpack(i.name, dir + "in/", dir + "out/" + i.name + "/")

#pack(r"F:\udav\twewyds\font\out\Grp_Font.bin_8.bin")
#pack(r"F:\udav\twewyds\font\0002")
#pack(r"F:\udav\twewyds\font\0006")
#pack(r"F:\udav\twewyds\font\0008")
#pack(r"F:\udav\twewyds\font\0009")
#pack(r"F:\udav\twewyds\font\itog")

#unpack("F:/udav/twewyds/font/Grp_Font.bin", "F:/udav/twewyds/font/orig/")
#unpack("F:/udav/twewyds/font/in_works/Grp_Font.bin_2.bin", "F:/udav/twewyds/font/in_works/0002/")
#unpack("F:/udav/twewyds/font/in_works/Grp_Font.bin_6.bin", "F:/udav/twewyds/font/in_works/0006/")
#unpack("F:/udav/twewyds/font/in_works/Grp_Font.bin_8.bin", "F:/udav/twewyds/font/in_works/0008/")
#unpack("F:/udav/twewyds/font/in_works/Grp_Font.bin_9.bin", "F:/udav/twewyds/font/in_works/0009/")
#pack("F:/udav/twewyds/font/in_works/0002")
#pack("F:/udav/twewyds/font/in_works/0006")
#pack("F:/udav/twewyds/font/in_works/0008")
#pack("F:/udav/twewyds/font/in_works/0009")
#pack("F:/udav/twewyds/font/in_works/res")

#pack(r"F:\desktop\amog\Grp_Title.bin")

#unpack(r"F:/udav/twewyds/Tutorial/Grp_Tutorial.bin/Grp_Tutorial.bin_3.bin", r"F:/udav/twewyds/Tutorial/0003/")
#pack("F:/udav/twewyds/Tutorial/0003")
#pack("F:/udav/twewyds/Tutorial/Grp_Tutorial")
#pack("F:/udav/twewyds/menu_pins/out/MenuTop_OBD01")