import os
import ffmpy

def get_path():
    return os.listdir("E:\\Bilibili\\")

def get_name(path):
    file = open("E:\\Bilibili\\"+path+"\\desktop.ini")
    name_file = file.read()
    name_1 = name_file.split("=")
    name_2 = name_1[1].split("[")
    name_3 = name_2[0].split("\n")
    name_4 = name_3[0] + ".mp4\""
    vid_name = name_4.replace(":", "：")
    print(vid_name)
    return vid_name

def get_txt(path):
    get_file_name = open("E:\\Bilibili\\"+path+"\\1\\ff.txt", "w")
    files = os.listdir("E:\\Bilibili\\"+path+"\\1")
    for name in files:
        if os.path.splitext(name)[1] == '.flv':
            get_file_name.write("file 'E:\\Bilibili\\" + path +"\\1\\" + name+"'"+"\n")

def create_txt():
    folders_in_bi =  get_path()
    for file in folders_in_bi:
        if "." not in file:
            get_txt(file)

def create_bat():
    folders_in_bi = get_path()
    for path in folders_in_bi:
        if "." not in path:
            create = open("E:\\Bilibili\\"+path+"\\1\\concat.bat", "w")
            create.write("ffmpeg -f concat -safe 0 -i \"E:\\Bilibili\\"+path+"\\1\\ff.txt\" -c copy \"E:\\Bilibili2\\" + get_name(path)+"\n")
            create.write("echo 按任意键结束\npause\nexit\n ")

def create_bat2():
    folders_in_bi = get_path()
    create = open("E:\\Bilibili\\concat.bat", "w")
    check = open("E:\\Bilibili2\\check.txt", "a+")
    for path in folders_in_bi:
        if "." not in path and get_name(path) not in check:
            create.write("ffmpeg -f concat -safe 0 -i \"E:\\Bilibili\\"+path+"\\1\\ff.txt\" -c copy \"E:\\Bilibili2\\" + get_name(path)+"\n")
            check.write(get_name(path)+"\n")
    create.write("echo 按任意键结束\npause\nexit\n ")

#def check_complete:






create_txt()
create_bat2()
