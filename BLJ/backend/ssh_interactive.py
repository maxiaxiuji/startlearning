from django.contrib.auth import authenticate
# 验证登陆

from backend import paramiko_ssh

from web import models

class SshHandle(object):
    """堡垒机交互脚本"""
    def __init__(self,argv_handler_item):
        self.argv_handler_item=argv_handler_item
        self.models=models
    def auth(self):
        """认证程序"""
        count = 0
        while count < 3:
            username = input("堡垒机账号:").strip()
            password = input("Password:").strip()
            user=authenticate(username=username,password=password)
            # 用户验证
            if user:
                self.user=user
                return True
            else:
                count +=1

    def interactive(self):
        """启动交互脚本"""

        if self.auth():
            '''验证'''
            print("验证通过...")
            host_goup_list=self.user.host_groups.all()
            # 获取属于对象的主机组列表
            while True:
                host_goup_list=self.user.host_groups.all()
                for index,host_goup_obj in enumerate(host_goup_list):
                    print("%s.\t[%s](%s)"%(index,host_goup_obj.name,host_goup_obj.host_to_remote_users.count()))

                print('z.\t未分组主机[%s]'%(self.user.host_to_remote_users.count()))
                choice = input("请选择主机组>>>：")
                if choice.isdigit():
                    choice=int(choice)
                    selected_host_group=host_goup_list[choice]
                elif choice =='z':
                    selected_host_group = self.user

                while True:
                    """ 没有分组"""
                    for  index,host_to_user_obj in enumerate(selected_host_group.host_to_remote_users.all()):

                        print("%s.\t%s" % (index, host_to_user_obj))
                    choice = input("请选择主机>>>：").strip()

                    if choice.isdigit():
                        choice = int(choice)
                        selected_host_to_user_obj = selected_host_group.host_to_remote_users.all()[choice]
                        print('------->%s'% selected_host_to_user_obj)
                        paramiko_ssh.ssh_connect(self,selected_host_to_user_obj)
                    #     远程建立连接
                    elif choice =='b':
                        break




