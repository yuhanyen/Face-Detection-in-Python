import requests
from json import JSONDecoder
http_url='https://api-cn.faceplusplus.com/facepp/v3/detect'
key = "Input Key"
secret = "Input Secret"
filepath ="students1.jpg"
data = {"api_key": key, "api_secret": secret, "return_landmark":"1"}
files = {"image_file": open(filepath, "rb")}
response = requests.post(http_url, data=data, files=files)
req_con = response.content.decode('utf-8')
req_dict = JSONDecoder().decode(req_con)
print(req_dict)