# Tấn công từ chối dịch vụ trong mạng IoT và giảm thiểu

Báo cáo tiểu luận cuối kỳ – Học phần: Bảo mật IoT (INT4410)  
Trường Đại học Văn Hiến – Khoa Công nghệ Thông tin  
**Đề tài:** 25 — Tấn công từ chối dịch vụ trong mạng IoT và giảm thiểu (Hướng D)  
**Sinh viên thực hiện:** Trịnh Minh Hoàng Bảo — MSSV 231A010432  
**Lớp học phần:** 253INT441001 (INT4410) — Bảo mật IoT  
**Giảng viên hướng dẫn:** Hồ Nhựt Minh  

---

## Phạm vi nghiên cứu

Đề tài tập trung nghiên cứu, thiết kế và triển khai mô hình phòng thủ chống lại các cuộc tấn công Từ chối dịch vụ (DoS/HTTP Flood) nhắm vào tầng API Gateway trong hệ thống IoT quy mô nhỏ thông qua:
* Nhận diện và phân loại tài sản hệ thống, xác định ranh giới tin cậy (Trust Boundary).
* Phân tích mối đe dọa, lỗ hổng và mô hình hóa theo khung STRIDE.
* Triển khai mô hình giả lập API Gateway bằng ngôn ngữ Python (micro-framework Flask) tích hợp cơ chế giới hạn tần suất (Rate Limiting) bằng `Flask-Limiter`.
* Xây dựng script kiểm thử tự động (`flood_test.py`) để mô phỏng lưu lượng chuẩn (200 OK) và kịch bản ngập lụt quá tải (429 Too Many Requests).
* Lưu trữ toàn bộ minh chứng chạy thực nghiệm, log hệ thống và ảnh chụp màn hình tại thư mục `results/logs/` và `results/screenshots/`.

Mọi thử nghiệm đều được thực hiện trong môi trường phòng lab nội bộ (Localhost), không tác động hay tấn công hệ thống thực tế và không sử dụng dữ liệu cá nhân nhạy cảm.

---

## Cấu trúc repository

text
iot-gateway-dos-defense/
├── README.md
├── report/
│   └── Baocao/
│       ├── 231A010432_TrinhMinhHoangBao_DeTai25_TieuLuan_CuoiKy.docx
│       └── 231A010432_TrinhMinhHoangBao_DeTai25_TieuLuan_CuoiKy.pdf
├── slides/
│   ├── SlideTrinhBay.pptx
│   └── SlideTrinhBay.pdf
├── results/
│   ├── screenshots/
│   │   ├── Demo.PNG
│   │   └── SoDoCauTruc.png
│   └── logs/
│       ├── syslogs.txt
│       ├── TC-01.PNG
│       ├── TC-02-Client.PNG
│       ├── TC-02-Server.PNG
│       ├── TC-04.PNG
│       └── TC-05.PNG
├── src/
│   ├── app.py              # API Gateway (Flask + Flask-Limiter)
│   └── flood_test.py       # Script mô phỏng kiểm thử DoS & Rate Limiting
├── data/
│   └── payload_mau.json    # Payload JSON mẫu mô phỏng dữ liệu cảm biến
├── configs/
│   └── config.json         # Tệp cấu hình tham số hệ thống
└── references/
    └── link_nguon.md       # Danh mục nguồn tài liệu chi tiết
Hướng dẫn sử dụng và chạy Lab
Đọc báo cáo chi tiết:

Tham khảo tệp báo cáo đầy đủ tại report/Baocao/.

Khởi động API Gateway (Terminal 1):

Kích hoạt môi trường ảo venv và chạy máy chủ Flask:

DOS
python src/app.py
(Server sẽ lắng nghe tại http://127.0.0.1:5000)

Chạy Script kiểm thử và mô phỏng DoS (Terminal 2):

Thực thi script kiểm thử để quan sát trạng thái phản hồi hợp lệ (200 OK) và trạng thái bị chặn khi vượt ngưỡng (429 Too Many Requests):

DOS
python src/flood_test.py
Cam kết an toàn
Toàn bộ nội dung được thực hiện trong môi trường học tập và nghiên cứu (mô phỏng cục bộ).

Không sử dụng dữ liệu cá nhân thật; tệp payload_mau.json chỉ chứa dữ liệu giả lập thông số môi trường.

Không chứa secret, token, mật khẩu hoặc thông tin nhạy cảm.


---

### 3. Nội dung tệp `references/link_nguon.md`

```markdown
# Danh mục nguồn tài liệu tham khảo

1. OWASP Foundation — OWASP Internet of Things Security Verification Standard (ISVS) — https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS — Truy cập ngày 17/07/2026 — Dùng cho Chương 2, 3 và 6 (Khung tiêu chuẩn xác thực an ninh IoT)[cite: 1].
2. OWASP Foundation — OWASP IoT Security Testing Guide (ISTG) — https://github.com/OWASP/owasp-istg — Truy cập ngày 17/07/2026 — Dùng cho Chương 3 và 5 (Phương pháp luận kiểm thử xâm nhập tài nguyên).
3. Pallets Projects — Flask Documentation & Repository — https://github.com/pallets/flask — Truy cập ngày 17/07/2026 — Dùng cho Chương 3 và 4 (Xây dựng API Gateway).
4. OWASP Foundation — OWASP Top 10 Internet of Things — https://owasp.org/www-project-internet-of-things/ — Truy cập ngày 17/07/2026 — Dùng cho Chương 2 và 5 (Tham chiếu các nguy cơ bảo mật phổ biến).
5. International Organization for Standardization — ISO/IEC 27400:2022 - Cybersecurity — IoT — Guidelines for risk management — (Tài liệu tiêu chuẩn quốc tế) — Truy cập ngày 17/07/2026 — Dùng cho Chương 3 và 5 (Nguyên tắc kiểm soát rủi ro IoT).
6. Trịnh Minh Hoàng Bảo — Tấn công từ chối dịch vụ trong mạng IoT và giảm thiểu (Mã nguồn đề tài) — ht
