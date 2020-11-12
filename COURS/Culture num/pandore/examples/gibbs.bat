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
rem @(#)gibbs.bat
rem 
rem (C)Ludovic Soltys -  02-02-2003
rem

set TMPFILE=a.pan b.pan c.pan d1.pan d2.pan d3.pan d4.pan e2.pan e3.pan e4.pan f.pan gibbsout.pan


echo - Building a synthetic image to illustrate the Gibbs phenomenon in wavelets analysis

pshapedesign 256 256 0 2 150 150 a.pan
pvisu a.pan
pqmf daubechies 4 b.pan
pdwt 1 a.pan b.pan c.pan
psplitimage c.pan d1.pan d2.pan d3.pan d4.pan
pthresholding 20 400 d2.pan e2.pan
pthresholding 20 400 d3.pan e3.pan
pthresholding 20 400 d4.pan e4.pan
pmergeimages d1.pan e2.pan e3.pan e4.pan f.pan
pidwt 1 f.pan b.pan gibbsout.pan
pvisu gibbsout.pan

del %TMPFILE%
