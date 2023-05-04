# Ch10	請 ChatGPT 教我們用 Python 撰寫網路爬蟲

### 10.1 詢問適合撰寫網路爬蟲的程式語言

`我想要開發爬蟲程式，請推薦幾個程式語言。`  

`我是個初學者，想用 Python 開發，要如何建立開發環境。`  

### 10.2 撰寫第一支爬蟲程式

iT 邦幫忙: https://ithelp.ithome.com.tw/

`如果要爬蟲 https://ithelp.ithome.com.tw/ 的文章標題與連結，程式怎麼寫？`

```py
import requests
from bs4 import BeautifulSoup
 
# 發送請求
url = "https://ithelp.ithome.com.tw/"
res = requests.get(url)
 
# 解析HTML
soup = BeautifulSoup(res.text, "html.parser")
 
# 找到所有文章的標題與連結
titles = soup.find_all("a", class_="qa-list__title-link")
for title in titles:
    print(title.text.strip())  # 列印文章標題
    print(title["href"])  # 列印文章連結
```

`如何確認我爬蟲網站的合法性和隱私保護？`

```
網站的 robots.txt 顯示如下，這是可以爬蟲的意思嗎？
User-agent: *
Disallow:
```

### 10.3 指令不存在？程式沒反應？

- macOS
    ```
    pip3 install requests beautifulsoup4
    python3 crawler.py
    ```
- Windows
    ```
    pip install requests beautifulsoup4
    python crawler.py
    ```

`我執行程式後沒有得到結果，也沒錯誤訊息，是什麼地方出問題了嗎？`

```py
import requests
from bs4 import BeautifulSoup
 
# 發送請求
url = "https://ithelp.ithome.com.tw/"
res = requests.get(url)
print(res.text)  # 確認是否成功取得網頁
 
# 解析HTML
soup = BeautifulSoup(res.text, "html.parser")
 
# 找到所有文章的標題與連結
titles = soup.find_all("a", class_="qa-list__title-link")
for title in titles:
    print(title.text.strip())  # 列印文章標題
    print(title["href"])  # 列印文章連結
```

```
我印出了如下訊息：
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
</body>
</html>
```

`要如何在原有程式中加入 User-Agent 呢？`


```py
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
```
