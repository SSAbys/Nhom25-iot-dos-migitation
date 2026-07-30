from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import datetime

app = Flask(__name__)

# Khởi tạo Flask-Limiter cấu hình giới hạn (Ví dụ: tối đa 5 requests / 10 giây)
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["5 per 10seconds"]
)

@app.route('/telemetry', methods=['POST'])
def handle_telemetry():
    # Xử lý lưu lượng hợp lệ
    return jsonify({
        "status": "success",
        "message": "Đã tiếp nhận dữ liệu cảm biến thành công."
    }), 200

# Hàm tùy chỉnh thông điệp trả về khi vượt quá giới hạn (Rate Limit Exceeded -> 429)
@app.errorhandler(429)
def ratelimit_handler(e):
    client_ip = get_remote_address()
    # In cảnh báo lên console của Server (khớp với hình minh họa TC-02-Server.PNG)
    print(f"[!] Cảnh báo: Phát hiện lưu lượng vượt ngưỡng từ IP {client_ip} (Dấu hiệu DoS/Flooding)")
    return jsonify({
        "error": "Too Many Requests",
        "message": "Vượt quá giới hạn cho phép. Yêu cầu đã bị từ chối để bảo vệ hệ thống."
    }), 429

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)