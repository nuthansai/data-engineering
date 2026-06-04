from typing import Any
import pandas as pd
from sqlalchemy import engine


def click_per_page(records):
    data_dict = {}
    # field_names: list[Any] = []
    for line in records:
        page = line["page"]
        data_dict[page] = data_dict.get(page, 0) + 1
    # for i in data_dict:
    #     field_names.append(i)



    return data_dict

def unique_users_per_page(records):
    data_dict = {}
    result = {}

    for line in records:
        page = line["page"]
        user_id = line["user_id"]
        if page not in data_dict:
            data_dict[page] = set()
        data_dict[page].add(user_id)
    for i in data_dict:
        result[i] = len(data_dict[i])
    return result

def clicks_per_hour(records):
    data_dict = {}


    for line in records:
        try:
            time = line["timestamp"].split(' ')[1]
            hour = time.split(':')[0]
        except:
            continue




        data_dict[hour] = data_dict.get(hour, 0) + 1

    return data_dict

def top_n_users(records,n):
    data_dict = {}
    result = {}

    for line in records:
        # page = line["page"]
        user_id = line["user_id"]
        #         if page not in data_dict:
        #             data_dict[page] = set()

        data_dict[user_id] = data_dict.get(user_id, 0) + 1

    sorted_dict = sorted(data_dict.items(), key=lambda x: (-x[1], x[0]))

    for i in range(0, n):
        result[sorted_dict[i][0]] = sorted_dict[i][1]
    return result

def top_n_pages(records,n):
    data_dict = {}
    result = {}

    for line in records:
        page = line["page"]
        # user_id = line["user_id"]
        #         if page not in data_dict:
        #             data_dict[page] = set()

        data_dict[page] = data_dict.get(page, 0) + 1

    sorted_dict = sorted(data_dict.items(), key=lambda x: (-x[1], x[0]))

    for i in range(0, n):
        result[sorted_dict[i][0]] = sorted_dict[i][1]
    return result


def clicks_and_unique_users_per_page(records):
    data_dict = {}
    result = {}
    for line in records:

        page = line["page"]
        user_id = line["user_id"]
        if page not in data_dict:
            data_dict[page] = {
                "clicks": 0,
                "users": set()
            }
        data_dict[page]["clicks"] += 1
        data_dict[page]["users"].add(user_id)

    for outer_key, inner_dict in data_dict.items():
        result[outer_key] = {}
        for inner_key, values in inner_dict.items():
            if inner_key == 'users':
                result[outer_key][inner_key] = len(values)
            else:
                result[outer_key][inner_key] = values
    return result

def page_wise_click_per_hour(records):
    data_dict = {}
    # result = {}

    for line in records:
        page = line['page']
        if "timestamp" not in line:
            continue

        ts = line["timestamp"]

        parts = ts.split(' ')
        if len(parts) != 2:
            continue

        time_part = parts[1]
        time_parts = time_part.split(':')

        if len(time_parts) != 3:
            continue

        hour = time_parts[0]

        if hour not in data_dict:
            data_dict[hour] = {}

        data_dict[hour][page] = data_dict[hour].get(page,0) + 1
    return data_dict

def user_activity_summary(records):
    data_dict = {}
    result = {}

    for line in records:
        user = line['user_id']
        # event = line['event']
        page = line['page']

        if user not in data_dict:
            data_dict[user] = {
                "clicks": 0,
                "pages": set()
            }

        data_dict[user]["clicks"] += 1
        data_dict[user]["pages"].add(page)

    for outer_key, inner_dict in data_dict.items():
        result[outer_key] = {}
        for inner_key, values in inner_dict.items():
            if inner_key == 'pages':
                result[outer_key][inner_key] = len(values)
            else:
                result[outer_key][inner_key] = values
    return result