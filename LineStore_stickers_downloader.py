import requests
from bs4 import BeautifulSoup
import shutil
import os
from time import sleep

def sticker_downloader(url, sticker_name):
    os.chdir("D:\Download\期末報告")
    fpath = os.getcwd()

    # url = 'https://store.line.me/stickershop/product/1316911'

    r = requests.get(url)  
    soup = BeautifulSoup(r.text, "html.parser")

    find_ul_span = soup.find_all('div', class_="mdCMN09LiInner FnImage")
    # find_ul_span = soup.find_all('div', class_="mdCMN09LiInner FnImage", limit=5)

    count = 0
    list_url = []
    for each in find_ul_span:

        url_get = each.select_one("span").get("style")

        url_get = url_get[url_get.find("(")+1 : url_get.find(";")]
        # print(url_get)
        # print(type(url_get))
        list_url.append(url_get)
        count += 1


    # print(f"count = {count}")
    # print(list_url)


    ########
    # 下載 #
    fpath += "\\stickers"
    # sticker_name = "很誠懇的一組貼圖"

    # 創建資料夾 #
    os.chdir(r"D:\Download\期末報告\stickers")
    found = os.listdir(fpath)
    if sticker_name not in found:
        os.mkdir(sticker_name)
        print("成功創建資料夾{}".format(sticker_name))

    save_path = fpath + "\\" + sticker_name + "\\"
    num = 1

    for each in list_url:
        with requests.get(each, stream=True) as response:
        
            file_name = save_path + sticker_name + "_" + str(num) + "_" + ".png"

            file = open(file_name, 'wb')
            shutil.copyfileobj(response.raw, file)
            file.close()
            print(f"file {num} Saved!")

            num += 1

if __name__ == '__main__':
    
    url = input("請輸入url:")
    sticker_name = input("請輸入sticker_name:")

    sticker_downloader(url, sticker_name)
