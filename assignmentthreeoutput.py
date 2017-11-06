  
In [ ]:
 
In [ ]:
 
In [ ]:
 
In [ ]:
 
In [229]:
import pandas as pd
import re
#energy=None
#GDP=None
#ScimEn=None
def energy():
    energy=pd.read_excel('/Users/biniam/coursera-panda/Indicators.xls')
    energy = energy[16:243]
    energy=energy.drop(['Unnamed: 0','Unnamed: 1'],1)
    energy.columns=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy['Energy Supply']=pd.to_numeric(energy['Energy Supply'], errors='coerce')
    energy['Energy Supply']=energy['Energy Supply'].apply(lambda x: x*1000000)
    #energy['Energy Supply'].apply(lambda x: x*1000000)
    
    def editCountryName(input):
    
        if -1!=input.find('('):
            return input.split('(')[0]
        else:
            return re.sub('\d+', '', input)
    
    energy['Country']=energy['Country'].apply(editCountryName)
    energy.Country.replace({'Republic of Korea': 'South Korea','United States of America': 'United States','United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',"China, Hong Kong Special Administrative Region": "Hong Kong"},inplace=True)
    energy['Country']=energy['Country'].str.strip()
    return energy
def GDP():
    GDP=pd.read_csv('/Users/biniam/coursera-panda/world_bank.csv',skiprows=4)
    GDP.rename(columns={"Country Name":"Country"},inplace=True)
    GDP.Country.replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"},inplace=True)
    GDP['Country']=GDP['Country'].str.strip()
    return GDP
def scimen():
    ScimEn=pd.read_excel('/Users/biniam/coursera-panda/scimagojr-3.xlsx')
    #ScimEn=ScimEn.sort_values(by='Rank',ascending=True).head(15)
    ScimEn['Country']=ScimEn['Country'].str.strip()
    return ScimEn
      
def answer_one():
    en=energy()
    gdp=GDP()
    scim=scimen()
    result=pd.merge(pd.merge(en,gdp, on='Country'),scim, on='Country')
    result.set_index('Country',inplace=True)
    result=result.sort_values(by='Rank',ascending=True).head(15)
    finalresult=result[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]  
    return finalresult
    
