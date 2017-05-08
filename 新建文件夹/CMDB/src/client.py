
from config import setting
import os
from lib.serialize import Json
from src import plugins
import json
import requests
import hashlib
import time

class Base(object):
    def __init__(self):
        self.key=setting.KEY

        self.asset_api=setting.ASSET_API
        self.key_name=setting.AUTH_KEY_NAME

    def auth_key(self):
        """
          接口认证
          :return:
          """

        current_time=time.time()

        app_id=self.auth_key
        print(1111111111111111,app_id)
        app_id_time="%s|%s"%(app_id,current_time,)
        md=hashlib.md5()
        md.update(bytes(app_id_time,encoding='utf-8'))
        authkey=md.hexdigest()
        authkey_time="%s|%s"%(authkey,current_time)
        print(authkey_time,11111111111111111111)
        return {self.key_name:authkey_time}



    def get_send(self):
        pass
    def post_sent(self,msg,callback=None):


        status=True
        try:
            headers={}

            headers.update(self.auth_key())



            response=requests.post(
                url=self.asset_api,
                headers=headers,
                json=msg
            )



        except Exception as e:
            response=e
            status=False

        # if callback:
        #     callback(status,response)


    def callback(self):
        """
        提交资产后的回调函数
        :param
        status: 是否请求成功
        :param
        response: 请求成功，则是响应内容对象；请求错误，则是异常对象
        :return:
        # """
        # if not status:
        #     Logger().log(str(response), False)
        #     return
        # ret = json.loads(response.text)
        # if ret['code'] == 1000:
        #     Logger().log(ret['message'], True)
        # else:
        #     Logger().log(ret['message'], False)
        pass


def process(self):
        """
        # 派生类需要继承此方法，用于处理请求的入口
        # :return:
        """
        raise NotImplementedError('you must implement process method')


class Agent(Base):
    def __init__(self):
        self.hosts_path=setting.HOSTS_DIR
#         获取主机信息路径
        self.hassys=setting.SYSTEM
        super(Agent, self).__init__()




    def get_host_informations(self):

        # 获取 当前主机的信息
        if os.path.exists(self.hosts_path):
            with open(self.hosts_path,'r') as f:
                data=f.read()
            hostname=data.strip()
            return hostname
        else:
            return None

    def create_hosts(self,hosts):
        '''写入本地主机信息'''
        if os.path.exists(self.hosts_path):
            os.makedirs(os.path.basename(self.hosts_path))
        with open(setting.HOSTS_DIR,mode='w') as f:
            f.write(hosts)
    def process(self):
        # ''''# 获取资产信息
        #         1.资产获取主机名  hostname
        #         2.本地文件hosts 获取hostname2
        ''
        servers_info=plugins.get_server_info()
        if not servers_info.status:
            return

        hostname=self.get_host_informations()
        # 获取主机信息
        if hostname:
            if hostname==servers_info.data['hostname']:

                pass
            else:
                servers_info.data['hostname']=hostname

        else:
            self.create_hosts(servers_info.data['hostname'])

        server_json = Json.dumps(servers_info.data)

        self.post_sent(server_json,self.callback)









class Ssh(Base):
    pass

class Salt(Base):
    pass


