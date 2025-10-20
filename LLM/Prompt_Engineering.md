# Prompt Engineering

Source: https://www.youtube.com/watch?v=_ZvnD73m40o&t=100s

Prompt Engineering liên quan đến việc:
+	 Cải thiện khả năng viết, tinh chỉnh, và tối ưu hóa prompt theo một cách có cấu trúc. 
+	 Tăng cường khả năng giao tiếp giữa con người và AI càng nhiều càng tốt
+  Giám sát prompt đảm bảo sự hiệu quả của chúng
+ Bắt kịp các update từ các prompt library

Thực trạng : AI hiện nay đang bùng nổ rất nhiều, đến mức mà các kiến trúc sư của các model đó cũng khó kiểm soát được nó và output từ model

Các khái niệm liên quan đến Prompt Engineering:
1.	Ngôn ngữ học: là lĩnh vực nghiên cứu về các khái niệm của ngôn ngữ
Các nhánh trong ngôn ngữ học:

<img width="975" height="406" alt="image" src="https://github.com/user-attachments/assets/11d5c84f-4bd3-4096-a4e7-995277277aaa" />
 
Việc hiểu các sắc thái của ngôn ngữ và tình huống mà chúng được sử dụng rất quan trọng trong việc tạo ra các prompt hiệu quả, biết cách sử dụng ngữ pháp và các cấu trúc của ngôn ngữ được sử dụng rộng rãi sẽ nhận được kết quả chính xác hơn từ hệ thống AI

<img width="975" height="526" alt="image" src="https://github.com/user-attachments/assets/cde5b693-1905-4cf1-96a5-8d252f91e19a" />

Các nguyên tắc để viết prompt hiệu quả:
+	Clear Instructions (Hướng dẫn rõ ràng):
Nêu rõ chúng ta muốn AI làm gì. Ví dụ:
Thay vì nói: “Viết về động vật”
Hãy nói: “Viết một đoạn 100 từ mô tả tập tính săn mồi của sư tử trong tự nhiên”

+	Adopt a persona (Chọn một vai trò cho AI):
Yêu cầu AI vài vai một nhân vật nào đó, giúp cho câu trả lời có giọng điệu và có góc nhìn phù hợp với tính huống đang gặp. Ví dụ:
“Hãy đóng vai chuyên gia dinh dưỡng và gợi ý cho tôi một thực đơn phù hợp cho vận động viên điền kinh”

+	Specify the format (Chỉ rõ định dạng):
Chỉ rõ cho AI biết chúng ta cần output ở định dạng nào. Ví dụ:
“Xuất kết quả bằng file JSON”

+	Avoid leading the answer (Tránh dẫn hướng câu hỏi theo ý muốn):
Tránh dẫn hướng câu hỏi theo ý muốn, ý nghĩ của bản thân mình. Ví dụ:
Thay vì hỏi: “Tại sao A lại là tốt nhất ?”
Hãy hỏi: “Ưu và nhược điểm của A là gì ?”

+	Limit the scope (Giới hạn phạm vi câu trả lời):
Giới hạn chủ đề, độ dài, mức độ chi tiết để tránh câu trả lời bị lan man. Ví dụ:
“Tóm tắt trong 5 dòng”
“Tập trung vào nguyên nhân chính”
 
<img width="975" height="881" alt="image" src="https://github.com/user-attachments/assets/68587b9a-1284-42e3-8597-18b5ed80c579" />

Các kiểu prompting:
1.	Zero-shot prompting: tận dụng sự hiểu biết của một pre_trained model ngôn ngữ ( ngữ pháp, quan hệ giữa các từ và khái niệm, …) mà không cần phải huấn luyện thêm

2.	Few-shot prompting: cải thiện model với các mẫu huấn luyện thông qua prompt, tránh retrain lại từ đầu. Ví dụ:

<img width="975" height="553" alt="image" src="https://github.com/user-attachments/assets/7e58d939-e6f6-4eab-8f45-38143a33c813" />
