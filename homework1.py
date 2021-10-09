#Author: Huaiqian Ye
#UCID: 12261853


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def read_bea_csv(fname):
    df = pd.read_csv(os.path.join(PATH, fname), skiprows=4)
    return df


def drop_cols(df, cols_to_keep):
    cols_to_drop = df.columns[~df.columns.isin(cols_to_keep)]
    df = df.drop(cols_to_drop, axis=1)
    return df


def clean_str(df, cols_str):
    for col_str in cols_str:
        df[col_str] = [c.lstrip() for c in df[col_str].astype(str)]
    return df


def clean_num(df, cols_num):
    for col_num in cols_num:
        df[col_num] = pd.to_numeric(df[col_num], errors='coerce')
    return df


def clean(df, cols_to_keep, cols_str=False, cols_num=False):
    df = df.dropna()
    df = drop_cols(df, cols_to_keep)
    if cols_str:
        df = clean_str(df, cols_str)
    if cols_num:
        df = clean_num(df, cols_num)
    return df


def reshape(df, wide_to_long=['Year','Employment'], long_to_wide=['Description']):
    if wide_to_long:
        df_reshaped = pd.melt(df, id_vars=df.columns[~df.columns.isin(cols_num)],
                              value_vars=cols_num,
                              var_name=wide_to_long[0],
                              value_name=wide_to_long[1])
        df = df_reshaped
    if long_to_wide:
        cols_index = df.columns[~df.columns.isin([*long_to_wide, wide_to_long[1]])]
        df_reshaped = df.pivot(index=cols_index, columns=long_to_wide[0], values=wide_to_long[1]).reset_index()
    return df_reshaped


def merge_and_calculate(df_industries,df_total):
    df = pd.merge(df_industries,df_total,on=df_total.columns[0:2].to_list())
    df = df.rename(columns={'GeoName':'state','Year':'year'})
    df[df.columns[2:12]] = df[df.columns[2:12]].div(df[df.columns[12]].values, axis=0)
    df = df.drop(df.columns[12],axis=1)
    return df


def top_states(df,industry='Manufacturing',top=5,year=2000):
    names_top_states = df[df['year'] == year].nlargest(top, industry)['state']
    print('top',top,'states that had the highest share of',
          industry,'employment in year',2000,'are:\n',
          names_top_states.tolist(),'\n')
    df_top_states = df[[c in names_top_states.tolist() for c in df['state']]][[*['state','year'], industry]]
    sns.lineplot(data=df_top_states, x='year', y=industry, hue='state')
    plt.savefig('manufacturing_shares.png')
    print('The change in share of manufacturing has been visualized and saved to manufacturing_shares.png','\n')


def find_max(df,year,top=5):
    df = df[df['year'] == year]
    df_max = pd.DataFrame()
    df_max['state'] = df['state']
    df = df.drop(['year','state'],axis=1)
    df_max['industry'] = df.idxmax(axis=1)
    df_max['concentration'] = df.max(axis=1)
    print('In year',year,', the following states had the highest concentration of employment in a single industry.\n',
          'The information of state, industry, and employment concentration are as follows:')
    print(df_max.nlargest(top, 'concentration'),'\n')


def q_1():
    df_industries = clean(read_bea_csv('SAEMP25N by industry.csv'), cols_to_keep, cols_str, cols_num)
    df_total = clean(read_bea_csv('SAEMP25N total.csv'), cols_to_keep, cols_num=cols_num)
    df_industries = reshape(df_industries)
    df_total = reshape(df_total, long_to_wide=False)
    df_merged = merge_and_calculate(df_industries, df_total)
    df_merged.to_csv('data.csv')

def q_2():
    df = pd.read_csv('data.csv').iloc[:, 1:]
    top_states(df)
    find_max(df, 2000)
    find_max(df, 2017)

PATH = r'E:\Files\HaHaHariss\21Fall\Data Skills for Public Policy\data_skills_2_hw1'
cols_to_keep = ['GeoName', '2000', '2017', 'Description']
cols_str = ['Description']
cols_num = ['2000', '2017']

q_1()
q_2()




