@echo off
rem
rem Copyright (c) 2013, GREYC.
rem All rights reserved
rem
rem You may use this file under the terms of the BSD license as follows:
rem
rem "Redistribution and use in source and binary forms, with or without
rem modification, are permitted provided that the following conditions are
rem met:
rem   * Redistributions of source code must retain the above copyright
rem     notice, this list of conditions and the following disclaimer.
rem   * Redistributions in binary form must reproduce the above copyright
rem     notice, this list of conditions and the following disclaimer in
rem     the documentation and/or other materials provided with the
rem     distribution.
rem   * Neither the name of the GREYC, nor the name of its
rem     contributors may be used to endorse or promote products
rem     derived from this software without specific prior written
rem     permission.
rem
rem THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
rem "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
rem LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
rem A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
rem OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
rem SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
rem LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
rem DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
rem THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
rem (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
rem OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
rem
rem For more information, refer to:
rem https://clouard.users.greyc.fr/Pandore/
rem

rem   @(#)configure-vc2005Express.bat

rem
rem   @(#)configure-binary.bat
rem 
rem @author Régis Clouard - 2004-07-01
rem @author Régis Clouard - 2005-08-08 (+ qt)
rem 


rem   *** Set the VCHOME with the convenient Visual C++ home.
rem   *** ex set VCHOME=C:\Program Files\Microsoft Visual Studio\VC98\
set VCHOME=

set CPP=cl
set CPPFLAGS=/nologo /MT /W3 /GR /GX /O2 /D "MAIN" /D "WIN32" /D "NDEBUG" /D "_CONSOLE" /YX /FD /c /Iinclude
set CPPFLAGSOBJ=
set CPPFLAGSOP=/I.\src\operatorsP0

set LD=link
set LDFLAGSLIB=-lib /nologo
set LDFLAGSOP= /nologo /subsystem:console /incremental:no /machine:I386 /LIBPATH:lib pandore.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib

set MAKE=nmake




















cls

rem Pandore directory
set PANDOREHOME=%cd%

set HOME=%HOMEDRIVE%%HOMEPATH%

rem *******************  BINARY VERSION
set tarball=Binary
echo.
echo Installation of the binary version
echo ----------------------------------
echo.

rem ----------------------------------------------------------------------
rem    Generate pandore script
echo generating pandore script ...
call :script_prologue
echo set PATH=%%PATH%%;%%PANDOREHOME%%\bin>>.\pandore.bat
call :script_epilogue
goto :summary

:script_prologue
rem common file header
echo @echo off> .\pandore.bat
echo set PANDOREHOME=%PANDOREHOME%>> .\pandore.bat
echo set HOME=%%HOMEDRIVE%%%%HOMEPATH%%>> .\pandore.bat
echo echo PANDORE Version >>.\pandore.bat
echo type "%%PANDOREHOME%%\version.txt">>.\pandore.bat
echo echo GREYC-IMAGE @ Caen France>>.\pandore.bat
echo echo. >>.\pandore.bat
goto :EOF

:script_epilogue
echo. >>.\pandore.bat
echo prompt Pandore$G >>.\pandore.bat
echo if not %%1x==/Cx cmd /T:1F /k>>.\pandore.bat
goto :EOF

:summary
echo.
echo SUMMARY
echo.
echo    Version of Pandore: %tarball%
echo    Local installation of Pandore in: %PANDOREHOME%
echo    User directory is: %HOME%
echo.
if "%tarball%" neq "developer" goto :end
echo    Microsoft Visual Directory is: %VCHOME%
echo    C++ compiler is: %CPP%.exe
echo    Linker is: %LD%.exe
echo    Make is : %MAKE%.exe
echo.
echo If this is correct, you can just launch the 'install' script.

:end
pause
