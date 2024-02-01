#!/bin/bash

REGISTRY_URL="us-docker.pkg.dev"
PROJECT_ID="mlops-405823"
REPOSITORY="repo1"

#------------------------------------------------- image_read_data
SOURCE_IMAGE="image_read_data"
TARGET_IMAGE="image_read_data"

# gcloud auth configure-docker $REGISTRY_URL

#link local docker image to revised image name as per GCP specifications
docker tag $SOURCE_IMAGE $REGISTRY_URL/$PROJECT_ID/$REPOSITORY/$TARGET_IMAGE 

#docker push to google cloud artifact registry
docker push $REGISTRY_URL/$PROJECT_ID/$REPOSITORY/$TARGET_IMAGE

#------------------------------------------------- image_display_stat
SOURCE_IMAGE="image_display_stats"
TARGET_IMAGE="image_display_stats"

# gcloud auth configure-docker $REGISTRY_URL

#link local docker image to revised image name as per GCP specifications
docker tag $SOURCE_IMAGE $REGISTRY_URL/$PROJECT_ID/$REPOSITORY/$TARGET_IMAGE 

#docker push to google cloud artifact registry
docker push $REGISTRY_URL/$PROJECT_ID/$REPOSITORY/$TARGET_IMAGE

#docker run syntax
#docker run -v local_dir:/mounted_dir load_data --data_path=mounted_dir/data/train_MpHjUjU.csv
