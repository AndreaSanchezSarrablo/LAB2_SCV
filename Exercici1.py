#EXERCICI1
import os

def parse_info_BBBvideo(line):

	# We put together all the information from the BBB video that must be shown in the terminal in a .txt file
	os.system("ffmpeg -i bbbVideo.mp4 2> info_ex1.txt")

	# We open the file with all the information of the video
	file = open('info_ex1.txt')
 
	# We read the content of the info_ex1.txt file
	content = file.readlines()
	  
	# Finally we read the line that we are interested in
	print(content[line])


print("The title of the input video is:")
parse_info_BBBvideo(17)
print("The encoder of the input video is:")
parse_info_BBBvideo(18)
print("The duration and bitrate of the input video is:")
parse_info_BBBvideo(20)

# If we want to show more information about the video, we should call again the function:
# 'parse_info_BBBvideo' with the correspondng line where we can find the information that we are interested in.
