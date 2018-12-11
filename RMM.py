"""
逆向最大匹配
"""
class IMM:
	def __init__(self,dic_path):
		self.dictionary = set()
		self.maximum = 0
		with open(dic_path,"r", encoding="utf-8") as f:
			for line in f:
				line = line.strip()
				if not line:
					continue
				self.dictionary.add(line)
				# 确定所有字典语料中的最大长度
				if len(line) > self.maximum:
					self.maximum = len(line)

	def cut(self,text):
		results = []
		index = len(text)
		# while 表示当一次匹配完成后没有匹配到内容，index -1表示从text的右边舍弃一位，在
		# piece = text[(index-size):index]体现出来。切片的起点到终点相隔size不变，但是index-1了，
		# 表示text的最右边，没有被取到。逆向匹配法即是如此的
		while index > 0:
			word = None
			for size in range(self.maximum,0,-1):
				if size > index:
					continue 
				piece = text[(index - size):index]
				# 如果匹配到了语料
				if piece in self.dictionary:
					# 其实word只要不为None就行，因为这里word=piece只是想告诉while，已经匹配到了东西
					word = piece
					results.append(piece)
					index -= size
					break
			# 如果一次匹配完成后没有匹配到，则indx-1,按照逆向最大匹配法的原理，目标字符的最右边的字符在接下来的匹配中
			# 被抛弃，正向最大匹配则相反
			if word is None:
				index -= 1
		return results[::-1]


if __name__ == "__main__":
	text = "南京市长江大桥"
	tokenizer = IMM('./data/rmm_dict.csv')
	print(tokenizer.cut(text))