from .base import BasePlugin

class CpuPlugin(BasePlugin):
    def window(self):
        output=self.shell_cmd('****')
        return output
    def linux(self):
        output = self.shell_cmd('****')
        return output