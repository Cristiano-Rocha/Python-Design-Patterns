from model import Person
import view

def showAll():
    people_in_db = Person.getAll()
    return

view.showAll(people_ind_db)

def start():
    view.startView()
    input = aw_input()
    if input == 'y':
        return showAll()
    else:
        return view.endView()

if __name__=="main":
    start()
