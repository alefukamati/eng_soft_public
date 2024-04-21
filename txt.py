def saveCadast(name, email,password):
    data = [name, email, password]
    with open('db.txt', 'a') as f:
        for info in data:
            f.write(info)
            f.write(',')

def saveResult(result):
    with open('db.txt', 'a') as f:
        f.write(result)
        f.write(',')
        f.write('\n')

def validateCredentials(email,senha):
    f = open("db.txt", "r")
    lines = f.readlines()
    for line in lines:
        elem= line.split(',')
        if elem[1] == email:
            if elem[2] == senha: return True
            else: return False 
    return False

def searchResult(email):
    f = open("db.txt", "r")
    lines = f.readlines()
    for line in lines:   
        elem= line.split(',')
        if elem[1] == email:
            return elem[3]
    return None