#EXERCICI3
import os

def resize_input(input_file, width, height, output_file):

	# We are able to resize the input file if we have the input file, the specific width and heigh in which we
	# wannt to resize the input, and finally the name of the output file we want to save the resizing operation.

	# Apply the resize operation to the input file with the input parameters of the function
	os.system("ffmpeg -i " + str(input_file) + " -vf scale="+str(width)+":"+str(height)+" "+str(output_file))


# Ask the user for the specifip parameters to be able to resize the input given
input_file = input("Write the name of the input file that you want to resize toguether with its extension(ex: inputVideo.mp4, inputImage.jpg):")
width = input("Choose the width you want to resize your input file(must be multiple of 2):")
height = input("Choose the height you want to resize your input file with(must be multiple of 2):")
output_file = input("Write the name of the output file with its extension(ex: outputVideo.mp4, outputImage.jpg):")

# Calling the function with all the given parameters from the user
resize_input(input_file, width, height, output_file)

