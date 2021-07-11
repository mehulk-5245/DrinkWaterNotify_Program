import time
from plyer import notification

if __name__ == "__main__":
    timm = int(input("Enter the minutes that at what interval do you want notification : "))
    while(True):
        notification.notify(
            title = "Please Drink Water Now!!",
            message = "Experts say that you should drink at least eight glasses of water every day; a glass of water is about 8 ounces US or about.236 milliliters.",
            #app_icon = "D:\\Python Codes\\icon.ico",
            timeout=10
        )
        time.sleep(timm*60)
