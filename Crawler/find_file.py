import os
# 定义文件操作的函数
# 输入一个地址，输出文件名和二进制信息
def find_file(path):
    img_ext = ['.bmp', '.jpeg', '.gif', '.psd', '.png', '.jpg']
    for x in os.listdir(path):
        # print(x)
        if os.path.splitext(x)[1] in img_ext:
            filename = os.path.basename(x)
            fp = open(path+'\\'+filename, 'rb')
            img = fp.read()
            # print(filename,img)
            jpginfo = {}
            jpginfo[filename]=img
            return jpginfo
        else:
            pass

path = 'D:\\OneDrive - Cooperative Office System\\Tupian图片\\主题设置\\NIEr'

print('s',find_file(path))
# jpg={fn: img for img, fn in find_file(path)}
# print(jpg)

