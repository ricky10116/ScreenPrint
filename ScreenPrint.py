

"""Python調用windows API實現屏幕截圖"""

import time
import win32gui, win32ui, win32con, win32api

# window_capture("C:\\Users\\rshang\\Desktop\\New folder\\123.jpg")
def window_capture(filename):
    hwnd = 0  # 窗口的編號，0號表示當前活躍窗口
    # 根據窗口句柄獲取窗口的設備上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根據窗口的DC獲取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC創建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 創建bigmap準備保存圖片
    saveBitMap = win32ui.CreateBitmap()
    # 獲取監控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print w,h　　　#圖片大小
    # 為bitmap開闢空間
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，將截圖保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取從左上角（0，0）長寬為（w，h）的圖片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)


beg = time.time()
'''
for i in range(10):
    window_capture("haha.jpg")  # Python調用windows API實現屏幕截圖
end = time.time()
print(end - beg)
'''
''' 使用PIL的ImageGrab模塊 '''
import time
import numpy as np
from PIL import ImageGrab
from PIL import Image
# 每抓取一次屏幕需要的時間約為1s,如果圖像尺寸小一些效率就會高一些
def Print(): 
    beg = time.time()
    debug = False
    for i in range(10):
        img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
        img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
    end = time.time()
    print(end - beg)
    
    # https://stackoverflow.com/questions/2659312/how-do-i-convert-a-numpy-array-to-and-display-an-image/2659371
    img1 = Image.fromarray(img, 'RGB')
    img1.save('my.png')
    #img1.show()
Print()


''' 使用Selenium截圖 '''

from selenium import webdriver
import time

"""
不設定環境變數，直接在程式中指出 chromedriver 的檔案路徑，
接著在 webdriver.Chrome() 函式中帶入檔案路徑。
"""
def capture(url, filename="capture.png"):
    browser = webdriver.Chrome(r"D:\\Python\\chromedriver.exe")
    browser.set_window_size(1200, 900)
    browser.get(url)  # Load page
    browser.execute_script("""
    (function () {
      var y = 0;
      var step = 100;
      window.scroll(0, 0);

      function f() {
        if (y < document.body.scrollHeight) {
          y += step;
          window.scroll(0, y);
          setTimeout(f, 50);
        } else {
          window.scroll(0, 0);
          document.title += "scroll-done";
        }
      }

      setTimeout(f, 1000);
    })();
  """)

    for i in range(30):
        if "scroll-done" in browser.title:
            break
        time.sleep(1)
    beg = time.time()
    for i in range(10):
        browser.save_screenshot(filename)
    end = time.time()
    print(end - beg)
    browser.close()


#capture("https://www.google.com.tw/")  # 使用Selenium截圖