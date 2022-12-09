from yaml import load, Loader

# 数据库 URL
db = 'sqlite:///db.sqlite3'
# MQTT服务器 URL
mqtt_server = 'mqtt://test.mosquitto.org/'


with open('config.yml', 'r', encoding='utf-8') as f:
    config = load(f, Loader=Loader)

globals().update(config)
