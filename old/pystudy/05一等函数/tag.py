def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    #   class 是python的关键字，此处改写
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                            for attr, value
                            in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                        (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

print(tag('p','hello'))
print(tag('p', 'hello', 'world', cls='sidebar'))
my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
        'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))
# 在 my_tag 前面加上 **，字典中的所有元素作为单个参数传入，同名键会绑定到对应
# 的具名参数上，余下的则被 **attrs 捕获。