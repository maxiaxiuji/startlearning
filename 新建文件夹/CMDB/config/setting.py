import  os


BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
''' cmdb的绝对路径'''
HOSTS_DIR=os.path.join(BASE_DIR,'config','hosts')
# hosts主机信息

MODE='agent'
# MODE='SHH'
# MODE='SALT'









# SYSTEM='WINDOW'
SYSTEM='LINUX'


PLUGINS={

    'disk': 'src.plugins.disk.DiskPlugin',
    # 'nit':'src.plugins.nit.NicPlugin',
    # 'memory':'src.plugins.memory.MemoryPlugin',
    # 'mainboard':'src.plugins.mainboard.MainboardPlugin',
    # 'cpu':'src.plugins.cpu.CpuPlugin',
}



# 是否测试模式，测试模时候数据从files目录下读取
TEST_MODE = True

# 资产信息API
ASSET_API = "http://127.0.0.1:8000/api/asset"



# 用于API认证的KEY
KEY = '299095cc-1330-11e5-b06a-a45e60bec08b'
# 用于API认证的请求头
AUTH_KEY_NAME = 'auth-key'