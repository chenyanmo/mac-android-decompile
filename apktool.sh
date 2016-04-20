#!/bin/bash
source function.sh
function error {
	RED='\033[0;31m'
	NC='\033[0m'
	GREEN='\033[0;32m'
	printf "${RED}error:#命令参数不正确#${GREEN}\n"
	printf "tips:命令列表如下${NC}\n"
	printf "	1.安装      --i apk  \n	2.反编译    --d apk  \n	3.打包      --b 目录  \n	4.签名      --s apk \n"
	printf "	5.反编译dex --ddex dex  \n	6.打包dex   --bdex 目录  \n	7.反编译xml --dxml xml  \n"
	printf "	8.解压file  --uzip file  \n"
	printf "	9.dex to jar --d2j  \n"
	
}

if (( ${#2} <= 1 )); then 
	error
	exit
fi  

if [ "$1" == "--i" ]; then
	echo 正在安装-$2...
	#replace your andriod sdk path here
	~/Desktop/adt-bundle-mac-x86_64-20140702/sdk/platform-tools/adb install -r $2
	exit
fi

if [ "$1" == "--d" ]; then
	echo 正在反编译-$2...
	dir=`getApkName $2`
	rm -rf $dir
	apktool d $2
	exit
fi

if [ "$1" == "--b" ]; then
	echo 正在打包-$2...
	apktool b $2
	exit
fi

if [ "$1" == "--s" ]; then
	echo 正在重新签名-$2...
	sign=`getApkName $2`
	java -jar tools/sign_tool/signapk.jar tools/sign_tool/platform.x509.pem tools/sign_tool/platform.pk8 $2 "$sign.apk"
	exit
fi

if [ "$1" == "--ddex" ]; then
	echo 正在反编译dex-$2...
	rm -rf dexout
	java -jar tools/baksmali.jar -o dexout/ $2
	exit
fi

if [ "$1" == "--bdex" ]; then
	echo 正在打包dex-$2...
	smali dexout/ -o $2
	exit
fi

if [ "$1" == "--dxml" ]; then
	echo 正在反编译xml-$2...
	java  -jar tools/axmlprinter2.jar "$2" > "$2.txt"
	exit
fi

if [ "$1" == "--uzip" ]; then
	echo 正在解压-$2...
	rm -rf $3
	unzip $2 -d $3
	exit
fi

if [ "$1" == "--d2j" ]; then
	echo 正在dex2jar-$2...
	./tools/dex2jar/dex2jar.sh "$2"
	exit
fi

error