# Assignment 2 Report

## 輸入格式
+ 數字代表音名
+ 減號 "-" 代表第二拍
+ 舉例："5-" 表示 Sol 這個音佔 2 拍

## 流程圖
### 第一部分 SoundGen 流程圖
![SGflow](/Assignment2/images/SGFlowChart.png)
### 第二部分 SoundMod 流程圖
![SMflow](/Assignment2/images/SMFlowChart.png)

## 如何使用
### 第一部分 SoundGen.py 使用方法
+ 前往 SoundGen.py 所在目錄
+ 在命令列輸入
```Bash
python SoundGen.py
```
+ 螢幕上會顯示出歌曲清單，請輸入數字選擇想要的歌曲
+ 最後就會在同目錄下產生 Gen.wav
### 第二部分 SoundMod.py 使用方法
+ 前往 SoundMod.py 所在目錄
+ 在命令列輸入 
```Bash
python SoundMod.py
```
+ 螢幕上會顯示出歌曲清單，請輸入數字選擇想要的歌曲
+ 接著會要求輸入 f，也就是 cos(2 * pi * f * t) 中的 f，
+ 此時請輸入數字 100、500 或 800 以符合題目要求
+ 最後就會在同目錄下產生 Mod.wav

## 成果圖
![Playing](/Assignment2/images/SoundPlaying.png)

## 遇到的問題
在完成這份作業時遇到幾個問題
+ 不知道怎麼做聲音檔案的處理
後來這個問題在網路上查了一下找到了答案，我是 import wave 的 model，
用 wave.open() 做寫入

+ 題目看很久
因為題目說明文件有點長，因此花了一點時間理解內容

+ 在 Frequency Modulation 的地方，無法用輸出的音樂判斷自己的程式有沒有寫對
因為做了 Fourier transforms，轉換過的音樂已經和原本轉換前有明顯的差異，
但是因為沒有聽過這種「特別」的音樂，所以沒有辦法得知這得輸出是正確與否。

+ 輸出的音樂有「Taktak」的聲響
這個問題到現在依然沒有想到辦法解決。在輸出的音樂會有不該出現的爆音聲，
我有 plot 過聲波圖，看起來並沒有異狀。希望老師或其他同學多多指教。
目前推測有可能是因為第一個音的結尾的聲波和第二個音的結尾的聲波
中間是不連續的，下面的圖片是一個例子
![Playing](/Assignment2/images/MaybeSquareWave.png)
兩個聲波中間因為插入一個 1 Hz 當作分隔音，因此第一個聲波結束後會迅速跳到
1 Hz 聲波的開始，1 Hz 聲波的結束後會迅速跳到第二個音的開始。

## 總結與心得
這次作業花了很多時間完成，初步估計有 18 小時，大部分時間花在 sine 波的產生
與聲音的細微調整，雖然還有很多地方不盡完美，但是應該可以用這個作業為基礎，
做出功能更多的聲音合成器。Frequency Modulation 的部分很有趣，乘上不同的參數，
就會有不同的聲音，有時候甚至會覺得是外星音樂！？
目前希望能增加更多音樂，但是礙於目前功能和能產生的音符數目有點少，
能新增的音樂也有所限制。