import random
import time


def delay_1_5():
    time.sleep(random.randint(1, 5))


g_url = "https://www.google.com/"

wiki_loc = '//a[@href="https://www.wikipedia.org/"]'

wiki_link = "https://www.wikipedia.org/"

logo_loc = "central-featured"


heading_loc = "//h1//span[contains(text(), 'Wikipedia')]"

sb_loc = "searchInput"

b_heading_loc = '//span[@class = "mw-page-title-main"]'

b_pic_loc = '//img[@alt = "Loaves of bread in a basket"]'



