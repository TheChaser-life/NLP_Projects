# LANGGRAPH BASIC

-	Khái niệm về LangGraph:
LangGraph là một thư viện dùng để xây dựng các ứng dụng có khả năng ghi nhớ trạng thái (những gì đã xảy ra trước đó), bao gồm nhiều tác nhân (AI Agent) khác nhau cùng làm việc; LangGraph còn được sử dụng để tạo Agent và Multi-Agent Workflow
LangGraph lấy cảm hứng từ Pregel và Apache Beam (là các hệ thống dùng để xử lý dữ liệu song song quy mô lớn), cũng như là NetworkX (một thư viện Python để làm việc với đồ thị). Từ đó, LangGraph xem một luồng công việc (workflow) như một sơ đồ khối với mỗi bước là một node, và các cạnh (edge) là mũi tên chỉ hướng đi. Cách tiếp cận này giúp quản lý các luồng phức tạp trở nên dễ dàng
LangGraph có thể sử dụng độc lập với LangChain
LangGraph đủ ổn định, mạnh mẽ và đáng tin cậy để chạy trong các sản phẩm thực tế, phục vụ người dùng thật (không chỉ là đồ án thử nghiệm) và được tin tưởng bởi nhiều công ty lớn như LinkedIn, Uber
LangGraph cho phép kiểm soát chi tiết workflow (sau khi làm xong bước A, agent nên làm bước B hay bước C? Khi nào nên quay lại bước A)  và state (Agent đang "nhớ" những gì? Dữ liệu nào cần được lưu lại, dữ liệu nào có thể quên đi?)
LangGraph được cài đặt với central persistence layer (Lớp lưu trữ bền bỉ tập trung) có thể lưu trữ dữ liệu lâu dài mà không bị mất khi tắt máy hay khi ứng dụng bị lỗi. LangGraph có một hệ thống trung tâm để quản lý việc lưu trữ, cho phép các tính năng thông dụng với hầu hết các kiến trúc agent như:
+ Memory: cho phép lưu trữ lại các state (trạng thái) hiện tại và xuyên suốt các lần tương tác, nhờ vào lớp lưu trữ ở trên; ví dụ như lưu lại lịch sử trò chuyện
+ Human-in-the-loop: các state tại các bước quan trọng được lưu lại gọi là các checkpoint; và vì đã được lưu lại nên workflow có thể được tạm dừng (interrupt) và tiếp tục chạy (resume) mà không mất dữ liệu. Ví dụ như AI tìm vé chuyến bay và cần user xác nhận xem có muốn mua vé đó không để tiếp tục các bước tiếp theo

-	Khái niệm về Directed Acyclic Graph hay đồ thị có hướng không tuần hoàn (DAG):
Là một đồ thị có hướng không có vòng lặp hay chu trình nhằm đảm bảo mọi quy trình đều có điểm bắt đầu và kết thúc rõ ràng, không bị kẹt trong vòng lặp vô tận
 
<img width="975" height="999" alt="image" src="https://github.com/user-attachments/assets/6caba704-4676-4fe0-857e-de6d06d3b272" />

-	Khái niệm về LangSmith:
LangSmith được phát triển bởi công ty LangChain Inc với mục đích giúp xây dựng, gỡ lỗi (debug), kiểm thử (test), đánh giá (evaluate) và giám sát (monitor) các ứng dụng sử dụng LLM
Các tính năng chính của LangSmith:
+ Tracing and Debugging (truy vết và gỡ lỗi): LangSmith ghi lại mọi bước mà ứng dụng AI thực hiện. Nếu ứng dụng bị lỗi thì chúng ta có thể nhìn vào các bước này để biết chính xác sai ở bước nào, với prompt nào, và ở thời điểm nào

