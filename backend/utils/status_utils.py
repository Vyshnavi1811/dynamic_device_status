from datetime import datetime, timedelta, timezone

def determine_status(last_timestamp):
    if not last_timestamp:
        return "offline"
    now_utc = datetime.now(timezone.utc)
    if last_timestamp.tzinfo is None:
        last_timestamp = last_timestamp.replace(tzinfo=timezone.utc)
    if now_utc - last_timestamp <= timedelta(minutes=2):
        return "online"
    return "offline"