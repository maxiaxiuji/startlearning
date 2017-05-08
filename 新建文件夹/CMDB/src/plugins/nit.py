from.base import BasePlugin


class NicPlugin(BasePlugin):
    def window(self):
        output=self.shell_cmd('****')
        return output

    def linux(self):
        output=self.shell_cmd('1111')
        return