In [230]:
answer_one()
Out[230]:
Rank	Documents	Citable documents	Citations	Self-citations	Citations per document	H index	Energy Supply	Energy Supply per Capita	% Renewable	2006	2007	2008	2009	2010	2011	2012	2013	2014	2015
Country																				
China	1	127050	126767	597237	411683	4.70	138	127191.0	93	19.7549	3.992331e+12	4.559041e+12	4.997775e+12	5.459247e+12	6.039659e+12	6.612490e+12	7.124978e+12	7.672448e+12	8.230121e+12	8.797999e+12
United States	2	96661	94747	792274	265436	8.20	230	90838.0	286	11.571	1.479230e+13	1.505540e+13	1.501149e+13	1.459484e+13	1.496437e+13	1.520402e+13	1.554216e+13	1.577367e+13	1.615662e+13	1.654857e+13
Japan	3	30504	30287	223024	61554	7.31	134	18984.0	149	10.2328	5.496542e+12	5.617036e+12	5.558527e+12	5.251308e+12	5.498718e+12	5.473738e+12	5.569102e+12	5.644659e+12	5.642884e+12	5.669563e+12
United Kingdom	4	20944	20357	206091	37874	9.84	139	7920.0	124	10.6005	2.419631e+12	2.482203e+12	2.470614e+12	2.367048e+12	2.403504e+12	2.450911e+12	2.479809e+12	2.533370e+12	2.605643e+12	2.666333e+12
Russian Federation	5	18534	18301	34266	12422	1.85	57	30709.0	214	17.2887	1.385793e+12	1.504071e+12	1.583004e+12	1.459199e+12	1.524917e+12	1.589943e+12	1.645876e+12	1.666934e+12	1.678709e+12	1.616149e+12
Canada	6	17899	17620	215003	40930	12.01	149	10431.0	296	61.9454	1.564469e+12	1.596740e+12	1.612713e+12	1.565145e+12	1.613406e+12	1.664087e+12	1.693133e+12	1.730688e+12	1.773486e+12	1.792609e+12
Germany	7	17027	16831	140566	27426	8.26	126	13261.0	165	17.9015	3.332891e+12	3.441561e+12	3.478809e+12	3.283340e+12	3.417298e+12	3.542371e+12	3.556724e+12	3.567317e+12	3.624386e+12	3.685556e+12
India	8	15005	14841	128763	37209	8.58	115	33195.0	26	14.9691	1.265894e+12	1.374865e+12	1.428361e+12	1.549483e+12	1.708459e+12	1.821872e+12	1.924235e+12	2.051982e+12	2.200617e+12	2.367206e+12
France	9	13153	12973	130632	28601	9.93	114	10597.0	166	17.0203	2.607840e+12	2.669424e+12	2.674637e+12	2.595967e+12	2.646995e+12	2.702032e+12	2.706968e+12	2.722567e+12	2.729632e+12	2.761185e+12
South Korea	10	11983	11923	114675	22595	9.57	104	11007.0	221	2.27935	9.410199e+11	9.924316e+11	1.020510e+12	1.027730e+12	1.094499e+12	1.134796e+12	1.160809e+12	1.194429e+12	1.234340e+12	1.266580e+12
Italy	11	10964	10794	111850	26661	10.20	106	6530.0	109	33.6672	2.202170e+12	2.234627e+12	2.211154e+12	2.089938e+12	2.125185e+12	2.137439e+12	2.077184e+12	2.040871e+12	2.033868e+12	2.049316e+12
Spain	12	9428	9330	123336	23964	13.08	115	4923.0	106	37.9686	1.414823e+12	1.468146e+12	1.484530e+12	1.431475e+12	1.431673e+12	1.417355e+12	1.380216e+12	1.357139e+12	1.375605e+12	1.419821e+12
Iran	13	8896	8819	57470	19125	6.46	72	9172.0	119	5.70772	3.895523e+11	4.250646e+11	4.289909e+11	4.389208e+11	4.677902e+11	4.853309e+11	4.532569e+11	4.445926e+11	4.639027e+11	NaN
Australia	14	8831	8725	90765	15606	10.28	107	5386.0	231	11.8108	1.021939e+12	1.060340e+12	1.099644e+12	1.119654e+12	1.142251e+12	1.169431e+12	1.211913e+12	1.241484e+12	1.272520e+12	1.301251e+12
Brazil	15	8668	8596	60702	14396	7.00	86	12149.0	59	69.648	1.845080e+12	1.957118e+12	2.056809e+12	2.054215e+12	2.208872e+12	2.295245e+12	2.339209e+12	2.409740e+12	2.412231e+12	2.319423e+12
In [231]:
def answer_two():
    energy2=energy()
    gdp2=GDP()
    scimen2=scimen()
    before=pd.merge(pd.merge(energy2,gdp2, on='Country', how='outer'),scimen2, on='Country',how='outer')
    after=pd.merge(pd.merge(energy2,gdp2, on='Country'),scimen2, on='Country')
    diff=len(before)-len(after)
    return diff
