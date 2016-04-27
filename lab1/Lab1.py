import urllib.request
import datetime
import pandas
import os
import matplotlib.pyplot as plt


def download(region):
    if 1 <= region <= 27:
        if 1 <= region <= 9:
            region = '0' + str(region)
        url = "http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R" + str(region) + ".txt"
        name = str(region) + '_' + str(datetime.datetime.now()).replace(':', '-').replace(' ', '_')
        name = name[:-10]
        out = open('vhi_r' + name + '.csv', 'wb')
        out.write(urllib.request.urlopen(url).read())
        out.close()
        print("VHI is downloaded...")
    else:
        print("Wrong region number!")


def opn(path):
    all_files = []
    for file_name in os.listdir(path):
        t = pandas.read_csv(path + '/' + file_name, index_col=False, header=1)
        t.insert(0, 'region', file_name[5:7])
        all_files.append(t)
    df = pandas.concat(all_files)
    df.index = range(len(df.index))
    return df


def change_reg(df):
    n = 0
    for value in df['region']:
        if value == '01': df.set_value(n, 'region', 'Вінницька')
        if value == '02': df.set_value(n, 'region', 'Волинська')
        if value == '03': df.set_value(n, 'region', 'Дніпропетровська')
        if value == '04': df.set_value(n, 'region', 'Донецька')
        if value == '05': df.set_value(n, 'region', 'Житомирська')
        if value == '06': df.set_value(n, 'region', 'Закарпатська')
        if value == '07': df.set_value(n, 'region', 'Запорізька')
        if value == '08': df.set_value(n, 'region', 'Івано-Франківська')
        if value == '09': df.set_value(n, 'region', 'Київська')
        if value == '10': df.set_value(n, 'region', 'Кіровоградська')
        if value == '11': df.set_value(n, 'region', 'Луганська')
        if value == '12': df.set_value(n, 'region', 'Львівська')
        if value == '13': df.set_value(n, 'region', 'Миколаївська')
        if value == '14': df.set_value(n, 'region', 'Одеська')
        if value == '15': df.set_value(n, 'region', 'Полтавська')
        if value == '16': df.set_value(n, 'region', 'Рівненська')
        if value == '17': df.set_value(n, 'region', 'Сумська')
        if value == '18': df.set_value(n, 'region', 'Тернопільська')
        if value == '19': df.set_value(n, 'region', 'Харківська')
        if value == '20': df.set_value(n, 'region', 'Херсонська')
        if value == '21': df.set_value(n, 'region', 'Хмельницька')
        if value == '22': df.set_value(n, 'region', 'Черкаська')
        if value == '23': df.set_value(n, 'region', 'Чернівецька')
        if value == '24': df.set_value(n, 'region', 'Чернігівська')
        if value == '25': df.set_value(n, 'region', 'Республіка Крим')
        n += 1
    return df


def get_vhi(df, year, region):
    df1 = df[(df['year'] == year) & (df['region'] == region)]
    print('Min VHI : ', min(df1['VHI']), ', max VHI : ', max(df1['VHI']))


def get_vhi_15(df, region, percent):
    df1 = df[(df['region'] == region) & (df['VHI'] < 15) & (df['%Area_VHI_LESS_15'] > percent)]
    print(df1['year'])


def get_vhi_35(df, region, percent):
    df1 = df[(df['region'] == region) & (df['VHI'] < 35) & (df['VHI'] > 15) & (df['%Area_VHI_LESS_35'] > percent)]
    print(df1['year'])


def col_graph(df):
    for column in df.select_dtypes(exclude=['object', 'flexible']).columns:
        df[column].plot.hist(500)
        plt.title(column)
        plt.show()


def clear_data(df, value):
    for column in df.select_dtypes(exclude=['object', 'flexible']).columns:
        df = df.drop(df[df[column] < value].index)
    return df


def graph(df, region, year):
    df = df[(df['region'] == region) & (df['year'] == year)]
    plt.plot(df['week'], df['VHI'])
    plt.xlabel('week')
    plt.ylabel('VHI')
    plt.title(str(year))
    plt.show()

#get_vhi(change_reg(opn("E:\Programs\Учьобка ((\СРП\Lab1\Data")), 2010, 'Рівненська')
#col_graph(change_reg(opn("E:\Programs\Учьобка ((\СРП\Lab1\Data")))
#col_graph(clear_data(change_reg(opn("E:\Programs\Учьобка ((\СРП\Lab1\Data")), 0))
#graph(clear_data(change_reg(opn("E:\Programs\Учьобка ((\СРП\Lab1\Data")), 0), 'Київська', 2005)
