from db import get_db_connection
from utils.status_utils import determine_status

def get_companies():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM companies;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1]} for r in rows]


def get_devices_by_company(company_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT d.id, d.name, MAX(dr.timestamp)
        FROM devices d
        LEFT JOIN device_readings dr ON d.id = dr.device_id
        WHERE d.company_id = %s
        GROUP BY d.id, d.name;
    """, (company_id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    devices = []
    for r in rows:
        device_id, name, last_time = r
        status = determine_status(last_time)
        devices.append({
            "id": device_id,
            "name": name,
            "status": status
        })
    return devices