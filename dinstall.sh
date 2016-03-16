#!/bin/bash
echo 正在安装当前目录apk...
for filename in *.apk; do
    ./apktool.sh --i $filename
done
