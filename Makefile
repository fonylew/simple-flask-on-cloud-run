.PHONY: enable-cloud-run
enable-cloud-run:
    gcloud services enable run.googleapis.com

.PHONY: cloud-build
cloud-build:
    read -p "Enter project_id: " PROJECT_ID; \
    read -p "Enter image name (with tag): " IMAGE_NAME; \
    gcloud builds submit --tag gcr.io/$$PROJECT_ID/$$IMAGE_NAME

.PHONY: cloud-run
cloud-run:
    read -p "Enter project_id: " PROJECT_ID; \
    read -p "Enter image name (with tag): " IMAGE_NAME; \
    read -p "Enter Cloud Run name:" CLOUD_RUN_NAME; \
    gcloud beta run deploy $$CLOUD_RUN_NAME --image gcr.io/$$PROJECT_ID/$$IMAGE_NAME --allow-unauthenticated


