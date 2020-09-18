import random
import time

# 假设游戏场景为范围（x, y）为0<=x<=10，0<=y<=10
# 游戏生成1只乌龟和10条鱼
# 它们的移动方向均随机
# 乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
# 当移动到场景边缘，自动向反方向移动
# 乌龟初始化体力为100（上限）
# 乌龟每移动一次，体力消耗1
# 当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
# 鱼暂不计算体力
# 当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束

class Turtle:
    def __init__(self):
        self.body = 100#体力
        self.x = random.randint(1,10)#坐标
        self.y = random.randint(1,10)
    def move(self):
        self.axis=random.choice([0,1])#移动坐标轴，0x轴，1y轴
        self.dir=random.choice([-1,1])#移动方向
        self.step=random.choice([1,2])#移动步长
        self.length=self.dir*self.step
        if self.x >=0 and self.y <=10:
            if self.axis == 0:
                self.x=self.x+self.length
            else:
                self.y=self.y+self.length
        elif self.x <0
        
    def bodychange(self):
        pass
    def eat(self)；
        pass

    
    pass
class Fish:
    def __init__(self):
        pass
    def move(self):
        pass
if __name__=="__main__":
