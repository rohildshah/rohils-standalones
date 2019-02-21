PImage rose;

void setup() {
  size(500, 331);
  rose = loadImage("img3.jpeg"); //desired image must be in the data folder of the sketch (see README.md)
  rose.resize(500,331);
  frameRate(1000000000);
}


void draw() {
  int xpix = (int) random(0, width);
  int ypix = (int) random(0, height);
  
  float loc = ypix*width+xpix;
  
  rose.loadPixels();
  float r = red(rose.pixels[(int) loc]);
  float g = green(rose.pixels[(int) loc]);
  float b = blue(rose.pixels[(int) loc]);
  rose.updatePixels();

  noStroke();
  fill(r, g, b);
  ellipse(xpix, ypix, 1, 1);
}
