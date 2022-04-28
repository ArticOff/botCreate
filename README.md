<a href="https://discord.gg/h7YFnP45jv"><img src="https://discord.com/api/guilds/968761964287365120/embed.png" alt="Discord" height="18"></a> <a href="https://badge.fury.io/py/pyfrench"> [![Downloads](https://pepy.tech/badge/botCreate/month)](https://pepy.tech/project/botCreate)
# botCreate

botCreate is a module to create discord bots in python.

## Installing

Type these commands in a command prompt.

```
# Linux/macOS
python3 -m pip install -U botCreate

# Windows
py -3 -m pip install -U botCreate
```

## Examples

### Client
```python
import botCreate

client_type = botCreate.CLIENT

botCreate.create(
    name='my super bot',
    token='Token.example.123456789',
    prefix='!',
    type=client_type,
    launch=True
)
```

### Bot
```python
import botCreate

bot_type = botCreate.BOT

botCreate.create(
    name='my super bot',
    token='Token.example.123456789',
    prefix='!',
    type=bot_type,
    launch=True
)
```

### Sharded bot
```python
import botCreate

sharded_bot_type = botCreate.SHARDED_BOT

botCreate.create(
    name='my super bot',
    token='Token.example.123456789',
    prefix='!',
    type=sharded_bot_type,
    launch=True
)
```
