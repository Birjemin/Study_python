# coding=utf-8
import urllib2
import re


class QsBaiKe:

    def __init__(self):
        self.page_index = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False

    def get_page(self, page_index):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(page_index)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            page_code = response.read().decode('utf-8')
            return page_code
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print "error", e.reason
                return None

    def get_page_items(self, page_index):
        page_code = self.get_page(page_index)
        if not page_code:
            print "page load error"
            return None
        pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</', re.S)
        items = re.findall(pattern, page_code)
        page_stories = []
        for item in items:
            page_stories.append([item[0].strip(), item[1].strip(), item[2].strip()])
        return page_stories

    def load_page(self):
        if self.enable is True:
                page_stories = self.get_page_items(self.page_index)
                if page_stories:
                    self.stories = page_stories
                    self.page_index += 1

    def get_one_story(self, page_stories, page):
        for story in page_stories:
            input_pa = raw_input()
            if input_pa == "Q":
                self.enable = False
                return
            print u"第%d页\t发布人：%s\t 赞：%s\n%s" % (page, story[0], story[2], story[1])

    def start(self):
        print u'正在读取，回车查看，Q退出'
        self.enable = True
        self.load_page()
        now_page = 0
        while self.enable:
            if self.stories:
                now_page += 1
                self.get_one_story(self.stories, now_page)
                self.stories = []
            else:
                self.load_page()

spider = QsBaiKe()
spider.start()
