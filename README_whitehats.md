## Installation

```
pip install .
```

Now you can use it as a `ctf` command

## Templates

You can specify templates in [ctfcli/templates](ctfcli/templates) directory. After that, you have to reinstall the tool with pip.

You can check where the templates are stored finally with `ctf templates dir`.

## Installing challenges

When you install the challenge for the first time in CTFd you have to use command:
```
python3 -m ctfcli challenge install PATH_TO_FOLDER
```

## Syncing challenges

When you have the challenge installed in your instance, you should use:
```
python3 -m ctfcli challenge sync PATH_TO_FOLDER
```