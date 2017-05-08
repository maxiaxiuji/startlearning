class ArgvHandler(object):
    """接收用户参数"""

    def __init__(self,sys_args):
        self.sys_args = sys_args

    def help_msg(self,error_msg=''):

        """Help"""
        msgs = """
        %s
        run 开启交互程序
        """%error_msg
        exit(msgs)

    def cmd(self):
        """根据用户输入de参数 ，调用对应的方法'"""
        if len(self.sys_args) == 1:
            # 如果命令行什么也没输入
            self.help_msg()

        if hasattr(self, self.sys_args[1]):
            # 获取命令行路径 code
            fun = getattr(self, self.sys_args[1])
            # 执行该函数
            a=fun()


        else:
            self.help_msg("由于我们正在完善系统，不提供（%s）该服务" % self.sys_args[1])

    def runb(self):
        '''启动交互程序'''
        from backend.ssh_interactive import SshHandle
        obj=SshHandle(self)
        obj.interactive()
