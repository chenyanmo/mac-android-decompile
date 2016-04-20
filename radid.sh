#!/bin/bash
echo 预处理中....
if (( ${#2} > 3 )); then
perl -pi -e "s/f3cb4d9b/$2/g" $1/com/fy/adsdk/demon/AdConfig.smali
perl -pi -e "s/2014437/$3/g" $1/com/fy/adsdk/demon/AdConfig.smali
cat $1/com/fy/adsdk/demon/AdConfig.smali
fi