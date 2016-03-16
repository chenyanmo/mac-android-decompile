#!/bin/bash
source function.sh
dir=`getApkName $1`
dex=`getDexName $4`
echo 自动打包中....
./pdg2.sh $1 $2 $3 $4
./apktool.sh --dxml $dir/AndroidManifest.xml
python auto2.py $dir/AndroidManifest.xml.txt $5
./dg2.sh $dex $dir
