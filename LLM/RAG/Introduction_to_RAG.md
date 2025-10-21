# Introduction to RAG (Retrieval-Augmented Generation)

+ Khái niệm: là một kỹ thuật mạnh mẽ để tăng cường các model ngôn ngữ bằng việc kết hợp khả năng tạo sinh của chúng và khả năng truy xuất thông tin từ các nguồn được thêm  vào (Documents, PDF, …). Giống như cho AI quyền truy cập vào một thư viện trong khi chúng đang trả lời câu hỏi. Thay vì phụ thuộc vào các kiến thức mà AI có được trong quá trình huấn luyện, chúng có thể tìm kiếm các thông tin phù hợp trong các nguồn thông tin được thêm vào trước khi tạo ra câu trả lời và phản hồi người dùng

+ Ví dụ về cách hoạt động của RAG system:

<img width="975" height="483" alt="image" src="https://github.com/user-attachments/assets/019bbb0c-348b-473e-be32-0e2a293c51d8" />
 
1.	Người dùng đưa vào câu hỏi “Chính sách cho vay của ngân hàng này như nào ?”
2.	Hệ thống nhận câu hỏi, tiến hành truy xuất trong vector database với kĩ thuật similarity search nhằm tìm kiếm các thông tin có liên quan đến câu hỏi
3.	Sau khi có được các thông tin liên quan, tiến hành đưa các thông tin này vào câu hỏi gốc tạo nên một prompt hoàn chỉnh
4.	Đưa prompt vừa tạo (câu hỏi gốc + thông tin bổ sung) vào một LLM model để sinh ra phản hồi cuối cùng và đưa nó đến người dùng

+ Lợi ích sử dụng RAG system: cho model một nguồn thông tin đặc biệt, cụ thể về một hoặc một vài lĩnh vực, vấn đề nào đó mà có thể được truy xuất để đưa ra câu trả lời chính xác mà người dùng cần. Giảm tình trạng hallucination (model đưa ra thông tin sai lệch hoặc bịa đặt do data trong quá trình pretrain không hề chứa hoặc đã bị outdated so với thông tin mà user cần) và cả model không trả lời được câu hỏi do thiếu thông tin. 

<img width="975" height="753" alt="image" src="https://github.com/user-attachments/assets/7f2ec116-4d94-4d54-ac61-870b74f40bd9" />

Ngoài ra còn có các lợi ích khác như:

<img width="975" height="178" alt="image" src="https://github.com/user-attachments/assets/18cc161f-e1c6-4859-85d4-2a8e87e33852" />

+ Ví dụ về trường hợp sử dụng RAG:
  
<img width="975" height="637" alt="image" src="https://github.com/user-attachments/assets/1285ca09-bcd1-42ac-9e40-5f9586ee05ad" />
 
Nếu dùng LLM thuần, response nhận được sẽ chỉ mang tính chất chung hoặc thiếu chính xác do chúng chỉ dựa trên training data
Kết hợp RAG, bơm thêm một nguồn thông tin cụ thể về một công ty, response sẽ chi tiết, chính xác và tập trung vào nguồn thông tin được bơm vào đó

+ Ảnh hưởng của RAG đến các doanh nghiệp:
 
<img width="975" height="628" alt="image" src="https://github.com/user-attachments/assets/1f5c2f70-49ba-4efb-bd5a-672f71da1f78" />

+ So sánh Prompt Engineering, Fine Tuning, RAG:
  
<img width="975" height="698" alt="image" src="https://github.com/user-attachments/assets/7ca67e01-2151-4f98-9202-20f2508c9b95" />
 
1.	Prompt Engineering: hướng dẫn model trả lời bằng một cấu trúc prompt cụ thể cùng với nội dung rõ ràng. Model giữ nguyên không thay đổi gì cả (về mặt weight, kiến trúc)

Ưu điểm:
Không cần các kĩ thuật phức tạp
Có kết quả ngay lập tức
Không tốn phí training
Hoạt động với bất kì LLM

Nhược điểm:
	Bị giới hạn bởi kiến thức cơ bản của modle
	Câu trả lời không nhất quán
	Câu trả lời bị giới hạn về độ phức tạp do độ giới hạn token của câu trả lời
	Không thể thêm kiến thức mới

2.	Fine Tuning: chuẩn bị dữ liệu huấn luyện về một lĩnh vực cụ thể và huấn luyện model với các dữ liệu đó. Tham số gốc của model được thay đổi, tạo ra một phiên bản đặc biệt của model đó

Ưu điểm:
	Hiểu sâu về một kiến thức cụ thể
	Hành vi nhất quán
	Không cần kĩ thuật viết prompt
	Có thể học kiểu viết mới

Nhược điểm:
	Tốn kém chi phí
	Yêu cầu các chuyên gia trong lĩnh vực ML, LLM
	Có thể quên các kiến thức tổng quát
	Cần phải finetune lại nếu muốn cập nhật

3.	RAG: lưu trữ tài liệu trong vector database, truy xuất các tài liệu liên quan thông qua câu truy vấn, kết hợp truy vấn và tài liệu thành context, sau cùng LLM sẽ tạo câu trả lời từ context

Ưu điểm:
	Luôn luôn bắt kịp các thông tin mới
	Không cần train model
	Có thể trích dẫn thông tin từ các nguồn ngoài được thêm vào
	Có thể xử lý dữ liệu riêng tư, độc quyền
	Hiệu quả trong chi phí

Nhược điểm:
	Cần chuẩn bị hạ tầng (vector database)
	Phản hồi bị ảnh hưởng mạnh bởi chất lượng truy xuất
	Có độ trễ do bước truy xuất
	Giới hạn bởi cửa sổ ngữ cảnh (không thể xử lý một lúc tài liệu liên quan lớn)
	
+ Ví dụ về kiến trúc RAG:	

<img width="975" height="649" alt="image" src="https://github.com/user-attachments/assets/3262cce4-7341-4349-ac0c-29c63416ff5b" />

		

 

