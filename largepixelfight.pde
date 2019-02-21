// Constants
int Y_AXIS = 1;
int X_AXIS = 2;
color b1, b2;

void setup() {
  
  size(500, 500);

  setGradient(0, 0, 500, 500, 255, 0, X_AXIS);
  
  frameRate(1000000);
}

void draw() {
  int xpix = (int) random(0, width);
  int ypix = (int) random(0, height);
  
  float loc = ypix*width+xpix;
  
  loadPixels();
  float r = red(pixels[(int) loc]);
  float g = green(pixels[(int) loc]);
  float b = blue(pixels[(int) loc]);
  updatePixels();

  noStroke();
  
  rectMode(CENTER);
  
  fill(r, g, b);
  rect(xpix, ypix, 50, 50);
}


void setGradient(int x, int y, float w, float h, color c1, color c2, int axis ) {

  noFill();

  if (axis == X_AXIS) {  // Top to bottom gradient
    for (int i = x; i <= x+w; i++) {
      float inter = map(i, x, x+w, 0, 1);
      color c = lerpColor(c1, c2, inter);
      stroke(c);
      line(i, y, i, y+h);
    }
  }
}





// Size of cells
int cellSize = 5;


// Colors for active/inactive cells
color alive = color(0, 255, 0);
color dead = color(0);

// Array of cells
int[][] cells; 
// Buffer to record the state of the cells and use this while changing the others in the interations
int[][] cellsBuffer;
