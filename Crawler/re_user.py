import re
data='<div class="m-cmmt"><div class="iptarea">' \
     '<div class="head"><img src="http://s4.music.126.net/style/web2/img/default/default_avatar.jpg?param=50y50"></div>'
print(data)

# img = re.findall(r'<img [\w./]+',data)
img = re.findall(r'<img(.*?)>',data)
print(img)