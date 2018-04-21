def say_hi(name,age):

    return "Hi, My name is %s and I'm %d years old" % (name,age)

def correct_sentence(text:str) -> str:
    #首字母大写,末尾加句号
    if text[0].isupper():
        pass
    else:
        text = text.replace(text[0], text[0].upper(),1)
    if text[len(text)-1] != '.':
        text = text + '.'
    else:
        pass
    return text
def first_word(text:str) ->str:
    # text = text.split()[0].split(',')[0]
    # 匹配第一个单词，可能出现的情况，单个单词，空格开头，.开头等
    text = text.replace('.',' ').replace(',',' ').split()[0]
    return text

if __name__ == '__main__':
   print(correct_sentence('greeting,friends'))
   print(first_word("... and so on ..."))