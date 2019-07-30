import configparser
import utils


def get_post_params(session,key,**kw):
    conf = configparser.ConfigParser()
    conf.read(utils.BASE_DIR+'\\config\\ConfigParser.ini',encoding='utf-8')
    value = conf.get(session,key)
    params= value.split('?')[1]

    if isinstance(value,dict):
        try:
            return kw
        except:
            pass



def get(session,key):
    conf =configparser.ConfigParser()
    conf.read(utils.BASE_DIR+'\\config\\ConfigParser.ini',encoding='utf-8')
    value = conf.get(session,key)
    return value


