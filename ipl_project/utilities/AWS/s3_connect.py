a=1
p=2
import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id=a,
    aws_secret_access_key=  p,
    region_name='eu-north-1'  # Just the region code
) 

response = s3.list_objects_v2(Bucket='ipl-all-data')
print(response['Contents'][0]['Key'])

response=s3.upload_file(r"E:\Sivadatt K\ipl_project\data\ipl_json_files\335982.json", "ipl-all-data", "335982.json")
print(response)

respose=s3.delete_object(Bucket='ipl-all-data', Key='335982.json')