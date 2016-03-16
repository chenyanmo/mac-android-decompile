#!/bin/bash
source function.sh
dir=`getApkName $1`
echo 自动打包中....
./pdg.sh $1 $2 $3
python auto.py $dir/AndroidManifest.xml $4
./dg.sh $dir

