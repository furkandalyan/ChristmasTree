def draw_tree(height):
    for line in range(1,height+1):
        for spaces in range(height-line):
            print(" ",end="")

        for stars in range(2*line-1):
            print("*",end="")
        
        print()

        

draw_tree(int(input("Enter height of the tree:")))
