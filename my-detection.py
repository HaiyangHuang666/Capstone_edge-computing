#!/usr/bin/python3
#
# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE
import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
display = jetson.utils.videoOutput("display://0")
while display.IsStreaming():

	img = jetson.utils.loadImage("/home/nvidia/Desktop/cat4.jpg")
	
	if img is None:
		print("cannot load image")
	
	else:
		detections = net.Detect(img)
		
	for detection in detections:
		class_id = detection.Class_ID
		confidence = detection.Confidence
		left = detection.Left
		top = detection.Top
		right = detection.Right
		bottom = detection.Bottom
		width = detection.Width
		height = detection.Height
		area = detection.Area
		center_x = detection.Center[0]
		center_y = detection.Center[1]

		print(f"Class ID: {class_id}")
		print(f"Confidence: {confidence:.2f}")
		print(f"Left: {left:.2f}, Top: {top:.2f}, Right: {right:.2f}, Bottom: {bottom:.2f}")
		print(f"Wigth: {width:.2f}, Height: {height:.2f}, Area: {area:.2f}")
		print(f"Center: {center_x:.2f}, center: {center_y:.2f}")
	
	display.Render(img)
	display.SetStatus("Detecting objects...")