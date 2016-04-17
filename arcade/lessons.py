##help file
##Here you will find functions made to help you program

def help(function):
    function = function.upper()
    helpSearch = open("helper.txt", "r")
    for line in helpSearch:
        if function in line: print(line)
    helpSearch.close()
    
help("numberonedickhuntjohncena")
