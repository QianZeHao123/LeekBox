from m5stack import *
from m5stack_ui import *
from uiflow import *
from m5mqtt import M5mqtt

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x000000)

stockName = M5Label('stockName', x=35, y=10, color=0xffffff, font=FONT_UNICODE_24, parent=None)
stockCode = M5Label('stockCode', x=180, y=10, color=0xffffff, font=FONT_MONT_24, parent=None)
stockPrice = M5Label('stockPrice', x=120, y=60, color=0xffffff, font=FONT_MONT_48, parent=None)
Prev_Close = M5Label('PrevClose', x=9, y=150, color=0xffffff, font=FONT_MONT_12, parent=None)
Open = M5Label('Open', x=22, y=205, color=0xffffff, font=FONT_MONT_12, parent=None)
Bid = M5Label('Bid', x=145, y=150, color=0xffffff, font=FONT_MONT_12, parent=None)
Ask = M5Label('Ask', x=143, y=205, color=0xffffff, font=FONT_MONT_12, parent=None)
label0 = M5Label('Text', x=84, y=150, color=0xffffff, font=FONT_MONT_12, parent=None)
label1 = M5Label('Text', x=84, y=205, color=0xffffff, font=FONT_MONT_12, parent=None)
label2 = M5Label('Text', x=190, y=150, color=0xffffff, font=FONT_MONT_12, parent=None)
label3 = M5Label('Text', x=190, y=205, color=0xffffff, font=FONT_MONT_12, parent=None)
label4 = M5Label('Text', x=240, y=150, color=0xffffff, font=FONT_MONT_12, parent=None)
label5 = M5Label('Text', x=240, y=205, color=0xffffff, font=FONT_MONT_12, parent=None)

def fun_stockName_(topic_data):
  # global params
  lcd.clear()
  Prev_Close.set_text('PrevClose')
  Open.set_text('Open')
  Bid.set_text('Bid')
  Ask.set_text('Ask')
  stockName.set_text(str(topic_data))
  pass

def fun_stockCode_(topic_data):
  # global params
  stockCode.set_text(str(topic_data))
  pass

def fun_stockPrice_(topic_data):
  # global params
  stockPrice.set_text(str(topic_data))
  pass

def fun_todayStart_(topic_data):
  # global params
  label1.set_text(str(topic_data))
  pass

def fun_bid0_(topic_data):
  # global params
  label2.set_text(str(topic_data))
  pass

def fun_yesterdayEnd_(topic_data):
  # global params
  label0.set_text(str(topic_data))
  pass

def fun_ask0_(topic_data):
  # global params
  label3.set_text(str(topic_data))
  pass

def fun_bid1_(topic_data):
  # global params
  label4.set_text(str(topic_data))
  pass

def fun_ask1_(topic_data):
  # global params
  label5.set_text(str(topic_data))
  pass

def fun_color_(topic_data):
  # global params
  if topic_data == '1':
    screen.set_screen_bg_color(0x990000)
  else:
    screen.set_screen_bg_color(0x009900)
  pass

def buttonC_wasPressed():
  # global params
  power.powerOff()
  pass
btnC.wasPressed(buttonC_wasPressed)

m5mqtt = M5mqtt('M5stack', '192.168.1.105', 1883, 'qianzehao', '123456', 4096)
m5mqtt.subscribe(str('stockName'), fun_stockName_)
m5mqtt.subscribe(str('stockCode'), fun_stockCode_)
m5mqtt.subscribe(str('stockPrice'), fun_stockPrice_)
m5mqtt.subscribe(str('todayStart'), fun_todayStart_)
m5mqtt.subscribe(str('bid0'), fun_bid0_)
m5mqtt.subscribe(str('yesterdayEnd'), fun_yesterdayEnd_)
m5mqtt.subscribe(str('ask0'), fun_ask0_)
m5mqtt.subscribe(str('bid1'), fun_bid1_)
m5mqtt.subscribe(str('ask1'), fun_ask1_)
m5mqtt.subscribe(str('color'), fun_color_)
m5mqtt.start()