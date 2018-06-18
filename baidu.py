from aip import AipOcr
import configparser


class BaiDuAPI():  #图片文字识别
    def __init__(self, filePath):
        target = configparser.ConfigParser()
        target.read(filePath)
        app_id = target.get('工单id', 'APP_ID')
        api_key = target.get('工单key', 'API_Key')
        secret_key = target.get('密码', 'Secret_Key')
        self.client = AipOcr(app_id, api_key, secret_key)

    def picture2text(self, filePath):
        images = self.getPicture(filePath)
        texts = self.client.basicGeneral(images)
        alltexts = ''
        for word in texts['words_result']:
            alltexts = alltexts + word.get('words', '')
        return alltexts

    def getPicture(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()


if __name__ == '__main__':

    baiduapi = BaiDuAPI('password.ini')
    print(baiduapi.picture2text('picture.png'))
