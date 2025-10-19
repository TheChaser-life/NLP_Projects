# MODEL QUANTIZATION
Source tham khảo:  https://www.youtube.com/watch?v=7Iw5rDuju-o

IOT: 
+ Concept: ngày nay internet không chỉ được ứng dụng trên máy tính hay điện thoại mà còn trên cả các thiết bị đầu cuối như tủ lạnh, máy lạnh, …
+ Vấn đề với các model ML: ta không thể deploy model gốc lên các thiết bị đầu cuối được do các vấn đề về phần cứng (bộ nhớ, bộ xử lý)
+ IOT yêu cầu model phải:
1.	Kích thước nhỏ để có thể lưu vào bộ nhớ
2.	Dùng ít năng lượng để tiết kiệm vòng đời của pin
3.	Tốc độ xử lý nhanh tạo cho users cảm giác chạy trong thời gian thực

Giải pháp : TFLite
+ Được phát triển bởi google để đáp ứng 3 yêu cầu của IOT
+ Hỗ trợ các thiết bị có dùng GPU thông qua GPU delegates. GPU delegates sẽ làm việc với các native library
+ Cách thức hoạt động:

<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/e871f840-d2eb-4565-8863-b83bc84f8aad" />

1.	Model sẽ được huấn luyện bằng tf.Keras hoặc Low leval API
2.	Sau khi huấn luyện xong model sẽ được lưu theo chuẩn Keras (tf.Keras model) và chuẩn TensorFlow (SavedModel), Concrete Functions lưu lại các functions mà model có thể thực hiện (dự đoán, tính toán, v.v)
3.	Tf.Keras model, SavedModel, Concrete Functions được đưa vào TFLite Converter để nén thành file TFLite Flatbuffer
4.	File TFLite Flatbuffer được nạp vào TFLite Interpreter để running trên thiết bị đầu cuối
5.	TFLite Interpreter có thể chạy trên các các phần cứng của thiết bị đầu cuối như CPU, GPU, NN API, v.v

Quantization: 
+ khái niệm lượng tử hóa ám chỉ đến việc giảm từ các kiểu dữ liệu số có độ chính xác cao như FLOAT64, FLOAT32 về các dạng có độ chính xác thấp hơn như INT8, INT4, từ đó giảm size của nó đi (model sẽ cần ít bytes để lưu trữ)
+ Có 2 loại quantization: Post-training quantization (lượng tử hóa model sau khi train) và Quantization-aware training (lượng tử hóa model trong khi train)
+ Post-traing quantization: có 2 loại là weight và hybrid

<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/1bb7aa65-c173-4a65-a481-da090ce10d67" />

1.	Weight Quantization:

<img width="975" height="366" alt="image" src="https://github.com/user-attachments/assets/e8d58fe2-f906-492a-8afb-9bc56e909878" />

Sau khi đươc train xong thì các weights của nó sẽ được quantization và mỗi khi tính toán xong thì kết quả sẽ trải qua quá trình dequantization để biểu diễn chính xác hơn
Ví dụ về Post-training Quantization (Weight):
Model gốc:

<img width="975" height="675" alt="image" src="https://github.com/user-attachments/assets/1d692138-3546-4c17-9a8f-4ba6bbf28ae0" />

<img width="975" height="202" alt="image" src="https://github.com/user-attachments/assets/570c8020-2384-4c88-b334-d6c541e95fc6" />
 
Quantization model:

<img width="975" height="735" alt="image" src="https://github.com/user-attachments/assets/0a05dec8-d6e2-45da-ac31-ccc4c9158c3e" />

 
Sự khác biệt giữa model bình thường và model đã quan quantization:

<img width="975" height="255" alt="image" src="https://github.com/user-attachments/assets/9d5772f7-618c-4d2e-84d9-6007dd90912d" />

Từ 1.2 MB chỉ còn 104 KB

2.	Hybrid (Fully) Quantization:

<img width="975" height="456" alt="image" src="https://github.com/user-attachments/assets/00fe4d9f-4fae-404f-94dc-85b430a70132" />

Ta sẽ thực hiên quantization với cả kết quả của các activation function bằng cách ánh xạ kết quả về các khoảng giá trị như [-128,127] (int). Để ánh xạ được thì ta cần 1 bước nữa gọi là calibration step, chọn 1 tập con hay toàn bộ data từ tập test cho chạy trên activation function để lấy giá trị min, max và giá trị min, max này sẽ được scale về khoảng giá trị [-128,127] (int) bởi 1 tham số mà chúng ta có thể gọi là scale quantization value
Fully Quantization có lợi hơn weight quantization ở chỗ không cần chuyển output về lại các dạng có độ chính xác cao hơn từ đó tăng tốc độ tính toán và giảm bộ nhớ tiêu hao nhiều hơn
Ví dụ về Post-training Quantization (Fully):
Cách này khác với chỉ quantize weight ở chỗ ta sẽ cần tạo Class dataset và dataloader để truyền vào model từ đó tìm được giá trị min, max của activation function từ data truyền vào để ánh xạ kết quả của activation function tới một khoảng (vd: [-127,128])

<img width="813" height="731" alt="image" src="https://github.com/user-attachments/assets/abd9f1d0-ac82-4da4-9971-16f7b17f66b5" />

<img width="975" height="458" alt="image" src="https://github.com/user-attachments/assets/5b26caac-a953-4581-afac-c1b103ba0d4f" />

<img width="975" height="223" alt="image" src="https://github.com/user-attachments/assets/c913fd76-c478-460e-a2b8-43048f751405" />

<img width="975" height="665" alt="image" src="https://github.com/user-attachments/assets/1bf8948e-c375-4748-b418-34a31ddb65dc" />

<img width="975" height="363" alt="image" src="https://github.com/user-attachments/assets/dcfd0080-c0b3-44a4-8d89-c6318bcde92e" />

Như ta thấy kết quả giảm từ 1.2 MB (Model gốc) về 105 KB

+ Quantization-aware training:

<img width="975" height="428" alt="image" src="https://github.com/user-attachments/assets/606e4ec1-e3e9-4bd7-9d5c-253bac1700da" />
    
Trước hết chúng ta sẽ tiến hành quantization model rồi sau đó finetuning model đó và convert model về dạng lite. Cách này không làm giảm đi kích thước của model so với Post-training Quantization nhưng nó sẽ tạo ra một model tốt hơn do model sau khi quantization sẽ được train với data, các weight sẽ được hiệu chỉnh theo data
Ví dụ về Quantization-aware training:

<img width="975" height="819" alt="image" src="https://github.com/user-attachments/assets/6fcd73b4-abd7-4587-85e1-bf22d2c462c8" />
 
Load model đã train rồi sau đó ta lấy ra 1 phần data để train lại model với số epoch nhỏ để thích nghi với lỗi lượng tử hóa

<img width="975" height="449" alt="image" src="https://github.com/user-attachments/assets/8c1a8ae1-5bb7-4128-a547-80163499b5c9" />
 
Kích thước đã giảm từ 1.2 MB (model gốc) về 105 KB nhưng điều quan trọng là độ chính xác đã tăng so với cách Post-training quantization do có bước train lại
