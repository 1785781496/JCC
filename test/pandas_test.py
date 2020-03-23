import numpy as np
import pandas as pd
from pandas import Series


def pandas_series():
    s = pd.Series([1, 2, 3, np.nan, 5, 6])
    print(s)  # 索引在左边 值在右边


def pandas_date_range():
    dates = pd.date_range('20180310', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])  # 生成6行4列位置
    print(df)  # 输出6行4列的表格
    print(df['B'])

def pandas_date_range_2():
    # 创建特定数据的DataFrame
    df_1 = pd.DataFrame({'A': 1.,
                         'B': pd.Timestamp('20180310'),
                         'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                         'D': np.array([3] * 4, dtype='int32'),
                         'E': pd.Categorical(["test", "train", "test", "train"]),
                         'F': 'foo'
                         })
    print(df_1)
    print(df_1.dtypes)
    print(df_1.index)  # 行的序号
    # Int64Index([0, 1, 2, 3], dtype='int64')
    print(df_1.columns)  # 列的序号名字
    # Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
    print(df_1.values)  # 把每个值进行打印出来
    print(df_1.describe())  # 数字总结
    print(df_1.T)  # 翻转数据
    print(df_1.sort_index(axis=1, ascending=False))  # axis等于1按列进行排序 如ABCDEFG 然后ascending倒叙进行显示
    print(df_1.sort_values(by='E'))  # 按值进行排序


if __name__ == '__main__':
    # pandas_series()
    # pandas_date_range()
    pandas_date_range_2()

# 【简书】Python之Pandas使用教程
# https://www.jianshu.com/p/218baa41bab9
# 【CSDN】python之pandas简单介绍及使用（一）
# https://blog.csdn.net/aasdad1/article/details/91812714
