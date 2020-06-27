import os
import yaml


def sum_data():
    # 空列表 存储测试数据
    sum_list = []
    # 读取yaml文件数据
    with open("./Data" + os.sep + 'sum.yaml', "r", encoding="utf-8") as f:
        # yaml读取文件
        data = yaml.safe_load(f)
        print("data：", data)
        print("values：", data.values())
        for i in data.values():
            # 添加元组数据到列表
            sum_list.append((i.get("a"), i.get("b"), i.get("c")))
    return sum_list
