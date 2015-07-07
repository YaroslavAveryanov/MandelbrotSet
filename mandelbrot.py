from PIL import Image
import numpy as np
import os

max_iteration = 1000
x_center = -1.0
y_center =  0.0
size = 300
step = 0.5
s = raw_input("Enter min, max of start point, step:")
numbers = eval(s)

center = np.arange(numbers[0],numbers[1],numbers[2])

for k in range(len(center)):
	im = Image.new("RGB", (size,size))
	for i in xrange(size):
    		for j in xrange(size):
        		x,y = ( x_center + 4.0*float(i-size/2)/size,
        	        	y_center + 4.0*float(j-size/2)/size
        	        	)

        		a,b = (center[k], 0.0)
        		iteration = 0

        		while (a**2 + b**2 <= 4.0 and iteration < max_iteration):
        	    		a,b = a**2 - b**2 + x, 2*a*b + y
        	    		iteration += 1
        		if iteration == max_iteration:
        	    		color_value = 255
        		else:
        	    		color_value = iteration*10 % 255
        		im.putpixel( (i,j), (color_value, color_value, color_value))

	im.save("mandelbrot" + repr(k) + ".png", "PNG")

os.system("convert -delay 20 -loop 0 *.png animate.gif")
os.system("xdg-open animate.gif")
