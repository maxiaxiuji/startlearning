from src.plugins.basic import BasicPlugin
from config import setting
import importlib

def get_server_info(hostname=None):
    '''获取服务器信息'''
    response=BasicPlugin(hostname).execute()

    if not response.status:
        return response
    #     'disk': 'src.plugins.disk.DiskPlugin',
    for k,v in setting.PLUGINS.items():
        module_path,cls_name=v.rsplit('.',1)
        # print(module_path,cls_name)
        cls=getattr(importlib.import_module(module_path),cls_name)

        # 映射找到
        obj=cls(hostname).execute()
        # print(111111111111111111111)

        #获取数据
        response.data[k]=obj
        print(k,obj)



# importlib.模块（模块路径）
    return response


if __name__ == '__main__':
    ret=get_server_info()
