import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class D17 {
  private static final Path INPUT = Path.of("src/inputs/d17.txt");
  
  private static String[] readInput() {
    try {
      List<String> lines = Files.readAllLines(INPUT);
      return lines.toArray(new String[0]);
    } catch (Exception e) {
      throw new RuntimeException("Failed to read input", e);
    }
  }
  
  record Point3D(int x, int y, int z) {}
  
  public static long part1() {
    String[] input = readInput();
    Set<Point3D> active = new HashSet<>();
    
    for (int j = 0; j < input.length; j++) {
      for (int i = 0; i < input[j].length(); i++) {
        if (input[j].charAt(i) == '#') active.add(new Point3D(j, i, 0));
      }
    }
    
    for (int c = 0; c < 6; c++) {
      Map<Point3D, Integer> neighborCount = new HashMap<>();
      for (Point3D p : active) {
        for (int dx = -1; dx <= 1; dx++) {
          for (int dy = -1; dy <= 1; dy++) {
            for (int dz = -1; dz <= 1; dz++) {
              if (dx == 0 && dy == 0 && dz == 0) continue;
              Point3D neighbor = new Point3D(p.x + dx, p.y + dy, p.z + dz);
              neighborCount.merge(neighbor, 1, Integer::sum);
            }
          }
        }
      }
      
      Set<Point3D> nextActive = new HashSet<>();
      for (Map.Entry<Point3D, Integer> entry : neighborCount.entrySet()) {
        Point3D point = entry.getKey();
        int count = entry.getValue();
        
        if (active.contains(point)) {
          if (count == 2 || count == 3) {
            nextActive.add(point);
          }
        } else {
          if (count == 3) {
            nextActive.add(point);
          }
        }
      }
      
      active = nextActive;
    }
    
    return active.size();
  }
  
  record Point4D(int x, int y, int z, int w) {}
  
  public static long part2() {
    String[] input = readInput();
    Set<Point4D> active = new HashSet<>();
    
    for (int j = 0; j < input.length; j++) {
      for (int i = 0; i < input[j].length(); i++) {
        if (input[j].charAt(i) == '#') active.add(new Point4D(j, i, 0, 0));
      }
    }
    
    for (int c = 0; c < 6; c++) {
      Map<Point4D, Integer> neighborCount = new HashMap<>();
      for (Point4D p : active) {
        for (int dx = -1; dx <= 1; dx++) {
          for (int dy = -1; dy <= 1; dy++) {
            for (int dz = -1; dz <= 1; dz++) {
              for (int dw = -1; dw <= 1; dw++) {
                if (dx == 0 && dy == 0 && dz == 0 && dw == 0) continue;
                Point4D neighbor = new Point4D(p.x + dx, p.y + dy, p.z + dz, p.w + dw);
                neighborCount.merge(neighbor, 1, Integer::sum);
              }
            }
          }
        }
      }
      
      Set<Point4D> nextActive = new HashSet<>();
      for (Map.Entry<Point4D, Integer> entry : neighborCount.entrySet()) {
        Point4D point = entry.getKey();
        int count = entry.getValue();
        
        if (active.contains(point)) {
          if (count == 2 || count == 3) {
            nextActive.add(point);
          }
        } else {
          if (count == 3) {
            nextActive.add(point);
          }
        }
      }
      
      active = nextActive;
    }
    
    return active.size();
  }
  
  public static void run() {
    System.out.println("----- Day 17 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
