import random

EnemyList = [
'gremlin',
'demon',
'sloth',
'oger'
]


def myRandomEnemy(EnemyList):
    random_num = random.randint(0,3)
    print(EnemyList[random_num])

myRandomEnemy(EnemyList)
