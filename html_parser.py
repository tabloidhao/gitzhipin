from bs4 import BeautifulSoup

class Html_parser(object):
    def parser(self, text):
        if text is None:
            print('抓取内容为空！')
            return None
        soup = BeautifulSoup(text, 'html.parser')
        content = soup.find('div', {'class': 'job-list'}).select('ul > li')

        result = []
        for con in content:
            result.append(self.get_one_company(con))

        return result


    def get_one_company(self, soup):
        try:
            company_soup = soup.find('div', {'class':'info-company'})
            # company name
            com_name = company_soup.find('a').text
            # company desc
            com_desc = company_soup.find('p').text

            primary_soup = soup.find('div', {'class':'info-primary'})
            # job name
            job = primary_soup.find('div', {'class':'job-title'}).text
            # 去除一些不能写入MySQL的编码
            job = ''.join(str(job.split()))
            # salary
            salary = primary_soup.find('span', {'class':'red'}).text
            # 去除一些不能写入MySQL的编码
            salary = ''.join(str(salary.split()))
            # conpany require
            job_require = primary_soup.find('p').text
            # 去除一些不能写入MySQL的编码
            job_require = ''.join(str(job_require.split()))

            return [com_name, job, salary, job_require, com_desc]
        except Exception as err:
            print(err)
            print('网页解析错误')
            return None




