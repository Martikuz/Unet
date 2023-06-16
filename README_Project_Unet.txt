******************************************************
		Read Me File
		Project Unet

******************************************************
This project is ment to gain experiences with the Unet
architecture.

Using Python Interpreter 3.8

Log:
------------------------------------------------------

------------------------------------------------------
16.06.2023
	- Starting with Python VENV
	- Modul Installation
		- numpy 1.24.3
		- tensorflow 2.12.0
			-> causes uninstallation of
			   numpy 1.24.3
				-> why?
			   seems to use numpy 1.23.5
			   instead.
	- download and installation of opencv
	  via opencv.org and github 4.7.0
	  double click the downloaded
	  opencv-windows.exe. this create a new
	  folder next to that .exe called opencv

	  copy:
.../opencv/build/x64/vc16/bin/opencv_world470.dll
	  into your projects virtual env directory:
	  in my case something like:
.../01_Unet/venv/Lib/site-packages

	  copy:
.../opencv/build/python/cv2/python-3.8/
cv2.cp38-win_amd64.pyd
	  into the same folder as the previous file:
.../01_Unet/venv/Lib/site-packages

	  the official tutorial names a different path
	  so it might be possible that it varies.
	  the tutorial uses the following path:
.../opencv/build/python/2.7
	  And the files were called:
	  cv2.pyd instead of 
	  cv2.cp38-win_amd64.pyd
	  opencv_world.dll instead of 
	  opencv_world470.dll

	  follow the logic!

	  if the python code

	  import cv2 as cv
	  print( cv.__version__ )

	  outputs the correct version number,
	  it should have worker correctly
------------------------------------------------------
07.06.2023
	- Repository Created
------------------------------------------------------
------------------------------------------------------