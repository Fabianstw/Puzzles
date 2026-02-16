import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.List;
import java.util.Map;

public class D5 {
  private static final Path INPUT = Path.of("src/inputs/d5.txt");
  
  private static String[] readInput() {
    try {
      List<String> lines = Files.readAllLines(INPUT);
      return lines.toArray(new String[0]);
    } catch (Exception e) {
      throw new RuntimeException("Failed to read input", e);
    }
  }
  
  private static int toInt(String value) {
    Map<Character, Boolean> map = Map.of(
      'F', false,
      'B', true,
      'L', false,
      'R', true
    );
    int sum = 0;
    for (int i = value.length() - 1; i >= 0; i--) {
      if (map.get(value.charAt(i))) {
        sum += (int) Math.pow(2, value.length() - i - 1);
      }
    }
    return sum;
  }
  
  public static long part1() {
    int max = -1;
    String[] input = readInput();
    
    for (String line : input) {
      String firstPart = (String) line.subSequence(0, 7);
      String secondPart = (String) line.subSequence(7, 10);
      max = Math.max(max, toInt(firstPart) * 8 + toInt(secondPart));
    }
    
    return max;
  }
  
  public static long part2() {
    String[] input = readInput();
    HashSet<Integer> seats = new HashSet<>();
    
    for (String line : input) {
      String firstPart = (String) line.subSequence(0, 7);
      String secondPart = (String) line.subSequence(7, 10);
      seats.add(toInt(firstPart) * 8 + toInt(secondPart));
    }
    
    for (int i = 1; i < 127 * 8 + 8; i++) {
      if (seats.contains(i)) continue;
      if (seats.contains(i - 1) && seats.contains(i + 1)) return i;
    }
    
    return 0;
  }
  
  public static void run() {
    System.out.println("----- Day 5 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
