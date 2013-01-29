"""
Stack Class Defintion
-------------------------------------------------------
Author:  Tyler Blakeley
ID:      090603980
Email:   blak3980@wlu.ca
Version: 2013-01-28
-------------------------------------------------------
"""
import copy

class Stack:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    DIRECTIONS = ( 'f', 'r' )

    def __init__( self ):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a list.
        -------------------------------------------------------
        Postconditions:
          Initializes an empty stack.
        -------------------------------------------------------
        """
        self._values = []
        return

    def __len__( self ):
        """
        -------------------------------------------------------
        Returns the size of the stack.
        Use as len(stack)
        -------------------------------------------------------
        Postconditions:
          Returns the number of values in the stack.
        -------------------------------------------------------
        """
        return len( self._values )

    def is_empty( self ):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        -------------------------------------------------------
        Postconditions:
          Returns True if the stack is empty, False otherwise.
        -------------------------------------------------------
        """

        # your code here
        if len(self._values)!=0:
            result=False
        else:
            result=True

        return result

    def push( self, value ):
        """
        -------------------------------------------------------
        Pushes a copy of value onto stack.
        -------------------------------------------------------
        Preconditions:
          value - a data element (?)
        Postconditions:
          value is added to the top of the stack.
        -------------------------------------------------------
        """
        self._values.append( copy.deepcopy( value ) )
        return

    def pop( self ):
        """
        -------------------------------------------------------
        Pops and returns the top of stack.
        -------------------------------------------------------
        Postconditions:
          Returns the value at the top of the stack - the value is
          removed from the stack. Returns None if the stack is empty.
        -------------------------------------------------------
        """

        # your code here
        if Stack.is_empty(self)==True:
            value=None
        else:
            value=self._values[len(self)-1]
            del self._values[len(self)-1]
        return value

    def peek( self ):
        """
        -------------------------------------------------------
        Peeks at the top of the stack.
        -------------------------------------------------------
        
        Postconditions:
          Returns a copy of the value at the top of the stack -
          the value is not removed from stack. Returns None
          if the stack is empty.
        -------------------------------------------------------
        """

        # your code here
        if Stack.is_empty(self)==True:
            value=None
        else:
            value=copy.deepcopy(self._values[len(self)-1])
        return value
    
    def combine(self, stack1,stack2):
        """
        -------------------------------------------------------
        Combine 2 stacks into current stack
        -------------------------------------------------------
        Preconditions:
          stack1 - stack
          stack2 - stack
        Postconditions:
          Both stack1 and stack2 are emptyed and are the elements are placed into current stack
        -------------------------------------------------------
        """
        s1= False
        s2 = False
        
        while True:
            if(len(stack1._values)!=0):
                x = stack1._values.pop()
                self._values.append(x)
            else:
                s1 = True
                if s1 == True and s2==True:
                    break
            if(len(stack2._values)!=0):
                y = stack2._values.pop()
                self._values.append(y)
            else:
                s2 = True
                if s1 == True and s2==True:
                    break
        return
    
            
    def print_i( self, direction ):
        """
        -------------------------------------------------------
        Prints the contents of the stack using stack's custom
        printing function in the order direction' ('f' or 'r').
        -------------------------------------------------------
        Preconditions:
          direction - direction to print stack contents in (str)
        Postconditions:
          Prints each value in the stack using pf.
          Prints in forward order (top to bottom) if direction is 'f',
          in reverse order (bottom to top) if direction is 'r'. Otherwise
          does nothing.
        -------------------------------------------------------
        """
        assert direction in self.DIRECTIONS
        n = len( self._values )

        if direction == 'f':
            for i in range( n - 1, -1, -1 ):
                print( self._values[i] )
        elif direction == 'r':
            for i in range( n ):
                print( self._values[i] )
        return