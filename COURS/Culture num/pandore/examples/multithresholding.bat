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
rem @(#)multithreshoding.bat
rem 
rem (C)R�gis Clouard - 2006-09-06
rem

set TMPFILE=weszka.pan deravi.pan chanda.pan fisher.pan contrast.pan histo.pan mass.pan a.pan b.pan c.pan d.pan

echo - Performs tangram.pan segmentation using Weska multithresholding
   pweszka 10 tangram.pan weszka.pan
   pvisu weszka.pan

echo - Performs tangram.pan segmentation using Deravi multithresholding
   pderavi 15 tangram.pan deravi.pan
   pvisu deravi.pan

echo - Performs tangram.pan segmentation using Chanda multithresholding
   pchanda 20 tangram.pan chanda.pan
   pvisu chanda.pan

echo - Performs trangram.pan segmentation using fisher multithresholding
   pfisher 0 2 tangram.pan fisher.pan
   pvisu fisher.pan

echo - Performs trangram.pan segmentation using multithresholding based on contrast
   pgradient 1 tangram.pan a.pan b.pan
   pnonmaximasuppression a.pan b.pan c.pan
   pthresholding 10 1e20 c.pan d.pan
   pcontrastthresholding 2 tangram.pan d.pan contrast.pan
   pvisu contrast.pan


echo - Performs trangram.pan segmentation using histogram thresholding
   phistothresholding 10 tangram.pan histo.pan
   pvisu histo.pan

echo - Performs trangram.pan segmentation using pixel mnass thresholding
   pmassthresholding 86 tangram.pan mass.pan
   pvisu mass.pan

del %TMPFILE%
