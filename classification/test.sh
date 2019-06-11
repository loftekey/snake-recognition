gcloud ml-engine jobs submit training `whoami`_object_detection_pets_`date +%m_%d_%Y_%H_%M_%S` \
    --runtime-version 1.12 \
    --job-dir=gs://dprojectbucket/model_dir \
    --packages dist/object_detection-0.1.tar.gz,slim/dist/slim-0.1.tar.gz,/tmp/pycocotools/pycocotools-2.0.tar.gz \
    --module-name object_detection.model_main \
    --region us-central1 \
    --config object_detection/samples/cloud/cloud.yml \
    -- \
    --model_dir=gs://dprojectbucket/model_dir \
    --pipeline_config_path=gs://dprojectbucket/data/faster_rcnn_resnet101_pets.config