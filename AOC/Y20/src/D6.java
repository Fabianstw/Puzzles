import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.List;
import java.util.Map;


public class D6 {
  private static final Path INPUT = Path.of("src/inputs/d6.txt");
  
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
    int sum = 0;
    
    HashSet<Character> groupQuestions = new HashSet<>();
    for (String line : input) {
      if (line.isBlank()) {
        sum += groupQuestions.size();
        groupQuestions.clear();
      } else {
        line.chars()
          .mapToObj(c -> (char) c)
          .forEach(groupQuestions::add);
      }
    }
    
    return sum + groupQuestions.size();
  }
  
  public static long part2() {
    String[] input = readInput();
    int sum = 0;
    
    HashSet<Character> groupQuestions = new HashSet<>();
    boolean newLine = true;
    for (String line : input) {
      if (line.isBlank()) {
        sum += groupQuestions.size();
        groupQuestions.clear();
        newLine = true;
      } else if (newLine) {
        line.chars()
          .mapToObj(c -> (char) c)
          .forEach(groupQuestions::add);
        newLine = false;
      } else {
        HashSet<Character> intersection = new HashSet<>();
        line.chars()
          .mapToObj(c -> (char) c)
          .forEach(intersection::add);
        groupQuestions.retainAll(intersection);
      }
    }
    
    return sum + groupQuestions.size();
  }
  
  public static void run() {
    System.out.println("----- Day 6 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
