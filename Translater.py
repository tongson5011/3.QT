import os
import requests
import uuid
import sys
import logging
import time
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s : %(message)s')

API_KEY = '2b553ac62ccf404ca9b725e6710ee9f8'
SERVICE_REGOIN = 'southeastasia'
SERVICE_ENPOINT = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0'


class Translate():
    '''
    This class translate using azure API \n
    api_key(str): API key \n
    service_region(str): service region \n
    service_enpoint(str): service enpoint
    '''

    def __init__(self, *args, **kwargs):
        self.api_key = kwargs['api_key'] if 'api_key' in kwargs else API_KEY
        self.service_region = kwargs['service_region'] if 'service_region' in kwargs else SERVICE_REGOIN
        self.service_enpoint = kwargs['service_enpoint'] if 'service_enpoint' in kwargs else SERVICE_ENPOINT
        self.charaters = kwargs['charaters'] if 'charaters' in kwargs else {}
        self.headers = {
            'Ocp-Apim-Subscription-Key': self.api_key,
            'Ocp-Apim-Subscription-Region': self.service_region,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }
    
    # format data
    def formatTranslate(self, text='', charaters={}):
        for char in charaters.keys():
            text = text.replace(char, f'''<mstrans:dictionary translation="{charaters[char]}"> {char} </mstrans:dictionary>''')
        return text
    
    # translate CN to VI
    def translateCNtoVI(self, cn_vi_text):
        time.sleep(0.1)
        '''
        This function translate CN to VI
        src_text(str): source text (CN language)
        '''
        try:
            params = '&from=zh-Hans&to=vi'
            constructed_url = self.service_enpoint + params
            text = self.formatTranslate(cn_vi_text, self.charaters)
            self.body = [{
                'text': f'''{text}'''
            }]
            logging.info('Staring translate chapter')
            request = requests.post(constructed_url,
                                    headers=self.headers, json=self.body)
            if not request.ok:
                return {'status': 'Faild',
                        'message': f'Faild to request with code: {request.status_code}',
                        'more': request.text}
            response = request.json()
        except Exception as e:
            return {'status': 'Faild', 'message': e}
        else:
            # print(response[0]['translations'][0]['text'])
            return {'status': 'Success',  'data': 'VI', 'result': response[0]['translations'][0]['text']}

    # translate CN to EN
    def translateCNtoEN(self, cn_en_text):
        '''
        This function translate CN to EN
        src_text(str): source text (CN language)
        '''
        try:
            params = '&from=zh-Hans&to=en'
            constructed_url = self.service_enpoint + params
            self.body = [{
                'text': f'{cn_en_text}'
            }]
            logging.info('Staring translate chapter')
            request = requests.post(constructed_url,
                                    headers=self.headers, json=self.body)
            if not request.ok:
                return {'status': 'Faild',
                        'message': f'Faild to request with code: {request.status_code}',
                        'more': request.text}
            response = request.json()
        except Exception as e:
            return {'status': 'Faild', 'message': e}
        else:
            return {'status': 'Success', 'data': 'EN', 'result': response[0]['translations'][0]['text']}
    
    # translate EN to VI
    def translateENtoVI(self, src_text):
        '''
        This function translate EN to VI
        src_text(str): source text (EN language)
        '''
        try:
            params = '&from=en&to=vi'
            constructed_url = self.service_enpoint + params
            self.body = [{
                'text': f'{src_text}'
            }]
            logging.info('Staring translate chapter')
            request = requests.post(constructed_url,
                                    headers=self.headers, json=self.body)
            if not request.ok:
                return {'status': 'Faild',
                        'message': f'Faild to request with code: {request.status_code}',
                        'more': request.text}
            response = request.json()
        except Exception as e:
            return {'status': 'Faild', 'message': e}
        else:
            return {'status': 'Success', 'data': 'EN-VI', 'result': response[0]['translations'][0]['text']}

    # translate VietPhrase
    def translateVietPhrase(self, text):
        try:
            chapter_url = 'https://vietphrase.info/Vietphrase/TranslateVietPhraseS'
            payload = {
                "chineseContent": f"{text}"}
            response = requests.post(chapter_url, data=payload)
            logging.info('Staring translate chapter')
            if not response.ok:
                return {'status': 'Faild',
                        'message': f'Faild to request with code: {response.status_code}',
                        'more': response.text}
        except Exception as e:
            return {'status': 'Faild', 'message': e}
        else:
            return {'status': 'Success', 'data': 'vietPhrase', 'result': response.text.replace('\t', '   ')}
    
    # translate HAN VIET
    def translateHanViet(self, text):
        try:
            chapter_url = 'https://vietphrase.info/Vietphrase/TranslateHanViet'
            payload = {
                "chineseContent": f"{text}"}
            response = requests.post(chapter_url, data=payload)
            logging.info('Staring translate chapter')
            if not response.ok:
                return {'status': 'Faild',
                        'message': f'Faild to request with code: {response.status_code}',
                        'more': response.text}
        except Exception as e:
            return {'status': 'Faild', 'message': e}
        else:
            return {'status': 'Success',  'data': 'hanViet','result': response.text.replace('\t', '   ')}
        
from charaters import charaters_name
if __name__ == '__main__':
    translate = Translate(charaters = charaters_name)
    result = translate.translateCNtoVI('''第9章 儿童相见不相识 ''')
    print(result)