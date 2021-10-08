# mtakagishi

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/) [![Netlify Status](https://api.netlify.com/api/v1/badges/cf669616-af9c-424e-bd66-d00fe89e9420/deploy-status)](https://app.netlify.com/sites/jolly-brown-b98547/deploys)

## M.Takagishi

* IT Enginner
* Japan

## URL

* "https://mtakagishi.tk/"
* "https://jolly-brown-b98547.netlify.app/"

## poetry準備

[poetryは推奨方法でインストール](https://python-poetry.org/docs/#installation)

## install

``` bash
poetry config --list
poetry config virtualenvs.in-project true
poetry install
```

## sphinx build

``` bash
sphinx-build docs/ docs/_build
```

## sphinx-autobuild

``` bash
poetry run poe doc
```

## VSCODEのターミナルをgit bashへ

`terminal.integrated.shell.windows` に "C:\\Program Files\\Git\\bin\\bash.exe" を設定

## proxy

### pip

```ini:$HOME/pip/pip.ini
 [global]
proxy = [user:passwd@]http://proxy:port
```

### shell

```bash
export HTTP_PROXY="http://proxy:port"
export HTTPS_PROXY="http://proxy:port"
```

### git

```bash
git config --global http.proxy http://proxy:port
git config --global https.proxy http://proxy:port
```
