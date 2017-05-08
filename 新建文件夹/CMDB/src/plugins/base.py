from config import setting
import subprocess
class BasePlugin(object):
    def __init__(self,hostanem=''):
        self.model_list=['sSH','salt',"agent"]
        # self.logge=Looger()
        self.hostname=hostanem
        self.test_mode=setting.TEST_MODE
        '''测试模式'''
        if setting.MODE in self.model_list:
            self.mode=setting.MODE
        else:
            raise Exception('<><><>')
    def ssh(self,cmd):
        pass
    def agent(self,cmd):
        output=subprocess.getoutput(cmd)
        return output
    def salt(self):
        pass
    def shell_cmd(self,cmd):
        # if self.mode=="SSH":
        #     ret=self.ssh(cmd)
        # elif self.mode=="Salt":
        #     ret=self.salt(cmd)
        # elif self.mode=='Agent':
        #     ret=self.agent(cmd)
        # else:
        #     raise Exception("settings.mode must be one of ['agent', 'salt', 'ssh']")
        if self.mode not in self.model_list:
            raise Exception("settings.mode must be one of ['agent', 'salt', 'ssh']")


        func=getattr(self,self.mode)

        ret=func(cmd)



        return ret



    def execute(self):

        # ret=self.shell_cmd('code')
        # if ret=='window':
        #     return self.window()
        # elif ret=='linux':
        #     print('----------------->')

            return self.linux()
        # else:
        #     pass





    def window(self):
        pass
    def linux(self):
        raise Exception('You must implement linux method.')

    def mac(self):
        pass


