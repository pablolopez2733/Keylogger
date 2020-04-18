import base64,os

f=open('base64-string.txt','r')
string=f.read()
f.close()
photo=base64.b64decode(string)
f=open('snap.png','wb')
f.write(photo)
f.close()
