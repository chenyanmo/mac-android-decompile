#!/bin/bash
echo 预处理中....
source function.sh
dir=`getApkName $1`
dex=`getDexName $4`

./apktool.sh --uzip $1 $dir
mv $dir/$dex $dex
./apktool.sh --ddex $dex
cp -f -R sdk/baidu dexout/com
cp -f -R sdk/fy dexout/com
cp -f sdk/close.png $dir/assets
cp -f -R sdk/biduad_plugin $dir/assets
echo 更新广告ID....
./radid.sh dexout



