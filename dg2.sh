#!/bin/bash
echo 正在反编译apk...
./apktool.sh --bdex $1
rm -f $2/$1
mv -f $1 $2
cd $2
zip -r deapk.zip ./*
cd ..
./apktool.sh --s $2/deapk.zip
rm -rf $2/deapk.zip
mv deapk.apk $2.apk
./apktool.sh --i $2.apk

