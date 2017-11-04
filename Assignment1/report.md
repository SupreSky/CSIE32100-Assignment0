# Gray Level

* 原始圖片是 iPhone X

![alt text](https://github.com/SupreSky/MMS2017FALL/blob/master/Assignment1/Application1/Application1/X.png "iPhone X")

* 經過灰階轉換之後的 iPhone X 圖片

![alt text](https://github.com/SupreSky/MMS2017FALL/blob/master/Assignment1/Application1/Application1/GreyX.png "Gray iPhone X")

* Code 的核心部分
```C++
	Mat img;
	img = imread("X.png", 1);			// 讀入原始 iPhone X
	namedWindow("Color", WINDOW_AUTOSIZE);		// 原始圖片放的視窗
	namedWindow("Grey", WINDOW_AUTOSIZE);		// 灰階圖片要放的視窗

	Mat copy(img.rows, img.cols, CV_8UC1);
	for (int i = 0; i < img.rows; i++)
		for (int j = 0; j < img.cols; j++)
			copy.at<uchar>(i, j) = (uchar)((img.at<Vec3b>(i, j)[0] + img.at<Vec3b>(i, j)[1] + img.at<Vec3b>(i, j)[2]) / 3);

	imshow("Color", img);		// 原始 iPhone X
	imshow("Grey", copy);		// 轉換之後的灰階 iPhone X
	imwrite("GreyX.png", copy);	// 儲存灰階 iPhone X
	waitKey(0);
	return 0;
```

# Dithering Algorithm Gray Level

* 原始圖片依然是 iPhone X

![alt text](https://github.com/SupreSky/MMS2017FALL/blob/master/Assignment1/Application1-2/Application1-2/X.png "iPhone X")

* 使用第一個演算法轉換之後的 iPhone X 圖片

![alt text](https://github.com/SupreSky/MMS2017FALL/blob/master/Assignment1/Application1-2/Application1-2/Grey_Algo1.png "Algo1 iPhone X")

* 使用第二個演算法轉換之後的 iPhone X 圖片

![alt text](https://github.com/SupreSky/MMS2017FALL/blob/master/Assignment1/Application1-2/Application1-2/Grey_Algo2.png "Algo2 iPhone X")

* Code 的核心部分

```C++
Mat copy1;
copy1.create(img.rows * 2, img.cols * 2, CV_8U);
for (int i = 0; i < img.rows; i++)
	for (int j = 0; j < img.cols; j++) {
		if (img.at<uchar>(i, j) > 204) {
			copy1.at<uchar>(i * 2, j * 2) = 255;
			copy1.at<uchar>(i * 2, j * 2 + 1) = 255;
			copy1.at<uchar>(i * 2 + 1, j * 2) = 255;
			copy1.at<uchar>(i * 2 + 1, j * 2 + 1) = 255;
		}
		else if (img.at<uchar>(i, j) > 153) {
			copy1.at<uchar>(i * 2, j * 2) = 0;
			copy1.at<uchar>(i * 2, j * 2 + 1) = 255;
			copy1.at<uchar>(i * 2 + 1, j * 2) = 255;
			copy1.at<uchar>(i * 2 + 1, j * 2 + 1) = 255;
		}
		else if (img.at<uchar>(i, j) > 102) {
			copy1.at<uchar>(i * 2, j * 2) = 0;
			copy1.at<uchar>(i * 2, j * 2 + 1) = 255;
			copy1.at<uchar>(i * 2 + 1, j * 2) = 255;
			copy1.at<uchar>(i * 2 + 1, j * 2 + 1) = 0;
		}
		else if (img.at<uchar>(i, j) > 51) {
			copy1.at<uchar>(i * 2, j * 2) = 0;
			copy1.at<uchar>(i * 2, j * 2 + 1) = 0;
			copy1.at<uchar>(i * 2 + 1, j * 2) = 255;
			copy1.at<uchar>(i * 2 + 1, j * 2 + 1) = 0;
		}
		else {
			copy1.at<uchar>(i * 2, j * 2) = 0;
			copy1.at<uchar>(i * 2, j * 2 + 1) = 0;
			copy1.at<uchar>(i * 2 + 1, j * 2) = 0;
			copy1.at<uchar>(i * 2 + 1, j * 2 + 1) = 0;
		}
}
Mat copy2;
copy2.create(img.rows * 4, img.cols * 4, CV_8U);
for (int i = 0; i < img.rows; i++)
	for (int j = 0; j < img.cols; j++)
		for (int pixi = 0; pixi < 4; pixi++)
			for (int pixj = 0; pixj < 4; pixj++) {
				if (img.at<uchar>(i, j) > arr[pixi][pixj])
					copy2.at<uchar>(i * 4 + pixi, j * 4 + pixj) = 255;
				else
					copy2.at<uchar>(i * 4 + pixi, j * 4 + pixj) = 0;
			}
imshow("Grey", img);
imshow("Algo1", copy1);
imshow("Algo2", copy2);
imwrite("Grey_Algo1.png", copy1);
imwrite("Grey_Algo2.png", copy2);
```

# 心得
這份作業並不困難，最難的部分我想應該是安裝環境的部分，VStudio和裡面的路徑設定花了我很多時間。雖然這份報告快要完成了，我依然需要在網路上找 Markdown 的用法，不過也因為這次的練習而更加熟練了。這次作業最有趣的地方反而是這邊，因為 Markdown 還有很多用法比如說 Horizontal Rule 和 Syntax Highlighting，可以讓原本的純文字變得易讀又生動。
