import os
from minio import Minio
from dotenv import load_dotenv

load_dotenv("minio.env")

client = Minio(
    os.getenv("MINIO_ENDPOINT").replace("http://", ""),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False
)

bucket = os.getenv("MINIO_BUCKET")
if not client.bucket_exists(bucket):
    client.make_bucket(bucket)

for filename in os.listdir("../models"):
    file_path = f"../models/{filename}"
    client.fput_object(bucket, filename, file_path)
    print(f"Uploaded {filename} to MinIO bucket '{bucket}'")
