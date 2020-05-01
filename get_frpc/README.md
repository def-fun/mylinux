# frpc一键脚本
自动安装frpc并设置为系统服务

## 部署

部署前要先确认`frpc.ini`与`frps.ini`的配置匹配

```shell script
# server
cat payload.tar.gz >> install.sh

# client
wget http://${server_ip}/install.sh
sudo ./install.sh
```


## todo
+ 自动检测机器的ssh端口并修改`/etc/frp/frpc.ini`中的相关配置
