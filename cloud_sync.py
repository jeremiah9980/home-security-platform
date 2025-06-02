import boto3
import os

s3 = boto3.client('s3')

BUCKET_NAME = "Jeremiah9980"

# Sync local logs folder to S3
for filename in os.listdir("logs"):
    filepath = os.path.join("logs", filename)
    if os.path.isfile(filepath):
        s3.upload_file(filepath, BUCKET_NAME, f"device_logs/{filename}")
        print(f"Uploaded {filename} to S3")
