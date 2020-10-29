import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
    
    pattern = "[A-Z]{1}\w+" #"[A-Z]{1}\w+? #name"""
    L = re.findall(pattern, simple_string)
    
    # or 
    for item in re.finditer(pattern, simple_string):
        print(item.group())
    
    '''    
    words = simple_string.split(" ")
    L = []
    for i in words:
        if (i.istitle() and not i.isspace()):
            print(i)
            L.append(i)
    #print(len(L))
        return L 
    '''
    
    return L

#############################
import re
def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()
        
        L = []
        pattern = "([A-Z]{1}\w+ [A-Z]{1}\w+)(: )(\w)"  
        for i in re.finditer(pattern, grades):
            #print(i[3])
            if i[3] == 'B':
                L.append(i[1])
        '''
        lines = grades.split("\n")
        L = []
        for i in lines:
            if (i.split(": ")[1])[0] == 'B':
                L.append(i.split(": ")[0])
        #print(L, len(L))
        '''

    return L
#############################
import re
def logs():
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()
    
        pattern = """
        (?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})    #host
        (\s\-\s)    # seperator
        (?P<user_name>\-|\w{5,18})    #user_name
        (\s\[)    # seperator
        (?P<time>\S+\s-\d{4})    #time
        (\]\s\")    # seperator
        (?P<request>.+?)    #request
        (\"\s)(.+?$)    # end part which is not important       """

        L = []
        for item in re.finditer(pattern, logdata, re.VERBOSE|re.MULTILINE):

            #print(item.groupdict())
            L.append(item.groupdict())
       
    return L 
