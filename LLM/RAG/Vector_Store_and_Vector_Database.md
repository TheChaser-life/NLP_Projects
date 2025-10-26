# VECTOR STORES AND VECTOR DATABASES
-	Phân biệt giữa vector stores và vector databases:

<img width="975" height="669" alt="image" src="https://github.com/user-attachments/assets/eba51a64-5110-45f2-baba-fbe3d36d8b7d" />

1.	Vector Store:
+ Là một thư viện hoặc một công cụ nhỏ tập trung và lưu trữ và tìm kiếm vector một cách hiệu quả
+ Chức năng cốt lõi: tìm kiếm tương đồng (similarity search) đơn giản, tìm K vector tương đồng với query nhất
+ Thường chạy trong bộ nhớ hoặc một file cục bộ, thực thi trên một máy
+ Được sử dụng cho nghiên cứu, các ứng dụng nhỏ với < 1M vectors
+ Ví dụ các vector stores: FAISS, HNSWlib, ScaNN, ChromaDB.

2.	Vector Database:
+ Là một hệ thống cơ sở dữ liệu được thiết kế dữ liệu dưới dạng vector
+ Chức năng chính: tìm kiếm nâng cao với filters (lọc dữ liệu), metadata queries và các thao tác trong databases (CRUD: Create-Read-Update-Delete) 
+ Là hệ thống phân tán (distributed system chạy trên nhiều máy tính), có nhiều bản sao của dữ liệu được tạo ra tránh bị mất mát dữ liệu khi có sự cố xảy ra (replication), dữ liệu được phân mảnh (sharding) mỗi phần được lưu trên server riêng để tránh một server chứa quá nhiều dữ liệu cũng như tăng tốc độ truy cập. Từ đó tạo ra một hệ thống luôn hoạt động (High availability)
+ Dùng cho hệ thống trong sản phẩm, ứng dụng của doanh nghiệp với hàng tỷ vector
+ Ví dụ một số vector databases: Pinecone, Weaviate, Qdrant, Milvus, Vespa 

So sánh nhanh giữa vector stores (purple)  và vector databases (blue):
 
<img width="975" height="380" alt="image" src="https://github.com/user-attachments/assets/1fcb70cd-cb57-4f52-9bb1-22b99dc429f7" />

  <img width="975" height="422" alt="image" src="https://github.com/user-attachments/assets/a648c808-1eeb-41f2-b3a0-b59f1616bd58" />
 
-	Xây dựng một RAG system với LangChain và ChromaDB
Load biến môi trường để truy cập vào model trên OPENAI
 
<img width="949" height="247" alt="image" src="https://github.com/user-attachments/assets/ae7c7d00-584f-4ca5-92ea-f99c2be28c50" />

Import các thư viện cần thiết như:
+ Document: đây là kiểu dữ liệu chính của langchain
+ OpenAIEmbeddings: load và sử dụng embedding model từ OPENAI
+ RecursiveCharacterTextSplitter: dùng để chia các documents sau khi load thành các chunks
+ TextLoader: dùng để load document có dạng text (.txt)
+ Chroma: là vector store mà chúng ta sẽ dùng để lưu embedding vector
  
<img width="975" height="391" alt="image" src="https://github.com/user-attachments/assets/683bc66a-3dea-4ce1-b20e-aa55bf7067e5" />

Nhắc lại kiến trúc của RAG:
 
<img width="975" height="399" alt="image" src="https://github.com/user-attachments/assets/a30a872c-9354-4e2f-b0ea-0c03ffe5a114" />

Tạo dữ liệu mẫu:
 
<img width="975" height="842" alt="image" src="https://github.com/user-attachments/assets/a17e1016-ec7d-4704-98a0-de106c1f0045" />

Lưu vào một đường dẫn tạm thời:

<img width="888" height="372" alt="image" src="https://github.com/user-attachments/assets/bd77aa27-b167-49b1-9465-29c86dfe3620" />
 
Load documents từ đường dẫn tạm thời:
 
<img width="975" height="741" alt="image" src="https://github.com/user-attachments/assets/08806e2e-dc5d-4911-93c1-e33262cb7346" />

