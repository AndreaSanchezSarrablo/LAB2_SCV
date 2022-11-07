#EXERCICI2
import os

def ex2(video):

	# Cut 1minute = 60 seconds from the input video
	os.system("ffmpeg -i " + str(video) + " -ss 0 -t 60 -c:v copy -c:a copy 1min_cuttedVideo.mp4")
	
	# Export the audio of the 1 minute video as MP3 stereo tack
	os.system("ffmpeg -i 1min_cuttedVideo.mp4 -map a -ac 2 stereo_track.mp3")

	#-map a: means that we are excluding the video/subtitles and only grabing the audio part
	# -ac 2: means that we want the stereo track

	# Export the audio of the 1 minute video as AAC with lower bitrate
	os.system("ffmpeg -i 1min_cuttedVideo.mp4 -vn -b:a 128k aac_lowerBitrate.aac")

	# -vn: means that we are not getting the video part of the file
	#-b:a 128k: sets the bitrate to 128k (lower one because the original video has a bitrate of 581k)

	# Finally we put together the video and the two audios in an .mp4 file
	os.system('ffmpeg -i 1min_cuttedVideo.mp4 -i stereo_track.mp3 -i aac_lowerBitrate.aac -map 0 -map 1:a -map 2:a -c copy output_ex2.mp4')


#Calling the function
ex2("bbbVideo.mp4")
