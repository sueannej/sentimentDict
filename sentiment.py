import requests
import json
import nltk

## Oxford Dictionaries API
# settings
app_id = "9cf2877d"
app_key = "26e0bd18500ee95a67467be2cfb79bbd"
language = 'en'
# requests
def request_definition(word):
	url = "https://od-api.oxforddictionaries.com:443/api/v1/entries/" + language + "/" + word.lower()
	r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})

	def_beg = r.text.find("definitions")+57
	def_end = def_beg + r.text[def_beg:].find('"')
	return r.text[def_beg:def_end]

# print(request_definition('sol'))

## text-processing.com
def request_sentiment(word):
	data = [('text', word)]
	r = requests.post('http://text-processing.com/api/sentiment/', data=data)

	neg_beg = r.text.find("neg")+6
	neg_end = neg_beg + r.text[neg_beg:].find(',')
	neg = r.text[neg_beg:neg_end]

	neu_beg = r.text.find("neu")+10
	neu_end = neu_beg + r.text[neu_beg:].find(',')
	neu = r.text[neu_beg:neu_end]

	pos_beg = r.text.find("pos")+6
	pos_end = pos_beg + r.text[pos_beg:].find('}')
	pos = r.text[pos_beg:pos_end]

	return (float(pos)+float(neg))/float(neu)

#request_sentiment('car')
#request_sentiment('standard')
#request_sentiment('good')
#request_sentiment('logic')
#request_sentiment('energic')
#request_sentiment('president')
#request_sentiment('processing')
#request_sentiment('argument')

def request_score(word):
	sent = 0
	w_def = request_definition(word)
	w_tok = nltk.word_tokenize(w_def)
	for w in w_tok:
		sent = sent + request_sentiment(w)
	return sent/len(w_tok)

# print(request_score('solar'))
# print(request_score('bear'))
# print(request_score('great'))
# print(request_score('pole'))
# print(request_score('excellent'))
# print(request_score('announcement'))
print(request_score('soldier'))
# print(request_score('obama'))
print(request_score('happening'))
print(request_score('largely'))