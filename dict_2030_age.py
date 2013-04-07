
member_info = {'minsu' : 43 , 'jisu':33 , 'john' : 21 , 'david' : 33, 'jisu' : 21, 'hary':36, 'messi' :33, 'ronaldo' : 27}

'''
result 
30s : ['jisu','john','hary'] , 20s: ['john','ronaldo','david']
'''


'''
# origin source
dict_age ={}

for name in member_info:
    nAge = member_info[name]
    if (nAge >= 30 and nAge < 40) :
        if ('30s' in dict_age) :
            dict_age['30s'].append(name)
        else : 
            dict_age['30s'] = [name]

    elif (nAge < 30 and nAge > 20):
        if ('20s' in dict_age) :
            dict_age['20s'].append(name)
        else :
            dict_age['20s'] = [name]
    else :
        print 'error age data :', name , ' : ' ,nAge 
            
print dict_age
'''


# refactioring code : using function, remove duplicate code
def addNewData(key,dictData,human_name) :
    if (key in dictData) :
        dictData[key].append(human_name)
    else : 
        dictData[key] = [human_name]


def reModelNameAgeData() : 
    dict_age ={}

    for name in member_info:
        nAge = member_info[name]
        if (nAge >= 30 and nAge < 40) :
            addNewData('30s',dict_age,name)
        elif (nAge < 30 and nAge > 20):
            addNewData('20s',dict_age,name)
        else :
            print 'error age data :', name , ' : ' ,nAge 

    return dict_age
            
print reModelNameAgeData()
