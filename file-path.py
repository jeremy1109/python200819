import os.path
if os.path.isfile("y.txt"):
    print("存在")
    file=open("y.txt","a")
    file.write("檔案就是存在")
    file.close()
else:
    print("不存在") 
    file=open("y.txt","w")
    file.write("這是新的檔案")
    file.close()