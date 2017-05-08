import sys,os


if __name__ == '__main__':


    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BLJ.settings")
    # 添加系统环境变量
    import django
    django.setup()

    # 从新加载一边app 不加会 报错


    from backend import main
    interactive_obj = main.ArgvHandler(sys.argv)
    # sys.argv  获取命令行
    interactive_obj.cmd()