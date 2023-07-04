def getAge(age):
    cat = "baby"
    if (age <=5):
        cat = "baby"
    elif (age > 5 and age <=13):
        cat = "kids"
    else:
        cat = "big people"
    return cat

#myage = input("Enter your age as an integer (ex. 5): ")
#mycat = getAge(int(myage))
#print(mycat)


friends = ["anny", "aaron", "kc"]
friends.append("william")
friends.sort()

for f in friends:
    print(f + " is cool")


for i in range(4):
    print(friends[i])
