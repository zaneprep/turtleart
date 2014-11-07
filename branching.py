import turtle as t
 
def y(length=100):
    """ 
    paints a branch of a tree with 2 smaller branches, like an Y
    """
    # escape the function when done (we're iterating down)
    if length < 10:
       return       
    # paint the thick branch of the tree
    t.fd(length)        
    # rotate left for smaller "fork" branch
    t.left(30)          
    # create a smaller branch with 2/3 the lenght of the parent branch
    y(length * 0.6)     
    # rotoate right for smaller "fork" branch 
    t.right(60)         
    # create second smaller branch
    y(length * 0.6)     
    # rotate back to original heading 
    t.left(30)          
    t.fd(-length)       
    return              
 
# calling the function the first time
y(200) # create a tree, the first branch has a length of 200 pixel
