# 编译与配置
安装
```shell script
sudo apt install -y libxml2-dev libcppunit-dev autoconf automake autotools-dev autopoint libtool \
   nettle-dev libgmp-dev libssh2-1-dev libc-ares-dev libxml2-dev zlib1g-dev \
  libsqlite3-dev pkg-config libgpg-error-dev libgcrypt-dev libssl-dev libexpat1-dev
wget https://github.com/aria2/aria2/archive/release-1.35.0.zip -O aria2-release-1.35.0.zip
unzip aria2-release-1.35.0.zip
cd aria2-release-1.35.0/
autoconf -i
# autoreconf --install
./configure
make
sudo make install
```

配置
```shell script
mkdir -p ".aria2" && touch .aria2/aria2.session
```