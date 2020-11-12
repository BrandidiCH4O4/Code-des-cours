/* -*- mode: c++; c-basic-offset: 3 -*-
 *
 * Copyright (c) 2013, GREYC.
 * All rights reserved
 *
 * You may use this file under the terms of the BSD license as follows:
 *
 * "Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met:
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in
 *     the documentation and/or other materials provided with the
 *     distribution.
 *   * Neither the name of the GREYC, nor the name of its
 *     contributors may be used to endorse or promote products
 *     derived from this software without specific prior written
 *     permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
 *
 * 
 * For more information, refer to:
 * https://clouard.users.greyc.fr/Pandore
 */

/*
 * @author David Tschumperle - 2005-12-09
 */

/**
 * @file viewer_example.cpp
 *
 * Example of the use the viewer.
 */

#include "pviewer.h"

namespace operateur{
#include "contour/pdistance.cpp"
}

int main( int argc, char **argv ) {
  Img2duc img(256,256);
  Img2dsf distance(256,256);
  
  Viewer disp(img,"Click on this image",0);
  Viewer disp2(distance,"Distance function",0);
  
  while (!disp.is_closed && !disp2.is_closed) {
    disp.wait(20);
    if (disp.button) {
      const int x = disp.mouse_x, y = disp.mouse_y;
      if (x>=0 && y>=0) {
        img[y][x] = 255;
        
        disp.display(img);      
        operateur::PDistance(img,distance);
        
        disp2.display(distance);
      }
    }
    if (disp.is_resized) disp.resize(disp);
  }
  return 0;
}
