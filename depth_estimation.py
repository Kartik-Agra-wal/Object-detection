import cv2

# distance from camera to object measured
# centimeter
Known_distance = 30

# width of objecy in the real world or Object Plane
# centimeter
Known_width = 5.5

# Colors
GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# defining the fonts
fonts = cv2.FONT_HERSHEY_COMPLEX






def colorProfiles(n):
    if n == 0 :
        name = "Sprite"
        hsv_lower = (36,50,70)
        hsv_upper = (89,255,255)
        return (name,hsv_lower,hsv_upper)
    if n == 1 :
        name = "Coke"
        hsv_lower = ( 159,50,70)
        hsv_upper = (180,255,255)
        return (name,hsv_lower,hsv_upper)







# focal length finder function
def Focal_Length_Finder(measured_distance, real_width, width_in_rf_image):

	# finding the focal length
	focal_length = (width_in_rf_image * measured_distance) / real_width
	return focal_length

# distance estimation function
def Distance_finder(Focal_Length, real_width, width_in_frame):

	distance = (real_width * Focal_Length)/width_in_frame

	# return the distance
	return distance




# reading reference_image from directory
ref_image = cv2.imread("Ref_image.jpg")

# find the object width(pixels) in the reference_image
hsv = cv2.cvtColor(ref_image, cv2.COLOR_BGR2HSV)
rects = {}

for i in range(2):
    name, hsv_lower, hsv_upper = colorProfiles(i)
    mask = cv2.inRange(hsv,hsv_lower,hsv_upper)
    conts, herirarchy = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    try:
        biggest = sorted(conts,key = cv2.contourArea,reverse=True)[0]   
    except:
        pass
    rect = cv2.boundingRect(biggest)
    x,y,w,h = rect
    if w < 50 or h < 50:
        continue
    ref_image_width=w


Focal_length_found = Focal_Length_Finder(
	Known_distance, Known_width, ref_image_width)

print(Focal_length_found)





vid_capture = cv2.VideoCapture('/home/demonic/Desktop/Object detection/dynamic.mp4')

frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
out = cv2.VideoWriter('out_distance.mp4', cv2.VideoWriter_fourcc(
   'M', 'J', 'P', 'G'), 30, (frame_width, frame_height))



if (vid_capture.isOpened() == False):
  print("Error opening the video file")
else:

  fps = vid_capture.get(5)


  frame_count = vid_capture.get(7)

 
while vid_capture.isOpened():
    ret, frame = vid_capture.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        rects = {}

        for i in range(2):
            name, hsv_lower, hsv_upper = colorProfiles(i)
            mask = cv2.inRange(hsv,hsv_lower,hsv_upper)
            conts, herirarchy = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            try:
                biggest = sorted(conts,key = cv2.contourArea,reverse=True)[0]   
            except:
                pass
            rect = cv2.boundingRect(biggest)
            x,y,w,h = rect
            if w < 50 or h < 50:
                continue
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            cv2.putText(frame, name, (x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            width=w
            if width!= 0:
        
            # finding the distance by calling function
            # Distance finder function need
            # these arguments the Focal_Length,
            # Known_width(centimeters),
            # and Known_distance(centimeters)
                Distance = Distance_finder(
                    Focal_length_found, Known_width, width)

                # draw line as background of text
                cv2.line(frame, (x+w, y+h), ((x+w+200), y+h), RED, 32)
                cv2.line(frame, (x+w, y+h), ((x+w+200), y+h), BLACK, 28)

                # Drawing Text on the screen
                cv2.putText(
                    frame, f"Distance: {round(Distance,2)} CM", ((x+w), (y+h)),
                fonts, 0.6, GREEN, 2)
        out.write(frame)    
    else:
        break
 
# Release the video capture object
vid_capture.release()
out.release()
cv2.destroyAllWindows()



