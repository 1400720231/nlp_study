"""
jieba高频词提取,TF
"""
import jieba
# 数据提取,把数据字变成一个很长的字符串
def get_content(path):
	with open(path, "r", encoding="utf8") as f:
		content = ""
		for line in f:
			# 取空格　制表符　回车　空格　以及这份数据的一个不晓得什么鬼的特殊字符
			content += line.strip("\n").strip("").strip("\t").strip("\r").strip("\u3000")
		print(content)
		return content

# 提取前k个高频词语
def get_TF(words,topK=10):
	tf_dict = {}
	for w in words:
		tf_dict[w] = tf_dict.get(w,0) + 1
	# 这个写法还是有意思的，根据items的key排序，默认从小到大，reverse=True，从大到小排序，取前topK个
	return sorted(tf_dict.items(), key=lambda x: x[1], reverse=True)[:topK]

# 加载停用词
def stop_word(path):
	with open(path,'r',encoding='utf8') as f:
		return [l.strip() for l in f]

if __name__ == "__main__":
	content = get_content("data.csv")
	# 列表推倒式．．．．
	cut_word = [i for i in jieba.cut(content) if i not in stop_word("stop_word.csv") and i !=' ']
	print(cut_word)
	topK_word = get_TF(cut_word)
	print(topK_word)