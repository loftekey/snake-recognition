# snake-recognition

## dataset folder
this folder contains scripts for downloading images and annotaion data from google and imagenet.

## Pre-process
this folder contains files to transfer images and annotation files to meet the requirement of object detection api input.

## classification
this part is about using VGG model to train classification model.

## object detection
this part contains the pipeline configure file and possible commands used in this project. Also the installation info are involved in this part.

## mobile application
in android folder, there is a description of building and running apk.

# import
after installing necessary python packages
this project takes advantage of https://github.com/tensorflow/models.git
many processes are conducted under the path/to/model/research folder

# overall procedures
1. download raw images
2. preprocess images
3. train classification model
4. train object detection model
5. turn models into frozen graph suitable for adroid platform