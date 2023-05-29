import logging
import requests
import time
from requests_html import HTML
from bs4 import BeautifulSoup
import re
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s : %(message)s')


class AppException(Exception):
    'app exceptions'


def validateURL(url):
    '''
        This function valid URL
    '''
    regex = "^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"
    r = re.compile(regex)
    if (re.search(r, url)):
        return True
    else:
        return False

    # format text


def formatText(data=''):
    data = data.replace('\n', '\n    ')
    return data


class Story():
    '''
    Class Scrawl chapter of story \n
    chapter_url(str): url of story \n
    find_title(str): find chapter title \n
    find_content(str): find chapter content \n
    find_next_chapter(str): find next content \n
    find_prev_chapter(str): find prev content \n
    '''

    # init value
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.chapter_url = kwargs['url'] if 'url' in kwargs else ''
        self.find_title = kwargs['find_title'] if 'find_title' in kwargs else '.j_chapterName'
        self.find_content = kwargs['find_content'] if 'find_content' in kwargs else '.read-content.j_readContent'
        self.find_next_chapter = kwargs['next_chapter'] if 'next_chapter' in kwargs else '#j_chapterNext'
        self.find_prev_chapter = kwargs['prev_chapter'] if 'prev_chapter' in kwargs else '#j_chapterPrev'

    # scrawl chapter HTML

    def scrawlChapterHTML(self):
        try:
            if not self.chapter_url:
                logging.error('URL is emtry. Check your URL')
                return {'status': 'Faild', 'message': 'URL is emtry. Check your URL'}
            if not validateURL(self.chapter_url):
                logging.error('URL is not validate. Check your URL')
                return {'status': 'Faild', 'message': 'URL is not validate. Check your URL'}
            logging.info(f'Stating crawl {self.chapter_url}')
            response = requests.get(self.chapter_url)
            if not response.ok:
                return {'status': 'Faild', 'message': f'Request Faild with status code: {response.status_code}'}
        except Exception as message:
            logging.error('An error when scrawl chapter')
            return {'status': 'Faild', 'message': f'{message}'}
        else:
            logging.info('Success scrawl chapter data')
            return {'status': 'Success', 'result': response.text}

    # scrawl chapter DATA
    def scrawlChapterDATA(self):
        try:
            chapterHTML = self.scrawlChapterHTML()
            if chapterHTML['status'] == 'Faild':
                return {'status': 'Faild', 'message': f'{chapterHTML["message"]}'}
            logging.info('Staring extract data from HTML')
            chapter_html = HTML(html=chapterHTML['result'])

            chapter_title = chapter_html.find(self.find_title, first=True).text
            chapter_content = chapter_html.find(
                self.find_content, first=True).text
            chapter_data = f'''{chapter_title} \n {chapter_content}'''

        except Exception as e:
            logging.error('Someting went wrong while extract data')
            return {'status': 'Faild', 'message': f'{e}'}
        else:
            logging.info('Success extract data from HTML')
            return {'status': 'Success', 'data': 'CN', 'result': formatText(chapter_data)}

    # next chapter
    def handleNextPrevChapter(self):
        try:
            chapterHTML = self.scrawlChapterHTML()
            if chapterHTML['status'] == 'Faild':
                return {'status': 'Faild', 'message': f'{chapterHTML["message"]}'}
            chapter_html = HTML(html=chapterHTML['result'])
            next_chapter = chapter_html.find(
                self.find_next_chapter, first=True).attrs['href']
            prev_chapter = chapter_html.find(
                self.find_prev_chapter, first=True).attrs['href']
        except Exception as e:
            logging.error('Someting went wrong while handle next/prev chapter')
            return {'status': 'Faild', 'message': f'{e}'}
        else:
            logging.info('Success load Next/Prev chapter')
            print('next chapter:', next_chapter)
            return {
                'status': 'Success',
                'result': {
                    'next_chapter': 'https:' + next_chapter,
                    'prev_chapter': 'https:' + prev_chapter
                }
            }

    def nextChapter(self):
        try:
            chapter = self.handleNextPrevChapter()
            if chapter['status'] == 'Faild':
                return {'status': 'Faild', 'message': f'{chapter["message"]}'}
            next_chapter = chapter['result']['next_chapter']
        except Exception as e:
            logging.error('Someting went wrong while handle next chapter')
            return {'status': 'Faild', 'message': f'{e}'}
        else:
            logging.info('Success Next chapter')
            return {
                'status': 'Success', 'isUrl': 'prev_chapter', 'chapter_url': next_chapter}

    def prevChapter(self):
        try:
            chapter = self.handleNextPrevChapter()
            if chapter['status'] == 'Faild':
                return {'status': 'Faild', 'message': f'{chapter["message"]}'}
            prev_chapter = chapter['result']['prev_chapter']
        except Exception as e:
            logging.error('Someting went wrong while handle prev chapter')
            return {'status': 'Faild', 'message': f'{e}'}
        else:
            logging.info('Success Prev chapter')
            return {
                'status': 'Success', 'isUrl': 'next_chapter', 'chapter_url': prev_chapter}


if __name__ == '__main__':
    story = Story(
        url='https://www.qidian.com/chapter/1036506211/747924467/', find_title='.print>h1', find_content='.content')

    result = story.scrawlChapterDATA()

    print(result)
# chapter_url='', find_title='', find_content='', find_next_chapter='', find_prev_chapter=''
