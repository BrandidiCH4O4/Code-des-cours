@echo off
set PANDOREHOME=C:\Users\brand\OneDrive\Bureau\pandore
set HOME=%HOMEDRIVE%%HOMEPATH%
echo PANDORE Version 
type "%PANDOREHOME%\version.txt"
echo GREYC-IMAGE @ Caen France
echo. 
set PATH=%PATH%;%PANDOREHOME%\bin
 
prompt Pandore$G 
if not %1x==/Cx cmd /T:1F /k
