import os
import shutil
import chardet
import time
import datetime


class FileSystem():
    __encoding = ''  # 读入文件的编码模式
    __basename = ''  # 读入文件的basename
    __directory = ''  # 读入文件所在的目录
    __filesize = ''  # 读入文件的大小

    def __init__(self):
        pass

    @property
    def basename(self):
        return self.__basename

    @property
    def encoding(self):
        return self.__encoding

    @property
    def directory(self):
        return self.__directory

    @property
    def filesize(self):
        return self.__filesize

    #
    # @methods: 读取传入文件的字符串
    # @params: file 传入文件
    # @return: none
    #
    def stringReader(self, file, encoding=None):
        if not self.exists(file):
            raise FileNotFoundError()
        else:
            if encoding == None:
                encode = self.getEncode(file)
            with open(file, 'r', encoding=encode) as f:
                for line in f.readline():
                    print(line.strip())
            return 'done'

    #
    # @methods: 以二进制模式读取传入文件
    # @params: file 传入文件
    # @return: none
    #
    def BinaryReader(self, file):
        if not self.exists(file):
            raise FileNotFoundError()
        else:
            with open(file, 'rb') as f:
                f.read()
            return 'done'

    #
    # @methods: 检测传入文件的编码方式
    # @params: file 传入文件
    # @return: none
    #
    def getEncode(self, file):
        try:
            with open(file, 'rb') as f:
                data = f.read()
                encode = (chardet.detect(data))['encoding']
                return encode
        except IOError as e:
            print('Exception:', e)

    #
    # @methods: 检测传入文件是否存在
    # @params: file 传入文件
    # @return: boolean
    #
    def exists(self, file):
        if not os.path.isfile(file):
            return False
        if not os.path.exists(file):
            return False
        else:
            return True

    #
    # @methods: 检测传入文件的大小
    # @params: file 传入文件
    # @return: int 文件的大小(单位:字节)
    #
    def filesize(self, file):
        if not self.exists(file):
            raise FileNotFoundError()
        else:
            return os.path.getsize(file)

    #
    # @methods: 删除传入的文件
    # @params: file 传入文件
    # @return: boolean (删除与否)
    #
    def delete(self, file):
        try:
            if os.path.isdir(file):
                os.rmdir(file)
                return True
            if os.path.isfile(file):
                os.remove(file)
                return True
            return False
        except FileNotFoundError as e:
            print('Exception ', e)
        except Exception('delete %s failed' % file) as e:
            print('Exception ', e)

    #
    # @methods:         拷贝文件
    # @params: file     传入文件或目录
    # @return: boolean  拷贝成功与否
    #
    def copy(self, src_file, dst_file):

        if os.path.isdir(src_file):
            # 使用copytree()
            # 复制文件夹的一个棘手的问题是对于错误的处理。 例如，在复制过程中，函数可能会碰到损坏的符号链接，
            # 因为权限无法访问文件的问题等等。为了解决这个问题，
            # 所有碰到的问题会被收集到一个列表中并打包为一个单独的异常，到了最后再抛出
            try:
                shutil.copytree(src_file, dst_file)
            except shutil.Error as e:
                for src_file, dst_file, msg in e.args[0]:
                    # msg
                    print(src_file, dst_file, msg)
            return True
        if os.path.isfile(src_file):
            shutil.copy(src_file, dst_file)
            return True
        return False

    def search(self, top_dir, file_name):
        for relpath, dirs, files in os.walk(top_dir):
            if file_name in files:
                full_path = os.path.join(top_dir, relpath, file_name)
                print(os.path.normpath(os.path.abspath(full_path)))

    #
    # @methods:         获取传入文件的修改时间
    # @params: file     传入文件或目录
    # @return: string   返回时间的字符串类型
    #
    def mtime(self, file):
        if not self.exists(file):
            raise FileNotFoundError()
        else:
            time = os.path.getmtime(file)
            return self.__timeStampToTime(time)

    #
    # @methods:         获取传入文件的创建时间
    # @params: file     传入文件或目录
    # @return: string   返回时间的字符串类型
    def ctime(self, file):
        if not self.exists(file):
            raise FileNotFoundError()
        else:
            t = os.path.getctime(file)
            return self.__timeStampToTime(t)

    #
    # @methods:         获取传入文件的访问时间
    # @params: file     传入文件或目录
    # @return: string   返回时间的字符串类型
    def actime(self, file=None):
        if not self.exists(file):
            raise FileNotFoundError()
        else:
            time = os.path.getatime(file)
            str_time = self.__timeStampToTime(time)
            return str_time

    #
    # @methods:          时间戳转换人可认知的时间
    # @params: timestamp 时间戳
    # @return: string    时间的字符串类型
    #
    def __timeStampToTime(self, timestamp):
        timeStruct = time.localtime(timestamp)
        return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)
