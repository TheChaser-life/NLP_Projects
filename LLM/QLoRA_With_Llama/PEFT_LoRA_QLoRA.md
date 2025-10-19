# FINETUNING LLM WITH PEFT, LoRA, QloRA
Source: https://www.youtube.com/watch?v=ctdN8gQb7qo&t=161s

+ 3 cách finetuning:
1.	Self-supervised: mô hình tự gán nhãn cho dữ liệu khi finetune, các task thường thấy như: next-token prediction, masked language modeling, v.v
2.	Supervised: data finetune có sẵn label, ví dụ
Question: …
Answer:…

<img width="975" height="243" alt="image" src="https://github.com/user-attachments/assets/8727bdac-767f-40d8-9825-8b8624dd16cf" />

4.	Reinforcement learning: học thưởng phạt
   
+ Các lựa chọn cho model parameter training:

<img width="975" height="777" alt="image" src="https://github.com/user-attachments/assets/ebb5c3e4-d7e2-4b23-b095-2bf059b13ebf" />

1.	Retrain all parameters: train lại toàn bộ tham số của model, cách này không hiệu quả vì chúng ta sẽ cần tài nguyên phần cứng rất lớn để làm điều này
2.	Transfer learning: thêm 1 vài lớp vào cuối model sau đó train các lớp này
3.	Parameter Efficient Fine-tuning (PEFT): tham 1 vài weight vào model và chỉ train trên các weight này
   
+ Các phương pháp finetuning trong PEFT:
1.	LoRA (Low-Rank Adaptation):
Giả sử ta có một lớp tuyến tính y = Wx, thay vì cập nhật toàn bộ tham số trong W thì LoRA sẽ phân rã W thành hai ma trận A và B
# W (n,m) -> A (n,r) và B (r,m)
Trong đó r thường là 1 số nhỏ
Khi finetuning, A và B sẽ được cập nhật:
# Y = (W + AB)X = WX + ABX
LoRA sẽ nhân theo thứ tự đặc biệt để không bao giờ phải tạo ra và lưu ma trận lớn:
Nhân B cho X trước ta được (BX) (r,1) sau đó nhân cho A được ABX (n,1)
Sau cùng ta chỉ việc cộng AB vào W, không cần phải thay đổi cấu trúc của model:
# W’ = W + AB
Trong thực tế thay vì phải cập nhật hàng triệu tham số thì ta chỉ cần cập nhật vài nghìn tham số theo phương pháp này
Ví dụ sử dụng:

<img width="519" height="267" alt="image" src="https://github.com/user-attachments/assets/cc21144b-4e3b-4287-8b0a-4be21f05ec82" />
 
Các tham số có trong LoraConfig:
+	r : là kích thước không gian ẩn khi phân rã W thành AB ( A (n,r) )
r càng lớn thì mô hình có nhiều khả năng học hơn (nhiều tham số hơn), nhưng cũng tốn nhiều bộ nhớ và thời gian train hơn
Với các mô hình nhỏ thì r = 4 hoặc 8 là hợp lý, nếu lớn hơn có thể là 16, 64, v.v

+	lora_alpha : là hệ số khuếch đại tác động của AB trong công thức cập nhật W
# W’ = W + (alpha/r)*AB
Alpha càng lớn thì sự điều chỉnh của LoRA càng ảnh hưởng mạnh đến weight gốc
Thường thì lora_alpha = 16 hoặc 32
Ta thường chọn alpha sao cho alpha/r xấp xỉ 1 -> 4

+	target_modules : là danh sách các layers sẽ được áp dụng lora, ví dụ như các phần trọng yếu của attention:
‘q_proj’ : ma trận tạo querry vectors
‘v_proj’ : ma trận tạo value vectors
Vì các phần này có ảnh hưởng mạnh đến hành vi ngôn ngứ của mô hình

+	lora_dropout : tỷ lệ dropout áp dụng trong nhánh lora giúp tránh overfitting khi fintune trên dataset nhỏ
Thường dùng 0.05 hoặc 0.1 hoặc giảm về 0 (khi dataset lớn và khái quát hóa)

+	bias : lựa chọn cách xử lý bias trong các lớp được áp dụng lora
‘none’ : không thêm trainable bias và giữ nguyên bias gốc
‘all’ : thêm bias trainable cho tất cả lớp lora
‘lora_only’ : finetune bias trong các lớp có lora

