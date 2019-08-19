import pillow
im=Image.open('E:\\pictures\\壁纸\\1.jpg') #打开图片
print(im.format, im.size, im.mode)  #打印图片格式、尺寸
im.thumbnail((200, 100))  #压缩图片
im.save('E:\\pictures\\壁纸\\thumb.jpg', 'JPEG')  #保存图片