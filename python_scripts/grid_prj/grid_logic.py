#!/usr/bin/python3

#with this we can write a function that gives us one row or column and that can be multiplied to give us whatever number of grid colum we want then it can be printed in the next line to give us the grid feel 

#print("""|   |   |  """*2)
#print("""|   |   |  """ + """|   |   |""")

"""
    I used this logic so that no matter the number of row or col the user might request, it is printed correctly if no one is given it returns just a single row and column if a zero or -nve number is provided, it returns False
"""

def row(n =1): #if the row number is not specified return just one row
    if(n==1):
        return """|      |""" *n
    elif n>1:
        return """|      """ *(n+1)
    else: return False
    

def col(n=1): #if the col number is not specified return just one col
    if(n==1):
        return """+------+""" *n
    elif(n>1):
        return f"""+{'------+' *n}"""
    else: return False


def display_grid(n):
   #logic works for every entry
   row_len=4
   grid_no=is_num(n)

   if grid_no is False:
       return False

   for i in range(grid_no):
       print(col(grid_no))
       for a in range(row_len):
           print(row(grid_no))
        
   print(col(grid_no))

   return True


def is_num(x):
    """Return True if x can be converted to an integer and is positive"""
    try:
        n=int(x) #an excepted err should occur if n is not an int
        #check if int is +ve
        if n > 0:
            return n
        else:
            return False #not a +ve int n is negative
    except (ValueError, TypeError):
        #this manages the exception and returns False if it does 
        return False

