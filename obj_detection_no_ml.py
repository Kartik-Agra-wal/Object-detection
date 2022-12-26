import cv2

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




 

vid_capture = cv2.VideoCapture('/home/demonic/Desktop/Object detection/dynamic.mp4')

frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
out = cv2.VideoWriter('out1.mp4', cv2.VideoWriter_fourcc(
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
        out.write(frame)    
    else:
        break
 
# Release the video capture object
vid_capture.release()
out.release()
cv2.destroyAllWindows()