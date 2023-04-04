# Bazalka_menu_scraper

This script fetches the daily menu from the website of a restaurant called Bazalka (https://rozvoz.bazalkahk.cz/jidelnicek/) and sends an email containing the menu to a specified email address.

# Requirements
This script requires the following packages to be installed:

- BeautifulSoup 
- requests 
- textwrap 
- smtplib
- email.mime.text

# Usage

1) Make sure you have the required packages installed.
2) Replace the email addresses in the send_email function with your own email address and the email address you want to send the daily menu to.
3) Run the script using Python.
4) The script will fetch the daily menu from the restaurant's website, scrape the menu data, format it into an email message, and send it to the specified email address. The email message includes the date of the menu and the different items on the menu, including soups, main courses, and other dishes.

Note: This script is specific to the restaurant Bazalka, so it may not work for other restaurants.
