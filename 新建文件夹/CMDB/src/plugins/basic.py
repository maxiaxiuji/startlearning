import traceback
from .base import BasePlugin
from lib.response import BaseResponse

class BasicPlugin(BasePlugin):
    def os_platform(self):
         """
        获取系统平台

        :return:
        """
         if self.test_mode:
             output='linux'
             # print(output, 88888888888888888888)
         else:
             output=self.shell_cmd('uname')
         return output.strip()

    def os_verision(self):
        """
              获取系统版本
              :return:
              """
        if self.test_mode:
            output='''CentOS release 6.6 (Final)\nKernel \r on an \m'''
        else:
            output=self.shell_cmd('cat/etc/issue')
        result=output.strip().split('\n')[0]
        return result

    def os_hostname(self):
        '''获取主机名'''
        if self.test_mode:
            output='c1.com'
        else:
            output=self.shell_cmd('hostname')

        return output.strip()

    def linux(self):
        response=BaseResponse()
        # print(90909090)

        try:
            ret={
                'os_platform':self.os_platform()
                ,'os_version':self.os_verision()
                ,'hostname':self.os_hostname(),

            }
            response.data=ret
        except Exception as e:
            msg = "%s BasicPlugin Error:%s"
            self.logger.log(msg % (self.hostname, traceback.format_exc()), False)
            response.status = False
            response.error = msg % (self.hostname, traceback.format_exc())
        return response