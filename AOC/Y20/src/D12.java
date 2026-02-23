import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Map;

public class D12 {
  private static final Path INPUT = Path.of("src/inputs/d12.txt");
  
  private static String[] readInput() {
    try {
      List<String> lines = Files.readAllLines(INPUT);
      return lines.toArray(new String[0]);
    } catch (Exception e) {
      throw new RuntimeException("Failed to read input", e);
    }
  }
  
  public static long part1() {
    String[] input = readInput();
    int we = 0;
    int ns = 0;
    char dir = 'e';
    int degree = 90;
    Map<Integer, Character> direction = Map.of(
      0, 'n',
      90, 'e',
      180, 's',
      270, 'w'
    );
    
    for (String line : input) {
      char start = line.charAt(0);
      int value = Integer.parseInt(line.split(String.valueOf(start))[1]);
      if (start == 'N') {
        ns += value;
      } else if (start == 'S') {
        ns -= value;
      } else if (start == 'E') {
        we += value;
      } else if (start == 'W') {
        we -= value;
      } else if (start == 'L') {
        degree = (degree - value + 360) % 360;
      } else if (start == 'R') {
        degree = (degree + value) % 360;
      } else if (start == 'F') {
        if (dir == 'n') ns += value;
        if (dir == 's') ns -= value;
        if (dir == 'e') we += value;
        if (dir == 'w') we -= value;
      }
      dir = direction.get(degree);
    }
    
    return Math.abs(ns) + Math.abs(we);
  }
  
  public static long part2() {
    String[] input = readInput();
    int we = 0;
    int ns = 0;
    int wwe = 10;
    int wns = 1;
    
    for (String line : input) {
      char start = line.charAt(0);
      int value = Integer.parseInt(line.split(String.valueOf(start))[1]);
      if (start == 'N') {
        wns += value;
      } else if (start == 'S') {
        wns -= value;
      } else if (start == 'E') {
        wwe += value;
      } else if (start == 'W') {
        wwe -= value;
      } else if (start == 'L' || start == 'R') {
        int times = (value / 90) % 4;
        for (int i = 0; i < times; i++) {
          int tmp = wwe;
          if (start == 'L') {
            wwe = -wns;
            wns = tmp;
          } else { // 'R'
            wwe = wns;
            wns = -tmp;
          }
        }
      } else if (start == 'F') {
        ns += value * wns;
        we += value * wwe;
      }
    }
    
    return Math.abs(ns) + Math.abs(we);
  }
  
  public static void run() {
    System.out.println("----- Day 12 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
