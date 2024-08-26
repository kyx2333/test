# # 导入
# import yaml
# import requests
# # 定义文件路径
# path = 'C:\\Users\\14238\\Desktop\\test\\pytest_day01\\data\\data1.yaml'

# def get_test_data(path):
#     case = []  # 存储测试用例名称
#     http = []  # 存储请求对象
#     expected = []  # 存储预期结果
#     with open(path) as f:
#         dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
#         # print(type(dat))
#         # print(type(dat['tests']))
#         # print(dat.get('tests'))
#         # print(dat.get('http'))
#         # for index,value in dict(dat['tests']).items():
#         #     dt = {
#         #         index: value
#         #     }
#         #     print(dt.get('case'))
#         for i in enumerate(dat):
#             print(type(i))
#         # print(dat.get('tests'))
#         # for td in dat:
#         #     print(td.get('case'))
#         #     case.append(td.get('case', ''))
#         #     http.append(td.get('http', {}))
#         #     expected.append(td.get('expected', {}))
#     parameters = zip(case, http, expected)
#     return case, parameters

# cases, parameters = get_test_data(path)
# list_params=list(parameters)

# class TestInTheaters(object):
#     def test_in_theaters(self):
#         host = "http://api.douban.com"
#         r = requests.request(list_params[0][1]["method"],
#                              url=host + list_params[0][1]["path"],
#                              headers=list_params[0][1]["headers"],
#                              params=list_params[0][1]["params"])
#         response = r.json()
#         assert response["count"] == list_params[0][2]['response']["count"]
#         assert response["start"] == list_params[0][2]['response']["start"]
#         assert response["total"] == len(response["subjects"])
#         assert response["title"] == list_params[0][2]['response']["title"], "实际的标题是：{}".format(response["title"])


a = int(input())
sum = 0
for i in range(0,a+1):
    sum = sum + i
print(sum)