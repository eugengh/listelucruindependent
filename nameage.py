with open("nameage.txt","r") as f:
    prenume = (f.readline().split(","))
    varsta = list(eval(f.readline()))
prenume.pop(7)
with open("output.txt", "w") as f:
    f.write(str(prenume))
    f.write("\n")
    f.write(str(varsta))
    f.write("\n")
    for i in range(0, len(prenume)):
        a=(prenume[i], " are varsta de ", varsta[i], "ani")
        i+=1
        f.write(str(a))
    prenume.extend(["Andreea", "Ioan"])
    varsta.extend([34, 23])
    f.write("\n")
    f.write(str(prenume))
    f.write("\n")
    f.write(str(varsta))
    f.write("\n")
    prenume.pop(2)
    varsta.pop(2)
    f.write(str(prenume))
    f.write("\n")
    f.write(str(varsta))
    f.write("\n")
    f.write(str(prenume[0:3]))
    f.write("\n")
    f.write(str(prenume[::-1]))
    f.write("\n")
    c= (prenume[2],  prenume[4])
    f.write(str(c))
    f.write("\n")
    b=(varsta[2],varsta[4])
    f.write(str(b))
    f.write("\n")
    f.write(str(prenume[0:5]))
    f.write("\n")
    f.write(str(varsta[0:5]))