class CompositePoint {
  int x;
  int y;
  
  CompositePoint(int x_pos, int y_pos){
    x = x_pos;
    y = y_pos;
  }
  
}

ArrayList<CompositePoint> startPoints = new ArrayList<CompositePoint>();

int end_x;
int end_y;
int start_x = 0;
int start_y = 0;

void setup() {
  size(1024, 768);
  background(10, 80, 100);  
  //CompositePoint start = new CompositePoint(width/2, mouseY/2);
  //startPoints.add(start);  
}

void draw() {
  background(10, 80, 100);
  if ((mousePressed) && (mouseButton == LEFT)) {    
    CompositePoint point = new CompositePoint(mouseX, mouseY);
    startPoints.add(point);    
  } else if ((mousePressed) && (mouseButton == RIGHT)) {
    background(10, 80, 100);
  }
  for (CompositePoint point : startPoints){
    stroke(mouseX, mouseY, start_x);
    end_x = mouseX;
    end_y = mouseY;
    line(point.x, point.y, end_x, end_y);
  }
  
  
}
