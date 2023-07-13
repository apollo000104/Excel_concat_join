import pandas as pd
import openpyxl

final_df=pd.read_excel("final.xlsx", header= None)
final_df.rename(columns= final_df.iloc[0], inplace= True)
final_df=final_df[1:]

new_df=pd.read_excel("new.xlsx", header= None)
new_df.rename(columns=new_df.iloc[0],inplace= True )
new_df=new_df[1:]
## find common columns
common_columns = final_df.columns.intersection(new_df.columns)
## remake new_df with common columns between final and new.
new_df_common_columns = new_df[common_columns]
## join two dataframe , keep all the final columns and just add common columns in new dataframe
join_df = pd.concat([final_df, new_df_common_columns.reindex(final_df.columns, axis=1)], axis=1)
## Save into "out.xlsx" file
join_df.to_excel("out.xlsx", index= False)
print(join_df)
            
            