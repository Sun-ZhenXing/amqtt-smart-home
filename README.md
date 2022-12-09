# aMQTT Broker/Client + MySQL

- [aMQTT Broker/Client + MySQL](#amqtt-brokerclient--mysql)
  - [安装依赖](#安装依赖)
  - [构建项目](#构建项目)
    - [初始化数据库](#初始化数据库)
    - [运行服务端](#运行服务端)
    - [运行客户端](#运行客户端)
  - [如何生成密码](#如何生成密码)

特征：
- 🚀：全部异步操作，包括网络 I/O 和数据库操作
- 🧲：`uvloop` 接近系统级别的事件循环，比 Node.js 快两倍
- 🍒：YAML 配合 Python 脚本进行可扩展配置
- 🍡：零耦合，极简配置，可以替换为你需要的东西

## 安装依赖

要求 Python >= 3.9。

```bash
pip install -r requirements.txt
```

## 构建项目

### 初始化数据库

在 MySQL 中执行 `resources/mysql-init.sql` 即可。

### 运行服务端

```bash
cd broker
python broker.py
```

### 运行客户端

```bash
cd client
python client.py
```

## 如何生成密码

如果已经安装了 `mosquitto`，可以使用下面的命令生成密码文件

```bash
mosquitto_passwd passwd_file username
```

在 `broker/makepwd/` 文件夹下也提供了一个密码生成器：

```bash
python makepwd.py username password
```
