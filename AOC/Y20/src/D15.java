import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class D15 {
  private static final Path INPUT = Path.of("src/inputs/d15.txt");
  
  private static String readInput() {
    try {
      List<String> lines = Files.readAllLines(INPUT);
      return Arrays.toString(lines.toArray(new String[0])).replace("[", "").replace("]", "");
    } catch (Exception e) {
      throw new RuntimeException("Failed to read input", e);
    }
  }
  
  public static int part1() {
    String input = readInput();
    int[] values = Arrays.stream(input.split(",")).mapToInt(Integer::parseInt).toArray();
    
    Map<Integer, Integer> lastTurn = new HashMap<>();
    int turn = 1;
    int current = 0;
    
    for (; turn <= values.length; turn++) {
      current = values[turn - 1];
      lastTurn.put(current, turn);
    }

    for (; turn <= 30000000; turn++) {
      if (turn % 3000000 == 0) System.out.println(turn);
      int next;
      if (lastTurn.containsKey(current)) {
        next = (turn - 1) - lastTurn.get(current);
      } else {
        next = 0;
      }
      lastTurn.put(current, turn - 1);
      current = next;
    }
    
    return current;
  }
  
  public static long part2() {
    
    return 0;
  }
  
  public static void run() {
    System.out.println("----- Day 15 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
