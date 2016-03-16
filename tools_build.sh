#!/bin/bash
echo 正在安装相关工具...

function existCommond(){
	if hash $1 2>/dev/null; then
        echo "True"
    else
        echo "False"
    fi
}

if [ `existCommond brew` == "False" ]; then
	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

if [ `existCommond apktool` == "False" ]; then
	brew install apktool
fi

if [ `existCommond smali` == "False" ]; then
	curl -o tools/smali.jar https://bitbucket.org/JesusFreke/smali/downloads/smali-2.1.1.jar
fi

if [ `existCommond baksmali` == "False" ]; then
	curl -o tools/baksmali.jar https://bitbucket.org/JesusFreke/smali/downloads/baksmali-2.1.1.jar
fi

