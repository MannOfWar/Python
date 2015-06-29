list_menu = ['nasi','ayam']

def program():
    print ("Program")
    print ("1.Show Menu")
    print ("2.Input Menu")
    print ("3.Delete Menu")
    print ("4.Rename Menu")
    print ("5.Exit")
def program_input():
    program = input ("What's your choice?  ")
    if program ==1:
        print list_menu
        print""
        out()
        any_key()
        program_input()
    elif program ==2:
        inp()
        any_key()
        program_input()
    elif program ==3:
        delete()
        any_key()
        program_input()
    elif program ==4:
        rename()
        any_key()
        program_input()
    elif program ==5:
        exit()
        
def out():
    print "Our menu"
    idx=0
    for menu in list_menu:
        idx=idx+1
        print"{}.{}".format(idx,menu)
def rename():
    rename = raw_input ("Which menu to change: ")
    update = list_menu.index(rename)
    list_menu[update]= raw_input ("Input a new name for {}".format(rename))
    print list_menu
    

def delete():
    delete = raw_input ("Remove a menu: ")
    list_menu.remove(delete)
    
def inp():
    add = raw_input("Add a menu: ")
    list_menu.append(add)

def any_key():
    key=raw_input ("Press any key")
    
program()
program_input()

