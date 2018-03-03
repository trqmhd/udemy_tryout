'''
asdfasdfasdf afsdfasdf afsadfa
'''


temperatures=[10,-20,-289,100]
def c_to_f(c):
    '''asfasdfasd'''
    if c< -273.15:
        return "That temperature doesn't make sense!\n"
    else:
        f=c*9/5+32
        return f
        '''asfasdfasd'''

file = open ("math.txt", "w")
for t in temperatures:
    file.write(str(c_to_f(t))+"\n")
print ("sfaks asf asdf ")

    #print(c_to_f(t))
