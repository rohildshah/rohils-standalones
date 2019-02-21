color army1 = color(0, 0, 0);
color army2 = color(255, 255, 255);

color [][] pixelsBuffer;

int x;
int y;
int start1 = 5;
int start2 = 495;

void setup(){  
  size(500,500);
  background(150, 150, 150);
  
  pixelsBuffer = new color[width][height];
  
  set(start1,start1,army1);
  set(start2,start2,army2);
  
  pixelsBuffer[start1][start1] = color(army1);
  pixelsBuffer[start2][start2] = color(army2);

  //frameRate(1000000);
}

void draw() {
  loadPixels();
  for(int y = 2; y < height-2; y++) {
    for(int x = 2; x < width-2; x++){
      
      float loc = y*width+x;
          
      float direction1 = int(random(1,9));
      if(pixels[(int) loc] == color(army1)) {
        float temp1 = int(random(3,5));
        float contested1 = int(random(1,temp1));
        if(direction1 == 1.0) {
          if(pixelsBuffer[x][y-1] == color(army2) || pixelsBuffer[x-1][y-1] == color(army2)){
            if(contested1 == 1.0){
              pixelsBuffer[x][y-1] = color(army1);
              pixelsBuffer[x-1][y-1] = color(army1);
            }
          }else{
          pixelsBuffer[x][y-1] = color(army1);
          pixelsBuffer[x-1][y-1] = color(army1);
          }
        }
        if(direction1 == 2.0){
          if(pixelsBuffer[x-1][y] == color(army2) || pixelsBuffer[x-1][y+1] == color(army2)){
            if(contested1 == 1.0){
              pixelsBuffer[x-1][y] = color(army1);
              pixelsBuffer[x-1][y+1] = color(army1);
            }
          }else{
          pixelsBuffer[x-1][y] = color(army1);
          pixelsBuffer[x-1][y+1] = color(army1);
          }
        }
        if(direction1 == 3.0){
          if(pixelsBuffer[x][y+1] == color(army2) || pixelsBuffer[x+1][y+1] == color(army2)){
            if(contested1 == 1.0){
              pixelsBuffer[x][y+1] = color(army1);
              pixelsBuffer[x+1][y+1] = color(army1);
            }
          }else{
          pixelsBuffer[x][y+1] = color(army1);
          pixelsBuffer[x+1][y+1] = color(army1);
          }
        }
        if(direction1 == 4.0){
          if(pixelsBuffer[x+1][y] == color(army2) || pixelsBuffer[x+1][y-1] == color(army2)){
            if(contested1 == 1.0){
              pixelsBuffer[x+1][y] = color(army1);
              pixelsBuffer[x+1][y-1] = color(army1);
            }
          }else{
          pixelsBuffer[x+1][y] = color(army1);
          pixelsBuffer[x+1][y-1] = color(army1);
          }
        }
        if(direction1 == 5.0){
          if(pixelsBuffer[x+1][y-2] == color(army2) || pixelsBuffer[x][y-2] == color(army2) || pixelsBuffer[x-1][y-2] == color(army2)){
            if(contested1 == 1.0){
              pixelsBuffer[x+1][y-2] = color(army1);
              pixelsBuffer[x][y-2] = color(army1);
              pixelsBuffer[x-1][y-2] = color(army1);
            }
          }else{
          pixelsBuffer[x+1][y-2] = color(army1);
          pixelsBuffer[x][y-2] = color(army1);
          pixelsBuffer[x-1][y-2] = color(army1);
          }
        }
        if(direction1 == 6.0){
          if(pixelsBuffer[x-2][y+1] == color(army2) || pixelsBuffer[x-2][y] == color(army2) || pixelsBuffer[x-2][y-1] == color(army2)){
            if(contested1 == 1.0){
              pixelsBuffer[x-2][y+1] = color(army1);
              pixelsBuffer[x-2][y] = color(army1);
              pixelsBuffer[x-2][y-1] = color(army1);
            }
          }else{
          pixelsBuffer[x-2][y+1] = color(army1);
          pixelsBuffer[x-2][y] = color(army1);
          pixelsBuffer[x-2][y-1] = color(army1);
          }
        }
        if(direction1 == 7.0){
          if(pixelsBuffer[x-1][y+2] == color(army2) || pixelsBuffer[x][y+2] == color(army2) || pixelsBuffer[x+1][y+2] == color(army2)){
            if(contested1 == 1.0){
              pixelsBuffer[x-1][y+2] = color(army1);
              pixelsBuffer[x][y+2] = color(army1);
              pixelsBuffer[x+1][y+2] = color(army1);
            }
          }else{
          pixelsBuffer[x-1][y+2] = color(army1);
          pixelsBuffer[x][y+2] = color(army1);
          pixelsBuffer[x+1][y+2] = color(army1);
          }
        }
        if(direction1 == 8.0){
          if(pixelsBuffer[x+2][y-1] == color(army2) || pixelsBuffer[x+2][y] == color(army2) || pixelsBuffer[x+2][y+1] == color(army2)){
            if(contested1 == 1.0){
              pixelsBuffer[x+2][y-1] = color(army1);
              pixelsBuffer[x+2][y] = color(army1);
              pixelsBuffer[x+2][y+1] = color(army1);
            }
          }else{
          pixelsBuffer[x+2][y-1] = color(army1);
          pixelsBuffer[x+2][y] = color(army1);
          pixelsBuffer[x+2][y+1] = color(army1);
          }
        }
      }
      
      float direction2 = int(random(1,9));
      
      if(pixels[(int) loc] == color(army2)) {
        float temp3 = int(random(5, 7));
        float temp2 = int(random(3,temp3));
        float contested2 = int(random(1,temp2));
        if(direction2 == 1.0) {
          if(pixelsBuffer[x][y-1] == color(army1) || pixelsBuffer[x-1][y-1] == color(army1)){
            if(contested2 == 1.0){
              pixelsBuffer[x][y-1] = color(army2);
              pixelsBuffer[x-1][y-1] = color(army2);
            }
          }else{
          pixelsBuffer[x][y-1] = color(army2);
          pixelsBuffer[x-1][y-1] = color(army2);
          }
        }
        if(direction2 == 2.0){
          if(pixelsBuffer[x-1][y] == color(army1) || pixelsBuffer[x-1][y+1] == color(army1)){
            if(contested2 == 1.0){
              pixelsBuffer[x-1][y] = color(army2);
              pixelsBuffer[x-1][y+1] = color(army2);
            }
          }else{
          pixelsBuffer[x-1][y] = color(army2);
          pixelsBuffer[x-1][y+1] = color(army2);
          }
        }
        if(direction2 == 3.0){
          if(pixelsBuffer[x][y+1] == color(army1) || pixelsBuffer[x+1][y+1] == color(army1)){
            if(contested2 == 1.0){
              pixelsBuffer[x][y+1] = color(army2);
              pixelsBuffer[x+1][y+1] = color(army2);
            }
          }else{
          pixelsBuffer[x][y+1] = color(army2);
          pixelsBuffer[x+1][y+1] = color(army2);
          }
        }
        if(direction2 == 4.0){
          if(pixelsBuffer[x+1][y] == color(army1) || pixelsBuffer[x+1][y-1] == color(army1)){
            if(contested2 == 1.0){
              pixelsBuffer[x+1][y] = color(army2);
              pixelsBuffer[x+1][y-1] = color(army2);
            }
          }else{
          pixelsBuffer[x+1][y] = color(army2);
          pixelsBuffer[x+1][y-1] = color(army2);
          }
        }
        if(direction2 == 5.0){
          if(pixelsBuffer[x+1][y-2] == color(army1) || pixelsBuffer[x][y-2] == color(army1) || pixelsBuffer[x-1][y-2] == color(army1)){
            if(contested2 == 1.0){
              pixelsBuffer[x+1][y-2] = color(army2);
              pixelsBuffer[x][y-2] = color(army2);
              pixelsBuffer[x-1][y-2] = color(army2);
            }
          }else{
          pixelsBuffer[x+1][y-2] = color(army2);
          pixelsBuffer[x][y-2] = color(army2);
          pixelsBuffer[x-1][y-2] = color(army2);
          }
        }
        if(direction2 == 6.0){
          if(pixelsBuffer[x-2][y+1] == color(army1) || pixelsBuffer[x-2][y] == color(army1) || pixelsBuffer[x-2][y-1] == color(army1)){
            if(contested2 == 1.0){
              pixelsBuffer[x-2][y+1] = color(army2);
              pixelsBuffer[x-2][y] = color(army2);
              pixelsBuffer[x-2][y-1] = color(army2);
            }
          }else{
          pixelsBuffer[x-2][y+1] = color(army2);
          pixelsBuffer[x-2][y] = color(army2);
          pixelsBuffer[x-2][y-1] = color(army2);
          }
        }
        if(direction2 == 7.0){
          if(pixelsBuffer[x-1][y+2] == color(army1) || pixelsBuffer[x][y+2] == color(army1) || pixelsBuffer[x+1][y+2] == color(army1)){
            if(contested2 == 1.0){
              pixelsBuffer[x-1][y+2] = color(army2);
              pixelsBuffer[x][y+2] = color(army2);
              pixelsBuffer[x+1][y+2] = color(army2);
            }
          }else{
          pixelsBuffer[x-1][y+2] = color(army2);
          pixelsBuffer[x][y+2] = color(army2);
          pixelsBuffer[x+1][y+2] = color(army2);
          }
        }
        if(direction2 == 8.0){
          if(pixelsBuffer[x+2][y-1] == color(army1) || pixelsBuffer[x+2][y] == color(army1) || pixelsBuffer[x+2][y+1] == color(army1)){
            if(contested2 == 1.0){
              pixelsBuffer[x+2][y-1] = color(army2);
              pixelsBuffer[x+2][y] = color(army2);
              pixelsBuffer[x+2][y+1] = color(army2);
            }
          }else{
          pixelsBuffer[x+2][y-1] = color(army2);
          pixelsBuffer[x+2][y] = color(army2);
          pixelsBuffer[x+2][y+1] = color(army2);
          }
        }
      }
    }
  }
  for (int y=1; y<height-1; y++) {
    for (int x=1; x<width-1; x++) {
      pixels[(int) y*width+x] = pixelsBuffer[x][y];
     }
  }
  
  updatePixels();
}
