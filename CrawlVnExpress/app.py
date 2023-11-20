import requests
from bs4 import BeautifulSoup


url = "https://vnexpress.net/bong-da/champions-league"
token = "6961893297:AAG0KpeoBVQJmyByBOmhg4QpP8Zvv3j8xXc"
chat_id = -4097991853


def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tags_h2 = soup.find_all("h2", class_="title-news")

    title_list = []
    url_list = []
    for tag_h2 in tags_h2:
        title = tag_h2.text
        title_list.append(title)
        tags_a = tag_h2.find_all('a', href=True)
        for tag_a in tags_a:
            url_post = tag_a['href']
            url_list.append(url_post)

    dict_data = {"Title": title_list,
                 "Url": url_list}
    return dict_data


def send_message(token, chat_id, func):

    try:
        dict_data = func()
        for title, url in dict_data.items():

            # Gửi vào group Telegram theo từng cặp Title + URL của bài báo
            urlPost = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={title}\n{url}"
            requests.post(urlPost)

    except Exception as e:
        urlPost = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={e}"
        requests.post(urlPost)


send_message(token, chat_id, (get_data(url)))
