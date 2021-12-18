# Importing all necessary libraries 
import cv2 
import os 

while True:
        file_name = input("Enter The Video Name: ")
        # Read the video from specified path 
        vid = cv2.VideoCapture(file_name + '.mp4') 

        try: 
                
                # creating a folder named images 
                if not os.path.exists(file_name): 
                        os.makedirs(file_name) 

        # if not created then raise error 
        except OSError: 
                print ('Error: Creating directory of data') 

        # frame 
        currentframe = 0

        while(True): 
                
                # reading from frame 
                ret,frame = vid.read() 

                if ret: 
                        # if video is still left continue creating images 
                        name = file_name + '/' + str(currentframe) + '.jpg'
         

                        # writing the extracted images 
                        cv2.imwrite(name, frame) 

                        # increasing counter so that it will 
                        # show how many frames are created 
                        currentframe += 1
                else: 
                        break

        print('\n')
        print("Done!")
        print('All the images are in the ' + file_name + ' folder.')
        print('\n\n')

