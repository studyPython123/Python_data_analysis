# Author: 邵世昌
# CreatTime: 2024/11/14
# FileName: 不同高校类型的记录
def function(data):
    data_set = set(data)
    data_dict = {item:0 for item in data_set}
    for item in data_set:
        data_dict[item] = data.count(item)
    return data_dict
data = ["综合","理工","综合","综合","综合","综合","综合","综合","综合","综合","综合","师范",
        "理工""综合","理工","综合","综合","综合","综合","综合","理工","理工","农林", "理工","综合",
        "理工","理工","理工","师范","综合","理工","理工","综合","理工","综合","综合","理工","农林","民族","军事"]
print(sorted(function(data).items(), key=lambda x: x[1], reverse=True))
