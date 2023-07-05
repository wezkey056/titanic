
#def exData(blist,num):
#    for r in range(1,num):
#        line = blist[r]
 #       temp = line.split(",")
#        print(temp[3] + " survived? " + temp[1] + " m/f " + temp[5])


fi = open("titanic.csv", "r")
biglist = fi.readlines()
fi.close()




#print(len(biglist))
#print(biglist[0])
#exData(biglist,800)

# uri stands for user requested info


while True:
    uri = input("Which passenger would you like to learn more about? Enter a number from 1 891, Press 'q' to quit:")
    if uri == 'q':
        exit()
    else:
        print(biglist[int(uri)])
        uri = input("Which passenger would you like to learn more about? Enter a number from 1 891, Press 'q' to quit:")

            
