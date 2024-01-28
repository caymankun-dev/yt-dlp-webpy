#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.environ["PATH"] = "/usr/local/bin:/usr/bin:/bin"
os.environ["TMPDIR"] = "./tmp/"

import requests
import cgi
import cgitb
import subprocess

# エラーのデバッグ情報を出力する
cgitb.enable()

form = cgi.FieldStorage()

url = 'https://www.youtube.com/watch?v=pgXpM4l_MwI'

# 実際のパスに置き換えてください

yt_dlp_path = "./yt-dlp" 

ffmpeg_path = "./ffmpeg"  

command = [yt_dlp_path , "-o" , "%(title)s-%(id)s.%(ext)s" , "-f" , "22" , "--ffmpeg-location" , ffmpeg_path , url]
result = subprocess.check_output(command, stderr=subprocess.STDOUT)
