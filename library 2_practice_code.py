# Pandas Series Fundamentals

import pandas as pd

s = pd.Series([10,20,20,30,40], index=['a','b','c','d','e'])
print(s)

# Index vs Values
print("Values: ", s.values)
print("Index: ", s.index)
print("Dtype:", s.dtype)

print(s.head())        # first 5 rows
print(s.tail())        # last 5 rows
print(s.value_counts()) # frequency of values

""" Output
a    10
b    20
c    20
d    30
e    40
dtype: int64
Values:  [10 20 20 30 40]
Index:  Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
Dtype: int64
a    10
b    20
c    20
d    30
e    40
dtype: int64
a    10
b    20
c    20
d    30
e    40
dtype: int64
20    2
10    1
30    1
40    1
Name: count, dtype: int64
 """

# Pandas Dataframes-Creation & Inspection

import pandas as pd
data = {
    'Name' : ['Alice','Bob','Charlie'],
    'Age' : [25,30,35],
    'City' : ['New York','San Francisco','Los Angeles']
}
df = pd.DataFrame(data)
print(df)
 # Load Sample CSV

df = pd.read_csv('sample.csv')
print(df.head())
print("Info :\n", df.info())
print("\nshape: ",df.shape)
print("\nData Types:\n",df.dtypes)
print("\nStatistical Summary:\n",df.describe())

"""
 Output
  Name  Age           City
0    Alice   25       New York
1      Bob   30  San Francisco
2  Charlie   35    Los Angeles
   Id  MSSubClass MSZoning  LotArea LotConfig BldgType  OverallCond  \
0   0          60       RL     8450    Inside     1Fam            5   
1   1          20       RL     9600       FR2     1Fam            8   
2   2          60       RL    11250    Inside     1Fam            5   
3   3          70       RL     9550    Corner     1Fam            5   
4   4          60       RL    14260       FR2     1Fam            5   

   YearBuilt  YearRemodAdd Exterior1st  BsmtFinSF2  TotalBsmtSF  SalePrice  
0       2003          2003     VinylSd         0.0        856.0   208500.0  
1       1976          1976     MetalSd         0.0       1262.0   181500.0  
2       2001          2002     VinylSd         0.0        920.0   223500.0  
3       1915          1970     Wd Sdng         0.0        756.0   140000.0  
4       2000          2000     VinylSd         0.0       1145.0   250000.0  
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2919 entries, 0 to 2918
Data columns (total 13 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Id            2919 non-null   int64  
 1   MSSubClass    2919 non-null   int64  
 2   MSZoning      2915 non-null   object 
 3   LotArea       2919 non-null   int64  
 4   LotConfig     2919 non-null   object 
 5   BldgType      2919 non-null   object 
 6   OverallCond   2919 non-null   int64  
 7   YearBuilt     2919 non-null   int64  
 8   YearRemodAdd  2919 non-null   int64  
 9   Exterior1st   2918 non-null   object 
 10  BsmtFinSF2    2918 non-null   float64
 11  TotalBsmtSF   2918 non-null   float64
 12  SalePrice     1460 non-null   float64
dtypes: float64(3), int64(6), object(4)
memory usage: 296.6+ KB
Info :
 None

shape:  (2919, 13)

Data Types:
 Id                int64
MSSubClass        int64
MSZoning         object
LotArea           int64
LotConfig        object
BldgType         object
OverallCond       int64
YearBuilt         int64
YearRemodAdd      int64
Exterior1st      object
BsmtFinSF2      float64
TotalBsmtSF     float64
SalePrice       float64
dtype: object

Statistical Summary:
                 Id   MSSubClass        LotArea  OverallCond    YearBuilt  \
count  2919.000000  2919.000000    2919.000000  2919.000000  2919.000000   
mean   1459.000000    57.137718   10168.114080     5.564577  1971.312778   
std     842.787043    42.517628    7886.996359     1.113131    30.291442   
min       0.000000    20.000000    1300.000000     1.000000  1872.000000   
25%     729.500000    20.000000    7478.000000     5.000000  1953.500000   
50%    1459.000000    50.000000    9453.000000     5.000000  1973.000000   
75%    2188.500000    70.000000   11570.000000     6.000000  2001.000000   
max    2918.000000   190.000000  215245.000000     9.000000  2010.000000   

       YearRemodAdd   BsmtFinSF2  TotalBsmtSF      SalePrice  
count   2919.000000  2918.000000  2918.000000    1460.000000  
mean    1984.264474    49.582248  1051.777587  180921.195890  
std       20.894344   169.205611   440.766258   79442.502883  
min     1950.000000     0.000000     0.000000   34900.000000  
25%     1965.000000     0.000000   793.000000  129975.000000  
50%     1993.000000     0.000000   989.500000  163000.000000  
75%     2004.000000     0.000000  1302.000000  214000.000000  
max     2010.000000  1526.000000  6110.000000  755000.000000  
""" 

