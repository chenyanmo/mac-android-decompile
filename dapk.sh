#!/bin/bash
echo 正在反编译$1目录apk...
cd $1
for filename in *.apk; do
    ../apktool.sh --d $filename
done
