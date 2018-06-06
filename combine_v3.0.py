import os
import ffmpy

def get_target():
    global target
    target  = input("Target dir: ") + "\\"

def get_dir():
    return os.path.dirname(os.path.abspath(__file__))+"\\"

def get_path():
    return os.listdir(get_dir())

def get_name(path):
    file = open(get_dir()+path+"\\desktop.ini")
    name_file = file.read()
    name_1 = name_file.split("=")
    name_2 = name_1[1].split("[")
    name_3 = name_2[0].split("\n")
    name_4 = name_3[0] + ".mp4\""
    vid_name = name_4.replace(":", "：")
    print(vid_name)
    return vid_name

def get_txt(path):
    get_file_name = open(get_dir()+path+"\\1\\ff.txt", "w")
    files = os.listdir(get_dir()+path+"\\1")
    for name in files:
        if os.path.splitext(name)[1] == '.flv':
            get_file_name.write("file '"+ get_dir() + path +"\\1\\" + name+"'"+"\n")

def create_txt():
    folders_in_bi =  get_path()
    for file in folders_in_bi:
        if "." not in file:
            get_txt(file)

def create_bat():
    folders_in_bi = get_path()
    for path in folders_in_bi:
        if "." not in path:
            create = open( get_dir() +path+"\\1\\concat.bat", "w")
            create.write("ffmpeg -f concat -safe 0 -i \""+ get_dir() + path +"\\1\\ff.txt\" -c copy \""+ target + get_name(path)+"\n")
            create.write("echo 按任意键结束\npause\nexit\n ")

def create_bat2():
    folders_in_bi = get_path()
    create = open(get_dir() + "concat.bat", "w")
    check = open(target + "check.txt", "a+")
    for path in folders_in_bi:
        if "." not in path and check_complete(path):
            create.write("ffmpeg -f concat -safe 0 -i \"" +  get_dir() +path+"\\1\\ff.txt\" -c copy \"" +  target + get_name(path)+"\n")
            check.write(get_name(path)+"\n")

    create.write("echo 按任意键结束\npause\nexit\n ")

def check_complete(path):
    check = open( target +"check.txt", "r")
    L = check.read().split("\n")
    if get_name(path) not in L:
        return True
    else:
        return False

def open_bat():
    os.system("C:\Windows\System32\cmd.exe /c " + get_dir() + "concat.bat")



get_target()
create_txt()
create_bat2()
open_bat()
