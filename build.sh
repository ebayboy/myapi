#!/bin/bash

# ***************************************************************************
# * 
# * @file:build.sh 
# * @author:ebayboy@163.com 
# * @date:2019-12-24 21:29 
# * @version 1.0  
# * @description: Shell script 
# * @Copyright (c)  all right reserved 
#* 
#**************************************************************************/ 

#export 
pip freeze > requirements.txt

#install 
pip install -r requirements.txt


exit 0

