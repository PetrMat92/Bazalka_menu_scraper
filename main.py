from bs4 import BeautifulSoup
import requests
import textwrap
import smtplib
from email.mime.text import MIMEText


def get_url():
    response = requests.get("https://rozvoz.bazalkahk.cz/jidelnicek/")
    # Parse the HTML content using Beautiful Soup
    doc = BeautifulSoup(response.content, "html.parser")

    # Find the ul element with id "jidelnicek_menu2" and class "filtr"
    ul_tag = doc.find("ul", {"id": "jidelnicek_menu2", "class": "filtr"})

    # Iterate over the a tags within the ul tag and extract their href attributes
    current_menu_url = []
    for a_tag in ul_tag.find_all("a"):
        current_menu_url.append(a_tag.get("href"))
        return current_menu_url


def scrape_menu(url):
    base_url = "https://rozvoz.bazalkahk.cz"
    link = base_url + url[0]
    response = requests.get(link)
    doc = BeautifulSoup(response.text, "html.parser")
    tds = doc.find_all("td", {"class": "tj1"})
    menu = []
    for td in tds:
        a_tags = td.find_all("a")
        for a in a_tags:
            menu.append(a.get("title").strip("\ufeff"))
    return menu


def get_date(url):
    base_url = "https://rozvoz.bazalkahk.cz"
    link = base_url + url[0]
    response = requests.get(link)
    doc = BeautifulSoup(response.text, "html.parser")
    header = doc.find("h1")
    date = header.text.split()[1:4]
    formatted_date = " ".join(date)
    return formatted_date


def send_email(body):
    email_user = "matejicekpetr##@gmail.com"
    email_password = "fir######orlm"
    email_send = "matejicekpetr##@gmail.com"

    msg = MIMEText(body)
    msg["From"] = email_user
    msg["To"] = email_send
    msg["Subject"] = "Daily Menu Update"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_user, email_password)
    server.sendmail(email_user, email_send, msg.as_string())
    server.quit()


def main():
    url = get_url()
    menu = scrape_menu(url)
    date = get_date(url)

    body = (
        f"Menu v jídelně Bazalka ve dne {date}\n\n"
        f"Polévky: {str(menu[0])}; {str(menu[1])}\n\n"
        f"Hlavní chod: {str(menu[2])}; {str(menu[3])}; {str(menu[4])}\n\n"
        f"Hlavní jídlo salát: {str(menu[5])}\n\n"
        f"Hlavní jídlo sladké: {str(menu[6])}\n\n"
        f"////////////////////////////////////////////////////////////////////////\n\n"
        f'Ostatní: {textwrap.fill(" ".join(str(a + ",") for a in menu[6:]), 120)}'
    )

    send_email(body)


if __name__ == "__main__":
    main()
