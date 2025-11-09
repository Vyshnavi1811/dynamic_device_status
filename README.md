# Device Status Monitor

## Overview
Flask + PostgreSQL backend; Vanilla JS frontend. Shows devices per company and marks them online/offline based on recent readings.

## Requirements
- Python 3.10+, PostgreSQL 12+, Node/npm (optional), Docker (optional)

## Quick start
1. Create DB:
   - `createdb device_monitor`
   - `psql -d device_monitor -f db/init.sql`
   - `psql -d device_monitor -f db/seed.sql`
2. Backend:
   - `cd backend`
   - `python -m venv venv && source venv/bin/activate`
   - `pip install -r requirements.txt`
   - configure env vars: `DB_USER, DB_PASS, DB_HOST, DB_NAME`
   - `python app.py`
3. Frontend:
   - open `frontend/index.html` or serve via `python -m http.server 8000`

## API
- `GET /api/companies` -> `{ success: true, companies: [ {id, name}, ... ] }`
- `GET /api/companies/<company_id>/devices` -> `{ success: true, devices: [ {id, device_name, device_identifier, last_reading, status}, ... ] }`

## Assumptions
- Device is online if latest reading is within N seconds (configurable; default 120s).
- Timestamps use tz-aware `timestamptz`.

## Extensibility
- Add auth, websocket push, device details page, device health metrics, etc.

## Testing
- Use `simulate_readings.py` to simulate live readings.
