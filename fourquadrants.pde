PImage img;

void setup() {
  size(500,500);
  img = loadImage("Sunflower.jpg"); //desired image must be in the data folder of the sketch
  img.resize(500,500);
}

void draw() {
  img.loadPixels();
  noStroke();
  for(int i = 0; i<(height/2)*500;i = i + 500) {
    for(int x = i;x<250+i;x++) {
      img.pixels[x]=img.pixels[x]&0xFF0000;
    }
  }
  
  for(int i = width/2; i<125250;i = i + 500) {
    for(int x = i;x<250+i;x++) {
      img.pixels[x]=img.pixels[x]&0x00FF00;
    }
  }
  
  for(int i = 125000; i<250000;i = i + 500) {
    for(int x = i;x<250+i;x++) {
      img.pixels[x]=img.pixels[x]&0x0000FF;
    }
  }
  img.updatePixels();
  image(img,0,0);
}


/*
Permission needed to copy
*/
