# HYBRID SEARCH STRATEGIES
-	Khái niệm:
Là sự kết hợp giữa dense (dày đặc) score và sparse (thưa) score để cải thiện khả năng tìm kiếm document vừa đúng ý vừa đúng keyword
Dense vector là vector có chứa nhiều số khác 0 do được tạo bởi các embedding model và mang nhiều ngữ nghĩa
Dense retriever: là retriever truy xuất nghĩa dựa trên ngữ cảnh bằng cách sử dụng vector embedding
Sparse vector là vector có nhiều số 0 do được tạo ra bởi các kĩ thuật dựa trên xác suất xuất hiện của các từ
Sparse retriever: là retriever tìm chính xác từ cần tìm bằng các kĩ thuật như TF-IDF hoặc BM25

-	Điểm mạnh của Hybrid Search:
+ Boost recall (sự bao phủ): BM25 có thể bắt được keyword matches mà dense retriever có thể sót, dense retriever có thể bắt được ngữ nghĩa kể cả khi keyword khác nhau. Kết hợp chúng lại, ta có thể giảm rủi ro bỏ sót document
+ Xử lý synonyms và rephrasing: đây là điểm mạnh của dense retriever khi tìm kiếm dựa trên ngữ cảnh
+ Cải thiện sự robustness (khả năng duy trì độ chính xác và đưa ra dự đoán đúng đắn, ngay cả khi dữ liệu đầu vào có vấn đề) của truy vấn
+ Hỗ trợ sự quan trọng của các keywords: BM25 cho điểm các từ hiếm gặp cao hơn, điều này rất quan trọng trong các lĩnh vực có nhiều từ chuyên ngành như kĩ thuật, luật pháp, y tế
+ Thích nghi tốt với nhiều loại văn bản trong kho dữ liệu lớn; với các loại có cấu trúc tốt (well-structured text) như tài liệu kĩ thuật, văn bản pháp lý thì tìm kiếm keyword/sparse làm rất tốt do tìm chính xác các thuật ngữ, tên riêng, mã sản phẩm; với các loại được viết một cách không chỉnh chu (loosely written text) thì tìm kiếm semantic/dense làm rất tốt do hiểu được ý nghĩa và chủ đề chung
+ Dễ dàng điều chỉnh thông qua tham số đặt bên dense retriever và sparse retriever
+ Xử lý được các trường hợp sai chính tả   

-	Ví dụ sử dụng:
+ Khởi tạo mẫu:
 
<img width="975" height="261" alt="image" src="https://github.com/user-attachments/assets/9933ef6f-5c87-47b8-852f-b5b570d8a52a" />

+ Khởi tạo dense retriever:
 
<img width="975" height="159" alt="image" src="https://github.com/user-attachments/assets/f476bfef-fc5c-46e5-9671-dc64194157a7" />

+ Khởi tạo sparse retriever:
 
<img width="883" height="181" alt="image" src="https://github.com/user-attachments/assets/ec065280-4795-4c57-b031-046ec6b31ec6" />

+ Kết hợp dense retriever và sparse retriever,  tạo thành hybrid retriever. Tham số weights có nghĩa là lấy 70% score của dense retriever và 30% score của sparse retriever để kết hợp với nhau
 
<img width="864" height="256" alt="image" src="https://github.com/user-attachments/assets/05934e44-2d2f-4f86-a34d-cf5e720d56ae" />

+ Sử dụng hybrid retriever:
 
<img width="905" height="830" alt="image" src="https://github.com/user-attachments/assets/8a217577-ea68-4e04-a5f3-03b83095af28" />

+ Giải thích các bước hoạt động của hybrid retriever:
Khi hybrid retriever nhận query, sẽ có hai hoạt động xảy ra:
1.	Query được vector hóa bởi sparse retriever bởi các kĩ thuật như TF-IDF/BM25 dựa trên tần suất các từ trong query so với tần suất của các từ đó trong documents. Query sau khi được vector hóa sẽ được đem đi tính cosine similarity giữa nó và các vector khác cũng đã được vector hóa bởi sparse retriever
2.	Query sẽ được vector hóa bởi embedding model và dense retriever sẽ đi tính cosine similarity giữa vector query và các embedding vector khác 
3.	Sau đó mỗi score sẽ được nhân cho trọng số đã được gán sẵn cho sparse và dense retriever rồi cộng lại với nhau cho ra kết quả cuối cùng 

