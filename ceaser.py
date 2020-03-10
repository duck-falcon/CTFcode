import copy
import sys

args = sys.argv

#右回り変換
def ceaser(filepath,n,filew = "ceaser.txt",match = ""):
    alist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    Alist = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    temp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    Temp = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    i = n
    for v in alist:
        temp[i % 26] = v
        i += 1
    i = n
    for V in Alist:
        Temp[i % 26] = V
        i += 1

    with open(filepath) as f:
        contents = f.read()
        dict = {}
        Dict = {}
        i = 0
        for v in alist:
            dict[v] = temp[i]
            i = i + 1

        i = 0
        for V in Alist:
            Dict[V] = Temp[i]
            i = i + 1
        contents = contents.translate(contents.maketrans(dict))
        contents = contents.translate(contents.maketrans(Dict))
        if match in contents:
            with open(filew, mode='a') as F:
                F.write(contents)
                print("write success: " + str(n) + "rot ")
        else:print("no match")

a = len(args)

if a == 4:
	for i in range(26):
		ceaser(args[1],i,args[2],args[3])
else:
	print("please: <input_file_path> <output_file_path> <match_str>")
