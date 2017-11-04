// Application1-2.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <opencv2/opencv.hpp>
#include <stdio.h>
using namespace cv;
using namespace std;

int main()
{
	int arr[4][4] = { { 15, 127, 31, 159 },{ 191,63,223,95 },{ 47,175,1,143 },{ 239,111,207,79 } }; // color mixing matrix
	Mat img;
	img = imread("X.png", 0);
	namedWindow("Grey", WINDOW_AUTOSIZE);
	namedWindow("Algo1", WINDOW_AUTOSIZE);
	namedWindow("Algo2", WINDOW_AUTOSIZE);
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
	waitKey(0);
    return 0;
}