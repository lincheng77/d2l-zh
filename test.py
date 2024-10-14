import torch

class test:
    def __init__(self):
        print("我爱你中国")
        print(torch.version.cuda)
        print(torch.cuda.is_available())

# 创建类的实例
t = test()
