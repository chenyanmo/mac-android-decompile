#!/bin/bash
echo 预处理中....
source function.sh

dir=`getApkName $1`

./apktool.sh --d $1
cp -f -R sdk/baidu $dir/smali/com
cp -f -R sdk/fy $dir/smali/com
cp -f sdk/close.png $dir/assets
cp -f -R sdk/biduad_plugin $dir/assets
./radid.sh $dir/smali
