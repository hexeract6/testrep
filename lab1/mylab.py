import urllib2
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os


def d_load(number,url):
	ss = "vhi_id_"
	sf = ".csv"
	dt = datetime.datetime.now()
	sdate = str(dt.strftime('%y-%m-%d %H-%M-%S'))
	vhi_url = urllib2.urlopen(url)
	if(number < 10):
		res_s = ss + "0" + str(number) + " " + sdate + sf
	else:
		res_s = ss + str(number) + " " + sdate + sf
	out = open("D:\let's DANCE\post\sp\lab1\data" + "/" + res_s, 'wb')
	out.write(vhi_url.read())
	out.close()
	return res_s
	
def opn(pth) :
	ff=[]
	for file_name in os.listdir(pth):
		g = pd.read_csv(pth + "/" + str(file_name), index_col=False, header = 1)
		g.insert(0,'region',file_name[7:9])
		ff.append(g)
	df = pd.concat(ff)
	df.index = range(len(df.index))
	return df
	
def load_all(num):
	while(num!=0):
		if(num < 10):
			ter = "0" + str(num)
			surl = "http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"
			furl = ".txt"
			url = surl + str(ter) + furl
			print (url)
		else:
			surl = "http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"
			furl = ".txt"
			url = surl + str(num) + furl
			print (url)
		p = d_load(num,url)
		num = num - 1

def change_reg(df):
    n = 0
    for value in df['region']:
        if value == '01': df.set_value(n, 'region', '1')
        if value == '02': df.set_value(n, 'region', '2')
        if value == '03': df.set_value(n, 'region', '3')
        if value == '04': df.set_value(n, 'region', '4')
        if value == '05': df.set_value(n, 'region', '5')
        if value == '06': df.set_value(n, 'region', '6')
        if value == '07': df.set_value(n, 'region', '7')
        if value == '08': df.set_value(n, 'region', '8')
        if value == '09': df.set_value(n, 'region', '9')
        if value == '10': df.set_value(n, 'region', '10')
        if value == '11': df.set_value(n, 'region', '11')
        if value == '12': df.set_value(n, 'region', '12')
        if value == '13': df.set_value(n, 'region', '13')
        if value == '14': df.set_value(n, 'region', '14')
        if value == '15': df.set_value(n, 'region', '15')
        if value == '16': df.set_value(n, 'region', '16')
        if value == '17': df.set_value(n, 'region', '17')
        if value == '18': df.set_value(n, 'region', '18')
        if value == '19': df.set_value(n, 'region', '19')
        if value == '20': df.set_value(n, 'region', '20')
        if value == '21': df.set_value(n, 'region', '21')
        if value == '22': df.set_value(n, 'region', '22')
        if value == '23': df.set_value(n, 'region', '23')
        if value == '24': df.set_value(n, 'region', '24')
        if value == '25': df.set_value(n, 'region', '25')
        n += 1
    return df

def vhi_data(df, year, region):
	df = df[(df['year'] == year) & df['region'] == region]
	print('Min VHI : ', min(df['VHI']), ', max VHI : ', max(df['VHI']))
	
def drought_regdata(df, region, per):
	df = df[(df['region'] == region) & (df['VHI'] < 15) & (df['%Area_VHI_LESS_15'] > per)]
	print(df['year'])
	
def norm_regdata(df, region, per):
	df = df[(df['region'] == region) & (df['VHI'] < 35) & (df['VHI'] > 15)&(df['%Area_VHI_LESS_15'] > per)]
	print(df['year'])
	
def clear_data(df,val):
	for column in (list(df.select_dtypes(exclude=['object']).columns)):
		df = df.drop(df[df[column] < val].index)
	return df
	
def show(df,escala) : 
	for column in (list(df.select_dtypes(exclude=['object']).columns)):
		plt.hist(df[column], int(escala))
		plt.title(column)
		plt.show()
def myplot(df, region, year):
	df = df[(df['region'] == region) & (df['year'] == year)]
	plt.plot(df['week'], df['VHI'])
	plt.xlabel('week')
	plt.ylabel('VHI')
	plt.title(str(year))
	plt.show()

path = "D:\let's DANCE\post\sp\lab1\data"
#load_all(25)
df = opn(path)
df = change_reg(df)
print df

myplot(df,'4',1992)