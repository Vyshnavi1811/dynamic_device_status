from flask import Blueprint, jsonify
from models import get_companies

companies_bp = Blueprint('companies', __name__)

@companies_bp.route('/companies', methods=['GET'])
def companies():
    try:
        data = get_companies()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500