+ Evaluation: LangSmith cho phép tạo một dataset gồm nhiều câu hỏi mẫu sau đó cho AI của chúng ta trả lời các câu hỏi này và LangSmith sẽ hỗ trợ chấm điểm các câu trả lời (chấm bằng AI hoặc tự chúng ta chấm)

+ Monitoring and Analytics: khi ứng dụng đã được đưa ra thị trường và có người dùng, LangSmith sẽ giám sát mọi yêu cầu từ người dùng và cho biết các chỉ số quan trọng như:
1.	Latency (độ trễ): Mất bao lâu để AI trả lời?
2.	Cost (chi phí): Tốn bao nhiêu token cho mỗi câu trả lời
3.	Error Rate: Số lần AI bị lỗi không trả lời được
4.	User Feedback: Người dùng có bấm like hay dislike vào câu trả lời không 

-	Building simple graph:
Các thành phần chủ yếu trong một graph:
1.	Nodes: thường là các hàm (function) để thực hiện một task
2.	Edges: kết nối các nodes lại với nhau, edges có thể có hoặc không có điều kiện
3.	State: lược đồ các state đóng vai trò như input cho các node và edge
4.	State Graph: kiến trúc của toàn bộ Graph
 
<img width="975" height="176" alt="image" src="https://github.com/user-attachments/assets/2689e6c8-0425-4f87-9973-dfbfc8dd63ae" />

Ví dụ về các bước tạo một simple graph trong code:
1.	Tạo state of the graph:
+ Đây là trạng thái của graph sẽ đi vào khắp nơi trong graph
+ Sử dụng TypeDict để cho biết các giá trị (values) của state (keys) có kiểu dữ liệu gì
 
<img width="975" height="560" alt="image" src="https://github.com/user-attachments/assets/89bda826-d052-48af-b524-29122a91f51a" />

2.	Tạo các nodes:
+ Mỗi node là một hàm thực thi (function)
+ Tham số đầu tiên là state (là một TypeDict) đã được định nghĩa ở trên, vì vậy mỗi node có thể truy cập vào trạng thái hiện tại trong state thông qua các key của nó
+ Mỗi node sẽ trả về một giá trị mới cho một state và thông thường các giá trị mới sẽ được ghi đè lên giá trị cũ
 
<img width="975" height="810" alt="image" src="https://github.com/user-attachments/assets/342204a8-d912-4377-bdbf-81c872b98fd7" />

3.	Xây dựng graph hoàn chỉnh:
+ Khởi tạo lớp StateGraph từ langgraph.graph với lớp State (TypeDict) đã được định nghĩa ở trên
+ Thêm nodes và edges vào graph
+ Sử dụng START node (node đặc biệt để gửi input của user đến graph) để xác định điểm bắt đầu của graph
+ Sử dụng END node để cho biết quá trình thực thi đã xong
+ Biên dịch (compile) graph để chạy
+ Lấy cấu trúc của graph và hiển thị dưới dạng mermaid (một dạng sơ đồ khối)

<img width="975" height="521" alt="image" src="https://github.com/user-attachments/assets/9cc13227-c960-416f-8bbd-7e0ecc710daa" /> 
+ Ipython.display dùng để hiển thị ảnh trong môi trường notebook:
<img width="341" height="520" alt="image" src="https://github.com/user-attachments/assets/3eda9033-6385-462d-8ca2-af38c7d8368d" />
				 
Giải thích cách hoạt động khi gọi graph với phương thức invoke:
+ Bắt đầu ở Node START 
+ Đi đến start_play và in ra "start_play node has been called"
+ Chạy hàm random_play để đưa ra bước tiếp theo (coditional_egdes)
+ Sau khi có kết quả footbal/game node thì sẽ đi đến node được chon tiếp theo
+ Cuối cùng kết thúc ở Node END
 
<img width="861" height="309" alt="image" src="https://github.com/user-attachments/assets/7d483c97-0064-4409-8766-1026c97912f2" />

