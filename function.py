# -*- coding: utf-8 -*-
import os
import sys
import shutil
import xml.etree.ElementTree

def getSmaliName(pname,lname):
	if pname not in lname:
		lname = pname+lname
	lnames = lname.split(".")
	sname = lnames[len(lnames)-1]+".smali"
	return sname

def getDir():
	tmp = sys.argv[1].split("/");
	if len(tmp) > 1:
		return tmp[0]
	return ""

def wirteSmaliFileB(path, newpath):
	replacements= {' onCreate()V':' onCreate()V\n    invoke-static {p0}, Lcom/fy/adsdk/demon/AdStartUp;->b(Landroid/content/Context;)V'}
	with open(path) as infile, open(newpath, 'w') as outfile:
    		for line in infile:
       	 		for src, target in replacements.iteritems():
           	 		line = line.replace(src, target)
			outfile.write(line)
	shutil.copy(newpath, path);
	os.remove(newpath)

def wirteSmaliFileC(path, newpath):
	flag = 0;
	with open(path) as infile, open(newpath, 'w') as outfile:
    		for line in infile:
    			if flag == 1:
    				if "return-void" in line:
       	 				flag = 0
           	 			line = line.replace('return-void', 'invoke-static {p0}, Lcom/fy/adsdk/demon/AdStartUp;->c(Landroid/content/Context;)V\n    return-void')
           	 	if " onCreate(Landroid/os/Bundle;)V" in line:
    				flag = 1		
			outfile.write(line)
	shutil.copy(newpath, path);
	os.remove(newpath)

def searchBaseActivity(path):
	with open(path) as infile:
		for line in infile:
			if ".super" in line:
			    print line

def getPath(pname,lname):
	if pname not in lname:
		lname = pname+lname
	lname = lname.replace(".", "/")
	adir = getDir() +"/"+ "smali/"
	path = adir+lname+".smali"
	return path

def getPath2(pname,lname):
	if pname not in lname:
		lname = pname+lname
	lname = lname.replace(".", "/")
	path  = "dexout/"+lname+".smali"
	return path



def run(type):
	#初始化
	activityfilters = ["MainActivity", "BaseActivity", "StartActivity", "WelcomeActivity", "AppActivity"] #过滤哪些开始页面 目的是使广告展现不那么闲人
	androidName     = '{http://schemas.android.com/apk/res/android}name'
	xmlPath         = sys.argv[1]
	atype			= ""
	packageName     = ""
	activityName    = ""
	applicationName = ""
	path            = ""
	newpath         = ""
	activitys	    = list()
	if len(sys.argv) > 2:
		atype = sys.argv[2]

	#获取apk入口信息
	xml.etree.ElementTree.register_namespace('android', "http://schemas.android.com/apk/res/android")
	tree = xml.etree.ElementTree.parse(xmlPath)
	root = tree.getroot()
	packageName = root.attrib["package"];

	application = root.find("application")
	applicationName = application.attrib[androidName]

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
		if name == activityName:
			continue
		if flag:
			activitys.append(name)

	#写入权限和广告相关activity
	if type == 0:
		if atype == "":
			permission = xml.etree.ElementTree.SubElement(root, "uses-permission")
			permission.set('android:name', 'android.permission.SYSTEM_ALERT_WINDOW')

		activity = xml.etree.ElementTree.SubElement(application, "activity")
		activity.set('android:configChanges', 'keyboard|keyboardHidden|orientation')
		activity.set('android:name', 'com.baidu.mobads.AppActivity')
		tree.write(xmlPath, encoding='utf-8', xml_declaration=True)
	
	#相关信息输出
	print "包名:"+packageName
	print "入口:"+applicationName
	print "入口:"+activityName

	#修改入口smali
	if type == 0:
		path = getPath(packageName, applicationName)
	else:
		path = getPath2(packageName, applicationName)
	newpath = getSmaliName(packageName, applicationName)
	try:
		wirteSmaliFileB(path, newpath)
		print("写入"+applicationName)
	except (OSError, IOError) as e:
		print("##"+applicationName+' not found')

	for activity in activitys:
		try:
			if type == 0:
				path = getPath(packageName, activity)
			else:
				path = getPath2(packageName, activity)
			newpath = getSmaliName(packageName, activity)
			wirteSmaliFileC(path, newpath)
			print("写入"+activity)
		except (OSError, IOError) as e:
			print("##"+activity+' not found')
	

	
	