Tiến hành split các documents vừa load được thành các chunks:
 
<img width="975" height="803" alt="image" src="https://github.com/user-attachments/assets/44eb4315-3336-46a9-ba4b-9fc7049fa190" />

Khởi tạo Chroma vector store và lưu các chunks vào:

<img width="975" height="504" alt="image" src="https://github.com/user-attachments/assets/bc3cbd9e-d614-4d92-bb1d-9ec0b6314786" />
 
Chroma.from_documents() là một hàm tiện ích (helper function) của ChromaDB dùng để tự động chuyển đổi các chunks sang vector rồi lưu vào database
Giải thích các tham số của Chroma.from_documents():
+ documents: chỉ định nguồn dữ liệu đầu  vào
+ embedding: chỉ định embedding model để chuyển đổi chunks sang vectors
+ persist_directory: chỉ định nơi lưu trữ
+ collection_name: dùng để phân biệt với các bộ sưu tập khác trong cùng đường dẫn ”./chroma_db”

Search các chunks có độ tương đồng cao với query:

 <img width="975" height="202" alt="image" src="https://github.com/user-attachments/assets/11cdc4f0-c854-45c4-aae2-694ae1705a1b" />

Hàm similarity_search() sẽ tự động chuyển đổi query sang vector và thực hiện tìm kiếm k chunks có độ tương đồng cao
Hàm similarity_search_with_score() cho ta biết Chroma mặc định dùng Euclidcian Distance để tìm kiếm các chunks tương đồng, score càng thấp thì độ tương đồng càng cao (khoảng cách giữa chúng trong không gian vector càng gần)
 
<img width="975" height="239" alt="image" src="https://github.com/user-attachments/assets/58d11daf-44a4-416f-bcb0-7ebeb12a9916" />

Khởi tạo model:

<img width="677" height="416" alt="image" src="https://github.com/user-attachments/assets/5e0d4832-de5d-455e-9df7-294e396231f6" />
 
Hoặc dùng init_chat_model để khởi tạo các model tùy chọn khác
 
<img width="950" height="214" alt="image" src="https://github.com/user-attachments/assets/5f20ffd4-08ae-4ca6-858b-37e4c5a1d4f3" />

Xây dựng RAG chain, sử dụng LCEL (LangChain Expression Language):
+ Tạo retriever từ vector store, hàm as_retriever biến vector store thành một object có thể gọi như hàm
 
<img width="975" height="615" alt="image" src="https://github.com/user-attachments/assets/bfab1d36-af14-454b-aeb7-db9de05cb22c" />

+ Tạo prompt template có thể tự động chèn giá trị vào chỗ trống nhờ hàm  ChatPromptTemplate.from_template()
 
<img width="975" height="414" alt="image" src="https://github.com/user-attachments/assets/b6293bf7-5c7c-4242-b130-5cd421775dc1" />

+ Tạo RAG chain:

<img width="975" height="276" alt="image" src="https://github.com/user-attachments/assets/309cb216-8efd-422c-bd6e-8699228277cc" />
 
Giải thích những gì trong rag_chain:
“|” là phép nối pipeline giữa các “Runnable”, "Runnable" = bất cứ thứ gì có thể chạy được (LLM, retriever, prompt, parser, v.v.). Ví dụ Output của A là Input của B và Output của B là Input của C (A, B, C là các Runnable)
RunnablePassthrough(): là  Runnable mà trả về chính input được đưa vào nó, giống như tạo một đường đi cho dữ liệu nhưng không biến đổi nó trên đường 
{“context”:retriever, "question":RunnablePassthrough()} là một RunnableMap, nó nhận một input đầu vào rồi truyền đến 2 nhánh là retriever và RunnablePassthrough
Llm là model để sinh câu trả lời
StrOutParser() để lấy phần text từ output của llm do(output của chúng thường có định dạng phức tạp hoặc có các trường không cần thiết)