-	Re-Ranking Techniques:
+ Là một kĩ thuật dùng để sắp xếp lại các document được lấy ra từ vector store hay vector db thông qua bước truy vấn nhằm tăng cường độ chính xác của câu trả lời cuối cùng
+ Các bước thực hiện re-rank:
1.	Nhận documents từ retriever
  
<img width="797" height="631" alt="image" src="https://github.com/user-attachments/assets/9d44d07e-f8cd-4a16-bfdf-5a6c42fa188b" />

2.	Khởi tạo model để re-rank
 
<img width="927" height="113" alt="image" src="https://github.com/user-attachments/assets/0f6a9340-0d9f-42b9-b704-8ec1b63f73f3" />

3.	Viết prompt yêu cầu model re-rank
 
<img width="975" height="310" alt="image" src="https://github.com/user-attachments/assets/7f7b45ed-7209-4848-a04e-1abf962774f5" />

4.	Tạo re-ranking chain
 
<img width="863" height="111" alt="image" src="https://github.com/user-attachments/assets/430a1df2-6fab-4345-b39b-34e949d721df" />

5.	Nối các documents nhận được từ retriever thành một chuỗi để đưa vào prompt
 
<img width="975" height="106" alt="image" src="https://github.com/user-attachments/assets/edbdfb51-b3f5-4189-9915-5e5b4c8ba89b" />

6.	Lấy response từ model
 
<img width="975" height="328" alt="image" src="https://github.com/user-attachments/assets/01ec9d59-7da2-4f8b-8409-1cc98e0d6bc9" />

7.	Lược lấy dãy số từ model
 
<img width="975" height="517" alt="image" src="https://github.com/user-attachments/assets/ad9ea103-8725-4384-8040-304ecd8aefd5" />

8.	Thực hiện sắp xếp lại documents
 
<img width="975" height="368" alt="image" src="https://github.com/user-attachments/assets/695b8bb5-c1d5-4f12-a2b6-4ed3248d485a" />

-	Maximal Marginal Relevance (MMR)
+ Khái niệm: là một kĩ thuật để re-rank nhằm đảm bảo sự liên quan (Relevance) và sự đa dạng (Diversity) giữa các documents với query
+ Công thức tính MMR score, vế trái (trước dấu trừ) đại diện cho sự liên quan và vế phải (sau dấu trừ) đại diện cho sự đa dạng:

<img width="972" height="102" alt="image" src="https://github.com/user-attachments/assets/416b66a8-b74a-4387-a77b-d5fd8d9f0a59" />
 
Trong đó:
1.	Lambda là một tham số có giá trị từ 0->1 dùng để điều chỉnh tầm quan trọng giữa sự liên quan và sự đa dạng
2.	Sim(d,q) là cosine similarity score giữa document d và query
3.	Max cosine similarity score giữa document d và document s với s thuộc tập S (là những document đã được chọn trước đó
+ Ví dụ sử dụng MMR, ta cài đặt retriever với tham số search_type=’mmr’:

<img width="709" height="222" alt="image" src="https://github.com/user-attachments/assets/d3047c13-cb9a-4ee7-ac2f-d06a98c44ddc" />
 
+ Khi nào nên sử dụng MMR:
1.	Xây dụng hệ thống RAG: để tránh đưa vào LLM các documents dư thừa
2.	Xây dựng Chatbot
3.	Retriever trả về nhiều kết quả, cần loại bỏ các documents dư thừa
4.	Kết hợp với Hybrid Search
+ Khi nào không nên sử dụng MMR:
1.	LLM có context window ngắn và chỉ cần  1 document liên quan nhất
2.	Chỉ cần sự chính xác (precision)
3.	Các documents đã đa dạng sẵn, không trùng lặp
4.	Đã thực hiện re-ranking với một model LLM
