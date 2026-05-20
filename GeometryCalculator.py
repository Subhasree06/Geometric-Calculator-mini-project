print("GEOMETRY CALCULATOR: \n Choose the right geometric shape for which you want to perform the geometric operations:")
pi = 3.14
while True:
    print("1.Circle")
    print("2.Square")
    print("3.Rectangle")
    print("4.Triangle")
    print("5.Cube")
    print("6.Cuboid")
    print("7.Cylinder")
    print("8.Cone")
    print("9.Parallelogram")
    print("10.Rhombus")
    print("11.Trapezium")
    print("12.Lines")
    print("13.Exit")
    
    choice = int(input("Enter the Shape number(1-13):"))
    if (choice == 1):  #Circle Operations:
        print("1.Find Area of a Circle:")
        print("2.Find Circumference of a Circle:")
        print("3.Find the Radius of a Circle when Circumference is given:")
        print("4.Find the Radius of a Circle when Area is given:")
        print("5.Find the Diameter of a Circle:")

        option_1 = int(input("Enter the Circle operation to be performed(1-5):"))

        if(option_1 == 1):  #Area of a circle:
            radius = float(input("Enter the Radius of the Circle:"))
            print("The Area of a Circle is:",(pi*radius*radius))
        elif(option_1 == 2): #Circumference of a circle:
            radius = float(input("Enter the Radius of the Circle:"))
            print("The Circumference of a Circle is:",(2*pi*radius))
        elif(option_1 == 3): #Find radius when circumference is given:
            circum = float(input("Enter the Circumference of a Circle:"))
            print("The Radius of the Circle when Circumference is given is:",(circum/(2*pi)))
        elif(option_1 == 4): #Find radius when area is given:
            area = float(input("Enter the Area of the Circle:"))
            print("The Radius of the Circle when Area is given is:",((area/pi)**0.5))
        elif(option_1 == 5):
            radius = float(input("Enter the Radius of the Circle:"))
            print("The Diameter of a Circle is:",2*radius)
        else:
            print("Invalid operation number")

    elif (choice == 2):  #Square Operations:
        print("1.Find Area of a Square:")
        print("2.Find Perimeter of a Square:")
        print("3.Find Diagonal of a Square:")

        option_2 = int(input("Enter the Square operation to be performed(1-3):"))

        if(option_2 == 1):   #Area of square:
            side = float(input("Enter the side of the Square:"))
            print("The Area of the Square is:",side*side)
        elif(option_2 == 2):  #Perimeter of square:
            side = float(input("Enter the side of the Square:"))
            print("The Perimeter of the Square is:",4*side)
        elif(option_2 == 3):  #Diagonal of square:
            side = float(input("Enter the side of the Square:"))
            print("The Diagonal of the Square is:",side*(2**0.5))
        else:
            print("Invalid operation number")

    elif (choice == 3):   #Rectangle Operations:
        print("1.Find Area of a Rectangle:")
        print("2.Find Perimeter of a Rectangle:")
        print("3.Find Diagonal of a Rectangle:")

        option_3 = int(input("Enter the Rectangle operation to be performed(1-3):"))

        if(option_3 == 1):  #Area of a rectangle:
            length = float(input("Enter the length of the Rectangle:"))
            breadth = float(input("Enter the breadth of the Rectangle:"))
            print("The Area of Rectangle is:",length*breadth)
        elif(option_3 == 2):  #Perimeter of a rectangle:
            length = float(input("Enter the length of the Rectangle:"))
            breadth = float(input("Enter the breadth of the Rectangle:"))
            print("The Perimeter of Rectangle is:",2*(length+breadth))
        elif(option_3 == 3):  #Diagonal of a rectangle:
            length = float(input("Enter the length of the Rectangle:"))
            breadth = float(input("Enter the breadth of the Rectangle:"))
            print("The Diagonal of Rectangle is:",((length**2)+(breadth**2))**0.5)
        else:
            print("Invalid operation number")

    elif (choice == 4): #Triangle Operations:
        print("1.Find the Area of triangle using base and height:")
        print("2.Find the Area of triangle using Heron's formula:")
        print("3.Find the Perimeter of the triangle:")
        print("4.Check the Validity of the triangle:")

        option_4 = int(input("Enter the Triangle operation to be performed(1-4):"))

        if(option_4 == 1): #Area of a triangle using base and height:
            base = float(input("Enter the base of a triangle:"))
            height = float(input("Enter the height of a triangle:"))
            print("The Area of Triangle is:",(0.5*base*height))
        elif(option_4 == 2): #Area of a triangle using Heron's formula:
            a = float(input("Enter the first side:"))
            b = float(input("Enter the second side:"))
            c = float(input("Enter the third side:"))
            s = (a+b+c)/2
            print("The Area of Triangle is:",(s*(s-a)*(s-b)*(s-c))**0.5)
        elif(option_4 == 3): #Perimeter of a triangle:
            a = float(input("Enter the first side:"))
            b = float(input("Enter the second side:"))
            c = float(input("Enter the third side:"))
            print("The Perimeter of the Triangle is:",(a+b+c))
        elif(option_4 == 4): #Check triangle validity:
            a = float(input("Enter the first side:"))
            b = float(input("Enter the second side:"))
            c = float(input("Enter the third side:"))
            if (a+b>c) and (a+c>b) and (b+c>a):
                print("Triangle is Valid")
            else:
                print("Triangle is invalid")
        else:
            print("Invalid operation number")

    elif (choice == 5): #Cube Operations:
        print("1.Find the Volume of Cube:")
        print("2.Find the Surface Area of Cube:")
        print("3.Find the Space Diagonal of Cube:")

        option_5 = int(input("Enter the Cube operation to be performed(1-3):"))

        if(option_5 == 1): #Volume of cube:
            a = float(input("Enter the side of Cube:"))
            print("The Volume of Cube is:",a**3)
        elif(option_5 == 2): #Surface area of cube:
            a = float(input("Enter the side of Cube:"))
            print("The Surface Area of Cube is:",6*(a**2))
        elif(option_5 == 3): #Space diagonal of cube:
            a = float(input("Enter the side of Cube:"))
            print("The Space Diagonal of Cube is:",a*(3**0.5))
        else:
            print("Invalid operation number")

    elif (choice == 6): #Cuboid operations:
        print("1.Find the Volume of Cuboid:")
        print("2.Find the Surface Area of Cuboid:")
        print("3.Find the Space Diagonal of Cuboid:")

        option_6 = int(input("Enter the Cuboid operation to be performed(1-3):"))

        if(option_6 == 1): #Volume of cuboid:
            l = float(input("Enter the length of the Cuboid:"))
            b = float(input("Enter the breadth of the Cuboid:"))
            h = float(input("Enter the height of the Cuboid:"))
            print("The Volume of Cuboid is:", l*b*h)
        elif(option_6 == 2): #Surface area of cuboid:
            l = float(input("Enter the length of the Cuboid:"))
            b = float(input("Enter the breadth of the Cuboid:"))
            h = float(input("Enter the height of the Cuboid:"))
            print("The Surface Area of Cuboid is:",2*((l*b)+(b*h)+(l*h)))
        elif(option_6 == 3): #Space diagonal of cuboid:
            l = float(input("Enter the length of the Cuboid:"))
            b = float(input("Enter the breadth of the Cuboid:"))
            h = float(input("Enter the height of the Cuboid:"))
            print("The Space Diagonal of Cuboid is:",(((l**2)+(b**2)+(h**2))**0.5))
        else:
            print("Invalid operation number")

    elif (choice == 7): #Cylinder operations:
         print("1.Find the Volume of Cylinder:")
         print("2.Find the Curved Surface Area of Cylinder:")
         print("3.Find the Total Surface Area of Cylinder:")

         option_7 = int(input("Enter the Cylinder operation to be performed(1-3):"))


         if(option_7 == 1): #Volume of cylinder:
             r = float(input("Enter the radius of the Cylinder:"))
             h = float(input("Enter the height of the Cylinder:"))
             print("The Volume of Cylinder is:",pi*(r*r)*h)
         elif(option_7 == 2): #Curved surface area of cylinder:
             r = float(input("Enter the radius of the Cylinder:"))
             h = float(input("Enter the height of the Cylinder:"))
             print("The Curved Surface Area of Cylinder is:",2*pi*r*h)
         elif(option_7 == 3): #Total surface area of cylinder:
             r = float(input("Enter the radius of the Cylinder:"))
             h = float(input("Enter the height of the Cylinder:"))
             print("The Total Surface Area of Cylinder is:",2*pi*r*(r+h))
         else:
             print("Invalid operation number")


    elif (choice == 8): #Cone operations:
        print("1.Find the Volume of Cone:")
        print("2.Find the Curved Surface Area of Cone:")
        print("3.Find the Total Surface Area of Cone:")

        option_8 = int(input("Enter the Cone operation to be performed(1-3):"))


        if(option_8 == 1): #Volume of cone:
            r = float(input("Enter the radius of the Cone:"))
            h = float(input("Enter the height of the Cone:"))
            print("The Volume of Cone is:",(1/3)*pi*(r*r)*h)
        elif(option_8 == 2): #Curved surface area of cone:
            r = float(input("Enter the radius of the Cone:"))
            h = float(input("Enter the height of the Cone:"))
            l = ((r*r)+(h*h))**0.5
            print("The Curved Surface Area of Cone is:",pi*r*l)
        elif(option_8 == 3): #Total surface area of cone:
            r = float(input("Enter the radius of the Cone:"))
            h = float(input("Enter the height of the Cone:"))
            l = ((r*r)+(h*h))**0.5
            print("The Total Surface Area of Cone is:",pi*r*(r+l))
        else:
            print("Invalid operation number")


    elif (choice == 9): #Parallelogram operations:
        print("1.Find the Area of Parallelogram:")
        print("2.Find the Perimeter of Parallelogram:")

        option_9 = int(input("Enter the Parallelogram operation to be performed(1-2):"))

        if(option_9 == 1): #Area of parallelogram:
            a = float(input("Enter the base of the Parallelogram:"))
            b = float(input("Enter the height of the Parallelogram:"))
            print("The Area of Parallelogram is:",a*b)
        elif(option_9 == 2): #Perimeter of parallelogram:
            a = float(input("Enter the base of the Parallelogram:"))
            b = float(input("Enter the height of the Parallelogram:"))
            print("The Perimeter of Parallelogram is:",2*(a+b))
        else:
            print("Invalid operation number")

        
    elif (choice == 10): #Rhombus operations:
        print("1.Find the Area of Rhombus:")
        print("2.Find the Perimeter of Rhombus:")

        option_10 = int(input("Enter the Rhombus operation to be performed(1-2):"))

        if(option_10 == 1): #Area of rhombus:
            d1 = float(input("Enter the diagonal 1 of Rhombus:"))
            d2 = float(input("Enter the diagonal 2 of Rhombus:"))
            print("The Area of Rhombus is:",(d1*d2)/2)
        elif(option_10 == 2): #Perimeter of rhombus:
            a = float(input("Enter the side of Rhombus:"))
            print("The Perimeter of Rhombus is:",4*a)
        else:
            print("Invalid operation number")


    elif (choice == 11): #Trapezium operations:
        print("1.Find the Area of Trapezium:")
        print("2.Find the Perimeter of Trapezium:")

        option_11 = int(input("Enter the Trapezium operation to be performed(1-2):"))

        if(option_11 == 1): #Area of trapezium:
            a = float(input("Enter the first side of Trapezium:"))
            b = float(input("Enter the second side of Trapezium:"))
            h = float(input("Enter the height of Trapezium:"))
            print("The Area of Trapezium is:",0.5*(a+b)*h)
        elif(option_11 == 2): #Perimeter of trapezium:
            a = float(input("Enter the first side of Trapezium:"))
            b = float(input("Enter the second side of Trapezium:"))
            c = float(input("Enter the third side of Trapezium:"))
            d = float(input("Enter the fourth side of Trapezium:"))
            print("The Perimeter of Trapezium is:",a+b+c+d)
        else:
            print("Invalid operation number")


    elif (choice == 12): #Lines Operations:
        print("1.Find the Distance between two points:")
        print("2.Find the Midpoint of two points:")

        option_12 = int(input("Enter the Lines operation to be performed(1-2):"))

        if(option_12 == 1): #Distance between two points:
            x1 = float(input("Enter the x1 value:"))
            x2 = float(input("Enter the x2 value:"))
            y1 = float(input("Enter the y1 value:"))
            y2 = float(input("Enter the y2 value:"))
            print("The Distance between two points is:",(((x2-x1)**2)+((y2-y1)**2))**0.5)
        elif(option_12 == 2): #Midpoint of two points:
            x1 = float(input("Enter the x1 value:"))
            x2 = float(input("Enter the x2 value:"))
            y1 = float(input("Enter the y1 value:"))
            y2 = float(input("Enter the y2 value:"))
            print("The Midpoint of two points is:",((x1+x2)/2),((y1+y2)/2))
        else:
            print("Invalid operation number")

    elif (choice == 13):
        print("Geometric Calulator operations finished")
        break
    else:
        print("Invalid Shape number")
        
        
            
        

    
        
           
        

            

            
        
        


            
        
        