+ Cách rag_chain hoạt động:
1.	Input được đưa vào RunnableMap sau đó đi qua hai nhánh là retriever (để lấy truy vấn từ database) và RunnablePassthrough() (để giữ nguyên câu hỏi gốc). Kết quả là một dictionary có hai key là context và question
2.	Dictionary ở trên được đưa vào prompt và điền vào các chỗ trống còn thiếu trong prompt để tạo nên prompt hoàn chỉnh
3.	Prompt hoàn chỉnh được đưa vào llm để sinh output
4.	Output từ llm được đưa vào StrOutParser() để lấy đúng phần text, tức là câu trả lời
5.	Trả response về cho user

-	Add document mới vào vector store:
Trước khi được thêm vào vector store thì ta cũng sẽ trải qua ba bước gồm:
1.	Thu thập hoặc tạo document mới
2.	Chuyển về dạng document của LangChain
3.	Split document thành các chunks
 
<img width="975" height="790" alt="image" src="https://github.com/user-attachments/assets/6bd7a078-f600-4ad4-ba32-83045edb21dc" />

Sau đó ta có thể add vào vector store với với câu lệnh vector_store.add_documents, id của các chunks mới được thêm vào sẽ được trả về
 
<img width="652" height="263" alt="image" src="https://github.com/user-attachments/assets/3fc6f263-0420-4498-a521-afb339de66b7" />

-	Thêm lịch sử trò chuyện (chat history) vào RAG system:
Vấn đề: user thường đưa ra các câu hỏi mà thông tin trong đó lại liên quan đến câu hỏi hoặc câu trả lời trước đó mà không lặp lại ngữ cảnh của các câu trước, nhưng retriever lại cần câu hỏi mang đầy đủ ngữ cảnh (standalone question) để tiến hành truy vấn trong vector store. Ví dụ: 
User: "Tell me about Python" Bot: explains Python programming language User: "What are its main libraries?" ← "its" refers to Python, but retriever doesn't know this
Giải pháp: chia làm hai process
1.	Tái cấu trúc câu hỏi dựa trên chat history
2.	Sử  dụng câu hỏi đã được tái cấu  trúc tìm các documents liên quan
Các bước thực hiện:
Import các thư viện, hàm cần thiết:

<img width="975" height="64" alt="image" src="https://github.com/user-attachments/assets/2c6a13f7-3cb4-4b68-9ae2-3a3c39fb58af" />
 
+ MessagesPlaceholder là một object dùng để chèn các message trong chat_history vào prompt
+ HumanMessage và AIMessage là hai objects dùng để cho model biết ai đã nói gì trước đó

Tạo prompt bao gồm system prompt, chat_history và user input:
 
<img width="975" height="321" alt="image" src="https://github.com/user-attachments/assets/fc942566-9848-4c98-baea-7b18f9bcee5c" />

Tạo một chain để LLM nhận prompt bên trên và trả về câu hỏi đã được tái cấu trúc
 
<img width="975" height="85" alt="image" src="https://github.com/user-attachments/assets/522e1139-3b68-49f7-ac93-7e1863c14db0" />

Tạo một chain để truy vấn các document liên quan đến câu hỏi
 
<img width="975" height="66" alt="image" src="https://github.com/user-attachments/assets/6fcebfca-c53b-42a7-9b4f-3403d05123d5" />

Tạo prompt để đưa chat_history (để model biết ngữ điệu đã dùng trong các câu phản hồi trước đó), câu hỏi và context và LLM để sinh ra response
 
<img width="975" height="249" alt="image" src="https://github.com/user-attachments/assets/3ea70221-2222-4092-99ac-067b9bd79768" />

Tạo nên một Conversional RAG Chain hoàn chỉnh:
 
<img width="975" height="183" alt="image" src="https://github.com/user-attachments/assets/0f7bfe2c-aa7d-4f05-9c7a-c2538b60440e" />

Thử với câu hỏi đầu tiên:
 
<img width="975" height="214" alt="image" src="https://github.com/user-attachments/assets/cdc73e73-de91-4ae0-8cd2-5084c82dd646" />

Thêm câu hỏi đầu và phản hồi vào chat_history:
 
<img width="927" height="250" alt="image" src="https://github.com/user-attachments/assets/c29bc2c5-de88-42b3-ada1-e3a6e2f46db1" />

Thử với câu hỏi thứ 2:
 
