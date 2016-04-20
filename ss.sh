#!/bin/bash
echo 正在查找字符...
cd $1
grep -lr $2 *

