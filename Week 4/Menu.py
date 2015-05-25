close= "no"
while close != "yes":
    print ("Welcome to my calculating program")
    print ("What would you like to calculate?")
    choice = input ("1. Triangle Area 2. Square Area 3. Rectangle Area...")
    if choice == 1:
            triangle_base = input ("Insert the Base of the Triangle...")
            triangle_height = input ("Insert the Height of the Triangle...")
            triangle_area = triangle_base*triangle_height/2
            print ("The area of your Triangle is {0}".format(triangle_area))
        
    elif choice == 2:
            square_side = input ("Insert the side of the Square...")
            square_area = square_side*square_side
            print ("The area of your Square is {0}".format(square_area))

    elif choice == 3:
            rectangle_width = input ("Insert the Width of the Rectangle...")
            rectangle_height = input ("Insert the Height of the Rectangle...")
            rectangle_area = rectangle_width*rectangle_height
            print ("The area of your Rectangle is {0}".format(rectangle_area))

    close = raw_input("Close?(yes/no)")

        
