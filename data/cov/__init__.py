import time

import requests

def get_data():
    # data = requests.get('https://lab.isaaclin.cn/nCoV/api/area?latest=0')
    # data = data.json
    # print(type(data['results']))
    data = requests.get('https://lab.isaaclin.cn/nCoV/api/area?latest=0')
    data = data.json()
    print(data)
    # res = data['results']
    # df = pd.DataFrame(res)
    #
    # def time_c(timeNum):
    #     timeTemp = float(timeNum / 1000)
    #
    # tupTime = time.localtime(timeTemp)
    # stadardTime = time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
    # return stadardTime
    #
    # for i in range(len(df)):
    #
    # df.iloc[i, 16] = time_c(df.iloc[i, 16])
    #
    # for i in range(len(df)):
    #
    # df.iloc[i, 16] = df.iloc[i, 16][5:10]


if __name__ == '__main__':
    get_data()
