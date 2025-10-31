# MULTIMODAL RAG

-	Khái niệm:
Về cơ bản Multimodal RAG có thể vừa xử lý dữ liệu dạng text và ảnh nhờ vào các LLM và embedding model được train với cả 2 dạng dữ liệu trên
Cách hoạt động:
 
<img width="975" height="406" alt="image" src="https://github.com/user-attachments/assets/40b71ed2-80ea-4fe6-9cf6-a73fc5aa4454" />

-	Giới thiệu về Contrastive Language-Image Pre-training (CLIP):
Để xử lý được vừa ảnh vừa text thì ta sẽ cần CLIPModel và CLIPProcessor:
1.	CLIPModel: là một multimodal được phát triển bởi OPENAI. Nó học sự liên kết giữa hình ảnh và văn bản; không chỉ nhìn ảnh và đọc chữ mà còn hiểu được khái niệm nào trong văn bản ứng với nội dung của ảnh nào
CLIPModel gồm hai phần chính:
+ Image Encoder: (thường là ViT) nhận hình ảnh và chuyển đổi sang vector
+ Text Encoder: (thường là transformers) nhận văn bản và chuyển đổi sang vector
Hai bộ encoder này được huấn luyện để cùng nhau đưa các cặp vector ( ảnh, text) khớp nhau đến gần nhau trong không gian nhúng (embedding space) và các cặp không khớp ra xa nhau

2.	CLIPProcessor: là một lớp (class), công cụ tiền xử lý dữ liệu cho CLIPModel
CLIPProcessor gồm hai phần chính:
+ Image Processor: xử lý hình ảnh. Nó lấy ảnh được đưa vào thực hiện resize (thay đổi kích thước ảnh về một kích thước cố định mà Image Encoder mong đợi) và normalize (chuẩn hóa giá trị của pixel dựa trên giá trị trung bình và độ lệch chuẩn mà mô hình đã được huấn luyện)
+ Tokenizer: xử lý văn bản. Nó lấy văn bản thô được đưa vào và thực hiện tokenization (tách câu thành các word hay sub-word nhỏ hơn) sau đó chuyển đổi các token sang id ứng với token đó, cuối cùng là padding/truncation (thêm hoặc cắt bớt token để đảm bảo mọi câu có độ dài như nhau)

-	Ví dụ sử dụng trong code:
Load CLIPModel và CLIPProcessor:
 
<img width="975" height="241" alt="image" src="https://github.com/user-attachments/assets/3616f04a-2388-4f63-a100-384eae3acdbd" />

Khởi tạo embedding function cho text và image
 
<img width="975" height="486" alt="image" src="https://github.com/user-attachments/assets/c4ec7980-1cd0-4714-ab84-06c6b06c8c6e" />

Load file PDF và tạo các storage để chứa chunk (text), image, embedding
 
<img width="797" height="378" alt="image" src="https://github.com/user-attachments/assets/d2f4b1b7-eca7-41a3-be18-b9edc5d56ed2" />

Tiến hành duyệt qua mỗi page:
+ Xử lý text: 
1.	Lấy text từ page với phương thức .get_text()
2.	Kiểm tra xem đoạn text có rỗng hay không
3.	Nếu không sẽ tiến hành tạo Document tạm thời với page_content=text sau đó split document đó thành các chunks
4.	Tiến hành embedding từng chunk

+ Xử lý image:
1.	Lấy mã định danh của ảnh; page.get_images() trả về 1 list các tuple, mỗi tuple sẽ chứa thông tin về một ảnh trên page và phần tử đầu tiên của mỗi tuple sẽ là mã định danh của mỗi ảnh, sau đó trích xuất dữ liệu thô (bytes) từ ảnh với mã định danh
 
<img width="975" height="267" alt="image" src="https://github.com/user-attachments/assets/b08507d7-454d-4dd8-852e-5250991a9aed" />

2.	Chuyển đổi dữ liệu bytes của ảnh sang đối tượng Image với 3 kênh màu
 
<img width="959" height="120" alt="image" src="https://github.com/user-attachments/assets/f74617cd-11de-47cb-9f87-152c54a9f31d" />

3.	Tạo id duy nhất cho mỗi ảnh dựa trên số trang và index của ảnh trên trang đó
 
<img width="703" height="105" alt="image" src="https://github.com/user-attachments/assets/a5a0b62c-86ec-48e5-ba51-aeb35a76f737" />

4.	Lưu vào bộ nhớ RAM với định dạng PNG để xử lý các bước tiếp theo như mã hóa base64 và gửi qua API mà không cần tốn thời gian tạo và xóa một tệp tin trên ổ đĩa. Sau đó mã hóa ảnh dưới dạng base64 (một chuỗi văn bản đại diện cho ảnh) và lưu nó vào một dictionary với img_id (id duy nhất cho mỗi ảnh) làm khóa, để sau này có thể lấy ảnh gốc hiển thị hoặc đưa vào model AI
 
<img width="975" height="228" alt="image" src="https://github.com/user-attachments/assets/f7652eb2-bdfe-405f-85c3-7133a8bd2cce" />

5.	Tiến hành embedding ảnh và tạo Document với ảnh
 
<img width="975" height="395" alt="image" src="https://github.com/user-attachments/assets/1a5c8755-c1c0-4003-995e-221be0dd6ceb" />

Khởi tạo vector_store, do đã có embedding vector nên ta sẽ không cần truyền embedding model vào đây
 
<img width="975" height="217" alt="image" src="https://github.com/user-attachments/assets/fa6b514b-4d47-4150-8a91-6748a3e5eaff" />

Khởi tạo chat model:
 
<img width="725" height="153" alt="image" src="https://github.com/user-attachments/assets/b3b52f1d-af22-42f6-9ae8-1a934c32d9ad" />

Viết hàm truy vấn riêng
 
<img width="955" height="445" alt="image" src="https://github.com/user-attachments/assets/429909de-67fb-4162-a45d-2aba65f0318c" />

Viết hàm tạo message cho multimodal, hoạt động với các bước sau:
1.	Khởi tạo message chứa câu hỏi
2.	Phân loại text documents và image documents
3.	Thêm nội dung văn bản vào message
4.	Thêm ảnh (ở dạng base64) vào message
5.	Thêm instruction vào message
 
<img width="975" height="402" alt="image" src="https://github.com/user-attachments/assets/11d1836d-0f0f-4a0a-a623-77a2bf34a690" />

<img width="975" height="357" alt="image" src="https://github.com/user-attachments/assets/be4e27be-f68a-4845-a156-a2e83538e36a" />
Content là một list chứa các dictionary chứa các khóa như “type” để định danh kiểu dữ liệu, Ví dụ "type": "text" báo cho mô hình: "Đây là văn bản, hãy đọc nó" hay "type": "image_url" báo cho mô hình: "Đây là một hình ảnh, hãy 'nhìn' nó". Và cũng để phân biệt giữa chỉ dẫn (str) và dữ liệu ảnh base64 (str)

RAG pipeline:
 
<img width="975" height="543" alt="image" src="https://github.com/user-attachments/assets/f9844a69-26cc-4f47-9027-7d4c4ead3faa" />

Response của model:
 
<img width="975" height="534" alt="image" src="https://github.com/user-attachments/assets/e2d06b24-b373-4f25-a253-5c1a1cd5b18c" />

