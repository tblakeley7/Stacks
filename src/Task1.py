"""
-------------------------------------------------------
Author:  Tyler Blakeley
ID:      090603980
Email:   blak3980@wlu.ca
Version: 2013-01-28
-------------------------------------------------------
"""

from stack import Stack
def combine_stacks(newstack,stack1,stack2):
    s1= False
    s2 = False
    while True:
        
        x = stack1.pop()
        if x != None:
            newstack.push(x)
        else:
            s1 = True
            if s1 == True and s2==True:
                break
        y = stack2.pop()
        if y != None:
            newstack.push(y)
        else:
            s2 = True
            if s1 == True and s2==True:
                break
    newstack.print_i("r")

    return

x=Stack()
s=Stack()
sp=Stack()
s.push(9)
s.push(7)
s.push(5)
s.push(3)
s.push(1) 
sp.push(14)
sp.push(12)
sp.push(10)
sp.push(8)
sp.push(6)
sp.push(4)
sp.push(2)
combine_stacks(x,s,sp)
x.combine(s,sp)
x.print_i("r")


