import re

def mlist(mylist): # bad: modifies its argument and also returns it
    mylist.sort()
    return mylist


def Wait(): #void function
    print('Please Wait..........')
    
def st(strr):
    strrcopy=strr.split()
    strrlength=len(strrcopy)
    if strrlength==4:
        strr=re.sub(r'(\w+ \w+) (\w+ \w+)','<surname>\g<1></surname>\n<givenname>\g<2></givenname>',strr)
        return strr
    if strrlength==3:
        strr=re.sub(r'(\w+) (\w+ \w+)','<surname>\g<1></surname>\n<givenname>\g<2></givenname>',strr)
        return strr
    if strrlength==2:
        strr=re.sub(r'(\w+) (\w+)','<surname>\g<1></surname>\n<givenname>\g<2></givenname>',strr)
        return strr
    if strrlength==1:
               return ' cannot proces for single name '

def MX(MAX,MIN):
    if MAX>MIN:
        return MAX
    else:
        return MIN
def wordcount(con):
    concopy=con.split()
    conlength=len(concopy)
    return conlength

def statement(cn):
    cncopy=cn.split('\n')
    cnlength=len(cncopy)
    return cnlength

def Nmonth(value):
    monval={10:"oct"}
    return monval[value]

def Smonth(value):
    monval={"oct":10}
    return monval[value]
def month(value):
    monval={10:"oct"}
    monval1={"oct":10}
    if 'int' in str(type(value)):
        return monval[value]
    else:
        return monval1[value]

def m(num):
    print(type(num))
    num=max(num)
    return num
##    if value==
    ##words = ['turned', 'off', 'I', 'the', 'spectroroute']
##Wait()
##print(mlist(words))
##Wait()
##Wait()

##strr=" jhfhj"
##proce=st(strr)
##print(proce)

##value=MX(5,6)
##print(value)

##con1='bad: modifies its argument and also returns it'
##length=wordcount(con1)
##print(length)

##con1="""bad: modifies its argument and also returns it
##bad: modifies its argument and also returns it
##bad: modifies its argument and also returns it"""
##length=statement(con1)
##print(length)

numval=[1,2,5,79]
max1=m(1,2,5,79)
print(max1)
