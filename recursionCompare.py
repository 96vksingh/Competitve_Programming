def recursion(s,t,m,si):
    l = len(s)
    if(m==si):
        return True 
    elif(l==0 or len(t)==0):
        return False
    if(s[0] in t[0]):
        return recursion(s[1:],t[1:],m,si+1)
    else:
        return recursion(s[1:],t[:],m,si)

s = input()
t = input()
l = len(t)
if(len(s)>0 and l>0 and recursion(s,t,l,0)):
    print("true")
else:
    print("false")
