import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.List;

public class D8 {
  private static final Path INPUT = Path.of("src/inputs/d8.txt");
  
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
    int acc = 0;
    int currentLine = 0;
    HashSet<Integer> seen = new HashSet<>();
    while (true) {
      if (seen.contains(currentLine)) return acc;
      seen.add(currentLine);
      String line = input[currentLine];
      String[] parts = line.split(" ");
      if (parts[0].equals("nop")) {
        currentLine++;
      } else if (parts[0].equals("acc")) {
        acc += Integer.parseInt(parts[1]);
        currentLine++;
      } else {
        currentLine += Integer.parseInt(parts[1]);
      }
    }
  }
  
  public static long part2() {
    String[] input = readInput();
    for (int i = 0; i < input.length; i++) {
      String editline = input[i];
      if (editline.startsWith("nop")) {
        editline = editline.replace("nop", "jmp");
      }
      if (editline.startsWith("jmp")) {
        editline = editline.replace("jmp", "nop");
      }
      String[] inputDuplicate = input.clone();
      inputDuplicate[i] = editline;
      
      int acc = 0;
      int currentLine = 0;
      HashSet<Integer> seen = new HashSet<>();
      while (!seen.contains(currentLine)) {
        if (currentLine == inputDuplicate.length) return acc;
        seen.add(currentLine);
        String line = inputDuplicate[currentLine];
        String[] parts = line.split(" ");
        if (parts[0].equals("nop")) {
          currentLine++;
        } else if (parts[0].equals("acc")) {
          acc += Integer.parseInt(parts[1]);
          currentLine++;
        } else {
          currentLine += Integer.parseInt(parts[1]);
        }
      }
      
    }
    return 0;
  }
  
  public static void run() {
    System.out.println("----- Day 8 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
