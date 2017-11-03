########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, json

img_filename = sys.argv[1]

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'Input Key',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
})

try:
    conn = http.client.HTTPSConnection('southeastasia.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, open(img_filename,'rb'), headers)
    response = conn.getresponse()
    data = response.read() 
    print(data)
    conn.close()
except Exception as e:
    print(e.args)

####################################