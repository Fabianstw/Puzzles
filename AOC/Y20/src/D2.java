import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class D2 {
  private static final Path INPUT = Path.of("src/inputs/d2.txt");

  private static String[] readInput() {
    try {
      List<String> lines = Files.readAllLines(INPUT);
      return lines.toArray(new String[0]);
    } catch (Exception e) {
      throw new RuntimeException("Failed to read input", e);
    }
  }

  public static int part1() {
    String[] lines = readInput();
    int counter = 0;
    for (String line : lines) {
      String[] parts = line.split(": ");
      String[] range = parts[0].split(" ")[0].split("-");
      String letter = parts[0].split(" ")[1];
      String password = parts[1];
      int countChar = password.length() - password.replace(letter, "").length();
      if (Integer.parseInt(range[0]) <= countChar && countChar <= Integer.parseInt(range[1])) {
        counter++;
      }
    }
    return counter;
  }

  public static int part2() {
    String[] lines = readInput();
    int counter = 0;
    for (String line : lines) {
      String[] parts = line.split(": ");
      String[] range = parts[0].split(" ")[0].split("-");
      String letter = parts[0].split(" ")[1];
      String password = parts[1];
      if (password.charAt(Integer.parseInt(range[0]) - 1) == letter.charAt(0)
          ^ password.charAt(Integer.parseInt(range[1]) - 1) == letter.charAt(0)) {
        counter++;
      }
    }
    return counter;
  }

  public static void run() {
    System.out.println("----- Day 2 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
