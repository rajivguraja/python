def fileoperations(file_locations,key,value):
    with open("server.conf", "r") as config:
        content = config.readlines()
        print (content)
    with open("server.conf", "w") as file:
        for line in content:
            if key in line:
                file.write(value + key  + "\n")
            else:
                file.write(line)
    with open("server.conf", "r") as config:
        content2 = config.readlines()
        print (content2)   

def filestringreplcae(key,value):
    with open("server.conf", "r") as file:
        content3 = file.read()
        print (content3)
        content3 = content3.replace(key,value)
        print (content3)
    with open("server.conf","w") as file:
        file.write(content3)
                   

#fileoperations("server.conf", "MAX_CONNECTIONS=500", "")  
filestringreplcae( "makeup", "MAX_CONNECTIONS" )      