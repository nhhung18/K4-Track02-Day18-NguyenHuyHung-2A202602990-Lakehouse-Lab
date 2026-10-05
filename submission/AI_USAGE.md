# Khai Báo Sử Dụng Trợ Lý AI (AI Usage Declaration)

Theo quy định học tập của chương trình, phạm vi sử dụng trợ lý AI (Gemini / Antigravity Agent) trong bài làm cá nhân này được công khai minh bạch như sau:

## 1. Mục đích và phạm vi sử dụng:
- **Tự động hóa thực thi và kiểm thử:** Hỗ trợ thực thi lệnh `scripts/execute_and_render_notebooks.py`, chạy headless 8 notebook và bộ 24 test cases của pytest để kiểm tra tính toàn vẹn của mã nguồn.
- **Sinh dữ liệu và kiểm tra số liệu:** Hỗ trợ tính toán đối chiếu các chỉ số benchmark trong rubric (file compaction ratios, pruning speedup, int8 vector recall@10, cosine similarity).
- **Soạn thảo và kiểm duyệt tài liệu:** Hỗ trợ rà soát cấu trúc báo cáo kiến trúc bonus (`ARCHITECTURE.md`) đảm bảo tuân thủ đầy đủ 6 tiêu chí khắt khe của Rubric.

## 2. Trách nhiệm học viên:
- Toàn bộ kết quả thực nghiệm, transaction logs, các bài đo lường Delta/Iceberg và giải thích nguyên lý vận hành do chính học viên chịu trách nhiệm thẩm định và giải trình.
