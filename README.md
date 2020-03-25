# Simple Flask on Cloud Run

## How to deploy
please make sure you are working on the right project.
`gcloud config set project $PROJECT_NAME`
```
make enable-cloud-run
make cloud-build
make cloud-run
```
Note: some of these command will ask for your project name again
