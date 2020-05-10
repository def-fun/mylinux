# 为ubuntu desktop开启VNC

参考 https://www.jianshu.com/p/c5f6300e6671
```shell script
sudo apt-get install x11vnc
x11vnc -storepasswd

Enter VNC password: *********
Verify password: *********
Write password to /home/xx/.vnc/passwd? [y]/n y
Password written to: /home/xx/.vnc/passwd

```