<img width="975" height="192" alt="image" src="https://github.com/user-attachments/assets/114d31d3-e7e0-49a3-a125-7881e911f33f" />

-	Sử dụng model với GROQ:
GROQ cung cấp cho chúng ta quyền truy cập vào tất cả model trên trang của họ miễn phí trong một giới hạn sử dụng nhất định
 
<img width="975" height="425" alt="image" src="https://github.com/user-attachments/assets/6fa8d478-29ad-4ea2-bf6c-1ae3b5eb131f" />

-	FAISS vector store:
FAISS là một thư viện hiệu quả trong việc tìm kiếm tương đồng (similarity search) và phân cụm vector
Điểm mạnh của FAISS
+ Tìm kiếm nhanh do dữ liệu được lưu trong RAM (có thể mất nếu không lưu vào đĩa)
+ Hiệu quả trong việc xử dụng bộ nhớ
+ Hỗ trợ GPU
+ Có thể xử lý hàng triệu vector

Ví dụ sử dụng FAISS vector store:
+ Khởi tạo vector store:
 
<img width="975" height="311" alt="image" src="https://github.com/user-attachments/assets/544308c7-f671-49da-b6d2-62a2040e2e19" />

+ Lưu vector store vào đĩa:
 
<img width="633" height="145" alt="image" src="https://github.com/user-attachments/assets/62578efe-0ade-44c5-8eb4-6d9fd7081219" />

+ Load một vector store có sẵn để sử dụng:
 
<img width="975" height="319" alt="image" src="https://github.com/user-attachments/assets/b58a4c0d-d9f8-4d79-8b58-c3f446a610a5" />

-	Astra Database (from Datastax)
Astra DB là một dịch vụ cung cấp cơ sở dữ liệu đám mây (DBaaS – Database-as-a service) được xây dựng trên nền tảng Cassandra, có khả năng mở rộng và chịu lỗi. Astra DB có tính chất serverless, chúng ta không cần phải tự thuê máy chủ và cài đặt
Điểm mạnh:
+ Không cần quản lý: Cassandra "thô" (tự host) cực kỳ phức tạp để cài đặt, cấu hình, mở rộng và sửa chữa. Astra DB loại bỏ 100% gánh nặng vận hành này
+ Tích hợp vector search mạnh mẽ: Astra DB được tối ưu hóa để lưu trữ và truy vấn vector embeddings. Điều này làm cho nó trở thành một vector store hiệu suất cao, lý tưởng để xây dựng các hệ thống RAG (Retrieval-Augmented Generation) cho chatbot và AI
+ Khả năng mở rộng tốt: Astra DB được thiết kế để xử lý lượng dữ liệu khổng lồ (petabytes) và hàng triệu lượt truy cập mỗi giây. Chúng ta có thể mở rộng quy mô mà không bị gián đoạn dịch vụ
+ Tính sẵn sàng cao (Always-On): Kiến trúc phân tán của Cassandra (không có điểm lỗi trung tâm) đảm bảo rằng cơ sở dữ liệu của bạn gần như không bao giờ "chết", ngay cả khi một vài máy chủ gặp sự cố
+ API linh hoạt: Ngoài ngôn ngữ truy vấn CQL (giống SQL) của Cassandra, Astra DB còn hỗ trợ các API hiện đại như REST, GraphQL, và API tài liệu (JSON), giúp các nhà phát triển web dễ dàng kết nối mà không cần biết sâu về Cassandra
+ Đa đám mây (Multi-cloud): Bạn có thể chạy Astra DB trên AWS, Google Cloud, và Azure, giúp bạn tránh bị "khóa" vào một nhà cung cấp đám mây duy nhất

Ví dụ sử dụng Astra DB:
+ Trước hết, chúng ta cần phải có tài khoản trên Datastax
+ Tạo một database trên website của Datastax
+ Lấy API Endpoint và Token từ website
+ Khởi tạo vector store với Astra DB
 
<img width="975" height="613" alt="image" src="https://github.com/user-attachments/assets/b90fe930-c1ca-4e4a-b929-5594874fabb9" />

+ Thực hiện thêm documents vào vector store
 
