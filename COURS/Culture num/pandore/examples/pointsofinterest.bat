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

rem
rem @(#)pointofinterest.bat
rem 
rem (C)R�gis Clouard - 2006-09-06
rem

set TMPFILE=a.pan b.pan harris_out.pan

echo - Extracting points of interest from image tangram.pan using the Harris detector

   pharris 2 0.04 tangram.pan a.pan
   pbinarization 1e4 1e30 a.pan b.pan
   padd b.pan tangram.pan harris_out.pan
   pvisu harris_out.pan

echo - Extracting points of interest from image tangram.pan using the SUSAN detector

set TMPFILE=%TMPFILE% susan_out.pan

   psusan 20 tangram.pan a.pan
   pbinarization 1000 1e30 a.pan b.pan
   padd b.pan tangram.pan susan_out.pan
   pvisu susan_out.pan
del %TMPFILE%