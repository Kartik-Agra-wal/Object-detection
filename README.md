# Object-detection
Object detection


## Files
This repo contains three files

**1.detection_with_tracker.py**
This is the implementation of object detection on cans using yolov5 and norfair tracker

https://github.com/tryolabs/norfair

The script is tested on three samples:
1. static objects 



https://user-images.githubusercontent.com/87862080/209578105-d72573dc-885c-466b-89ec-5331a981ad58.mp4





2. moving object



https://user-images.githubusercontent.com/87862080/209577749-583e2aa4-9d8f-4e4a-a5ee-c5c5b669175a.mp4



3. static and moving objects 


https://user-images.githubusercontent.com/87862080/209577761-564ec7ea-514d-4fed-ae44-06b705a72023.mp4



**2. obj_detection_no_ml.py**
This scripts uses color masks to detect coke and sprite cans wihtout using any ml model.
1. on static objects


https://user-images.githubusercontent.com/87862080/209577840-384f1529-8383-4a7d-90e2-2b5e2d983330.mp4

2. on moving object



https://user-images.githubusercontent.com/87862080/209577872-a974d98a-385a-45b3-8359-432189a6b143.mp4


**3. depth_estimation.py**
This script uses a reference image to calcluate the focal lenghth of the camera using known paramaeters and uses it to estimate objects depth detected by the ml model or the color mask.

https://user-images.githubusercontent.com/87862080/209578003-c5397a25-6116-46b9-925b-728f8cba5850.mp4



https://user-images.githubusercontent.com/87862080/209578018-6f71a225-e700-4cad-a926-fc4842168cbd.mp4


