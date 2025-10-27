# QUERY ENHANCEMENT
-	Khái niệm:
Query Enhancement là một kĩ thuật để tăng cường hoặc reformat lại câu truy vấn của user để truy xuất được tài liệu liên quan nhiều hơn, tốt hơn
Được sử dụng khi:
+ Câu truy vấn gốc quá ngắn, mơ hồ
+ Muốn mở rộng phạm vi để bắt từ đồng nghĩa, các phrase liên quan hoặc spelling variant ( ví dụ colour = color)

-	Query Expansion:
Ví dụ về Query Expansion:
 
<img width="975" height="408" alt="image" src="https://github.com/user-attachments/assets/707ff395-0d64-419b-96f1-5f0615c13031" />

Cách hoạt động: sử dụng LLM + prompt để tăng cường query sau đó mới đưa vào retriever
  
<img width="975" height="809" alt="image" src="https://github.com/user-attachments/assets/c29b6b19-c51f-4ef9-a4a8-7f861d2d18d5" />

Ví dụ sử dụng:
+ Tạo prompt để model tiến hành query expansion
 
<img width="975" height="189" alt="image" src="https://github.com/user-attachments/assets/e9326c2c-02f9-4612-87de-d2e4cb2d76e3" />

+ Query Expansion chain:
 
<img width="975" height="154" alt="image" src="https://github.com/user-attachments/assets/812e1269-5519-41ea-897f-ed7f3aa70e5c" />

+ Ví dụ kết quả sau khi thực hiện query expansion:
 
<img width="975" height="216" alt="image" src="https://github.com/user-attachments/assets/6120d10f-2736-4a40-9e5b-eebed1bccd82" />

+ Đưa vào RAG chain và sử dụng:
 
<img width="975" height="459" alt="image" src="https://github.com/user-attachments/assets/c8878b34-4d0b-4b84-9491-4c3461619f2b" />
 
<img width="975" height="126" alt="image" src="https://github.com/user-attachments/assets/07e7924e-2c43-4c46-acec-1331b58e3786" />

-	Query Decomposition:
Là một kĩ thuật dùng để xử lý một câu hỏi dài, có nhiều phần. Kĩ thuật này sẽ chia nhỏ câu hỏi dài ra thành các câu hỏi nhỏ hơn mà có thể thực hiện truy vấn và phản hồi một cách độc lập

Lý do sử dụng Query Decompositon:
+ Các query phức tạp thường chứa nhiều khái niệm
+ LLM hoặc retriever có thể bỏ qua một số phần trong câu hỏi gốc
+ Cho phép suy luận nhiều bước
+ Cho phép thực hiện song song (multi-agent)

Cách hoạt động:

<img width="975" height="782" alt="image" src="https://github.com/user-attachments/assets/989aba03-39a2-4dc3-aa7f-bb6fb2f7fa7d" />
 
Nhược điểm: gọi LLM quá nhiều dẫn đến phản hồi chậm và chi phí cao

-	Hypothetical Document Embeddings (HyDE)
Là một kĩ thuật truy vấn, thay vì biến đổi trực tiếp query từ user sau đó tìm kiếm trong vector store thì trước hết ta sẽ dùng một LLM để tạo ra một câu trả lời giả định (Hypothetical) từ câu hỏi đó và sau đó biến đổi câu trả lời giả định này sang vector và bắt đầu tìm kiếm trong vector store

Vì sao dùng HyDE:
+ Queries quá ngắn, mơ hồ: LLM sẽ tạo ra câu trả lời giàu ngữ nghĩa hơn
+ Khả năng tổng quát hóa: hoạt động tốt ngay cả khi cách diễn đạt của tài liệu khác với câu hỏi do HyDE không bị "ám ảnh" bởi cách diễn đạt (phrasing) cụ thể ví dụ như từ vựng giữa query và documents là khác nhau. Do HyDE sẽ embed theo câu trả lời thay vì câu hỏi
+ Sử dụng LLM để hiểu ý định thực sự đằng sau câu hỏi, cung cấp ngữ cảnh tốt hơn, vector hóa câu trả lời giả định, thứ mà trông giống câu trả lời thật sự
+ Zero-shot Retrieval: không cần huấn luyện embedding model trên tập document riêng, thay vào đó tận dụng khả năng zero-shot của các LLM mạnh sinh ra các tài liệu giả định chi tiết từ đó embedding model sẽ sinh ra vector giống với tài liệu trong vector store/database


Cách hoạt động:
 
<img width="975" height="438" alt="image" src="https://github.com/user-attachments/assets/b725f43e-4c1e-4818-b6ee-f0516a623ed2" />

Ví dụ sử dụng:
 
<img width="975" height="555" alt="image" src="https://github.com/user-attachments/assets/af2ac28a-0b18-476c-a926-56b59c416cfd" />

<img width="975" height="470" alt="image" src="https://github.com/user-attachments/assets/ea38b6f3-c903-415a-912c-7af356fe7569" />

 
