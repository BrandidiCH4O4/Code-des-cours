@@echo off
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

rem
rem @(#)edgedetection1.bat
rem 
rem (C)Régis Clouard - 2006-09-06
rem

set TMPFILE=i1.pan i2.pan i3.pan i4.pan i5.pan i6.pan i7.pan edge.pan

echo - Performing an edge detection based on hysteresis threshold

   pexponentialfiltering 0.7 tangram.pan i1.pan
   pgradient 1 i1.pan i2.pan i3.pan

   pnonmaximasuppression i2.pan i3.pan i4.pan
   ppostthinning i4.pan i5.pan

   pgradientthreshold 0.03 i2.pan
   call pstatus >%TMP%\null
   call pset seuilhaut
   echo %seuilhaut%

   pbinarization %seuilhaut% 1e30 i5.pan i6.pan
   pgradientthreshold 0.2 i2.pan
   call pstatus >%TMP%\null
   call pset seuilbas
   pbinarization %seuilbas% 1e30 i5.pan  i7.pan 
   pgeodesicdilatation 1 1 -1 i6.pan i7.pan edge.pan

   pvisu edge.pan

del %TMPFILE%
