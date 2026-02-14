import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class D3 {
  private static final Path INPUT = Path.of("src/inputs/d3.txt");

  private static String[] readInput() {
    try {
      List<String> lines = Files.readAllLines(INPUT);
      return lines.toArray(new String[0]);
    } catch (Exception e) {
      throw new RuntimeException("Failed to read input", e);
    }
  }

  private static long countTrees(String[] map, int dx, int dy) {
    int width = map[0].length();
    int col = 0;
    long trees = 0;

    for (int row = 0; row < map.length; row += dy) {
      if (map[row].charAt(col) == '#') trees++;
      col = (col + dx) % width;
    }

    return trees;
  }

  public static long part1() {
    String[] map = readInput();
    return countTrees(map, 3, 1);
  }

  public static long part2() {
    String[] map = readInput();
    int[][] slopes = {{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}};

    long product = 1;
    for (int[] s : slopes) {
      product *= countTrees(map, s[0], s[1]);
    }
    return product;
  }

  public static void run() {
    System.out.println("----- Day 3 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
