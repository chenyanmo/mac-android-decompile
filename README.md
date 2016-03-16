#mac 平台下android自动化反编译脚本
##环境要求
          1.mac os 
          2.java sdk
          3.android sdk
##脚本说明
          ### 1.tools_build.sh
          安装相关工具
          ### 2.apktool.sh
          相关工具命令的集合
          ### 3.pdg.sh
          1.反编译包
          2.将sdk复制到相关目录
          3.更换广告ID
          ### 4.auto.py
          1.分析AndroidMainest.xml文件
          2.写入application.smali文件oncreate广告入口
          3.写入所有activity文件oncreate广告入口
          ### 5.dg.sh
          1.打包
          2.重新签名
          3.安装
          
  
