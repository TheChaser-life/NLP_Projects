# CORE COMPONENTS IN RAG
-	RAG có 3 phần cốt lõi:

<img width="975" height="649" alt="image" src="https://github.com/user-attachments/assets/2ee8acd3-7ae4-46bb-b403-358e6d50e98e" />

1.	 Document Ingestion and Preprocessing: là quá trình thu thập, xử lý và nạp các tài liệu vào một hệ thống để chúng sẵn sàng cho việc tìm kiếm và phân tích. Gồm các bước:

<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/754b1efc-9d6c-4e4f-88da-7738ce2fd3f5" />

+ Đầu tiên ta cần chuẩn bị dữ liệu (pdf, doc, website, …)
+ Chia data thành các chunks. Lý do cho việc này là để giới hạn về kích thước do model không thể xử lý file quá lớn, tăng cường hiệu quả truy xuất vì khi chia nhỏ data thành các chunks có kích thước vừa phải thì hệ thống RAG có thể tìm được thông tin cần thiết dễ dàng hơn trong mỗi chunk, cuối cùng là tiết kiệm chi phí và tăng tốc độ tính toán
+ Sử dụng embedding model để ánh xạ mỗi chunks đó qua một vector embedding
+ Lưu trữ các vector embedding vào vector database


2.	Querry Processing Phase: là quá trình xử lý inputs và kết hợp nó với các thông tin liên quan để tạo nên context hoàn chỉnh sẵn sàng tạo câu trả lời. Các bước thực hiện:
 
<img width="975" height="535" alt="image" src="https://github.com/user-attachments/assets/e986614d-e62e-4b80-ab91-32b9ef094adf" />

+ Sử dụng embedding model ánh xạ inputs sang embedding vector
+ Dùng các kĩ thuật cosine similarity, euclidcian distance, similarity search để tìm các vector trong vector database có độ tương đồng cao (có khả năng cao là câu trả lời) với vector inputs 
+ Kết hợp các vector tương đồng vừa trích xuất tạo thành context
+ Tăng cường context bằng cách thêm metadata (Augment). Metadata là dữ liệu của dữ liệu, nó cho biết các thông tin như data này được tạo ra ngày nào, bởi ai, nằm ở đâu trong tài liệu
+ Kết hợp với input (câu truy vấn) thành một context hoàn chỉnh


3.	Generation Phase: sau khi có được context hoàn chỉnh, tiến hành đưa vào các LLM để tạo ra câu trả lời “giống con người”

<img width="975" height="437" alt="image" src="https://github.com/user-attachments/assets/24511238-85c5-46d0-8fe1-467c3b10dcc4" />

 