+	task_type : lựa chọn kiểu tác vụ đang finetune
‘CASUAL_LM’ : mô hình ngôn ngữ sinh văn bản (GPT, LlaMA, Mistral, v.v)
‘SEQ_2_SEQ_LM : mô hình dịch hoặc tóm tắt (T5, BART)
‘TOKEN_CLS’ : Phân loại token (NER, POS tagging)
‘SEQ_CLS’ : Phân loại chuỗi (sentiment classification)
Và các tác vụ khác

+	modules_to_save : giữ nguyên 1 số modules gốc

+	layers_to_transform : chỉ định layer index nào được áp dụng lora

+	inference_mode : True khi dùng để chạy (không finetune), False khi finetune
Load và merge model sau khi finetune:

<img width="975" height="485" alt="image" src="https://github.com/user-attachments/assets/35715a23-e159-473d-98bb-6a069efebe1f" />

Đầu tiên ta sẽ tải lại model mới sau đó tiến hành merge model mới và phần lora đã được finetune (finetune_model là đường dẫn đến model đã được finetune trước đó có áp dụng lora config)

2.	QLoRA (Quantization Low-Rank Adaptation):
Khá là giống với LoRA bình thường nhưng thay vì áp dụng LoRA lên model gốc thì ta sẽ thực hiện Quantization model gốc trước rồi mới áp dụng LoRA vào. Giúp giảm mạnh yêu cầu về bộ nhớ nhưng vẫn giữ được hiệu năng gần tương đương với LoRA chuẩn
Ví dụ về sử dụng QLoRA (ChatGPT):

<img width="975" height="745" alt="image" src="https://github.com/user-attachments/assets/b8c6984b-aedf-48f0-9ce0-af3021efeff1" />

Load base_model kèm với quantization nó sang 4bit

Các tham số dùng cho BitsAndBytesConfig:
+	load_in_4bit : nếu True, model sẽ được load ở định dạng 4-bit quantization (giảm VRAM mạnh)

+	load_in_8bit : nếu True, model sẽ được load ở định dạng 8-bit quantization (nặng hơn 4 bit nhưng tăng độ chính xác)

+	bnb_4bit_compute_dtype : Kiểu dữ liệu dùng trong tính toán sau khi nén, thường là torch.float16, torch.bfloat16, bfloat16

+	bnb_4bit_quant_type : loại thuật toán lượng tử hóa 4 bit. Có 2 giá trị là “fp4” (chuẩn cũ, ít chính xác hơn nf4) và “nf4” (chuẩn mới)

+	bnb_4bit_use_double_quant : nếu true áp dụng double quantization để giảm thêm VRAM tiêu hao mà vẫn giữ được độ chính xác tốt

+	llm_int8_threshold : ngưỡng xác định độ nhạy khi chuyển trọng số sang int8 (mặc định là 6.0). Giá trị thấp hơn tương đương với độ chính xác cao hơn nhưng dùng nhiều VRAM hơn

+	llm_int8_skip_modules : tên các modules không muốn quantize, giữ nguyên float16 để tránh sai lệch

+	llm_int8_enable_fp32_cpu_offload : khi True, sẽ đưa phần trọng số fp32 về cpu để giảm tải gpu nhưng sẽ chạy chậm hơn

+	bnb_8bit_use_double_quant : tượng tự bnb_4bit_use_double_quant nhưng dùng cho 8bit

+	bnb_8bit_quant_type : loại thuật toán lượng tử hóa 8bit (“fp8” hoặc “int8”) mặc định là “int8”
 
Khởi tạo cấu hình LoRA giống như LoRA chuẩn và gắn adapter LoRA vào model đã được quantization:

<img width="975" height="652" alt="image" src="https://github.com/user-attachments/assets/28d7a7f8-f73d-4660-affe-97dc1d707246" />

Khởi tạo training args và supervised finetuning trainer sau đó tiến hành finetune model:

<img width="975" height="1118" alt="image" src="https://github.com/user-attachments/assets/78bb35b7-5907-4177-8b35-e018f16acb9f" />
 
Load model gốc lại (vẫn quantization) và phần LoRA đã được finetune trước đó. Lúc này, chúng ta không cần dùng lệnh merge_and_unload do nó sẽ giải lượng tử hóa model, khiến VRAM tăng nhiều lần, làm mất đi sức mạnh của QLoRA. Trên thực tế, đa phần các trường hợp sẽ không cần phải merge phần LoRA vào model gốc, model sẽ chạy song song với adapter (adapter đã được finetune). Khi inference, model sẽ tính song song cả 2 phần là :
xW và Abx
và kết quả cuối cùng là:
y = xW + (lora_alpha/r)*(ABx)

<img width="975" height="439" alt="image" src="https://github.com/user-attachments/assets/12b15b4d-2286-4014-a1fe-a4b8a131f3b6" />






