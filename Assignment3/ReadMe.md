## Result
+ Sequential Search Time:   86.80(Sec)
+ Sequential Search SNR:    13.14
+ 2D logarithm search Time: 0.096(Sec)
+ 2D logarithm search SNR:  1.185

|           |Time   |SNR    |
| --------- | ----- | ----- |
|Seq Search |86.80  |13.14  |
|2D Search  |0.096  |1.185  |

這次成果發現，2D Search 速度快很多，但是 SNR 卻不及 Sequential Search。再進一步做比較， Sequential Search 的 SNR 約是 2D Search 的 13 倍，但花費時間卻遠大於 13 倍，也就是說，2D Search 考量到時間成本的話，是比較優質的演算法，雖然 SNR 的表現不佳，但花費時間海放 Sequential Search

#### 每一次跑的結果都不一樣，上面數據只取其中一次並有做四捨五入

## 心得與討論
這次作業實作兩種計算 motion vector 的演算法，演算法本身並不難，但過程中遇到不少細節的問題。
例如：numpy array 在傳遞值時是 pass by reference，和一般 list 或 C/C++ 中陣列的 pass by value 的方式不一樣，這讓我花了很多時間才找出問題點。最後使用 np.copy 把第一個 numpy array 的值複製一份到第二個 numpy array。再來是計算 SNR 時，int overflow 的問題。剛開始計算 SNR 時發現值是負數，根據公式，分子分母都有平方所以 SNR 值應該要是正數的才是正確的，進一步檢查發現是數字太大超出範圍造成的。但照理來說，Python3 的 int 是不會有 overflow 問題才對，之後才發現又是 numpy 在作怪，因為 numpy 的 int 和 C/C++ 一樣有大小限制所以 SNR 算到一半就 overflow。現在先把要計算的 numpy array 中的值傳到一個 Python 的 int 變數再做運算即可解決。

## 實作圖
![alt text](/Assignment3/images/report.png "Done")