# file = open ("test.txt","a+")


import datetime
filename= datetime.datetime.now()


def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt",'w') as file:
        file.write("")
    #file.seek(0)
#content = file.read()
    #print (content)


create_file()
