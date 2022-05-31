# # #
# # # class Hero:
# # #     def __init__(self, nickname,aggressivity,life_value):
# # #         self.nickname = nickname
# # #         self.aggressivity = aggressivity
# # #         self.life_value = life_value
# # #     def attack(self, enemy):
# # #         print('Hero attack')
# # #
# # # class Garen(Hero):
# # #     camp = 'Demacia'
# # #     def attack(self, enemy): #self=g1,enemy=r1
# # #         # self.attack(enemy) #g1.attack(r1)，这里相当于无限递归
# # #         Hero.attack(self,enemy)  # 引用 父类的 attack，对象会去跑 父类的 attack
# # #         print('from garen attack')  # 再回来这里
# # #
# # #     def fire(self):
# # #         print('%s is firing' % self.nickname)
# # #
# # # class Riven(Hero):
# # #     camp = 'Noxus'
# # #
# # # g1 = Garen('garen', 18, 200)
# # # r1 = Riven('rivren', 18, 200)
# # # g1.attack(r1)
# # # # print(g1.camp)
# # # # print(r1.camp)
# # # # g1.fire()
# # class Equip: #武器装备类
# #     def fire(self):
# #         print('我是暴风大剑，攻击力加999')
# #     def fire1(self):
# #         print('我是暴风2大剑，攻击力加999')
# #
# # class Riven: #英雄Riven的类,一个英雄需要有装备,因而需要组合Equip类
# #     camp='Noxus'
# #     def __init__(self,nickname):
# #         self.nickname=nickname
# #         self.equip=Equip() #用Equip类产生一个装备,赋值给实例的equip属性
# #
# # r1=Riven('亚瑟')
# # r1.equip.fire1() # 可以使用组合的类产生的对象所持有的方法，对其他英雄造成999的伤害
# #
# # # 我是暴风大剑，攻击力加999
# # from collections import OrderedDict
# # my_dict=OrderedDict()
# # my_dict['jen']="python"
# # my_dict['ken']="python"
# # for name,language in my_dict.items():
# #     print(name,language)
# # my_dict={}
# # my_dict['3jen']="python"
# # my_dict['2ken']="python"
# # my_dict['1ken']="python"
# # for name,language in my_dict.items():
# #     print(name,language)
# import unittest
#
#
# class Employee():
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def give_raise(self, quanty=5000):
#         self.salary += quanty
#         return self.salary
#
#
# class Test(unittest.TestCase):
#     def setUp(self) -> None:
#         self.emp = Employee("mac", 1000)
#
#     def test_give_default_raise(self):
#         self.emp.give_raise()
#         self.assertEqual(6000, self.emp.salary)
#
#
# if __name__ == '__main__':
#     unittest.main()
