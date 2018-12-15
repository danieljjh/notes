# how to run opencv on pi

## project folder
`/home/pi/project/`

## python env
cv3py3  python3 with opencv3.4

if you can not run workon:
`source ~/.profile`

### picamera

Use Picamera to capture image and video
[Picamera Doc](https://picamera.readthedocs.io/en/latest/quickstart.html)


### opencv python
For object detect 
[Opencv Python](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html)

[Opencv tutorial](https://pythonprogramming.net/loading-images-python-opencv-tutorial/)

https://pythonprogramming.net/self-driving-car-python-plays-gta-v/

autopilot https://wroscoe.github.io/compound-eye-autopilot.html

https://pythonprogramming.net/self-driving-car-python-plays-gta-v/

### mac 上查看 pi camera 视频流

pi 安装 vlc server 
`sudo apt-get install vlc`

启动视频流
`raspivid -o - -w 320 -h 240 -t 9999999 |cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264`

w: 宽度，h 高 , 8554  端口  h264 视频编码

mac, 安装 vlc 播放器
播放地址 rtsp://192.168.0.5:8554/


### pi  webcam  视频流
https://pimylifeup.com/raspberry-pi-webcam-server/


### 设置 pi 自启动服务

https://www.jianshu.com/p/86adb6d5347b

python 脚本 自启动
https://www.embbnux.com/2015/04/12/raspberry_pi_setting_python_script_start_on_boot/


### 在树莓派上轻松实现深度学习目标检测
http://shumeipai.nxez.com/2018/10/05/how-to-easily-detect-objects-with-deep-learning-on-raspberry-pi.html



## system

free  命令  查看内存
htop 查看进程

## 使用 jupyter notebook server 远程调试代码

https://www.techcoil.com/blog/how-to-setup-jupyter-notebook-on-raspberry-pi-3-with-raspbian-stretch-lite-supervisor-and-virtualenv-to-run-python-3-codes/

在 pi 上 运行 `jupyter notebook --ip 0.0.0.0 --port 9999 --no-browser`
在 mac 浏览器上 `http://(raspberrypi 地址):9999/?token=24970c42bb31323ebc6a0258e99dc109145aa3576283cc29`

### jupyter tricks
https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/

on pi run 
`jupyter notebook --ip 0.0.0.0 --port 9999 --no-browser`

