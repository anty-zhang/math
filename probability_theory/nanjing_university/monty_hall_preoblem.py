# -*- coding: utf-8 -*-
import random
is_change_list = [True, False]


def monty_hall(is_change):
    echo = 1000000
    match_num = 0

    car = random.randint(1, 3)

    for i in range(echo):
        first_choose = random.randint(1, 3)
        # left = -1
        if first_choose == car:
            # 第一次选到汽车，第二次随便选择一个
            left = (first_choose + 1) % 3 + 1
        else:
            # 第一选择了山羊，那第二次一定是汽车
            left = car

        # second_choose = -1
        if is_change:
            second_choose = left
        else:
            second_choose = first_choose

        if second_choose == car:
            match_num += 1
    print("{0}选择汽车的概率为: {1}".format("change" if is_change else "not change", float(match_num/echo)))


for c in is_change_list:
    monty_hall(c)
