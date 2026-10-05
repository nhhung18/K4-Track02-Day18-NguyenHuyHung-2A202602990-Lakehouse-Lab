# Reflection: Lakehouse Anti-Pattern Analysis

Trong các hệ thống RAG và LLM Observability quy mô lớn, anti-pattern nguy hiểm và dễ vướng nhất là **"The Stale Shadow Index" (Đồng bộ một chiều giữa Lakehouse và Vector DB rời)**.

### Lý do dễ vướng:
Khi xây dựng AI pipeline, đội ngũ kỹ sư thường lưu metadata vào Lakehouse (Delta/Iceberg) và đẩy embeddings sang Vector DB bên ngoài (Qdrant, Pinecone) qua cơ chế batch upsert một chiều. Khi người dùng thực hiện quyền riêng tư (GDPR/Nghị định 13) hoặc xóa dữ liệu lỗi, lệnh `DELETE` được commit trên Lakehouse nhưng Vector DB vẫn giữ nguyên embedding cũ do không nhận được delete event. Kết quả là RAG vẫn trả về dữ liệu đã xóa, gây vi phạm bảo mật nghiêm trọng.

### Cách phòng tránh:
1. **Delta Change Data Feed (CDF):** Kích hoạt CDF trên bảng embeddings để Vector DB đăng ký nhận luồng `_change_type = delete` và evict index tức thì.
2. **In-row Vector Storage:** Lưu vector trực tiếp trong Parquet (lượng tử hóa int8) và truy vấn semantic search nội bộ bằng DuckDB/LanceDB cho các bài toán phân tích mà không cần sync ngoài.

*(Sử dụng AI hỗ trợ phân tích và rà soát cú pháp theo `AI_USAGE.md`)*
