"""pass"""
"hello my name is jason"
"my name is jason and this will work"
"my name is mindy and this will work better than jason's"
"hello my name is winston and im the best one of them all"

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
