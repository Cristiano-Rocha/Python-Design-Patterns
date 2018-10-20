from model import Person

def showAllView(list):
    print(len(list))
    for item in list:
        print(item.name())

def startView():
    print 'MVC - The simplest example'
    print('Do you want to see everyone in my database?[y/n]')

def endView():
    print(' GoodBye!')