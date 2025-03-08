"""pass"""
"hello my name is jason"
"my name is jason and this will work"
"my name is mindy and this will work better than jason's"
"hello my name is winston and im the best one of them all"

# US – This is not a state, but a reference to the United States.
# PR – This is the abbreviation for Puerto Rico, a U.S. territory, not a state.
# GU – This refers to Guam, another U.S. territory, not a state.
# VI – This is the abbreviation for the U.S. Virgin Islands, a U.S. territory.
# DC – This stands for Washington, D.C., the capital of the United States, which is not a state but a federal district.

"""test 2 columns are same instantly"""
# (df['YearStart'] == df['YearEnd']).all()

"""get column information"""
# df.info()

"""creating your own dataframe"""
# df.columns
# winston_df = df[['YearStart', 'YearEnd', 'LocationAbbr', 'LocationDesc', 'Datasource',
#        'Class', 'Topic', 'Question', 'Data_Value_Unit']]
# winston_df.head()

"""determining your categorical and numerical columns"""
# # categorical columns
# cat_col = [col for col in df.columns if df[col].dtype == 'object']
# print('Categorical columns :',cat_col)
# # Numerical columns
# num_col = [col for col in df.columns if df[col].dtype != 'object']
# print('Numerical columns :',num_col)

"""check total number of unique values in categorical columns"""
# df[cat_col].nunique()

"""check the (row, column) count of a dataframe"""
# df.shape

"""checking for missing data"""
# round((winston_df.isnull().sum()/winston_df.shape[0])*100,2)

"""creating a box plot"""
# ensure 1 categorical and 1 quantitative variable for 2 total variables

# import matplotlib.pyplot as plt

# plt.boxplot(df3['Age'], vert=False)
# plt.ylabel('Variable')
# plt.xlabel('Age')
# plt.title('Box Plot')
# plt.show()

"""box plot numerical insights"""
# # calculate summary statistics
# mean = df3['Age'].mean()
# std  = df3['Age'].std()

# # Calculate the lower and upper bounds
# lower_bound = mean - std*2
# upper_bound = mean + std*2

# print('Lower Bound :',lower_bound)
# print('Upper Bound :',upper_bound)

# # Drop the outliers
# df4 = df3[(df3['Age'] >= lower_bound) 
#                 & (df3['Age'] <= upper_bound)]

"""data validation and verification"""
# X = df3[['Pclass','Sex','Age', 'SibSp','Parch','Fare','Embarked']]
# Y = df3['Survived']

"""min-max scaling"""
# rescales values to specified range, typically between 0-1. Preserves original distribution.

# from sklearn.preprocessing import MinMaxScaler

# # initialising the MinMaxScaler
# scaler = MinMaxScaler(feature_range=(0, 1))

# # Numerical columns
# num_col_ = [col for col in X.columns if X[col].dtype != 'object']
# x1 = X
# # learning the statistical parameters for each of the data and transforming
# x1[num_col_] = scaler.fit_transform(x1[num_col_])
# x1.head()
