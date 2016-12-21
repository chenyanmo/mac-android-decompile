# -*- coding: utf-8 -*-
import os
import sys
import shutil
import xml.etree.ElementTree

reload(sys)
sys.setdefaultencoding('utf8')
def getSmaliName(pname,lname):
	lnames = lname.split(".")
	sname = lnames[len(lnames)-1]+".smali"
	return sname

def getDir():
	tmp = sys.argv[1].split("/");
	if len(tmp) > 1:
		return tmp[0]
	return ""


def wirteSmaliFileA(path, newpath):
	flag = 0
	try:
		with open(path) as infile, open(newpath, 'w') as outfile:
    			for line in infile:
    				if flag == 1:
    					if "return-void" in line:
       	 					flag = 0
           	 				line = line.replace('return-void', 'invoke-static {p0}, Lcom/fy/adsdk/demon/AdStartUp;->a(Landroid/content/Context;)V\n    invoke-static {p0}, Lcom/fy/adsdk/demon/AdStartUp;->c(Landroid/content/Context;)V\n    return-void')
           	 		if " onCreate()V" in line:
    					line = line.replace(' onCreate()V', ' onCreate()V \ninvoke-static {p0}, Lcom/fy/adsdk/demon/AdStartUp;->a(Landroid/content/Context;)V\ninvoke-static {p0}, Lcom/fy/adsdk/demon/AdStartUp;->c(Landroid/content/Context;)V\n')		
				outfile.write(line)
		shutil.copy(newpath, path);
		os.remove(newpath)
	except (IOError) as e:
		if "_classes2" not in path:
			path = path.replace("smali", "smali_classes2");
			wirteSmaliFileA(path, newpath)

def wirteSmaliFileB(path, newpath):
	flag = 0
	try:
		with open(path) as infile, open(newpath, 'w') as outfile:
    			for line in infile:
    				if flag == 1:
    					if "return-void" in line:
       	 					flag = 0
           	 				line = line.replace('return-void', 'invoke-static {p0}, Lcom/fy/adsdk/demon/AdStartUp;->b(Landroid/content/Context;)V\n    return-void')
           	 		if " onCreate(Landroid/os/Bundle;)V" in line:
    					flag = 1		
				outfile.write(line)
		shutil.copy(newpath, path);
		os.remove(newpath)
	except (IOError) as e:
		if "_classes2" not in path:
			path = path.replace("smali", "smali_classes2");
			wirteSmaliFileB(path, newpath)

def searchBaseActivity(path):
	with open(path) as infile:
		for line in infile:
			if ".super" in line:
			    print line

def getPath(pname,lname):
	if len(lname.split(".")) <= 2:
		lname = pname+lname
	lname = lname.replace(".", "/")
	adir = getDir() +"/"+ "smali/"
	path = adir+lname+".smali"
	return path

def getPath2(pname,lname):
	if len(lname.split(".")) <= 2:
		lname = pname+lname
	lname = lname.replace(".", "/")
	path  = "dexout/"+lname+".smali"
	return path

def replace():
	bdadappid       = sys.argv[2]
	bdadapplaceid   = sys.argv[3]
	# ggappid		    = sys.argv[4]
	# ggplaceid		= sys.argv[5]
	bdadConfigFile    = getDir() +"/"+ "smali/com/fy/adsdk/demon/AdConfig.smali"
	newbdadConfigFile = "AdConfig.smali"
	with open(bdadConfigFile) as infile, open(newbdadConfigFile, 'w') as outfile:
    			for line in infile:
					if "f61f619d" in line:
						line = line.replace('f61f619d', bdadappid)
					if "2432165" in line:
						line = line.replace('2432165', bdadapplaceid)	
					outfile.write(line)
	shutil.copy(newbdadConfigFile, bdadConfigFile)
	os.remove(newbdadConfigFile)
	# ggadConfigFile = getDir() +"/"+ "smali/com/fy/adsdk/demon/AdViewHelper$GGAdConfig.smali"
	# newggadConfigFile = "AdViewHelper$GGAdConfig.smali"
	# with open(ggadConfigFile) as infile, open(newggadConfigFile, 'w') as outfile:
 #    			for line in infile:
	# 				if "ca-app-pub-1901262708733387~3662027350" in line:
	# 					line = line.replace('ca-app-pub-1901262708733387~3662027350', ggappid)
	# 				if "ca-app-pub-1901262708733387/5138760559" in line:
	# 					line = line.replace('ca-app-pub-1901262708733387/5138760559', ggplaceid)	
	# 				outfile.write(line)
	# shutil.copy(newggadConfigFile, ggadConfigFile)
	# os.remove(newggadConfigFile)

