import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class D10 {
  private static final Path INPUT = Path.of("src/inputs/d10.txt");
  
  private static Integer[] readInput() {
    try {
      List<String> lines = Files.readAllLines(INPUT);
      return lines.stream().map(Integer::parseInt).toArray(Integer[]::new);
    } catch (Exception e) {
      throw new RuntimeException("Failed to read input", e);
    }
  }
  
  public static int getMax(List<Integer> values) {
    int max = 0;
    for (int value : values) max = Math.max(max, value);
    return max;
  }
  
  public static long part1() {
    List<Integer> input = new ArrayList<>(List.of(readInput()));
    int max = getMax(input);
    input.add(0);
    input.add(max + 3);
    input.sort(Integer::compareTo);
    int ones = 0;
    int threes = 0;
    for (int i = 0; i < input.toArray().length;i++) {
      for (int j = 0; j < 3; j++) {
        if (i + j >= input.toArray().length) continue;
        if (input.get(i + j) - input.get(i) == 1) ones++;
        if (input.get(i + j) - input.get(i) == 3) threes++;
      }
    }
    return (long) ones * threes;
  }
  
  public static long part2() {
    List<Integer> input = new ArrayList<>(List.of(readInput()));
    int max = getMax(input);
    input.add(0);
    input.add(max + 3);
    input.sort(Integer::compareTo);
    long[] counting = new long[input.toArray().length];
    counting[0] = 1;
    for (int i = 0; i < input.toArray().length;i++) {
      for (int j = 1; j <= 3; j++) {
        if (i + j >= input.toArray().length) continue;
        if (input.get(i + j) - input.get(i) <= 3) {
          counting[i+j] += counting[i];
        }
      }
    }
    System.out.println(Arrays.toString(counting));
    return counting[counting.length - 1];
  }
  
  public static void run() {
    System.out.println("----- Day 10 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
