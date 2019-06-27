from threading import Timer
from wxpy import *
import requests
import itchat


API_KEY = '**********'

bot = Bot(cache_path=True)
my_friend = ensure_one(bot.search('***')) # 微信昵称
tuling = Tuling(api_key=API_KEY)



@bot.register(my_friend)
def reply_my_friend(msg):
	tuling_reply = tuling.do_reply(msg)



def get_news():
	url = "http://open.iciba.com/dsapi/"
	r = requests.get(url)
	contents = r.json()['content']
	translation = r.json()['translation']
	return contents, translation



def login_wechat():
	global bot
	bot = Bot(cache_path=True)




def send_news():
	if bot == None:
		login_wechat()

	try:
		my_friend = bot.friends().search('***')[0]  # 微信昵称
		my_friend.send(get_news()[1][5:] + '---来自一个喜欢你的人!')
		print('成功!')
		t = Timer(86400, send_news)
		t.start()
	except:
		print('失败！！')



if __name__ == '__main__':
	send_news()

bot.start()
