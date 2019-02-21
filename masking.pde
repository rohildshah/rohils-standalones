PImage bird;
PImage rose;

void setup() {
  size(300,168);
  bird = loadImage("img1.jpg"); //img1 must be in the data folder of the processing sketch
  rose = loadImage("img2.jpeg"); //img2 must be in the data folder of the processing sketch

  rose.resize(300, 168);
  bird.resize(300, 168);
  
  bird.mask(rose);
  
  tint(0, 255, 255);
}

void draw() {
  background(0);
  if(mousePressed) {
    exit();
  }
  image(bird,0,0);
}
