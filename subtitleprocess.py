import re



def no_much_spaces(string):
    string_list = string.split()
    returner = ''
    for word in string_list:
        returner += ' ' + word
    print(returner)
    return returner[1:]

def sub_to_list(path_file):
    file = open(path_file,'r',encoding = 'iso-8859-1')
    dialogue = []
    temp = ''
    for line in file.readlines():
        line = no_much_spaces(line)
        if line == '':
            continue
        if line[0].isnumeric():
            continue
        
        
        if temp != '':
            dialogue.append(temp + ' ' + line)
            temp = ''
        
        if (line[-1] == '.' or line[-1] == '?' or line[-1] == '!'):
            dialogue.append(line)
            continue
        else:
            temp = line
            continue
        
            
    return dialogue
    
dialogue = sub_to_list('legenda 1.srt')