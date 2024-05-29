#Open Github Profile Readme Generator Website
import webbrowser

website_address = "https://rahuldkjain.github.io/gh-profile-readme-generator/"
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open(website_address)
