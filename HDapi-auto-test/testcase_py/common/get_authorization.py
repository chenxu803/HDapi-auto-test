#从配置文件中获取访问权限信息
def get_Authorization():
    fp=open('D:\HDapi-auto-test\config\Authorization.txt')
    info=fp.read()
    fp.close()
    return info
