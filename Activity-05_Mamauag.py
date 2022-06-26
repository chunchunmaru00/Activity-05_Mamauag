from fileinput import filename
import cv2
import numpy as np

def menu():
    file = 'rick.jpg'
    image = cv2.imread(file)
    input= int(print("Please what you want (1-5 only): \n[1] - Show a Pixel Value \n[2] - Set a Pixel Value \n[3] - Set Image Dimension \n[4] - Set Image Total Pixel Count \n[5] - Print Data Type of Loaded Image"))

    if input == 1:
        x = int(input("Enter the row: "))
        y = int(input("Enter the column: "))
        blue = image[x,y,0]
        green = image[x,y,1]
        red = image[x,y,2]
        print("Pixel Value")
        print("Blue: ", blue)
        print("Green: ", green)
        print("Red: ", red)
        
    elif input == 2:
        x = int(input("Enter the row: "))
        y = int(input("Enter the column: "))
        pxB = image[x,y,0]
        pxG = image[x,y,1]
        pxR = image[x,y,2]
        b = int(input("Value for Blue: "))
        r = int(input("Value for Red: "))
        g = int(input("Value for Green: "))
        pxB1 = image.itemset((x,y,0),b)
        pxG1 = image.itemset((x,y,1),g)
        pxR1 = image.itemset((x,y,2),r)
        print("Before \nBlue: ", pxB, "\nGreen: ", pxG, "\nRed: ", pxR)
        print("After \nBlue: ", pxB1, "\nGreen: ", pxG1, "\nRed: ", pxR1)
        

    elif input == 3:
        print("Image Dimension")
        RStart = int(input("Enter the starting row:"))
        REnd = int(input("Enter the ending row:"))
        CStart = int(input("Enter the starting column:"))
        CEnd = int(input("Enter the ending column:"))
        a,b = image.shape
        if RStart <= a:
            if REnd <= a:                
                if CStart <= b:                   
                    if CEnd <= b:
                        print("Dimension set is within the bounderies")
                    else:
                        print(" Dimension set is out of bounderies")                     
                else:
                        print(" Dimension set is out of bounderies")
            else:
                        print(" Dimension set is out of bounderies")
        else:
                        print(" Dimension set is out of bounderies")
    
    elif input == 4:
        px = int(input("Set desired pixel count: "))
        if image.size < px:
            print("Original Pixel count:", image.size)
            print("Set Pixel count: ", px)
            print("Original Pixel count is less than Set Pixel count")
        elif image.size < px:
            print("Original Pixel count:", image.size)
            print("Set Pixel count: ", px)
            print("Original Pixel count is more than Set Pixel count")
        else:
            print("Original Pixel count:", image.size)
            print("Set Pixel count: ", px)
            print("Original Pixel count is equal to Set Pixel count")

    elif input == 5:
        print(image.dtype)

    else:
        print("Please choose between 1 to 5 only")
        menu()