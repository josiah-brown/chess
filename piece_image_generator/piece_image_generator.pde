PFont myFont;
PGraphics pg;

String qb = "U+265B";

void setup() {
  size(100, 100);
  //stroke(0, 0, 0);
  //fill(0, 0, 0);
  //myFont = createFont("FreeSerif.otf", 100);
  //textFont(myFont);
  //textAlign(CENTER, CENTER);
  //translate(0, -10);
  //text("\u265d", width/2, height/2);
  //save("black_bishop.png");
  
  pg = createGraphics(100,100,JAVA2D); //create the off-screen graphics
  pg.smooth();
  pg.beginDraw();
  //pg.stroke(0);
  pg.fill(#FFC947);
  //myFont = createFont("FreeSerif.otf", 100);
  //pg.textFont(myFont);
  //pg.textAlign(CENTER, CENTER);
  //pg.translate(0, -10);
  //pg.text("\u265a", width/2, height/2);
  pg.ellipse(width/2, height/2, width, height);
  pg.endDraw();
  pg.save("yellow.png");
 
}
