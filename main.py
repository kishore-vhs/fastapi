import boto3
import json
import os
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
import uvicorn
import mysql.connector
load_dotenv()
app = FastAPI()
con_name = os.getenv("HOSTNAME")
python_version  = os.getenv("PYTHON_VERSION")
@app.get("/")
def homepage():
        return f'Your API Request Is Processed By The Container ID {con_name} running Python Version {python_version}.'

@app.get("/getvpc")
def get_vpc_id_list(region)->list:
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_vpcs()
    vpc_id_list = []
    for vpc in response['Vpcs']:
        vpc_id_list.append(vpc['VpcId'])
    print(vpc_id_list)
    return vpc_id_list

@app.get("/s3")
def get_s3_buckets(region)->list:
    s3 = boto3.client('s3', region_name=region)
    response = s3.list_buckets()
    bucket_list = []
    for bucket in response['Buckets']:
        bucket_list.append(bucket['Name'])
    print(bucket_list)
    return bucket_list
@app.get("/checks3")
def check_bucket(bucket_name,region):
    s3 = boto3.client('s3', region_name=region)
    response = s3.list_buckets()
    print(response)
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    if bucket_name in buckets:
        return f"{bucket_name} exists"
    else:
        return f"{bucket_name} does not exist"
    
@app.get("/files")
def list_files_in_bucket(bucket_name, region):
    try:
       s3 = boto3.client('s3', region_name=region)
       response = s3.list_objects_v2(Bucket=bucket_name)
       file_list = []
       for obj in response['Contents']:
           file_list.append(obj['Key'])
       print(file_list)
       return file_list
    except NameError as e:
        return f"The bucket {bucket_name} does not exist." 
    except KeyError as e:
        return f"The bucket {bucket_name} does not exist or is empty"
    except s3.exceptions.ClientError as e:
        return f"The bucket {bucket_name} does not exist in your account."