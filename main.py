from src.aggregator import click_per_page
from src.aggregator import unique_users_per_page
from src.aggregator import clicks_per_hour
from src.aggregator import top_n_users
from src.aggregator import top_n_pages
from src.pipeline import get_valid_records
from src.aggregator import clicks_and_unique_users_per_page
from src.aggregator import page_wise_click_per_hour
from src.aggregator import user_activity_summary
# from src.read_to_csv import write_to_csv
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()


def flatten_dict(output_dict):
    result_list = []

    for k, v in output_dict.items():

        if isinstance(v, dict):
            for i, j in v.items():
                data_dict = {}
                data_dict['hour'] = k
                data_dict['page'] = i
                data_dict['clicks'] = j
                # print(data_dict)
                result_list.append(data_dict)
    return result_list


def flatten_user_activity(output_dict):
    result_list=[]

    for k,v in output_dict.items():


        if isinstance(v, dict):
            for i, j in v.items():
                data_dict = {}
                data_dict['user_id'] = k
                data_dict['clicks'] = v['clicks']
                data_dict['pages'] = v['pages']
                # print(data_dict)
                result_list.append(data_dict)
    return result_list

def main():
    engine = create_engine(f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}")
    # file_name = 'output.csv'
    print("Enter top n users for top_n_users() or top_n_pages(): ")
    try:
        n = int(input())
    except:
        print('Please enter integer')
    with open('sample.txt') as f:
        # records = f.readlines()
        lines = get_valid_records(f)



    # data, field_names = click_per_page(lines)
    # write_to_csv(data,file_name, field_names)

    df1 = pd.DataFrame(click_per_page(lines).items(),columns=['page', 'clicks'])
    df1.to_sql('clicks_per_page', con=engine, if_exists='replace',index=True)

    df2 = pd.DataFrame(unique_users_per_page(lines).items(), columns=['page', 'unq_users'])
    df2.to_sql('unique_users_per_page', con=engine, if_exists='replace', index=True)

    df3 = pd.DataFrame(clicks_per_hour(lines).items(), columns=['hour', 'clicks'])
    df3.to_sql('clicks_per_hour', con=engine, if_exists='replace', index=True)


    df4 = pd.DataFrame(top_n_users(lines,n).items(), columns=['rank', 'usr_count'])
    df4.to_sql('top_n_users', con=engine, if_exists='replace', index=True)

    df5 = pd.DataFrame(top_n_pages(lines,n).items(), columns=['page', 'count'])
    df5.to_sql('top_n_pages', con=engine, if_exists='replace', index=True)
    # print("clicks_and_unique_users_per_page: ", clicks_and_unique_users_per_page(lines).items())

    df6 = pd.DataFrame.from_dict(clicks_and_unique_users_per_page(lines))
    df6_transposed = df6.T
    df6 = df6_transposed.reset_index()
    df6.columns = ['page', 'clicks', 'users']
    # print(df6)
    df6.to_sql('clicks_and_unique_users_per_page', con=engine, if_exists='replace', index=True)
    # print(page_wise_click_per_hour(lines))


    # print(flatten_dict(page_wise_click_per_hour(lines)))
    # print("page_wise_click_per_hour: ", page_wise_click_per_hour(lines))

    df7 = pd.DataFrame(flatten_dict(page_wise_click_per_hour(lines)))

    df7.to_sql('page_wise_click_per_hour', con=engine, if_exists='replace', index=False)



    df8 = pd.DataFrame(flatten_user_activity(user_activity_summary(lines)))

    df8.to_sql('user_activity_summary', con=engine, if_exists='replace', index=False)

    # print("user_activity_summary: ", user_activity_summary(lines))
    # print("user_activity_summary: ", flatten_user_activity(user_activity_summary(lines)))

    df8 = pd.DataFrame(flatten_dict(user_activity_summary(lines)))
    df8.to_sql('user_activity_summary',con=engine,if_exists='replace',index=False)

if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
