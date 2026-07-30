import time
import json
import requests

# Đảm bảo endpoint khớp với Server (/telemetry)
URL = "http://127.0.0.1:5000/telemetry"
PAYLOAD_PATH = "data/payload_mau.json"

def load_payload():
    try:
        with open(PAYLOAD_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "device_id": "sensor_node_01",
            "temperature": 28.5,
            "humidity": 65.0
        }

def run_test():
    payload = load_payload()
    print("--- [TC-01] Kiểm tra lưu lượng hợp lệ (Nhịp độ chậm) ---")
    
    # Giai đoạn 1: Lưu lượng hợp lệ (TC-01)
    for i in range(2):
        res = requests.post(URL, json=payload)
        try:
            data = res.json()
        except:
            data = res.text
        print(f"Request {i+1}: Status Code = {res.status_code} | Phản hồi: {data}")
        time.sleep(1)

    print("\n--- [TC-02] Mô phỏng tấn công ngập lụt (Gửi dồn dập vượt ngưỡng 5 lần/10s) ---")
    
    # Giai đoạn 2: Tấn công dồn dập kích hoạt 429 (TC-02 & TC-04)
    for i in range(7):
        res = requests.post(URL, json=payload)
        try:
            data = res.json()
        except:
            data = res.text
        print(f"Flood Request {i+1}: Status Code = {res.status_code} | Phản hồi: {data}")

if __name__ == "__main__":
    run_test()