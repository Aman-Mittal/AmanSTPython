try:
    fh=open(r"c:\python\student.txt","r")
    fh.write("this is my file for exception handling!")
except Exception as ob:
    print(ob)
finally:
    print("Cant find file or read data")
    fh.close()
print("Thanks")
