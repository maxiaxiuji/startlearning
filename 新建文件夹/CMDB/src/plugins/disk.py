from .base import BasePlugin
import os
import traceback
import  re

from lib.response import BaseResponse
class DiskPlugin(BasePlugin):


    def window(self):

        output=self.shell_cmd('***code')
        return output

    def linux(self):
        response=BaseResponse()
        try:
            if self.test_mode:
                from config.setting import BASE_DIR
                output=open(os.path.join(BASE_DIR,'files/disk.out'),'r').read()

            else:
                shell_command='sudo MegaCli  -PDList -aALL'
                output=self.shell_cmd(shell_command)
            response.data=self.parse(output)


        except Exception as e:
            msg = "%s linux disk plugin error: %s"
            response.status = False
            response.error=msg %(self.hostname,traceback.format_exc())

        return response

    def parse(self,content):
        # 解析shell命令返回结果
        # :param
        # content: shell
        # 命令结果
        # :return:解析后的结果
          response={}
          result=[]
          for row in content.split('\n\n\n\n'):
              result.append(row)

          for item in result:
              temp_dict = {}
              for row in item.split('\n'):
                  if not row.strip():
                      continue
                  if len(row.split(':')) != 2:
                      continue
                  key, value = row.split(':')
                  name = self.mega_patter_match(key)
                  if name:
                      if key == 'Raw Size':
                          raw_size = re.search('(\d+\.\d+)', value.strip())
                          if raw_size:

                              temp_dict[name] = raw_size.group()
                          else:
                              raw_size = '0'
                      else:
                          temp_dict[name] = value.strip()
              if temp_dict:
                  response[temp_dict['slot']] = temp_dict
          return response

    @staticmethod
    def mega_patter_match(needle):
          grep_pattern = {'Slot': 'slot', 'Raw Size': 'capacity', 'Inquiry': 'model', 'PD Type': 'pd_type'}
          for key, value in grep_pattern.items():
              if needle.startswith(key):
                  return value
          return False




