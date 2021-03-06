
# FYI: may not be 100% correct, run and test it.
You are currently looking at version 1.2 of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the Jupyter Notebook FAQ course resource.
Assignment 2 - Pandas Introduction
All questions are weighted the same in this assignment.
Part 1
The following code loads the olympics dataset (olympics.csv), which was derrived from the Wikipedia entry on All Time Olympic Games Medals, and does some basic data cleaning.
The columns are organized as # of Summer games, Summer medals, # of Winter games, Winter medals, total # number of games, total # of medals. Use this dataset to answer the questions below.
In [ ]:
import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()
Question 0 (Example)
What is the first country in df?
This function should return a Series.
In [ ]:
# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
In [ ]:
answer_zero()
Question 1
Which country has won the most gold medals in summer games?
This function should return a single string value.
In [ ]:
def answer_one():
    return df['Gold'].argmax()
#answer_one()
Question 2
Which country had the biggest difference between their summer and winter gold medal counts?
This function should return a single string value.
In [ ]:
def answer_two():
    df['difference']=df['Gold']-df['Gold.1']
    df['difference']=df['difference'].abs()
    #return df [['Gold','Gold.1','difference']]
    return df['difference'].argmax()
#answer_two()
Question 3
Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?
Summer Gold−Winter GoldTotal Gold
Summer Gold−Winter GoldTotal Gold
Only include countries that have won at least 1 gold in both summer and winter.
This function should return a single string value.
In [ ]:
def answer_three():
    df2=df[(df['Gold']>0) & (df['Gold.1']>0)]
    df2['diffave']=df2['difference']/(df2['Gold']+df2['Gold.1'])
    #df2=df2[['Gold','Gold.1','difference','diffave']]
    #return df2
    return df2['diffave'].argmax()
#answer_three()
Question 4
Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return only the column (a Series object) which you created.
This function should return a Series named Points of length 146
In [ ]:
def answer_four():
    df['Points']=df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']*1
    return df
#answer_four()
Part 2
For the next set of questions, we will be using census data from the United States Census Bureau. Counties are political and geographic subdivisions of states in the United States. This dataset contains population data for counties and states in the US from 2010 to 2015. See this document for a description of the variable names.
The census dataset (census.csv) should be loaded as census_df. Answer questions using this as appropriate.
Question 5
Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
This function should return a single string value.
In [ ]:
census_df = pd.read_csv('census.csv')
census_df.head()
In [ ]:
def answer_five():
    #df2=census_df.set_index('STNAME')
    #return df2['COUNTY'].argmax()
    return census_df['STNAME'].value_counts().argmax()
#answer_five()
Question 6
Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use CENSUS2010POP.
This function should return a list of string values.
In [ ]:
def answer_six():
    f1 = census_df[census_df['SUMLEV'] == 50].groupby('STNAME')['CENSUS2010POP'].apply(lambda x: x.nlargest(3).sum()).nlargest(3).index.values.tolist()
    return f1
    #return "YOUR ANSWER HERE"
#answer_six()
Question 7
Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
This function should return a single string value.
In [72]:
def answer_seven():
    f1 = census_df[census_df['SUMLEV'] == 50].set_index(['STNAME','CTYNAME']).ix[:,['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].stack()
    f2 = f1.max(level=['STNAME','CTYNAME']) - f1.min(level=['STNAME','CTYNAME'])
    return f2.idxmax()[1]
#answer_seven()
Out[72]:
'Harris County'
Question 8
In this datafile, the United States is broken up into four regions using the "REGION" column.
Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).
In [73]:
def answer_eight():
    f1 = census_df[(census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014']) & ((census_df['REGION'] == 1) | (census_df['REGION'] == 2))]
    f1 = f1[f1['CTYNAME'].str.startswith('Washington')]
    return f1.ix[:,['STNAME', 'CTYNAME']]
#answer_eight()
Out[73]:
STNAME	CTYNAME
896	Iowa	Washington County
1419	Minnesota	Washington County
2345	Pennsylvania	Washington County
2355	Rhode Island	Washington County
3163	Wisconsin	Washington County
In [ ]:
 