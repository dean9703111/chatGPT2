import requests
from bs4 import BeautifulSoup
 
url = "https://ithelp.ithome.com.tw/"
# 指定一個 User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 發送請求
res = requests.get(url, headers=headers)
 
# 解析HTML
soup = BeautifulSoup(res.text, "html.parser")
 
# 找到所有文章的標題與連結
titles = soup.find_all("a", class_="qa-list__title-link")
for title in titles:
    print(title.text.strip())  # 列印文章標題
    print(title["href"])  # 列印文章連結