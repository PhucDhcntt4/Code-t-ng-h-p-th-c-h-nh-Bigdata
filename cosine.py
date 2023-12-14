from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dữ liệu mẫu - danh sách các văn bản
documents = [
  
"Trong quá trình nghiên cứu khoa học, viết luận án, bài báo hay một quyển sách, các tác giả thường tham khảo và sử dụng các tài liệu để trích dẫn vào công trình nghiên cứu, các tài liệu được tác giả trích dẫn gọi là tài liệu tham khảo (TLTK)..",
    "Khi trích dẫn một tài liệu, một ý kiến, một kết quả của một tác giả khác cần phải ghi rõ ý kiến này của ai, trích dẫn từ đâu trong phần TLTK. TLTK được trình bày ở phần cuối một luận án, một nghiên cứu khoa học, một bài báo, một quyển sách,…",
    "TLTK ngoài ý nghĩa là nơi ghi lại những trích dẫn còn có một ý nghĩa khác; người đọc có thể từ TLTK mà tìm ra các tài liệu gốc. Do đó TLTK phải bao gồm tất cả các tác giả với công trình có liên quan đã được trích dẫn trong luận văn; các chi tiết phải được ghi đầy đủ, rõ ràng và chính xác để độc giả quan tâm có thể tìm được tài liệu đó.",
    "Cũng có khái niệm cho răng: “Tài liệu tham khảo là đề cập đến danh mục hệ thống các tác phẩm của một tác giả hoặc lĩnh vực kiến ​​thức cụ thể”."
]

# Tạo vector đặc trưng TF-IDF cho các văn bản
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Tính độ tương tự cosine giữa các văn bản
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

# In ma trận độ tương tự cosine
print("Ma trận Cosine :")
print(cosine_similarities)

# In các cặp văn bản có độ tương tự cao nhất
num_documents = len(documents)
for i in range(num_documents):
    for j in range(i + 1, num_documents):
        similarity = cosine_similarities[i, j]
        print(f"Sự tương đồng tài liệu {i + 1} với tài liệu {j + 1}: {similarity:.4f}")
