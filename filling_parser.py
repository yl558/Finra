import sys
import os
print(sys.version)
from bs4 import BeautifulSoup

class FillingParser(object):
    def __init__(self):
        return
    def read_html(self, html_file_path):
        if not os.path.exists(html_file_path):
            print("File does not exist.")
            return None
        f = open(html_file_path, 'r', encoding = 'utf-8', errors = 'ignore')
        content = f.read()
        f.close()
        return content
    def get_soup(self, html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup
    def get_annual_fund_operating_expenses_table(self, html_file_path):
        html_doc = self.read_html(html_file_path)
        soup = self.get_soup(html_doc)
        p = soup.find_all('p', string='(expenses that you pay each year as a percentage of the value of your investment)')[0]
        tb = p.next_sibling.next_sibling
        return tb
    def get_total_annual_fund_operating_expenses_summary(self, html_file_path):
        tb = self.get_annual_fund_operating_expenses_table(html_file_path)
        trs = tb.find_all('tr')
        tr_title = trs[0]
        classes = []
        for td in tr_title.find_all('td')[1:]:
            classes.append(td.string.strip())
        tr_summary = trs[-1]
        numbers = []
        for td in tr_summary.find_all('td')[1:]:
            numbers.append(td.string.strip())
        summary = {}
        for i in range(len(classes)):
            summary[classes[i]] = numbers[i]
        return summary

def main():
    webpage_dir = 'webpages'
    html_file_name = 'filing210669862.htm'
    html_file_path = os.path.join(webpage_dir, html_file_name)
    parser = FillingParser()
    print(parser.get_total_annual_fund_operating_expenses_summary(html_file_path))
    return 

if __name__ == '__main__':
    main()
