import json


def parse_json(line):
    try:
        if not line:
            return None

        if '{' not in line:
            return None

        start = line.find('{')

        json_part = line[start:]
        timestamp = line[:start].strip()
        data = json.loads(json_part)
        data["timestamp"] = timestamp
    except json.JSONDecodeError:
        return None
    return data
