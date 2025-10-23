# DATA INGESTIONS AND DATA PARSING TECHNIQUES

-	LangChain Document Structure:

<img width="975" height="242" alt="image" src="https://github.com/user-attachments/assets/ecdf1603-5854-473b-9230-374ef12b68c4" />
 
Document trong LangChain bao gồm 2 phần chính:
1.	page_content (string): đây là phần nội dung văn bản chính của document, chứa các thông tin chính để ánh xạ sang embedding vector, được lưu dưới dạng string (ở bất cứ độ dài nào)
Ví dụ: "Retrieval-Augmented Generation (RAG) combines the benefits ofpre-trained language models with information retrieval systemsto generate more accurate and contextual responses..."

<img width="975" height="838" alt="image" src="https://github.com/user-attachments/assets/85ebace6-b30b-4af4-a9cd-929c56ed5cf9" />

2.	metadata (dictionary): thêm vào các thông tin về document, dùng để lọc, quan sát và làm giàu ngữ cảnh của document. Có thể chứa bất kì dữ liệu JSON có tính tuần tự hóa (JSON-serializable data)
 
<img width="975" height="837" alt="image" src="https://github.com/user-attachments/assets/c922f1a5-0b8e-4850-ba93-09d48682b525" />

-	Document Loaders:

<img width="975" height="260" alt="image" src="https://github.com/user-attachments/assets/c3f54713-2309-43e1-a4ca-0afb75a15421" />

1.	TextLoader: đọc một file đơn

<img width="975" height="399" alt="image" src="https://github.com/user-attachments/assets/ba2d6e45-619f-4f40-9629-5783462ddbfb" />
 
Hàm TextLoader sẽ đọc file text từ đường dẫn được lưu vào, encoding lựa chọn phiên dịc các byte (0 và 1) trong file văn bản thành kí tự mà chúng ta có thể đọc, dùng utf-8 vì đây là cuốn sổ khổng lồ, hiện đại, là tiêu chuẩn toàn cầu. Nó chứa hàng triệu mục, bao gồm tất cả các ký tự tiếng Anh, Tiếng Việt, Tiếng Trung, Tiếng Nhật, và cả emoji 

2.	DirectoryLoader : load nhiều file

<img width="975" height="716" alt="image" src="https://github.com/user-attachments/assets/5249e871-1284-4304-b71f-a94b20448bca" />

