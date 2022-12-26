# Object-detection
Object detection


## Files
This repo contains three files

**1.detection_with_tracker.py**
This is the implementation of object detection on cans using yolov5 and norfair tracker.

You can install the tracker package from their repo.

https://github.com/tryolabs/norfair

You also need the model
https://drive.google.com/file/d/1FVVLCxjBQjz1d-lEP0eOxT96MvKFm33R/view?usp=sharing

The script is tested on three samples:
1. static objects 

https://drive.google.com/file/d/1Vcs12jlA15qiITGhBCDqfqSWpzex_A2B/view?usp=sharing


2. moving object
https://drive.google.com/file/d/1oM85jwkMhTeP994YYnwTEBZvXTR-UPWu/view?usp=sharing



3. static and moving objects 

https://drive.google.com/file/d/1TWf41zT4TByZjuYJqxhRz8dKR9LJs0hf/view?usp=sharing



**2. obj_detection_no_ml.py**
This scripts uses color masks to detect coke and sprite cans wihtout using any ml model.
1. on static objects


https://drive.google.com/file/d/1yKokKINwFehH0zpI4a0Rs1AKk4hnUYo3/view?usp=sharing

2. on moving object

https://drive.google.com/file/d/1r61vilEaqfLnR6R00atUHv51A6AsnPx8/view?usp=sharing


**3. depth_estimation.py**
This script uses a reference image to calcluate the focal lenghth of the camera using known paramaeters and uses it to estimate objects depth detected by the ml model or the color mask.

https://drive.google.com/file/d/1zPFMDtL5YMpjjAwP3VFBlszggrMB67vd/view?usp=sharing


https://drive.google.com/file/d/1lSxhcf8_b2qwuCe_3qSrbXNGpDvb8Fz3/view?usp=sharing