-	Tạo chatbot với LangGraph:
Các bước thực hiện:
1.	Import các thư viện cần thiết:
+ Annotated để xác định kiểu dữ liệu và metadata của một biến. Khi LangGraph thấy một list có metadata là add_messages thì nó sẽ thêm tin nhắn vào list thay vì ghi đè tin nhắn cũ thành tin nhắn mới (giống với chat history)
+ add messages là một reducer (một hàm dùng để cập nhật state của graph có kiểm soát) dùng để nối messages mới vào các messages cũ
 
<img width="856" height="284" alt="image" src="https://github.com/user-attachments/assets/68582717-9559-44ba-8af6-d8527640eded" />

2.	Khởi tạo class State
 
<img width="756" height="138" alt="image" src="https://github.com/user-attachments/assets/a0d27834-4c05-4f3d-a993-b1bcee917c85" />

3.	Lấy API Key và khởi tạo model
 
<img width="975" height="519" alt="image" src="https://github.com/user-attachments/assets/16d09d45-4fa2-4750-ab76-4577ac20ece7" />

4.	Viết hàm trả lời câu hỏi
 
<img width="900" height="148" alt="image" src="https://github.com/user-attachments/assets/3670a4e5-5117-4a74-9b24-51c97bac0f27" />

5.	Khởi tạo node và các edges
 
<img width="975" height="984" alt="image" src="https://github.com/user-attachments/assets/62b6941c-95a0-4686-8f00-7c88f9ffca64" />

6.	Kiểm tra workflow
 
<img width="975" height="89" alt="image" src="https://github.com/user-attachments/assets/259ba3c2-7da1-436c-93ef-4c9e75cce260" />

Phương thức stream cho ta biết kết quả được trả ra ở từng node thì vì đợi đến khi cả graph thực thi xong
 
<img width="975" height="152" alt="image" src="https://github.com/user-attachments/assets/088e969a-dcb7-4326-a7a4-d182d7404c89" />
	
-	Tạo state graph với dataclass:
Dataclass là một decorator được đặt ngay trên class với cú pháp @dataclass. Nó sẽ tự động thêm các hàm như __init__, __repr__ (dùng để in) vào class
Khởi tạo state graph với dataclass
 
<img width="799" height="322" alt="image" src="https://github.com/user-attachments/assets/2e28a607-58b7-4ba8-9f59-139244d5e534" />

Cách gọi các thuộc tính khác với khi gọi key nếu ta sử dụng TypeDict

 <img width="975" height="447" alt="image" src="https://github.com/user-attachments/assets/24330694-827c-4678-9acf-2a940faae00c" />

Để chạy graph thì ta cũng cần truyền vào một đối tượng của class DataClassState và cần phải khởi tạo đủ thuộc tính
 
<img width="969" height="291" alt="image" src="https://github.com/user-attachments/assets/397beb3a-57e2-433b-a1a4-473a6ceb8d37" />

-	Pydantic:
Lớp cơ sở (BaseModel) của pydantic có khả năng xác thực dữ liệu (kiểm tra kiểu dữ liệu đầu vào). Mục đích sử dụng pydantic là để kiểm tra dữ liệu ngay khi được đưa vào chứ không phải đến lúc thực thi graph mới báo lỗi
Khởi tạo state graph với lớp cơ sở (BaseModel) từ thư viện pydantic: bất cứ thứ gì được định nghĩa trong State sẽ được pydantic quản lý. Pydantic sẽ tự động đảm bảo rằng:
+ Phải cung cấp đầy đủ giá trị cho thuộc tính trong class, nếu không sẽ báo lỗi
+ Phải cung cấp đúng kiểu dữ liệu cho các thuộc tính, nếu không sẽ báo lỗi
 
<img width="628" height="205" alt="image" src="https://github.com/user-attachments/assets/a1e4fbe4-d948-4eaf-8e93-824b80d8124a" />

Tạo graph với class được quản lý bởi pydantic:
 
