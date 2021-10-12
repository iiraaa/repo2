# Lecture code for week2
# inspired by https://www.programiz.com/python-programming/tuple

my_string = 'baldan'
type(my_string)

mystr1 = 'Nice'
mystr2 = "day"
myFullStr = mystr1 +" " + mystr2 + " baina tiime?"
myFullStr

my_int = -15
type(my_int)

my_float = 15.234
type(my_float)

my_bool = False #True #0
type(my_bool)

import datetime

from numpy.lib.arraypad import pad
today = datetime.date.today()
today.year
today.month
today.day

datetime.datetime.strptime('2017-01-22', "%Y-%m-%d") # Convert string to date time (strptime)
datetime.datetime.strptime('2017/01/22', "%Y/%m/%d")

today.strftime("%y/%m/%d") # convert datetime to string (stprftime)

#Push hiisen bolovch orsongui

my_list_str = ['bat', 'bold', 'dorj']
my_list_str[2]
my_list_str[:2]
my_list_str[1:]
my_list_str[::-1]
my_list_str[::-2]
my_list_str[-1]
my_list_str[-2]

my_list_num = [15, 15.2, 4.7]
type(my_list_num)

# tuple

my_tuple = (1,2,3) #iim haalttai bol tuple
my_tuple[1] = 2 #ingej edit hiij boldgu
my_list_str[0] = 'ider'#list bol ingej uurchult hj bolno
my_list_str

# set

my_set1 = {1,2,3} #{} haalttai bol set
my_set2 = {7,8,9}
type(my_set1)
my_set1 | my_set2 #concatenet
my_set1 & my_set2 #Davhtsaj bui toog oloh
my_set2 - my_set1 #hoorond ni hasah

# dictionary . json

my_dict = {"name": "Ider", "sex": "Male" "age": 32, "country": "Mongolia"}
my_dict["age"]
my_dict["name"]
my_dict["city"] = "Ulaanbaatar"
my_dict['city']
person1 = my_dict
person2 = {"name": "Mandukhai", "sex": "female", "age": 30, "country": "Mongolia", "city": "Erdenet"}
person2["sex"]
big_dict = {"younger": person1, "older": person2}
big_dict.keys()
big_dict["younger"]
big_dict["younger"].keys()
big_dict["younger"]["name"]
type(big_dict)

# Numerical package - numpy (scipy)

import numpy as np
a = np.array([[1,2], [4,5]])
b = a
a+b
np.dot(a,b)

# Pandas

# Pandas read examples
# https://www.datacamp.com/community/tutorials/importing-data-into-pandas

import pandas as pd

pd.read.excel("C:\Users\Ider.E\Desktop\PythonCourse\Lecture 2\repo2\week2\data.xlsx") # aldaa zaana 
pd.read_excel("C://Users/Ider.E/Desktop/PythonCourse/Lecture 2/repo2/week2/data.xlsx") # buh slash-g ni esreg zugt soliv
pd.read.excel("C:\\Users\\Ider.E\\Desktop\\PythonCourse\\Lecture 2\\repo2\\week2\\data.xlsx") # esvel bugdiig ni 2 slash-tai bolgoh

df = pd.read_excel("C://Users/Ider.E/Desktop/PythonCourse/Lecture 2/repo2/week2/data.xlsx")
df.dtypes # data-n turluudiig harna
df.head(5) #hamgiin ehnii 5 muriig harna
df.tail(5) #hamgiin suuliin 5 muriig harna
df.describe() # toon datanii stat-g harna
df['age']
df['firstName'] #tuhailsan baganiig songono
    # iloc - integer location
df.iloc[2,1] #integer location - iloc tuhain cell-g songono
df.iloc[2:5,1:3] # olon cell-g songono
    #loc - location
df.loc[5, "lastName"] #5-r murnii lastname-g songono
df.loc[5:8,('lastName', 'firstName')] # 5-8 murnii last first name gsn baganiig songono

df[df["age"]<27] #27-s doosh nastai humuusiig songono
df[df['age']>27][["firstName", "lastName", "salary", "age"]] # 27-s doosh nastai humuusiin ovog ner tsalin ni harah

df[(df["age"]<27) & (df["salary"]<2.0) & (df["gender"] != "M")]

#group by

df.groupby('gender')['salary'].mean()
df.groupby('gender')['salary'].max()
df.groupby('gender')['salary'].min()

df.groupby(['gender', 'politicalView'])[['age', 'salary']].mean()
df.groupby(['gender', 'politicalView'])[['age', 'salary']].max()

df.groupby(['gender', 'politicalView']).agg({'age': ["mean", "max"], 'salary': ["max", "count"]})

#sort

df.sort_values(by="yearsInCompany", inplace=True) #inplace hiivel data ni shuud sortlogdson chigeeree hadgalagdana

df["name"] = np.arange(10)

del df["name"] #delete column
df[["age", "salary"]]

df.columns #buh column-ii neriig harna


