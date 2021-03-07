from pytest import mark


class UITests:
    def test_can_navigate_to_163(self, chrome_browser):
            chrome_browser.get("http://163.com")

    def test_can_navigate_to_baidu(self,chrome_browser):
            chrome_browser.get("http://www.baidu.com")


    @mark.skip(reason='no webdriver for firefox and edge')
    def test_all_browser(self, all_browser):
        all_browser.get('http://www.baidu.com')