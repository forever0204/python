"""创建一个从单词到其出现情况的映射"""
import sys
import re
import collections
WORD_RE = re.compile(r'\w+')
index = collections.defaultdict(list)
# 把 list 构造方法作为 default_factory 来创建一个 defaultdict。
with open(sys.argv[1], encoding='utf-8') as fp:
    # 打开文件
    for line_no,line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            # print(word)
            column_no = match.start()+1
            # print(column_no)
            location = (line_no,column_no)
            # 这其实是一种很不好的实现，这样写只是为了证明论点
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences
            print(index)
            index[word].append(location)
            # index.setdefault(word, []).append(location)
            # 以字母顺序打印出结果
for word in sorted(index,key=str.upper):
    print(word,index[word])