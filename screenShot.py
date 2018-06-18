import keyboard
from PIL import ImageGrab
from time import sleep
import sys
from baidu import BaiDuAPI
from gettexts import GetText


def screenShot(): #用于截图和保存
    if keyboard.wait(hotkey='ctrl+alt+a') == None:  #截图开始
        if keyboard.wait(hotkey='ctrl+c') == None:  #截图结束条件
            sleep(1)  #防止获取的是上一张的图片
            im = ImageGrab.grabclipboard() #复制剪切板里的图片
            im.save('image.jpg')


if __name__ == '__main__':
    baiduapi = BaiDuAPI('password.ini')
    for _ in range(sys.maxsize):
        screenShot()
        texts = baiduapi.picture2text('image.jpg')
        #print(texts)
        GetText.setText(texts)
        sleep(0.5)
        GetText.getText()