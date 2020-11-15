# SphinxでMarkdownを扱う

SphinxでMarkdown扱えるように設定する。  

## 追加インストール

```bash
  poetry add --dev recommonmark
```

## conf.py

```python
  extensions = ['recommonmark']
  source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
  }
```

## 確認

このページはMarkdownで記述。  
うまく表示されてるようなのでOK.
