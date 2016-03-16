#!/bin/bash
echo 正在反编译$1apk...
./apktool.sh --b $1
./apktool.sh --s $1/dist/$1.apk
./apktool.sh --i $1.apk

