def is_valid_click(data):
    if not data:
        return False

    required_keys = {"user_id", "event", "page"}

    if not required_keys.issubset(data.keys()):
        return False

    if data["user_id"] is None or data["page"] is None or data["page"] == "":
        return False

    if data["event"] != "click":
        return False

    return True