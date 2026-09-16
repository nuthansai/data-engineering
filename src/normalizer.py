def normalize_data(data):
    if not data:
        return None

    normalized = {}

    for k, v in data.items():
        if isinstance(v, str):
            if k in ("event", "page"):
                normalized[k] = v.strip().lower()
            else:
                normalized[k] = v
        else:
            normalized[k] = v

    return normalized