import pandas

df = pandas.read_csv("basic_groupby.csv")
df.shape[0] 

df.columns = [x.strip() for x in df.columns]
df_50_perc = df['Speed'].quantile(0.5)
df_60_perc = df['Speed'].quantile(0.6)

fifty_percentile_list = []
sixty_percentile_list = []
model_list =[]
for (model) , data  in df.groupby(by = 'Model'):
    print(f"the model is ---- {model}")
    # print(f"the data is ---- {data}")

    df_50_perc = data['Speed'].quantile(0.5)
    df_60_perc = data['Speed'].quantile(0.6)
    print(f"the 50 percentiles are ---- {df_50_perc}")
    print(f"the 60 percentiles are ---- {df_50_perc}")
    model_list.append(model)
    fifty_percentile_list.append(df_50_perc)
    sixty_percentile_list.append(df_60_perc)

    summary_dictonary = {"model":model_list,
                         "50_percentile" : fifty_percentile_list,
                         "60_percentile" : sixty_percentile_list}


df_percentile= pandas.DataFrame(summary_dictonary)


"""more pythonic way"""
dataframe_list =[]
for (model) , data  in df.groupby(by = 'Model'):
    print(f"the model is ---- {model}")
    print(f"the data is ---- {data}")

    df_50_perc = data['Speed'].quantile(0.5)
    df_60_perc = data['Speed'].quantile(0.6)
    print(f"the 50 percentiles are ---- {df_50_perc}")
    print(f"the 60 percentiles are ---- {df_50_perc}")
    dataframe_list.append({"model":model,
                         "50_percentile" : df_50_perc,
                         "60_percentile" : df_60_perc}
)
    

df_percentile_pythonic_way= pandas.DataFrame(dataframe_list)





condition = ((df_percentile['50_percentile'] > df_50_perc ) \
    & (df_percentile['50_percentile'] > df_60_perc ))

df_percentile[condition]

    

    