In [232]:
anstwo=answer_two()
In [233]:
anstwo
Out[233]:
156
In [234]:
def answer_three():
    Top15 = answer_one()
    year=Top15[['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    avgGDP=year.mean(axis=1,skipna=True)
    avgGDP=avgGDP.sort_values(ascending=False)
    return avgGDP
In [235]:
ansfour=answer_three()
In [236]:
ansfour
Out[236]:
Country
United States         1.536434e+13
China                 6.348609e+12
Japan                 5.542208e+12
Germany               3.493025e+12
France                2.681725e+12
United Kingdom        2.487907e+12
Brazil                2.189794e+12
Italy                 2.120175e+12
India                 1.769297e+12
Canada                1.660647e+12
Russian Federation    1.565459e+12
Spain                 1.418078e+12
Australia             1.164043e+12
South Korea           1.106715e+12
Iran                  4.441558e+11
dtype: float64
In [237]:
def answer_four():
    Top15 = answer_one()
    avgsixdf = Top15
    avgsixdf['averageGDP']=answer_three()
    avgsixdf.sort_values(by='averageGDP',inplace=True,ascending=False)
    avgsix=abs(avgsixdf.iloc[5]['2015']-avgsixdf.iloc[5]['2006'])
    return avgsix
In [238]:
answer_four()
Out[238]:
246702696075.3999
In [239]:
def answer_five():
    Top15 = answer_one()
    energyPerCapita=Top15['Energy Supply per Capita'].mean()
    return float(energyPerCapita)
In [240]:
answer_five()
Out[240]:
157.59999999999999
In [241]:
def answer_six():
    Top15 = answer_one()
    Top15Sorted=Top15.sort_values(by='% Renewable', ascending=False)
    answersix=(Top15Sorted.index[0],Top15Sorted['% Renewable'][0])
    return answersix
In [242]:
answer_six()
Out[242]:
('Brazil', 69.64803)
In [243]:
def answer_seven():
    Top15 = answer_one()
    Top15['selfCitationTotal']=Top15['Self-citations']/Top15['Self-citations'].sum()
    citationSorted=Top15.sort_values(by='selfCitationTotal', inplace=False, ascending=False)
    answerseven=(citationSorted.index[0],citationSorted['selfCitationTotal'][0])
    return answerseven
In [244]:
answer_seven()
Out[244]:
('China', 0.39377339829858382)
In [245]:
def answer_eight():
    Top15 = answer_one()
    Top15['population']=Top15['Energy Supply']/Top15['Energy Supply per Capita']
    maxpop=Top15.sort_values(by='population',inplace=False,ascending=False)
    answereight=maxpop.index[2]
    return answereight
In [246]:
answer_eight()
Out[246]:
'United States'
In [247]:
def answer_nine():
    Top15 = answer_one()
    Top15['population']=Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['citabledocpercapita']=Top15['Citable documents']/Top15['population']
    energypercapita=Top15['Energy Supply per Capita']
    answernine=Top15['Energy Supply per Capita'].astype(float).corr(Top15['citabledocpercapita'].astype(float))
    return answernine
In [248]:
answer_nine()
Out[248]:
0.79400104354429446
In [249]:
def answer_ten():
    Top15 = answer_one()
    Top15['HighRenew']=Top15['% Renewable'].apply(lambda x: 1 if Top15['% Renewable'].median() > x else 0)
    Top15.sort_index(ascending=True,inplace=True)
    answerten=Top15['HighRenew']
    return answerten
In [250]:
answer_ten()
Out[250]:
Country
Australia             1
Brazil                0
Canada                0
China                 0
France                0
Germany               0
India                 1
Iran                  1
Italy                 0
Japan                 1
Russian Federation    0
South Korea           1
Spain                 0
United Kingdom        1
United States         1
Name: HighRenew, dtype: int64
In [251]:
def answer_eleven():
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    Top15['population']=Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['population']=pd.to_numeric(Top15['population'])
    Top15['ContinentDict']=pd.Series(ContinentDict)
    answereleven=Top15.groupby('ContinentDict').agg(['size', 'sum', 'mean', 'std'])['population']
    return answereleven
In [252]:
answer_eleven()
Out[252]:
size	sum	mean	std
ContinentDict				
Asia	5	2898.666387	579.733277	679.097888
Australia	1	23.316017	23.316017	NaN
Europe	6	457.929667	76.321611	34.647667
North America	2	352.855249	176.427625	199.669645
South America	1	205.915254	205.915254	NaN
In [253]:
def answer_twelve():
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    Top15['ContinentDict']=pd.Series(ContinentDict)
    Top15['bins'] = pd.cut(Top15['% Renewable'],5)
    answerthirteen=Top15.groupby(['ContinentDict','bins']).size()
    return answerthirteen
In [254]:
answer_twelve()
Out[254]:
ContinentDict  bins            
Asia           (2.212, 15.753]     4
               (15.753, 29.227]    1
Australia      (2.212, 15.753]     1
Europe         (2.212, 15.753]     1
               (15.753, 29.227]    3
               (29.227, 42.701]    2
North America  (2.212, 15.753]     1
               (56.174, 69.648]    1
South America  (56.174, 69.648]    1
dtype: int64
In [255]:
def answer_thirteen():
    Top15 = answer_one()
    Top15['population']=Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['population']=pd.to_numeric(Top15['population'])
    answerthirteen=Top15['population'].apply(lambda x: '{0:,}'.format(x))
    return answerthirteen
In [256]:
answer_thirteen()
Out[256]:
Country
China                 1,367.6451612903227
United States          317.61538461538464
Japan                  127.40939597315436
United Kingdom          63.87096774193548
Russian Federation                  143.5
Canada                  35.23986486486486
Germany                 80.36969696969697
India                 1,276.7307692307693
France                  63.83734939759036
South Korea             49.80542986425339
Italy                  59.908256880733944
Spain                  46.443396226415096
Iran                    77.07563025210084
Australia              23.316017316017316
Brazil                 205.91525423728814
Name: population, dtype: object
In [ ]:
 