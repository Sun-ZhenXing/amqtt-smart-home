from yaml import load, Loader

broker_config = {
    'listeners': {
        'default': {
            'max-connections': 1000,
            'type': 'tcp'
        },
        'my-tcp': {
            'bind': '0.0.0.0:1883'
        },
        'my-ws': {
            'bind': '0.0.0.0:8083',
            'type': 'ws'
        }
    }
}

with open('config.yml', 'r', encoding='utf-8') as f:
    broker_config.update(load(f, Loader=Loader))
