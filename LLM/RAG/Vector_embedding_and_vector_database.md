# VECTOR EMBEDDING AND VECTOR DATABASE
-	Introduction to Embeddings and Vector Databases

<img width="975" height="826" alt="image" src="https://github.com/user-attachments/assets/96098b58-71b6-4c6c-8f4b-6d9fdf71417d" />
 
So sánh giữa databases truyền thống và vector databases:
+ Khi tìm kiếm data trong databases truyền thống thì chỉ cho ra kết quả tuyệt đối (có, không). Ví dụ tìm từ  ‘cat’ thì chỉ cho ra kết quả về ‘cat’
+ Khi tìm kiếm data trong vector databases thì kết quả tìm được có thể vừa là data ta cần tìm và cả data tương đồng với nó nữa. Ví dụ tìm từ ‘cat’ ta có thể có kết quả về ‘cat’ và ‘kitten’
Nhờ vậy mà vector database được ứng dụng rất rộng rãi hiện nay, ví dụ như các recommendation system, v.v. Và RAG system cũng không ngoại lệ

-	Embedding là gì
Embedding là một kĩ thuật để ánh xạ word (token) sang biểu diễn dạng số học (không gian vector) mà máy tính có thể hiểu

<img width="975" height="729" alt="image" src="https://github.com/user-attachments/assets/b3d8de2b-9225-443b-ab4d-b97264545726" />
 
Ví dụ về biểu diễn embedding vector của các word. Như ta thấy thì cat sẽ gần kitten hơn thay vì dog hay car do giữa cat và kitten có độ tương đồng về ngữ nghĩa cao hơn, từ đó khoảng cách giữa chúng trong không gian vector cũng nhỏ hơn
-	Cosine Similarity
Cosine similarity là một kĩ thuật để tính độ tương đồng giữa các vector. 
Có 3 trường hợp xảy ra với kết quả từ cosine similarity:
+ Gần 1: 2 vector tương đồng nhau
+ Gần 0: 2 vector không liên quan đến nhau
+ Gần -1: 2 vector trái nghĩa nhau
 Công thức tính như sau:

<img width="975" height="348" alt="image" src="https://github.com/user-attachments/assets/9559ecc9-3462-4878-8784-76ee4e0709e5" />

Triển khai trong code:
 
<img width="975" height="551" alt="image" src="https://github.com/user-attachments/assets/52295500-b829-46e9-ae65-e3c3616e4c30" />

-	Tạo embedding vector với model từ HuggingFace
Load model:
 
<img width="963" height="258" alt="image" src="https://github.com/user-attachments/assets/67a89fb2-e8dc-4214-9d6f-1037f3442d8e" />

Tiến hành embedding:
 
<img width="975" height="691" alt="image" src="https://github.com/user-attachments/assets/547d106a-108b-41e1-9e7b-22d1d6a5ac79" />

So sánh một vài embedding model nổi bật:
 
<img width="975" height="999" alt="image" src="https://github.com/user-attachments/assets/4db9740e-deb5-4f19-bdfc-12f0933216e7" />

-	OPENAI embedding models:
Setup môi trường để sử dụng model từ OPENAI:
+ Chúng ta cần có một account OPENAI, và credit (money) trong account đó
+ Tiếp theo là tạo API_KEY và đưa vào file .env

<img width="975" height="276" alt="image" src="https://github.com/user-attachments/assets/b6fe12fb-d237-4063-8f7a-e5ec7194d00f" />
 
+ Load API_KEY vào file code với hàm load_dotenv từ dotenv. Set biến môi trường với os.environ và lấy key từ os.getenv

<img width="975" height="398" alt="image" src="https://github.com/user-attachments/assets/3c3e4fe0-1699-49a2-874b-cc594eb3b03f" />
 
+ Sau đó ta có thể sử dụng model một cách bình thường

-	Một vài so sánh giữa các model từ OPENAI

<img width="845" height="753" alt="image" src="https://github.com/user-attachments/assets/3d25f283-b16d-4846-a5d7-6f4af953d2e1" />
 
(Legacy applications là các ứng dụng cũ nhưng vẫn rất quan trọng ở hiện tại, gây khó găn trong việc bảo trì và nâng cấp)
-	Semantic Search:
Là một kĩ thuật để tìm kiếm các vector có độ tương đồng (similarity) cao với query vector
Ví dụ sử dụng:

<img width="975" height="308" alt="image" src="https://github.com/user-attachments/assets/395e6976-1832-49ff-a9b3-042140f9c84e" />

Giả sử chúng ta có query (câu truy vấn hay input) và documents (data được lưu trong database)

<img width="664" height="364" alt="image" src="https://github.com/user-attachments/assets/6c20f354-a640-40d1-b354-823364cc4148" />

Cài đặt hàm tính cosine similarity để so sánh giữa query và vector trong database

<img width="975" height="671" alt="image" src="https://github.com/user-attachments/assets/2066d3c1-ad1f-4206-8787-9ada1a37cad4" />

Hàm semantic_search sẽ tiến hành tính cosine_similarity cho query với từng vector trong database và trả về top_k vector có độ tương đồng cao nhất (cùng với document ứng với nó) so với query

