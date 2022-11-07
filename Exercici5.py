#EXERCICI5
import os

def main():
    # We are going to have a menu to select which exercise we want to run
    # So, we ask the user for the exercise to run:

    var = 1
    # Iterate a loop though all the exercises
    while (var != 0):

        current_ex = int(input("\nPlease select the number of the exercise that you want to run from 1 to 4 [0 for exit]:\n"))

        if (current_ex == 1):
            # Ask the user for the necessary parameters for the exercise
            print("The title of the input video is:")
            parse_info_BBBvideo(17)
            print("The encoder of the input video is:")
            parse_info_BBBvideo(18)
            print("The duration and bitrate of the input video is:")

            # Call the function
            parse_info_BBBvideo(20)

        elif (current_ex == 2):
            ex2("bbbVideo.mp4")

        elif (current_ex == 3):
            # Ask the user for the specifip parameters to be able to resize the input given
            input_file = input(
                "Write the name of the input file that you want to resize toguether with its extension(ex: inputVideo.mp4, inputImage.jpg):")
            width = input("Choose the width you want to resize your input file(must be multiple of 2):")
            height = input("Choose the height you want to resize your input file with(must be multiple of 2):")
            output_file = input(
                "Write the name of the output file with its extension(ex: outputVideo.mp4, outputImage.jpg):")

            # Calling the function with all the given parameters from the user
            resize_input(input_file, width, height, output_file)

        elif (current_ex == 4):
            # Ask the user for an input video
            input_video = input("Please, enter your input video:\n")

            # Calling the function
            ex4(input_video)
        else:
            var = 0


#EXERCICI 1
def parse_info_BBBvideo(line):
    # We put together all the information from the BBB video that must be shown in the terminal in a .txt file
    os.system("ffmpeg -i bbbVideo.mp4 2> info_ex1.txt")

    # We open the file with all the information of the video
    file = open('info_ex1.txt')

    # We read the content of the info_ex1.txt file
    content = file.readlines()

    # Finally we read the line that we are interested in
    print(content[line])


#EXERCICI2
def ex2(video):
    # Cut 1minute = 60 seconds from the input video
    os.system("ffmpeg -i " + str(video) + " -ss 0 -t 60 -c:v copy -c:a copy 1min_cuttedVideo.mp4")

    # Export the audio of the 1 minute video as MP3 stereo tack
    os.system("ffmpeg -i 1min_cuttedVideo.mp4 -map a -ac 2 stereo_track.mp3")

    # -map a: means that we are excluding the video/subtitles and only grabing the audio part
    # -ac 2: means that we want the stereo track

    # Export the audio of the 1 minute video as AAC with lower bitrate
    os.system("ffmpeg -i 1min_cuttedVideo.mp4 -vn -b:a 128k aac_lowerBitrate.aac")

    # -vn: means that we are not getting the video part of the file
    # -b:a 128k: sets the bitrate to 128k (lower one because the original video has a bitrate of 581k)

    # Finally we put together the video and the two audios in an .mp4 file
    os.system(
        'ffmpeg -i 1min_cuttedVideo.mp4 -i stereo_track.mp3 -i aac_lowerBitrate.aac -map 0 -map 1:a -map 2:a -c copy output_ex2.mp4')


#EXERCICI3
def resize_input(input_file, width, height, output_file):

    # We are able to resize the input file if we have the input file, the specific width and heigh in which we
    # wannt to resize the input, and finally the name of the output file we want to save the resizing operation.

    # Apply the resize operation to the input file with the input parameters of the function
    os.system("ffmpeg -i " + str(input_file) + " -vf scale="+str(width)+":"+str(height)+" "+str(output_file))


#EXERCICI4
def ex4(input_video):
    # First we save the .txt with all the info from the input video ( w/ audio tracks)
    os.system("ffmpeg -i " + str(input_video) + " 2> info_ex4.txt")

    # Now we are going to diplay all the lines which contain the audio tracks information
    print("The audio tracks founded in this video are the following ones: \n")

    # We are only interested in those lines where we find the word "Audio:"
    file = open("info_ex4.txt", "r")  # Open the file
    lines = file.readlines()  # Read lines

    idx = 0

    # Loop through each line of the file
    for line in lines:
        # If the line has the string "Audio:" then we  print that line
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

    # Close file after reading
    file.close()
    print("So the broadcasting standard that can fit with the overall video will be the one(s) that is/are common in all audio tracks\n")

#Call the main function
main()


