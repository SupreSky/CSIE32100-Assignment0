// Application1.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <opencv2/opencv.hpp>
#include <iostream>
#include <stdio.h>

using namespace cv;
using namespace std;

int main()
{
	Mat img;
	img = imread("X.png", 1);
	namedWindow("Color", WINDOW_AUTOSIZE);
	namedWindow("Grey", WINDOW_AUTOSIZE);

	Mat copy(img.rows, img.cols, CV_8UC1);

	for (int i = 0; i < img.rows; i++)
		for (int j = 0; j < img.cols; j++)
			copy.at<uchar>(i, j) = (uchar)((img.at<Vec3b>(i, j)[0] + img.at<Vec3b>(i, j)[1] + img.at<Vec3b>(i, j)[2]) / 3);

	imshow("Color", img);
	imshow("Grey", copy);
	imwrite("GreyX.png", copy);
	waitKey(0);
	return 0;
}