<img width="902" height="439" alt="image" src="https://github.com/user-attachments/assets/46489689-0882-4a23-beed-60212657e081" />

Lỗi không truyền đủ giá trị cho thuộc tính:
 
<img width="975" height="1001" alt="image" src="https://github.com/user-attachments/assets/8513c1f3-14de-42b9-8120-339be581b913" />

Lỗi truyền sai kiểu dữ liệu:
 
<img width="975" height="980" alt="image" src="https://github.com/user-attachments/assets/5d8ac18d-8657-4f3a-87d8-7b85f4ba26e1" />

-	Chain trong LangGraph:
Sử dụng chat messages để tạo state graph, mục đích là để xác định vai trò trong đoạn hội thoại
LangChain cung cấp nhiều thể loại của messages:
1.	HumanMessages: message từ người dùng
2.	AIMessages: message từ chat model
3.	SystemMessage: message để hướng dẫn hành vi, vai trò cho chat model
4.	ToolMessage: messages từ việc gọi tool
Mỗi message sẽ có 3 thành phần:
1.	content: nội dung chính của message
2.	name: cho biết bên nào gửi message
3.	response_metadata: chứa metadata của message
 
<img width="975" height="494" alt="image" src="https://github.com/user-attachments/assets/a5036f12-539d-4031-b023-14ca28dd13e6" />

List các message có thể đưa vào LLM
 
<img width="975" height="153" alt="image" src="https://github.com/user-attachments/assets/801014e8-2ce6-434c-841e-322b2a83136a" />

-	Router:
Khái niệm về router trong LangGraph liên quan đến các hàm logic được triển khai bằng  conditional_edge để quyết định ngã rẻ tiếp theo trong graph. Ví dụ như chat model sẽ lựa chọn trả về thẳng output hay gọi tool là tùy vào input từ user
Một ví dụ đơn giản về agent là LLM sẽ kiểm soát trực tiếp flow bằng việc gọi tool hay trả về output luôn 
-	Tool
Là các công cụ hỗ trợ graph để đưa ra phản hồi như calculator, weather API, …
LLM sẽ đóng vai trò như bộ não quyết định xem có nên gọi tool hay không bằng việc đọc hiểu mô tả của từng tool. Ví dụ:
 
<img width="975" height="559" alt="image" src="https://github.com/user-attachments/assets/659f5297-eb0b-4319-95ef-665faedcd107" />

Ví dụ về một tool đơn giản để cộng 2 số:
 
Trang bị tools cho LLM với phương thức bind_tools(), phương thức này sẽ tạo ra một bản sao của LLM gốc nhưng đã được cấu hình với thông tin về các tools
 
<img width="834" height="177" alt="image" src="https://github.com/user-attachments/assets/0ecc3737-7dee-4751-bc23-3466e8beb1a0" />

Ví dụ về LLM sử dụng tool, ta thấy hàm add đã được gọi với a=1 và b=2 dựa trên câu hỏi :
 
<img width="975" height="162" alt="image" src="https://github.com/user-attachments/assets/fc41fc8a-ca54-4bba-ba10-c92ff1fc72ae" />

Ví dụ một graph với LLM có thể sử dụng tools:
+ Khởi tạo state với messages và reducer (kiểm soát sự cập nhật state)
 
<img width="975" height="423" alt="image" src="https://github.com/user-attachments/assets/a7cc7ebb-83c8-45b4-a65f-5fc5d097da49" />

+ Tạo hàm tool_calling để quyết định nên gọi tools hay không
 
<img width="975" height="123" alt="image" src="https://github.com/user-attachments/assets/24c9bdba-e4b3-447f-9865-f95638d32c9d" />

+ Danh sách các tools:
 
<img width="369" height="117" alt="image" src="https://github.com/user-attachments/assets/493f4233-9c68-48c5-b308-72dca9544413" />

