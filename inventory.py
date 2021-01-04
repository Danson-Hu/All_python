#! /usr/bin/python3.5

def displayInventory(stuff):
    total = 0
    print("Inventory：")
    for k, v in stuff.items():  # 获取背包的键-值对：k为键，v为值
        print('\t' + str(v) + ' ' + k)
        total += v
    print('Total number of items: ' + str(total))


def addToInventory(inventory, addedTtems):
    for i in addedTtems:  # 循环boos奖励物品
        if i in inventory.keys():  # 如果背包存在该物品，则该物品数量加1
            inventory[i] += 1
        else:
            inventory.setdefault(i, 1)  # 如果背包没有该物品，那现在有一个了
    return inventory  # 返回更新后的字典


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}  # 初始背包--字典
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'torch', 'ruby']  # boss奖励物品--列表
stuff = addToInventory(stuff, dragonLoot)  # 更新打完boss后的背包

displayInventory(stuff)