def run(type):
	#初始化
	activityfilters = ["EnvSettingActivity", "ActivityFileList"] #过滤哪些开始页面 目的是使广告展现不那么闲人
	androidName     = '{http://schemas.android.com/apk/res/android}name'
	androidIcon     = '{http://schemas.android.com/apk/res/android}icon'
	xmlPath         = sys.argv[1]
	packageName     = ""
	activityName    = ""
	applicationName = ""
	path            = ""
	newpath         = ""
	baiduTJChannel     = ""
	activitys	    = list()
	if len(sys.argv) > 2:
		baiduTJChannel = sys.argv[4]
	else:
		baiduTJChannel = "common"
	#获取apk入口信息
	xml.etree.ElementTree.register_namespace('android', "http://schemas.android.com/apk/res/android")
	tree = xml.etree.ElementTree.parse(xmlPath)
	root = tree.getroot()

	packageName = root.attrib["package"];
	application = root.find("application")
	try:
		applicationName = application.attrib[androidName]
	except (KeyError) as e:
		print("##applicationName Not Found")
	
	for activity in application.findall("activity"):
		for ifilter in activity.findall("intent-filter"):
			for category in ifilter.findall("category"):
				if ( category.attrib[androidName] == "android.intent.category.LAUNCHER" ):
					activityName =  activity.attrib[androidName]
					break
		name = activity.attrib[androidName];
		flag = True
		for filterName in activityfilters:
			if filterName in name:
				flag = False
				break
		if packageName not in name:
			continue
		if name == activityName:
			continue
		if flag:
			activitys.append(name)


	#写入权限和广告相关activity
	if type == 0:
		if applicationName == "" :
			application.set("android:name", "com.fy.adsdk.demon.APP");
		else:
			path = getPath(packageName, applicationName)
			newpath = getSmaliName(packageName, applicationName)
			wirteSmaliFileA(path, newpath)

		permission = xml.etree.ElementTree.SubElement(root, "uses-permission")
		permission.set('android:name', 'android.permission.SYSTEM_ALERT_WINDOW')

		permission2 = xml.etree.ElementTree.SubElement(root, "uses-permission")
		permission2.set('android:name', 'android.permission.GET_TASKS')

		permission3 = xml.etree.ElementTree.SubElement(root, "uses-permission")
		permission3.set('android:name', 'android.permission.READ_PHONE_STATE')

		permission4 = xml.etree.ElementTree.SubElement(root, "uses-permission")
		permission4.set('android:name', 'android.permission.ACCESS_NETWORK_STATE')

		permission5 = xml.etree.ElementTree.SubElement(root, "uses-permission")
		permission5.set('android:name', 'android.permission.ACCESS_COARSE_LOCATION')
			
		permission6 = xml.etree.ElementTree.SubElement(root, "uses-permission")
		permission6.set('android:name', 'android.permission.WRITE_EXTERNAL_STORAGE')

		permission7 = xml.etree.ElementTree.SubElement(root, "uses-permission")
		permission7.set('android:name', 'android.permission.READ_EXTERNAL_STORAGE')

		permission8 = xml.etree.ElementTree.SubElement(root, "uses-permission")
		permission8.set('android:name', 'com.android.launcher.permission.INSTALL_SHORTCUT')

		permission9 = xml.etree.ElementTree.SubElement(root, "uses-permission")
		permission9.set('android:name', 'com.android.launcher.permission.UNINSTALL_SHORTCUT')

		service = xml.etree.ElementTree.SubElement(application, "service")
		service.set('android:name', 'com.fy.adsdk.demon.AdDaemonService')
		service.set('android:icon', application.attrib[androidIcon])

		service2 = xml.etree.ElementTree.SubElement(application, "service")
		service2.set('android:name', 'com.fy.adsdk.demon.AdDownloadService')
		service2.set('android:icon', application.attrib[androidIcon])
		service2.set('android:process', ":AdDownloadService")

		meta_appkey = xml.etree.ElementTree.SubElement(application, "meta-data")
		meta_appkey.set('android:name', 'BaiduMobAd_STAT_ID')
		meta_appkey.set('android:value', 'ec07844ed5')

		meta_channel = xml.etree.ElementTree.SubElement(application, "meta-data")
		meta_channel.set('android:name', 'BaiduMobAd_CHANNEL')
		print "渠道号:"+ baiduTJChannel
		meta_channel.set('android:value', baiduTJChannel)

		# meta_google_service = xml.etree.ElementTree.SubElement(application, "meta-data")
		# meta_google_service.set('android:name', 'com.google.android.gms.version')
		# meta_google_service.set('android:value', '7895000')

		# activity_google_ad = xml.etree.ElementTree.SubElement(application, "activity")
		# activity_google_ad.set('android:configChanges', 'keyboard|keyboardHidden|orientation|screenLayout|screenSize|smallestScreenSize|uiMode')
		# activity_google_ad.set('android:name', 'com.google.android.gms.ads.AdActivity')
		# activity_google_ad.set('android:theme', '@android:style/Theme.Translucent')
		
		tree.write(xmlPath, encoding='utf-8', xml_declaration=True)
	else:
		if applicationName == "" :	
			path = getPath2(packageName, applicationName)
			newpath = getSmaliName(packageName, applicationName)
			wirteSmaliFileA(path, newpath)

	replace()		
	#相关信息输出
	print "包名:"+packageName
	print "入口:"+applicationName
	print "入口:"+activityName

	# #修改入口smali	
	# for activity in activitys:
	# 	try:
	# 		if type == 0:
	# 			path = getPath(packageName, activity)
	# 		else:
	# 			path = getPath2(packageName, activity)
	# 		newpath = getSmaliName(packageName, activity)
	# 		wirteSmaliFileB(path, newpath)
	# 		print("写入"+activity)
	# 	except (OSError, IOError) as e:
	# 		print("##"+activity+' not found')
	

	
	
