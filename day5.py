def getKidz(data):
    numkids = 0
    numsurv = 0
    for p in data:
        temp = p.split(",")
        if (temp[6] != ""):
            if (float(temp[6]) < 16.0):
                numkids = numkids + 1
                if (temp[1] == "1"):
                    numsurv = numsurv + 1
    return (numsurv / numkids) * 100



def getGrp(data,sex):
    numgrp = 0
    numsurv = 0
    for p in data:
        temp = p.split(",")
        if (temp[5] == sex):
            numgrp = numgrp + 1
            if (temp[1] == "1"):
                numsurv = numsurv + 1
    return (numsurv / numgrp) * 100


#open titanic database
file = open("titanic.csv","r")
cols = file.readline()
data = file.readlines()
file.close()

k = getKidz(data)
g = getGrp(data,'male')
g2 = getGrp(data,'female')

#print(round(k,3))
#print(round(g,3))
#print(round(g2,3))


fo = open("index1.html","w")
fo.write("<html>")
fo.write("<h1>Titaninc Survival Rate Data</h1>")
fo.write("</html>")
fo.close()


keepgoing = True

while (keepgoing == True):
    key = input('f for female, k for kids, m for male, q to quit:')
    if (key == 'f'):
        print(round(g2,3))
    elif (key == 'k'):
        print(round(k,3))
    elif (key == 'm'):
        print(round(g,3))
    elif (key == 'q'):
        keepgoing = False
        print("girfhiuhsdfiuJIUOsdfuiohhsdf Y stisduifsdfopud d d U STUOOPDI sdhfiudhfgrrrrrrrr")
    else:
        print("That is not a valid input")
        
        
