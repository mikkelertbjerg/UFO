#Timecap: 3 hours

#0-30 min
"""
Setting up exercise, learning about basic stenography.
Trying to figure out which language is more optimal for solving the exercise.
Also trying to figure out how to approach the exercise
"""
#30-60 min
"""
Started out with c#, followed by quickly investigating python.
Quickly flipped to python rather than c#, because I found am article, I believe can solve the exercise.
Studying the libaries the article is using, as it's not yielding the expected result in vscode.
Might opt. for a jupyter notebook instead.
"""
#60-90 min
"""
I can see that there's another layer in the png (the ascii code), I know to read a single pixel.
I need to itterate over all of the pixels, store them in an array and translate each entry from ascii code.
I just need to write it in a smart way, and figure out how to store theese values in an array.
Realized I havn't read the exercise description properly.
I will have to find the lowest value in the red channel and store theese bit values in an array instead.
"""
#90-120 min
"""
Trying to understand the wording of least significant bit value. After consulting group memebers we agreed
that the last number of the bit value would be it. So if pixel at pos (0,0) red value red value is 218,
the least significant bit value is 8 in this example. Now I have to itterate through all of the pixels and 
store the last values in an array, and then I should be able to form a message.
"""
#120-150min
"""
Currently got an array with all of the r channels of the pictures, presuameably sorted correctly,
now I just gotta last digit of each element in the array.
Managed to store an array of the last digits in each red channel bit, now I have to figure out when the bits
should be concatanated. Approaching this as if the ascii code is in oct, which means I should concat every three
digits into one digit, untill I hit three (null), representing the ending of the message.
"""

#Queries
"""
"decrypt ascii message in png" 
"decrypt ascii message"
"read pixels in png"
"c# read png image pixels"
"read every pixel in png"
"matplotlib.imshow"
"imageio imread"
"python store every value of pixel in array"
"python shape of image"
"ascii chars"
"rgb bits"
"for loop python"
"python red channel in pixel at 0,0"
"python array"
"append last number of bit"
"looping over every pixel in img python"
"get last digit of number in array python"
"get last digit from each element in array python"
"Remove last digit from number python"
"Get last digit from number python"
"python convert array of ints to ascii"
"concact every three digits in array python"
"concatenate two digits in python list"
"""

#Sites
"""
https://stackoverflow.com/questions/6444869/how-do-i-read-pixels-from-a-png-file
https://social.msdn.microsoft.com/Forums/vstudio/en-US/0f8a89df-ab2c-4608-84fb-3bb28c1e95cb/reading-png-image-and-accessing-pixels?forum=vcgeneral
https://docs.microsoft.com/en-us/dotnet/framework/wpf/graphics-multimedia/how-to-encode-and-decode-a-png-image
https://docs.microsoft.com/en-us/dotnet/api/system.windows.media.imaging.bitmapsource?view=netframework-4.8
https://www.codementor.io/innat_2k14/image-data-analysis-using-numpy-opencv-part-1-kfadbafx6
https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html
https://imageio.readthedocs.io/en/latest/examples.html
https://stackoverflow.com/questions/23871300/python-array-processing-how-to-generate-new-values-on-pixel-by-pixel-basis
https://www.tutorialkart.com/opencv/python/opencv-python-get-image-size/
http://www.asciitable.com/
https://en.wikipedia.org/wiki/RGB_color_model
https://www.w3schools.com/python/python_for_loops.asp
https://stackoverflow.com/questions/52632718/display-image-only-in-rred-channel-using-python
https://www.w3schools.com/python/python_arrays.asp
https://codereview.stackexchange.com/questions/192739/looping-over-pixels-in-an-image
https://www.pyimagesearch.com/2017/08/28/fast-optimized-for-pixel-loops-with-opencv-and-python/
https://stackoverflow.com/questions/22552624/how-to-get-the-last-number-from-list-in-python
https://stackoverflow.com/questions/44265975/remove-last-number-of-a-integer
https://www.geeksforgeeks.org/python-ways-to-convert-list-of-ascii-value-to-string/
https://www.tutorialspoint.com/How-to-convert-an-integer-to-an-ASCII-value-in-Python
https://stackoverflow.com/questions/25876640/subsampling-every-nth-entry-in-a-numpy-array
https://www.w3resource.com/python-exercises/python-basic-exercise-27.php
"""

import imageio
import matplotlib.pyplot as plt


pic = imageio.imread('Stego.png')
#Short test validation
"""
print(pic[0, 0, 0])
print(pic[1, 0, 0])
print(pic[2, 0, 0])
"""


#Set up params for the loop
h = pic.shape[0] #height
w = pic.shape[1] #width

#Initialize array
rValues = []
for x in range(w):
    for y in range(h):
        rValues.append(pic[y, x, 0]%10) #%10 to only get the last digit

#Validate output
#print(rValues)

asciiValues = []
asciiValue = ""

for x in 

result = ""
for x in rValues:
    result = result + chr(x)

print(result)

