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
rem @(#)frequency.sh
rem 
rem (C)Régis Clouard - 2006-09-06
rem

set TMPFILE=square.pan empty.pan real.pan imaginary.pan modulus.pan phase.pan square1.pan empty1.pan square2.pan outsquare.pan i1.pan i2.pan i3.pan i4.pan i5.pan i6.pan i7.pan i8.pan

echo - Converting a white square from spatial domain to frequency domain and reciproquely

   pshapedesign 256 256 0 2 20 0 square.pan
   pshapedesign 256 256 0 0  0 0 empty.pan
   pfft square.pan empty.pan real.pan imaginary.pan
   pmodulus real.pan imaginary.pan modulus.pan
   pphase real.pan imaginary.pan phase.pan
   pifft real.pan imaginary.pan square1.pan empty1.pan
   plineartransform 0 0 255 square1.pan square2.pan
   pim2uc square2.pan outsquare.pan
   pvisu outsquare.pan

echo - Performing Butterworth lowpass filtering on tangram.pan
   psetcst 0 tangram.pan i1.pan
   pfft tangram.pan i1.pan i2.pan i3.pan
   pbutterworthfilter 256 256 0 0 0 50 2 i4.pan
   pmult i2.pan i4.pan i5.pan
   pmult i3.pan i4.pan i6.pan
   pifft i5.pan i6.pan i7.pan i8.pan
   pvisu i8.pan

echo - Performing Butterworth highpass filtering on tangram.pan
   psetcst 0 tangram.pan i1.pan
   pfft tangram.pan i1.pan i2.pan i3.pan
   pbutterworthfilter 256 256 0 1 0 50 2 i4.pan
   pmult i2.pan i4.pan i5.pan
   pmult i3.pan i4.pan i6.pan
   pifft i5.pan i6.pan i7.pan i8.pan
   pvisu i8.pan

echo - Performing Butterworth bandreject filtering on tangram.pan
   psetcst 0 tangram.pan i1.pan
   pfft tangram.pan i1.pan i2.pan i3.pan
   pbutterworthfilter 256 256 0 0 25 50 2 i4.pan
   pmult i2.pan i4.pan i5.pan
   pmult i3.pan i4.pan i6.pan
   pifft i5.pan i6.pan i7.pan i8.pan
   pvisu i8.pan

echo - Performing Butterworth bandpass filtering on tangram.pan
   psetcst 0 tangram.pan i1.pan
   pfft tangram.pan i1.pan i2.pan i3.pan
   pbutterworthfilter 256 256 0 1 25 50 2 i4.pan
   pmult i2.pan i4.pan i5.pan
   pmult i3.pan i4.pan i6.pan
   pifft i5.pan i6.pan i7.pan i8.pan
   pvisu i8.pan

echo - Performing Gaussian lowpass filtering on tangram.pan
   psetcst 0 tangram.pan i1.pan
   pfft tangram.pan i1.pan i2.pan i3.pan
   pgaussianfilter 256 256 0 0 0 100 i4.pan
   pmult i2.pan i4.pan i5.pan
   pmult i3.pan i4.pan i6.pan
   pifft i5.pan i6.pan i7.pan i8.pan
   pvisu i8.pan

echo - Performing Gaussian highpass filtering on tangram.pan
   psetcst 0 tangram.pan i1.pan
   pfft tangram.pan i1.pan i2.pan i3.pan
   pgaussianfilter 256 256 0 1 0 50 i4.pan
   pmult i2.pan i4.pan i5.pan
   pmult i3.pan i4.pan i6.pan
   pifft i5.pan i6.pan i7.pan i8.pan
   pvisu i8.pan

echo - Performing Gaussian bandreject filtering on tangram.pan
   psetcst 0 tangram.pan i1.pan
   pfft tangram.pan i1.pan i2.pan i3.pan
   pgaussianfilter 256 256 0 0 25 50 i4.pan
   pmult i2.pan i4.pan i5.pan
   pmult i3.pan i4.pan i6.pan
   pifft i5.pan i6.pan i7.pan i8.pan
   pvisu i8.pan

echo - Performing Gaussian bandpass filtering on tangram.pan
   psetcst 0 tangram.pan i1.pan
   pfft tangram.pan i1.pan i2.pan i3.pan
   pgaussianfilter 256 256 0 1 25 50 i4.pan
   pmult i2.pan i4.pan i5.pan
   pmult i3.pan i4.pan i6.pan
   pifft i5.pan i6.pan i7.pan i8.pan
   pvisu i8.pan

del %TMPFILE%
