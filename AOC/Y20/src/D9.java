import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.List;

public class D9 {
  private static final Path INPUT = Path.of("src/inputs/d9.txt");
  
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
    for (int k = 25; k < input.length; k++) {
      HashSet<Integer> seen = new HashSet<>();
      
      for (int i = k - 25; i < k-1; i++) {
        for (int j = i + 1; j < k; j++) {
          seen.add(Integer.parseInt(input[i]) + Integer.parseInt(input[j]));
        }
      }
      
      if (!seen.contains(Integer.parseInt(input[k]))) return Integer.parseInt(input[k]);
    }
    
    return 0;
  }
  
  public static long part2() {
    String[] input = readInput();
    long goal = part1();
    
    int left = 0;
    int right = 1;
    long sum = Long.parseLong(input[0]) + Long.parseLong(input[1]);
    
    while (true) {
      if (sum == goal) {
        long low = Long.MAX_VALUE;
        long high = Long.MIN_VALUE;
        for (int i = left; i <= right; i++) {
          if (Long.parseLong(input[i]) > high) high = Long.parseLong(input[i]);
          if (Long.parseLong(input[i]) < low) low = Long.parseLong(input[i]);
        }
        return high + low;
      } else if (sum > goal) {
        left += 1;
        sum -= Long.parseLong(input[left - 1]);
      } else {
        right += 1;
        sum += Long.parseLong(input[right]);
      }
    }
  }
  
  public static void run() {
    System.out.println("----- Day 9 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
