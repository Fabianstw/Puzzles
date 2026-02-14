import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class D1 {

  private static final Path INPUT = Path.of("src/inputs/d1.txt");

  private static int[] readInput() {
    try {
      List<String> lines = Files.readAllLines(INPUT);
      return lines.stream().mapToInt(Integer::parseInt).toArray();
    } catch (Exception e) {
      throw new RuntimeException("Failed to read input", e);
    }
  }

  public static int part1() {
    int[] input = readInput();

    for (int i = 0; i < input.length; i++) {
      for (int j = i + 1; j < input.length; j++) {
        if (input[i] + input[j] == 2020) {
          return input[i] * input[j];
        }
      }
    }
    throw new RuntimeException("No solution found");
  }

  public static int part2() {
    int[] input = readInput();

    for (int i = 0; i < input.length; i++) {
      for (int j = i + 1; j < input.length; j++) {
        for (int k = j + 1; k < input.length; k++) {
          if (input[i] + input[j] + input[k] == 2020) {
            return input[i] * input[j] * input[k];
          }
        }
      }
    }
    throw new RuntimeException("No solution found");
  }

  public static void run() {
    System.out.println("----- Day 1 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
