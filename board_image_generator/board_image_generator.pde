
color dark = #749454;
color light = #ebebd3;

void setup() {
  size(800, 800);
  noStroke();
  float w = width/8;
  background(#000000);
  for(int y = 0; y < 8; y++) {
    for(int x = 0; x < 8; x++) {
      push();
        translate(w*x, w*y);
        if((x + y) % 2 == 0) fill(light);
        else fill(dark);
        rect(0, 0, w, w);
      pop();
    }
  }
  save("board.png");
}
