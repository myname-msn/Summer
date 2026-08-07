# #最基础的接口测试形态
# import requests
# #发送一个get请求到giehub api
# response =requests.get('https://api.github.com')
#
# #打印状态码(100表示成功)
# print("状态码：",response.status_code)
#
# #打印相应内容的前200个字符
# print("相应内容：",response.text[:100])


import requests
#带参数查询 GITHUB 上的python仓库
params={
    'q':'python requests',
    'sort':'stars'
}
response=requests.get('https://api.github.com/search/repositories',
                      params=params
                      )
data=response.json()
print("状态码：",response.status_code)
print("查询到的仓库总数：",data['total_count'])
print("第一个仓库名：",data['items'][0]['name'])