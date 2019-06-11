Here is the official tutorial of running this api service for reference. As I did not record the command line logs completely, the later commands may have trouble running through.
https://github.com/tensorflow/models/tree/master/research/object_detection

# tensorflow installation
```
# For CPU
pip3 install tensorflow
# For GPU
pip3 install tensorflow-gpu
pip3 install -U Cython
pip3 install -U contextlib2
pip3 install -U pillow
pip3 install -U lxml
pip3 install -U jupyter
pip3 install -U matplotlib
```

# install CoCoApi
```
git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
make
cp -r pycocotools <path_to_tensorflow>/models/research/
```

# Protobuf Compilation
```
# From tensorflow/models/research/
protoc object_detection/protos/*.proto --python_out=.
```
# Add Libraries to PYTHONPATH
```
# From tensorflow/models/research/
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
```
# set enviroment
```
export PROJECT="My_Project_ID"
export YOUR_GCS_BUCKET="dprojectbucket"
```
# create tf record and copy to google bucket
```
# From tensorflow/models/research/
python object_detection/dataset_tools/create_pet_tf_record.py \
    --label_map_path=object_detection/data/pet_label_map.pbtxt \
    --data_dir=`pwd` \
    --output_dir=`pwd`

# From tensorflow/models/research/
gsutil cp pet_faces_train.record-* gs://${YOUR_GCS_BUCKET}/data/
gsutil cp pet_faces_val.record-* gs://${YOUR_GCS_BUCKET}/data/
gsutil cp object_detection/data/pet_label_map.pbtxt gs://${YOUR_GCS_BUCKET}/data/pet_label_map.pbtxt

```
# Downloading a COCO-pretrained Model for Transfer Learning
```
wget http://storage.googleapis.com/download.tensorflow.org/models/object_detection/faster_rcnn_resnet101_coco_11_06_2017.tar.gz
tar -xvf faster_rcnn_resnet101_coco_11_06_2017.tar.gz
gsutil cp faster_rcnn_resnet101_coco_11_06_2017/model.ckpt.* gs://${YOUR_GCS_BUCKET}/data/
```
# pipeline configure
```
# From tensorflow/models/research/

# Edit the faster_rcnn_resnet101_pets.config template. Please note that there
# are multiple places where PATH_TO_BE_CONFIGURED needs to be set.
sed -i "s|PATH_TO_BE_CONFIGURED|"gs://${YOUR_GCS_BUCKET}"/data|g" \
    object_detection/samples/configs/faster_rcnn_resnet101_pets.config

# Copy edited template to cloud.
gsutil cp object_detection/samples/configs/faster_rcnn_resnet101_pets.config \
    gs://${YOUR_GCS_BUCKET}/data/faster_rcnn_resnet101_pets.config
```
# Google Cloud ML engine
```
# From tensorflow/models/research/
bash object_detection/dataset_tools/create_pycocotools_package.sh /tmp/pycocotools
python setup.py sdist
(cd slim && python setup.py sdist)
```

# submit the ML api job
```
gcloud ml-engine jobs submit training `whoami`_object_detection_pets_`date +%m_%d_%Y_%H_%M_%S` \
    --runtime-version 1.13 \
    --job-dir=gs://dprojectbucket/model_dir \
    --packages dist/object_detection-0.1.tar.gz,slim/dist/slim-0.1.tar.gz,/tmp/pycocotools/pycocotools-2.0.tar.gz \
    --module-name object_detection.model_main \
    --region us-central1 \
    --config object_detection/samples/cloud/cloud.yml \
    -- \
    --model_dir=gs://dprojectbucket/model_dir \
    --pipeline_config_path=gs://dprojectbucket/data/faster_rcnn_resnet101_pets.config

gcloud ml-engine jobs submit training `whoami`_object_detection_eval_validation_`date +%s` \
--job-dir=gs://dprojectbucket/model_dir \
--packages dist/object_detection-0.1.tar.gz,slim/dist/slim-0.1.tar.gz,/tmp/pycocotools/pycocotools-2.0.tar.gz \
--module-name object_detection.model_main \
--runtime-version 1.13 \
--scale-tier BASIC_GPU \
--region us-central1 \
-- \
--model_dir=gs://dprojectbucket/model_dir \
--pipeline_config_path=gs://dprojectbucket/data/pipeline.config \
--checkpoint_dir=gs://dprojectbucket/model_dir
```