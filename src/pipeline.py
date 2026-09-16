from src.parser import parse_json
from src.normalizer import normalize_data
from src.validator import is_valid_click


# def get_valid_records(lines):
#     records = []
#     print("Entered pipeline")
#     for line in lines:
#         data = parse_json(line)
#         data = normalize_data(data)
#
#         if not is_valid_click(data):
#             continue
#
#
#         records.append(data)
#     print(records)
#     return records

def get_valid_records(lines):
    records = []
    # unique_data = set()
    # print("Entered pipeline")
    seen = set()

    for line in lines:
        line = line.strip()

        if not line:
            continue
        if line in seen:
            continue

        seen.add(line)

        # parse → normalize → validate → append
        data = parse_json(line)
        data = normalize_data(data)

        if not is_valid_click(data):
            continue

        records.append(data)

    return records