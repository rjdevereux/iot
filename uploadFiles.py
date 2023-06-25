import boto3
s3 = boto3.resource('s3')
s3Client = boto3.client('s3')

from os import listdir
from os.path import isfile, join
import shutil

onlyfiles = [f for f in listdir('/home/pi/logs') if isfile(join('/home/pi/logs', f))]
for fileName in onlyfiles:
    s3Client.upload_file('/home/pi/logs/' + fileName, 'tir-na-nog--data', fileName)
    shutil.move("/home/pi/logs/" + fileName,"/home/pi/logs/uploaded/" + fileName)
    print(fileName)


