# encoding:utf-8

import requests
import base64

'''
人脸搜索
'''

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        data = base64.b64encode(fp.read())
        return data

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"

img = get_file_content('metal.png')

params = {'image':img,'image_type':'BASE64','group_id_list':'dcbstudent1'}
access_token = '24.7bddb2d8cece1e8dc2aac2377968122b.2592000.1625450663.282335-10439231'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())

