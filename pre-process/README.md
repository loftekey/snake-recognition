#pre-process
We need to rename all the images files and xml files as snakespecies_xxxx.*
this is the requirements of google cloud ai platform. Also the we need to change the information in annotation files.
And for classification, the script also need the read snakespecies from name to set labels
Additonally, we remove images whoes extension is not jpg by shell command:
```
rm -r Path/To/!(*.jpg)
```

#tf-record.py
this is script given by google keras object detection tutorial.
here is the processed data: https://drive.google.com/file/d/1IsndL6TNI99yNIkynQzZMwYhbpaTqQeG/view?usp=sharing
it is said available for people in the unimelb as the account of this drive is student email

#command
From tensorflow/models/research/:
```
python object_detection/dataset_tools/create_pet_tf_record.py \
    --label_map_path=object_detection/data/pet_label_map.pbtxt \
    --data_dir=`pwd` \
    --output_dir=`pwd`
```
