from config import setting


from src.client import Agent
def client():

    mod=setting.MODE
    if mod =='agent':
        obj=Agent()

    else:
        raise Exception('请配置资产采集模式，如：ssh、agent、salt')
    obj.process()
#     获取数据




# MODE='Agent'
# MODE='SHH'
# MODE='SALT'