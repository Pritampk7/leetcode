import pandas as pd

filename = 'Bhagavan and Bhakta-Notebook.csv'

df = pd.read_csv(filename)

df.dropna()

print(df)
#print(clean_df)
# # column_names = df.columns.tolist()
#column_data = df['Annotation']
#print(type(df))
# # df = column_data.dropna()
#data_list = column_data.tolist()
# # print(data_list)
# book_name = filename.split('-')[0]
#print(column_data)