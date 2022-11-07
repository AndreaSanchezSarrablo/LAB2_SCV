#EXERCICI4
import os

def ex4(input_video):

	# First we save the .txt with all the info from the input video ( w/ audio tracks)
	os.system("ffmpeg -i "+str(input_video) +" 2> info_ex4.txt")

	# Now we are going to diplay all the lines which contain the audio tracks information
	print("The audio tracks founded in this video are the following ones: \n")

	#We are only interested in those lines where we find the word "Audio:"
	file = open("info_ex4.txt","r") # Open the file
	lines = file.readlines()		# Read lines
	
	idx = 0

	#Loop through each line of the file
	for line in lines:
		#If the line has the string "Audio:" then we  print that line
		if "Audio:" in line:
			print(lines[idx])
			if "dra" in line:
				print("Then, the video can fit in DTMB broadcasting standard \n")
			elif "aac" in line:
				print("Then, the video can fit in DVB, ISDB or DTMB broadcasting standards \n")
			elif "ac-3" in line:
				print("Then, the video can fit in DVB, ATSC or DTMB broadcasting standards \n")
			elif "mp3" in line:
				print("Then, the video can fit in DVB or DTMB broadcasting standards \n")
		idx += 1

	#Close file after reading
	file.close()
	print("So the broadcasting standard that can fit with the overall video will be the one(s) that is/are common in all audio tracks\n")
	
#Ask the user for an input video
input_video = input("Please, enter your input video:\n")

#Calling the function
ex4(input_video)
