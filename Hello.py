def new_line():
    print('.')

def three_line():
    new_line()
    new_line()
    new_line()

def nine_line():
    three_line()
    three_line()
    three_line()

def clearing_screen():
    nine_line()
    nine_line()
    three_line()
    new_line()    
    
        

print('printing nine lines')
nine_line()

print('printing twenty-lines')
clearing_screen()

