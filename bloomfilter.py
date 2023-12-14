
# Trước tiên hãy cài đặt mô-đun mmh3 và bitarray của bên thứ 3 
# pip install mmh3 
# pip install bitarray 
import math 
import mmh3 
from bitarray import bitarray 

''' 
	lớp cho bộ lọc Bloom, sử dụng hàm băm
	'''
class BloomFilter(object): 

	

	def __init__(self, items_count, fp_prob): 
		''' 
		items_count : int 
			 Số lượng mục dự kiến ​​sẽ được lưu trữ trong bộ lọc
		fp_prob : float 
			Sai Xác suất dương ở dạng thập phân
		'''
		
		self.fp_prob = fp_prob 

		# Size of bit array to use, kích thước mảng bit được sử dụng 
		self.size = self.get_size(items_count, fp_prob) 

		# number of hash functions to use , số lượng hàm được sử dụng 
		self.hash_count = self.get_hash_count(self.size, items_count) 

		# Bit array of given size, mảng bit có kich thước cho trước  
		self.bit_array = bitarray(self.size) 

		# initialize all bits as 0 , khởi tạo tất cả các bit bằng 0 
		self.bit_array.setall(0) 
		''' 
		Thêm thư mục vào bộ lọc  
		'''
	def add(self, item): 
	
		digests = [] 
		for i in range(self.hash_count): 

# tạo thông báo cho mục nhất định.
# tôi làm hạt giống cho hàm mmh3.hash()
# Với các hạt giống khác nhau, quá trình tiêu hóa được tạo ra cũng khác nhau
			digest = mmh3.hash(item, i) % self.size 
			digests.append(digest) 

			# set the bit True in bit_array , Đặt bit là True trong bit_Aray 
			self.bit_array[digest] = True

	def check(self, item): 
		''' 
		Check for existence of an item in filter 
		'''
		for i in range(self.hash_count): 
			digest = mmh3.hash(item, i) % self.size 
			if self.bit_array[digest] == False: 

				# nếu bất kì bit nào Sai thì nó không tồn tại 
				# nếu không thì có khả năng tồn tại 
				return False
		return True

	@classmethod
	def get_size(self, n, p): 
		m = -(n * math.log(p))/(math.log(2)**2) 
		return int(m) 

	@classmethod
	def get_hash_count(self, m, n): 
		k = (m/n) * math.log(2) 
		return int(k) 
