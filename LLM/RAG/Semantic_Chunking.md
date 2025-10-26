# SEMANTIC CHUNKING

-	Khái niệm về semantic chunking:
là một quá trình để chia các documents thành các chunks dựa trên độ tương đồng về ngữ nghĩa, không phải bởi số token hay số dòng. Điều này giúp tăng cường sự mạnh mẽ của hệ thống RAG do mỗi chunk giờ đây sẽ giàu thông tin hơn, làm cho việc sinh phản hồi tốt và chính xác hơn

-	Các bước hoạt động:
1. Documents được chia thành các đơn vị nhỏ hơn thường là một câu
2. Mỗi câu sẽ được biến đổi sang vector (sentence embedding)
3. Tính độ tương đồng (similarity) giữa các embedding gần nhau (câu 1 và câu 2, câu 2 và câu 3, …)
4. Merge các embedding gần nhau lại nếu similarity giữa chúng vượt qua một ngưỡng nhất định (threshold)
5. Hình thành các chunks sau khi merge. Ví dụ [s1,s2] -> chunk1, [s3] -> chunk2

-	Ví dụ về semantic chunking
 
<img width="975" height="426" alt="image" src="https://github.com/user-attachments/assets/7305bdb3-cb5b-40ff-b804-4a93c7bd5331" />

-	Semantic chunking trong code:
+ Split document thành các câu:
 
<img width="975" height="463" alt="image" src="https://github.com/user-attachments/assets/6454f114-54fa-4b1c-b913-dcf5805ab406" />

+ Biến đổi mỗi câu sang vector
 
<img width="688" height="148" alt="image" src="https://github.com/user-attachments/assets/a27e12b2-e967-4ae1-a9bf-e3a974cfc9d2" />

+ Khởi tạo các tham số
 
<img width="675" height="222" alt="image" src="https://github.com/user-attachments/assets/9ec00384-e403-4a67-ba30-724ebf8b0356" />

+ Tính toán similarity giữa các câu liền kề và tiến hành merge những câu có similarity cao
 
<img width="975" height="493" alt="image" src="https://github.com/user-attachments/assets/3edc5c31-bc7d-4ac8-a8aa-eb6a8fb66d79" />

+ Kết quả
 
<img width="975" height="183" alt="image" src="https://github.com/user-attachments/assets/25c23eb6-8a91-4d63-a4d2-5e2e19e3ae20" />

-	Sử dụng SemanticChunker trong trong thư viện langchain_experimental
 
<img width="975" height="440" alt="image" src="https://github.com/user-attachments/assets/e6250655-13c4-4b39-ab5a-73e48d5e4abe" />
 
