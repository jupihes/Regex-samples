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

grades= '''
Killian Kaufman: B
Elwood Page: B
Mukti Patel: A
Emily Lesch: C'''
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

logdata = """
32.86.3.51 - - [21/Jun/2019:16:01:59 -0700] "GET /optimize/impactful/sexy/channels HTTP/2.0" 405 18443
176.68.62.252 - turner3261 [21/Jun/2019:16:02:00 -0700] "GET /viral HTTP/1.1" 405 16692
35.86.149.61 - zemlak6334 [21/Jun/2019:16:02:01 -0700] "HEAD /incentivize HTTP/2.0" 304 9962
30.95.91.251 - larson8319 [21/Jun/2019:16:02:02 -0700] "PUT /one-to-one/whiteboard HTTP/1.0" 401 7270"""