Hàm DirectoryLoader có các tham số như:
+ path: đường dẫn thư mục chứa các file cần đọc
+ glob: dùng để lọc ra những file sẽ đọc. Ví dụ glob=’**/*.txt’ thì ** nghĩa là tìm các file trong thư mục hiện tại và trong các thư mục con của nó và *.txt nghĩa là chọn các file có phần đuôi là .txt để đọc
+ loader_cls: lựa chọn lớp tải (Loader class), ví dụ như TextLoader để đọc text
+ loader_kwargs: thiết lập tham số của lớp tải (loader keyword arguments)
+ show_progress: lựa chọn có hiển thị tiến trình tải file hay không

-	Text Splitting Strategies:

<img width="975" height="246" alt="image" src="https://github.com/user-attachments/assets/e5fec73d-4ba4-4473-be53-bcf658689a8e" />
 
1.	Character-based splitting

<img width="975" height="374" alt="image" src="https://github.com/user-attachments/assets/15457df4-42f0-4fb3-87ec-38b597600de9" />

Các tham số của hàm CharacterTextSplitter:
+ separator: hàm sẽ cắt đoạn text thành các phần tử nhỏ tại mỗi kí tự được chọn
+ chunk_size: kích thước tối đa mỗi chunk
+ chunk_overlap: số kí tự lặp lại ở chunk trước của chunk hiện tại
+ length_function: đây là hàm mà CharacterTextSplitter sẽ dùng khi cần kiểm tra xem chunk hiện tại có vượt quá chunk_size không

Cách CharacterTextSplitter hoạt động:
+ Tách đoạn văn thành các phần tử dựa trên kí tự separator
+ Ghép các phần tử lại thành chunk sao cho mỗi chunk không vượt quá chunk_size
+ Trả về list các chunks
 
<img width="975" height="466" alt="image" src="https://github.com/user-attachments/assets/8f7be890-9a0d-499d-99f5-bd16431ac0f4" />

2.	Recursive character splitting:

<img width="975" height="259" alt="image" src="https://github.com/user-attachments/assets/255a5c0a-88e4-4763-91bc-f4c80b34171a" />
 
Tham số được truyền vào cũng giống với CharacterTextSplitter
Cách RecursiveCharacterTextSplitter hoạt động:
+ Dùng separator đầu tiên trong list để tách đoạn văn thành các phần tử nhỏ
+ Kiểm tra các phần tử xem có vượt quá chunk size không
+ Nếu có phần tử vượt quá chunk size, tiến hành dùng separator thứ 2 để tách các phần tử vi phạm
+ Tiếp tục tách đến khi không còn phần tử nào vi phạm
+ Tiến hành gộp các phần tử thành một chunk nếu chưa vượt quá chunk size
 
<img width="975" height="680" alt="image" src="https://github.com/user-attachments/assets/761a317d-280f-4696-a4b2-55ad49300fd4" />

3.	Token -based splitting:

<img width="975" height="208" alt="image" src="https://github.com/user-attachments/assets/9bcb88fd-074f-47ae-b844-41fbbfae75af" />

Split dựa trên token thay vì kí tự

<img width="975" height="684" alt="image" src="https://github.com/user-attachments/assets/150adeab-22f5-4670-bf21-fbb894b6334c" />

So sánh ưu và nhược điểm của 3 loại split trên:

1.	CharacterTextSplitter:
+ Ưu điểm:
Đơn giản và có thể đoán được
Hoạt động tốt với text có cấu trúc
+ Nhược điểm:
Đôi khi phải cắt cưỡng chế giữa câu

2.	RecursiveCharacterTextSplitter:
+ Ưu điểm:
Giữ được cấu trúc của text bằng việc thử nhiều separator
Được sử dụng cho phần lớn các trường hợp
+ Nhược điểm: 
Phức tạp hơn CharacterTextSplitter

3.	TokenTextSplitter:
+ Ưu điểm:
Giữ được giới hạn token của model
Chính xác hơn cho embedding
+ Nhược điểm:
Chậm hơn character-based splitter

-	Load PDF files:
1.	PyPDFLoader:

<img width="975" height="361" alt="image" src="https://github.com/user-attachments/assets/1fae5a3e-2007-4649-9509-b8447e95bb64" />

Load file PDF trong đường dẫn, trả về một list mà mỗi phần tử là một trang đã được đọc trong file PDF (len = số trang của file pdf)

2.	PyMuPDFLoader

<img width="975" height="411" alt="image" src="https://github.com/user-attachments/assets/93e86d30-2023-4ee5-9e09-c3e201071331" />
 
Hoạt động tương tự như PyPDFLoader nhưng nhanh hơn. Hỗ trợ cả trích xuất từ ảnh

-	Xử lý các vấn đề gặp phải sau khi load file pdf:
Sau khi load file pdf, có thể gặp các vấn đề sau:
+ text được lưu trữ một cách phức tạp
+ vấn đề về format
+ có thể chứa ảnh (cần sử dụng OCR)
+ thường chứa các tài liệu đi kèm

<img width="533" height="397" alt="image" src="https://github.com/user-attachments/assets/4126f858-841c-449f-9893-186d9c6cbcce" />
	 
Đây là một trong những các đơn giản để xử lý text sau khi load từ pdf. Trước hết ta sẽ tách tất cả các từ ra với nhau sau nối chúng lại với một khoảng trắng ở giữa nhằm loại bỏ khoảng trắng thừa, sau đó loại bỏ các ligature (chữ ghép như ﬁ và ﬂ, hai chữ này chỉ được tính là một kí tự) và thay thế chúng bằng định dạng bình thường ( f và I, f và l)

-	Tổng quan hàm load và xử lý PDF:
 
<img width="975" height="316" alt="image" src="https://github.com/user-attachments/assets/b15b0206-d45c-4744-9761-0f126db1444a" />

<img width="975" height="840" alt="image" src="https://github.com/user-attachments/assets/c8d708c4-a6b5-4ac8-a848-c624f5028a9b" />
 
+  “__init__()” sẽ khởi tạo text splitter với chunk_size và chunk_overlap được truyền vào
+  “clean_text()” sẽ xử lý text sau khi được load
+  “forward()” sẽ nhận đường dẫn file pdf, load lên và xử lý với clean_text(), nếu page nào có số ký tự dưới một mức nhất định sẽ bị bỏ qua. Sau đó tiến hành split các đoạn text thành các chunk và được lưu dưới dạng langchain document với metadat
  
<img width="975" height="369" alt="image" src="https://github.com/user-attachments/assets/6a9110f7-6839-491d-9f87-6de4df2c13c4" />
	
-	Load và xử lý file docx, doc
1.	Docx2txtLoader:

<img width="975" height="379" alt="image" src="https://github.com/user-attachments/assets/a63a170d-18cf-41a7-93fc-a5b7a4647eb0" />
 
Hàm này chỉ đọc file docx/docs thành 1 khối
	
2.	UnstructuredWordDocumentLoader

<img width="975" height="454" alt="image" src="https://github.com/user-attachments/assets/c8a676bf-eebf-434e-8d94-9d11657ce2ec" />

UnstructuredWordDocumentLoader với mode=”element” là chế độ mạnh mẽ nhất để load và xử lý file docx/docs do nó sẽ chia file thành các elements dựa trên cấu trúc của file docx/docs được đưa vào (xuống dòng,…)
Các trường của metadata khi load với mode=”elements:

1.	category: cho biết loại của khối văn bản là gì
một vài ví dụ về loại của khối văn bản:
Title: Tiêu đề của tài liệu hoặc một phần.
NarrativeText: Các đoạn văn bản nội dung chính.
ListItem: Một mục trong danh sách (có gạch đầu dòng hoặc số thứ tự).
Header: Văn bản ở phần đầu trang (header).
Footer: Văn bản ở phần cuối trang (footer).
Table: Một bảng (văn bản của bảng thường được biểu diễn dưới dạng HTML trong metadata).

2.	source: cho biết đường dẫn của tệp Word gốc mà văn bản này được trích xuất
   
3.	page_number: số trang trong file Word mà văn bản được tìm thấy
   
4.	filetype: loại tệp của tài liệu

5.	text_as_html: nếu category là Table, trường này sẽ xuất hiện và chứa phiên bản HTML của bảng đó

6.	parent_id: Một số element có thể là "con" của các element khác (ví dụ: một ListItem nằm dưới một Title). Trường này giúp xác định mối quan hệ phân cấp đó 

-	Load và xử lý file csv
1.	CSVLoader

<img width="975" height="695" alt="image" src="https://github.com/user-attachments/assets/904ca3d6-d124-4056-bb2b-9ee0699aa1d4" />

Hàm CSVLoader nhận vào các tham số như:
+ file_path: đường dẫn đến file csv
+ encoding: chọn kiểu giải mã (tiêu chuẩn là utf-8)
+ delimiter: khi gặp delimiter thì hàm sẽ hiểu rằng đã kết thúc một cột và duyệt sang cột mới (ví dụ ở đây delimiter là dấu phẩy)
+ quotechar: mọi thứ nằm giữa kí tự quotechar thì hàm sẽ hiểu nó là một phần tử cho dù có delimiter trong đó

2.	Custom CSV processing

<img width="975" height="510" alt="image" src="https://github.com/user-attachments/assets/81c90df6-8e7d-4cfb-b9a6-36972ee4f76c" />
 
Thay vì dùng thư viện có sẵn thì ta sẽ tự tạo nên hàm load và xử lý file CSV trong trường hợp chúng ta muốn thêm một vài trường đặc biệt cho metadata

-	Load và xử lý file excel
1.	UnstructuredExcelLoader

<img width="975" height="421" alt="image" src="https://github.com/user-attachments/assets/0ee5432b-3baa-45b2-a274-a1d0d7f277e0" />
 
Là một hàm xử lý file excel mạnh mẽ, có thể xử lý các đặc trưng phức tạp trong Excel, bảo toàn thông tin về format 

2.	Using pandas for full control

<img width="975" height="506" alt="image" src="https://github.com/user-attachments/assets/67d0cf2f-b7ce-426a-b048-3b40eaae7a71" />
  
Chúng ta cũng có thể tự tạo nên một hàm để xử lý file Excel như của file CSV trong trường hợp muốn thêm một số metadata để làm giàu ngữ cảnh

-	Load và xử lý file JSON:
1.	JSONLoader

<img width="975" height="453" alt="image" src="https://github.com/user-attachments/assets/71df80f7-921f-4ef8-bc40-6c05d1f087b3" />
 
JSONLoader là một hàm dùng để load file JSON, trong đó tham số jq_schema chỉ định cách trích xuất dữ liệu từ file json. Ví dụ jq_schema=’.employee[]’ trong đó ‘.’ Cho biết bắt đầu từ thư mục gốc của file JSON, ‘employee’ truy cập vào khóa có tên  là ‘employees’, ‘[]’ cho biết đây là bộ lặp và yêu cầu loader lặp qua từng phần tử bên trong employees

2.	Custom JSON processor

<img width="975" height="584" alt="image" src="https://github.com/user-attachments/assets/d3769d81-69de-4440-a173-90c6a74fc558" />
 
Hàm load và xử lý file JSON tự tạo để xử lý file JSON theo ý muốn (thêm metadat, v.v)

-	Load và xử lý dữ liệu từ SQL Database
1.	SQLDatabase utility

<img width="975" height="485" alt="image" src="https://github.com/user-attachments/assets/ece33578-0886-4d22-a3ad-900b678752b0" />
 
Ta cần truyền tham số db_uri, Đây là tham số quan trọng nhất và duy nhất bắt buộc. Nó là một chuỗi (string) kết nối theo chuẩn của SQLAlchemy, chỉ định cách kết nối với cơ sở dữ liệu
Ví dụ: sqlite:///data/databases/company.db

2.	Custom function sql_to_documents
Gồm 2 phần:
Phần 1 sẽ tạo document cho từng table trong database

<img width="975" height="603" alt="image" src="https://github.com/user-attachments/assets/4f43f545-862d-4af8-bc32-064e3d39520b" />

<img width="975" height="196" alt="image" src="https://github.com/user-attachments/assets/a0bd15f0-dea2-458d-ac2b-c70cb6a97b5b" />
 
Các bước thực hiện:
+ tạo kết nối với database đã được lưu
+ tạo con trỏ (cursor) để thực thi code sql
+ lấy tất cả các table trong database
+ duyệt qua từng table
+ lấy cấu trúc (PRAGMA) của table
+ lấy tên các columns của table
+ lấy dữ liệu các dòng
+ tạo table_content
+ tạo Document với table_content và metadata

Phần 2 sẽ tạo Document cho các quan hệ giữa các table (nếu có)

<img width="975" height="433" alt="image" src="https://github.com/user-attachments/assets/acae8523-df20-474e-ac87-d077cf29b8dc" />

Các bước thực hiện:
+ Tiến hành kết các table lại nếu chúng có quan hệ với nhau
+ lấy tất cả các quan hệ đó
+ tạo rel_content (relationship_content)
+ tạo Document với rel_content và metadata
