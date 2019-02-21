PImage rose;
PImage mask;

void setup() {
  size(276, 183);
  rose = loadImage("img3.jpeg"); //referenced images must be in the data folder (see README.md)
  mask = loadImage("pic.jpeg"); //referenced images must be in the data folder (see README.md)
  mask.resize(276, 183);
  tint(255,100);
}

void draw() {
   rose.loadPixels();
   for (int i = 0; i < width*height; i++) {
      rose.pixels[i] = color (random(0, 255), random(0, 255), random(0, 255));
   }
   rose.updatePixels();
   image(rose,0,0);
   image(mask,0,0);
   if(mousePressed) {
      exit(); 
   }
}
