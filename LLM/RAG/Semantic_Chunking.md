# [cite_start] SEMANTIC CHUNKING [cite: 1]

## [cite_start] Khái niệm về semantic chunking: [cite: 2]

[cite_start]Là một quá trình để chia các documents thành các chunks dựa trên độ tương đồng về ngữ nghĩa, không phải bởi số token hay số dòng[cite: 3].

[cite_start]Điều này giúp tăng cường sự mạnh mẽ của hệ thống RAG do mỗi chunk giờ đây sẽ giàu thông tin hơn, làm cho việc sinh phản hồi tốt và chính xác hơn[cite: 4].

## [cite_start]Các bước hoạt động: [cite: 5]

* [cite_start]\+ Documents được chia thành các đơn vị nhỏ hơn thường là một câu [cite: 6]
* [cite_start]\+ Mỗi câu sẽ được biến đổi sang vector (sentence embedding) [cite: 7]
* [cite_start]\+ Tính độ tương đồng (similarity) giữa các embedding gần nhau (câu 1 và câu 2, câu 2 và câu 3, …) [cite: 8]
* [cite_start]\+ Merge các embedding gần nhau lại nếu similarity giữa chúng vượt qua một ngưỡng nhất định (threshold) [cite: 9]
* \+ Hình thành các chunks sau khi merge. [cite_start]Ví dụ [s1,s2] -> chunk1, [s3] -> chunk2 [cite: 10]

## [cite_start]Ví dụ về semantic chunking [cite: 11]

[cite_start]*(Nội dung hình ảnh [cite: 11])*
