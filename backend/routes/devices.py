from flask import Blueprint, jsonify
from models import get_devices_by_company

devices_bp = Blueprint('devices', __name__)

@devices_bp.route('/devices/<int:company_id>', methods=['GET'])
def devices(company_id):
    try:
        data = get_devices_by_company(company_id)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500