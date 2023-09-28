import sys, subprocess
subprocess.run('clear', shell=True)

def makeRecords(name):
    file = open(name,"r")
    record = []
    for i in range(0,25):
        record.append([])
    file.seek(0)
    for line in file:
        split = ([*line.strip()])
        total = 0
        for i in range(0,len(split)):
            total += ord(split[i])
        total=total%25
        record[total].append(line.strip())
    file.close()
    return record

def load(record, name):
    total = 0
    print("Enter what you want to load")
    add = input()
    add = add+"\n"
    file = open(name,"a")
    file.write(add)
    split = ([*add.strip()])
    for i in range(0,len(split)):
        total += ord(split[i])
    total=total%25
    record[total].append(add.strip())
    file.close()
    return record

def retrieve(record, name):
    total = 0
    pos = 0
    print("Enter what you want to retrieve")
    file = open(name,"r")
    retrieve = input()
    split = ([*retrieve.strip()])
    for i in range(0,len(split)):
        total += ord(split[i])
    total=total%25
    line = record[total]
    for x in range(0,len(line)):
        if line[x]==retrieve:
            pos = x
    print("'"+retrieve+"'","is located in record",str(total)+", position",str(pos))
    file.close

def chooseFile():
    print("Enter the file you want")
    name = input()
    return name

def menu():
    name = chooseFile()
    record = makeRecords(name)
    choice = ''
    while choice != '6':
        print()
        print("Press 1 > Display Records")
        print("Press 2 > Load Data")
        print("Press 3 > Delete Data")
        print("Press 4 > Retrieve Data")
        print("Press 5 > Change File")
        print("Press 6 > Quit")
        choice = input()
        if choice=='1':
            subprocess.run('clear', shell=True)
            print(record)
        if choice=='2':
            subprocess.run('clear', shell=True)
            record = load(record, name)
            print(record)
        if choice=='3':
            subprocess.run('clear', shell=True)
            print("Delete Function")
        if choice=='4':
            subprocess.run('clear', shell=True)
            retrieve(record, name)
        if choice=='5':
            subprocess.run('clear', shell=True)
            name = chooseFile()
            record = makeRecords(name)
        if choice=='6':
            subprocess.run('clear', shell=True)
            print("Goodbye")
menu()