#!/bin/bash
#提取apk名...
function getApkName(){
	IFS='/ ' read -r -a array <<< "$1"
	len="${#array[@]}"
	let idx=$len-1
	IFS='. ' read -r -a array2 <<< "${array[$idx]}"
	len2="${#array2[@]}"
	let idx2=$len2-1
	name=""
	for i in "${!array2[@]}"; do 
		if (( "$i" == 0 )); then
			name="${array2[0]}"
			continue
		fi
 		if (( "$idx2" != "$i" )); then
 			name="${name}.${array2[$i]}"
 		fi
	done
	echo $name
}

function getDexName(){
	dex='classes.dex'
	if (( ${#1} < 1 )); then 
		echo $dex
	else 
		echo $1
	fi
}
