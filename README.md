#mac 平台下android为apk自动化加入广告脚本
##环境要求
          1.mac os 
          2.java sdk
          3.android sdk
##脚本说明
###tools_build.sh
          安装相关工具
###apktool.sh
          相关工具命令的集合
###方案1 - 反编译
          #### 1.pdg.sh
          1.反编译包
          2.将sdk复制到相关目录
          3.更换广告ID
          #### 2.auto.py
          1.分析AndroidMainest.xml文件
          2.写入application.smali文件oncreate广告入口
          3.写入所有activity文件oncreate广告入口
          #### 3.dg.sh
          2.打包
          3.重新签名
          4.安装
          #### 4.auto.sh
          自动化打包 对前面三个工具的集成
###方案2 - 解压缩
          #### 1.pdg2.sh
          1.解压
          2.将sdk复制到相关目录
          3.更换广告ID
          #### 2.auto2.py
          1.解密AndroidMainest.xml
          2.分析AndroidMainest.xml.txt文件
          3.写入application.smali文件oncreate广告入口
          4.写入所有activity文件oncreate广告入口
          #### 3.dg2.sh
          1.对dexout进行反编译
          2.压缩
          3.重新签名
          4.安装
          #### 4.auto2.sh
          自动化打包 对前面三个工具的集成
##使用方法          
          ./auto.sh apk路径  应用id  广告id
          
  
