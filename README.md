# ps5-bot
Browser: FireFox, Website: Walmart.com

Seek out the product you want and replace the URL variable in the script to purchase the respective item.

There are a few dependencies, you can install using:
sudo apt install -y python3-pip
pip3 install selenium 
pip3 install webdrivermanager

Usage: python3 playstation.py -u 'user@name.com' -p 'Y0uRp@s%wOrd'

Note: This is NOT configured to be headless, you will see the browser window open. I see this as a good thing in the event the script fails, you can quickly take control and finish the purchase.