<img width="788" height="519" alt="image" src="https://github.com/user-attachments/assets/fd9ca1ea-72ca-48d6-bb0f-14531b8bafc3" />

+ Thực hiện truy vấn:
 
<img width="975" height="506" alt="image" src="https://github.com/user-attachments/assets/e686f596-19a3-4a58-8a39-4e582b46a68a" />

+ Biến đổi sang retriever
 
<img width="975" height="175" alt="image" src="https://github.com/user-attachments/assets/e70201f7-82e6-46c7-ba21-203834634563" />

-	Pinecone:
Là một vector store được quản lý hoàn toàn trên đám mây, được thiết kế để:
+ Lưu trữ hàng triệu hoặc hàng tỷ vector embeddings
+ Tìm kiếm và truy vấn các vector tương tự nhau với tốc độ cực nhanh

Là một DbaaS (Database-as-a -service) giống như Astra DB, chúng ta không cần phải tự thuê server và cài đặt

Điểm mạnh:
+ Hoàn toàn được quản lý (Fully Managed/Serverless): không cần lo lắng về việc cài đặt cấu hình máy chủ, vá lỗi hay mở rộng (scaling). Chỉ cần API key là có thể làm việc
+ Tốc độ cực cao (High Performance): Pinecone được xây dựng từ đầu chỉ cho một mục đích là tìm kiếm vector nhanh. Nó có thể lọc qua hàng tỷ vector trong vài mili giây, điều mà các vector store tự host như FAISS rất vất vả để đạt được ở quy mô lớn
+ Khả năng mở rộng (Scalability): được thiết kế để mở rộng quy mô một cách liền mạch. Có thể bắt đầu từ 10000 vector tăng lên 10 tỷ vector nhưng không cần thay đổi kiến trúc code
+ Dễ sử dụng với API đơn giản, về cơ bản chỉ có 2 thao tác chính: index.upsert() (để thêm/cập nhật database) và index.query() (để tìm  kiếm vector)
+ Hệ sinh thái lớn vì là một trong những vector DB đầu tiên và phổ biến, được tích hợp với các thư viện như LangChain và LlamaIndex

Điểm yếu: 
+ Chi phí tốn kém do là một dịch vụ serverless với hiệu suất cao
+ Độc quyền (Proprietary / Vendor Lock-in): Pinecone là sản phẩm thương mại, mã nguồn đóng. Việc di chuyển hệ thống với hàng tỷ vector sang nhà cung cấp khác (như AstraDB, Weaviate, hoặc Chroma) sẽ rất tốn kém
+ Chỉ tập trung vào việc tìm kiếm vector, chúng ta không thể thực hiện các truy vấn phức tạp hay lưu trữ quan hệ, thường phải dùng đến cơ sở dữ liệu thứ hai
+ Độ trễ mạng (Network Latency): vì là một dịch vụ đám mây, mọi thao tác upsert hay query đều là một lệnh gọi API qua mạng. Đối với các ứng dụng đòi hỏi độ trễ cực thấp (ví dụ: dưới 10ms), việc này có thể là một vấn đề so với việc chạy FAISS ngay trên cùng một máy chủ (in-process)

Ví dụ sử dụng:
+ Trước hết chúng ta cần tạo account trên Pinecone
+ Lấy API key từ website của Pinecone
 
<img width="789" height="189" alt="image" src="https://github.com/user-attachments/assets/8498f332-4761-42ce-857f-d0c79a0de2c1" />

+ Kiểm tra xem một index (vector database) đã tồn tại hay chưa, nếu chưa thì một index serverless sẽ được tạo với một cấu hình cụ thể
 
<img width="975" height="547" alt="image" src="https://github.com/user-attachments/assets/2f96bf81-7979-4172-9cd5-72d451f4a2d4" />

+ Khởi tạo vector store:
 
<img width="966" height="263" alt="image" src="https://github.com/user-attachments/assets/359ee0b0-265f-4f72-a4c3-7f1a319c01d9" />

+ Sau đó ta có thể thực hiện các thao tác như .add_documents() để thêm documents vào hoặc .similarity_search() để tìm kiếm vector tương đồng