+ Khởi tạo graph với 2 nodes là tool_calling và tools:
ToolNode là một Node được tạo sẵn trong langgraph.prebuilt có vai trò là một trình thực thi công cụ tự động (Tool Executor). Nó sẽ làm 3 việc:
1.	Read: tự động nhìn vào state, tìm AIMessage mới nhất và trích xuất bất kì yêu cầu tool_call nào từ message đó
2.	Execute: lấy tên công cụ và tham số từ tool_call, sau đó tìm hàm Python thích hợp mà nó đã được cấp cho trước đó để thực thi hàm đó
3.	Write: lấy kết quả trả về từ hàm, tự động đóng gói kết quả đó vào ToolMessage và trả về message này để cập nhật lại vào state
tools_condition là một router để kiểm tra xem message cuối cùng từ AI có phải là tool call hay không, nếu đúng nó sẽ trỏ đến ToolNode, nếu không sẽ trỏ về END
 
<img width="975" height="377" alt="image" src="https://github.com/user-attachments/assets/3ed9aabb-6ae6-4c3d-b054-98a9fd25b88d" />

<img width="213" height="520" alt="image" src="https://github.com/user-attachments/assets/c6a91e3b-5ab2-4d53-9732-a9b39084129a" />

Kết quả thực thi graph, dựa trên câu hỏi thì LLM quyết định gọi đến tool add và tool này đã trả về kết quả dưới dạng Tool Message:
 
<img width="975" height="604" alt="image" src="https://github.com/user-attachments/assets/1d9c0385-b0ec-4afd-a688-955faf1ee27e" />

-	Build chatbot with multiple tools using LangGraph
Import các tool và tiện ích (utility) cần thiết:
1.	WikipediaAPIWrapper và ArxivAPIWrapper: đây là các lớp bao bọc (wrapper) cung cấp các phương thức Python đơn giản để tương tác với một dịch vụ bên ngoài
Chúng sẽ kết nối mạng, định dạng câu truy vấn API, gửi yêu cầu, nhận phản hồi và trích xuất nội dung hữu ích
2.	ArxivQuerryRun và WikipediaQueryRun: đây là các công cụ được thiết kế để cho LLM Agent sử dụng. Chúng cung cấp cho LLM 2 thứ rất quan trọng:
name: tên công cụ mà LLM sẽ gọi trong tool_calls
description: là mô tả mà LLM đọc để quyết định khi nào nên sử dụng công cụ này
Bên trong các tool này đã có sẵn wrapper tuy nhiên nếu việc import các wrapper ở trên là để custom lại các tools này nếu cần thiết
 
<img width="975" height="110" alt="image" src="https://github.com/user-attachments/assets/06d5179a-7690-47c1-b8f5-30008a009ac9" />

Ví dụ custom và sử dụng tool arxiv
 
<img width="975" height="262" alt="image" src="https://github.com/user-attachments/assets/16c00457-8abd-4b24-a38c-1c9ec0ff665c" />

Import Tavily: Tavily là một search engine mạnh mẽ, nhanh và chính xác cho LLM, để sử dụng Tavily thì ta cần có API Key từ website của Tavily
 
<img width="975" height="420" alt="image" src="https://github.com/user-attachments/assets/c61d9de6-e4d0-45a9-a0b0-cb4cf69ba903" />

Ví dụ sử dụng Tavily:
 
<img width="975" height="267" alt="image" src="https://github.com/user-attachments/assets/266e7b0c-eda9-401e-af1d-da7af95be927" />

Khởi tạo LLM và trang bị các tools cho nó
 
<img width="975" height="313" alt="image" src="https://github.com/user-attachments/assets/76812d12-bdee-4dfc-804d-e10cd641ff90" />

Ví dụ khi LLM sử dụng tools:

<img width="975" height="787" alt="image" src="https://github.com/user-attachments/assets/3c41f137-27dd-48c5-a0c6-115a8ab2c603" />

 

