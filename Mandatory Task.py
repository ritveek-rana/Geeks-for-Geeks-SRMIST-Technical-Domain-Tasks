import googletrans as gt
trans=gt.Translator()
print("This program assumes that the source and destination text files are in the same directory")
print("Note: This program will work only with text files")
d1=input("Enter the name of the text file to be read:\n")
d2=input("Enter the name of the text file where the data is to be written after translation:\n")
l=input("Please enter the code of the language in which you wish to translate contents of the text file to:\n")
try:
    d1=d1+r".txt";d2=d2+r".txt"
    f1=open(d1,"r")
    f2=open(d2,"w")
except:
    print("Source file name isn't valid\nTerminating Program")
else:
    l1=f1.readlines()
    if l in gt.LANGUAGES:
        
        s=trans.translate(l1[0],dest=l)
        f2.writelines(s.text)
        print("The contents of the file have been translated and successfully copied to the destination file")
        f1.close();f2.close()
    else:
        print("Language code isn't recognised")