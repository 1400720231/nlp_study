"""
jieba高频词提取,TF
"""
import jieba
"""
加载自定义词典，比如这里我加入了“一带一路”，如果不加，就会被分词成“一带”，“一路”
需要注意的是该自定义词库的编码为utf8,而且词库中的顺序必须是 词语 词频(可省略) 词性(可省略) 
"""
jieba.load_userdict("data/user_load.csv") 


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
		tf_dict[w] = tf_dict.get(w, 0) + 1
	# 这个写法还是有意思的，根据items的key排序，默认从小到大，reverse=True，从大到小排序，取前topK个
	return sorted(tf_dict.items(), key=lambda x: x[1], reverse=True)[:topK]

# 加载停用词,该词库为自定义的，可以定期维护，按需求来
def stop_word(path):
	with open(path,'r',encoding='utf8') as f:
		return [l.strip() for l in f]

if __name__ == "__main__":
	content = get_content("data/data.csv")
	# 列表推倒式．．．．
	cut_word = [i for i in jieba.cut(content) if i not in stop_word("data/stop_word.csv") and i !=' ']
	print(cut_word)
	topK_word = get_TF(cut_word)
	print(topK_word)