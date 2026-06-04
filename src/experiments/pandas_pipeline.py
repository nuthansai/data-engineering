import pandas as pd
import json

def pandas_pipeline():
    data_list = []
    with open('/sample.txt') as f:
        for line in f:
            try:
                if not line:
                    continue
                if '{' not in line:
                    continue

                start = line.find('{')

                json_part = line[start:]
                timestamp = line[:start].strip()
                data_dict = (json.loads(json_part))
                data_dict["timestamp"] = timestamp
                data_list.append(data_dict)
            except json.JSONDecodeError:
                continue
    df = pd.DataFrame(data_list)
    df = df.drop_duplicates()
    df['user_id'] = df['user_id'].astype('Int64')

    df[['event','page']] = df[['event', 'page']].apply(lambda col: col.str.lower().str.strip())
    df = df.loc[df['event']=='click']
    df = df.loc[(df['page'] != '') & (df['page'].notna())]
    # df = df.groupby(['page'], as_index=False).agg({'event':['count'],'user_id':['nunique']})
    df = df.groupby(['page'], as_index=False).agg(clicks = ('event','count'), unique_users = ('user_id','nunique')).sort_values(by=["clicks"], ascending=[False])
    # print("data_list: ",data_list)
    print(df)


pandas_pipeline()