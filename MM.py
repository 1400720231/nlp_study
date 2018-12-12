"""
正向最大匹配
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
		index = 0
		length = len(text)
		while index < len(text):
			word = None
			for size in range(self.maximum,0,-1):
				if size > length:
					continue 
				# index:size+indx中间长度永远为size，这是合理的
				piece = text[index : size+index]
				# 如果匹配到了语料
				if piece in self.dictionary:
					# 其实word只要不为None就行，因为这里word=piece只是想告诉while，已经匹配到了东西
					word = piece
					results.append(piece)
					index += size
					break
			# 如果一轮匹配不到就index+1,表示text左边抛弃一个，
			if word is None:
				index += 1
		return results[::]


if __name__ == "__main__":
	text = "南京市长江大桥"
	tokenizer = IMM('./data/rmm_dict.csv')
	print(tokenizer.cut(text)) 