from bloomfilter import BloomFilter 
from random import shuffle 
  
n = 5 
p = 0.1 
  
bloomf = BloomFilter(n,p) 
print("kích thước của mảng bit :{}".format(bloomf.size)) 
print("xác suất dương tính giả :{}".format(bloomf.fp_prob)) 
print("Số lượng hàm :{}".format(bloomf.hash_count)) 
  
# những từ cần thêm vào 
word_present = [ 'gems','generosity','generous','generously','genial'] 
  
# từ chưa được thêm vào 
word_absent = ['bluff','cheater','hate','war','humanity',  
               'geeksforgeeks','twitter'] 
  
for item in word_present: 
    bloomf.add(item) 
  
shuffle(word_present) 
shuffle(word_absent) 
  
test_words = word_present[:10] + word_absent 
shuffle(test_words) 
for word in test_words: 
    if bloomf.check(word): 
        if word in word_absent: 
            print("'{}'Là kết quả dương giả !".format(word)) 
        else: 
            print("'{}'Có thể có mặt !".format(word)) 
    else: 
        print("'{}' chắc chắn là không có !".format(word))