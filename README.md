# Demo (GitHub Pages)

https://nayu7u.github.io/

# Memo
0byteのファイルを削除（cutのcオプションの数字は環境依存）

```shell
ls -l images | grep " 0 " | cut -c 46- | xargs -I{} rm images/
```

Vectorize

```shell
docker compose exec python python3 vectorize.py
```
