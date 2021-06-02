# Auto video editing 

[![hackmd-github-sync-badge](https://hackmd.io/saOjw3InQrqCEsWNNmg7cA/badge)](https://hackmd.io/saOjw3InQrqCEsWNNmg7cA)

###### tags: side_project

## Window 10 executable
[google drive link(chinese UI only)](https://drive.google.com/file/d/13UKMS-PCkZP-Kch4iRm0CNrDquCjXBQ2/view?usp=sharing)
## Mac/linux
* python 3.7up
* setuptool
* pyqt5
* pillow
* moviepy

run command  
```=bash
sudo pip install setuptool  
sudo pip install pyqt5
sudo pip install pillow
sudo pip install moviepy
```
execute main.py
```=bash
python ./main.py
```
## How to use (TW)
### Introduction
範例效果：[youtube](https://youtu.be/joYtSd551gg)  
剪輯師：夏多  

這個工具的起源是為了幫助火舞社影記自動化化的剪出如同範例效果的影片，建議觀看範例影片以理解後續說明。  
主要的功能是能一次排程幫複數支影片加上片頭動畫、ICON、以及基本的片頭片尾淡出，以下說明如何使用這個工具以及各項客製化選項。  

執行起main.exe後會跳出黑色命令提示字元是正常現象，請等待3-5秒操作介面會接著跳出來。
### Source video option
![](https://i.imgur.com/qMSroOd.png)
此區是影片毛片的設定區塊
1. 瀏覽檔案並讀入路徑
2. 設定毛片的開始時間與結束時間  
:::warning
影片開頭和結尾都有3秒的淡入淡出，建議設定時間時可以預留幾秒作為淡入淡出
:::

### Animate option
![](https://i.imgur.com/wmQVBwK.png)
此區是開頭動畫的設定區塊
1. 瀏覽檔案並讀入路徑
2. 選擇是否要過濾黑色背景
#### 過濾黑色背景說明：
由於創作片頭動畫特效時經常使用黑色背景，如下圖  
範例影片效果希望是將特效去背後和疊加在定格的開始畫面上，故這裡提供選項可以過濾黑色背景
![](https://i.imgur.com/lgP4kOi.png =320x)  
#### 疊加去背片頭動畫在定格的開始畫面上：
* 法一：可以用黑色背景創作新特效，並打勾選「去除動畫黑色背景」  
(注意，選擇這樣的方式動畫中其他部分不可使用黑色否則會一併過濾掉)
* 法二：創作片頭後就先自行去除背景，不必勾選「去除動畫黑色背景」  
:::warning
透明部分會由用定格的開始畫面補齊，開始畫面是前述開始時間的影格
:::
#### 片頭動畫不需去背：
直接使用不透明片頭動畫，不必勾選「去除動畫黑色背景」

### Icon option
![](https://i.imgur.com/aMvdIDg.png)
此區設定範例影片中左下角的圖標
1. 瀏覽檔案並讀入路徑
2. 設定ICON位置
3. 設定ICON尺寸  
:::warning
若不讀入ICON路徑，預設使用片頭動畫時間點中間的影格作為片頭，會受前點片頭是否有去背影響，建議使用有透明度資訊的PNG作為ICON
:::

### Output option
![](https://i.imgur.com/hyjUhdn.png)
此區設定排程複數影片及輸出
* 當設定好前三部分後點擊新增到處理清單
* 右邊表格可以查看待處理影片的所有設定值
* 若前三部分設定有錯誤可以清除表格後重新新增
* 表格內可以雙擊編輯，但請保持內容格式正確，否則可能出現錯誤
* 當清單全數增加完畢後選擇輸出影片
* 輸出影片後命令提示字元(黑色框框)可以看到個影片的輸出進度
* 文字狀態也會顯使目前處理了幾支影片
## release note
### customer needs V1
* load video
* remove redundant head and tail
* freeze title and add animate
* audio fade in
* add icon on the corner
* fade out video
* write video
* GUI
### V2
* queue video
* custimze icon size & position
* header animate black filter option

## Reference
[pymovie](https://zulko.github.io/moviepy/)  
[pyqt5](https://doc.qt.io/qt-5.15/search-results.html?q=qfiledialog)
