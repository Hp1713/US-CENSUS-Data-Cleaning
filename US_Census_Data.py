from states import *
import pandas as pd 
import matplotlib.pyplot as plt

# Analyzing the data types and columns of US_Census Data frame  
print('\nData Types of Data Frame:\n'+str(us_census.dtypes))
print('\nData Frame:\n'+str(us_census.head()))

# making Income Object column into a  numeric column. Replacing '$' first with empty space then using pd.to_numeric for better calculation 
us_census.Income = us_census['Income'].replace('[\$,]','',regex = True)
us_census.Income = pd.to_numeric(us_census.Income)

# expanding columns GenderPop into two columns, Men and Women, Numeric values for them
us_census[['Men', 'Women']] = us_census.GenderPop.str.split('_', expand = True)

us_census.Men = us_census.Men.replace('M','', regex = True)
us_census.Women = us_census.Women.replace('F','', regex = True)

us_census[['Men','Women']] = us_census[['Men','Women']].apply(pd.to_numeric)
# reasure which columns we need 
us_census = us_census[['State', 'TotalPop','Hispanic','White', 'Black', 'Native', 'Asian', 'Pacific','Income', 'Men', 'Women']]

print('\nData Types of Data Frame:\n'+str(us_census.dtypes))

plt.scatter(us_census.Women, us_census.Income)
plt.show()

# Display missing values in the data frame 
print('\nMissing values in columns:\n'+ str(us_census.isnull().sum()))

# Displaying the rows with missing values to later fill the values for better plotting
print('\nRows with missing values \n:'+str(us_census.loc[us_census.isnull().any(axis=1)]))

# got the female population value, filled up null values using fillna
value_women_NaN = us_census.TotalPop - us_census.Men
us_census.Women = us_census.Women.fillna(value = value_women_NaN)

# print to confirm the calculation was done right 
print('\nComfirming Nan values were filled:\n'+str(us_census.loc[us_census.State == 'Maryland']))


# Making sure if there are duplicates, and dropping them if found
print('\nAmount of duplicates in the US Census data frame:\n'+str(us_census.duplicated().sum()))

us_census = us_census.drop_duplicates()

# Scatter graph with accurate results 
plt.scatter(us_census.Women, us_census.Income)
plt.show()


print('\nAmount of null values left in the columns:\n'+str(us_census.isnull().sum()))

#converting the column values to numeric in order to fill up the Nan values of Pacific 
pd.options.mode.chained_assignment = None
us_census[['Hispanic','White', 'Black', 'Native', 'Asian', 'Pacific']] = us_census[['Hispanic','White', 'Black', 'Native', 'Asian', 'Pacific']] .replace('[\%]', '', regex=True)
us_census[['Hispanic','White', 'Black', 'Native', 'Asian', 'Pacific']] = us_census[['Hispanic','White', 'Black', 'Native', 'Asian', 'Pacific']].apply(pd.to_numeric)

Pacific_Nan = 100 - us_census.Hispanic - us_census.White - us_census.Native - us_census.Asian - us_census.Black

us_census.Pacific = us_census.Pacific.fillna(value = Pacific_Nan)

print('\nNo more null values:\n'+str(us_census.isnull().sum()))



plt.hist(us_census.Hispanic)
plt.xlabel('Percentage')
plt.ylabel('Frequency of occurance')
plt.show()



plt.hist(us_census.White)
plt.xlabel('Percentage')
plt.ylabel('Frequency of occurance')
plt.show()




plt.hist(us_census.Black)
plt.xlabel('Percentage')
plt.ylabel('Frequency of occurance')
plt.show()

plt.hist(us_census.Native)
plt.xlabel('Percentage')
plt.ylabel('Frequency of occurance')
plt.show()



plt.hist(us_census.Asian)
plt.xlabel('Percentage')
plt.ylabel('Frequency of occurance')
plt.show()



plt.hist(us_census.Pacific)
plt.xlabel('Percentage')
plt.ylabel('Frequency of occurance')
plt.show()



