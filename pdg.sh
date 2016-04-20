#!/bin/bash
echo 预处理中....
source function.sh

dir=`getApkName $1`

./apktool.sh --d $1

smali="smali"
if [ -d "${dir}/smali_classes2" ]; then
	smali="smali_classes2"
fi
cp -f -R sdk/baidu $dir/$smali/com
cp -f -R sdk/fy $dir/$smali/com
cp -f sdk/close.png $dir/assets
cp -f -R sdk/biduad_plugin $dir/assets
./radid.sh $dir/$smali $2 $3
