
from .base import BasePlugin
class MainboardPlugin(BasePlugin):
    def window(self):
        output=self.shell_cmd('***code')
        return output

    def linux(self):
        output=self.shell_cmd('*****code')
        return output



