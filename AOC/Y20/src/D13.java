import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class D13 {
  private static final Path INPUT = Path.of("src/inputs/d13.txt");
  
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
    int time = Integer.parseInt(input[0]);
    String[] busID_ = input[1].split(",");
    Integer[] busID = Arrays.stream(busID_).filter(x -> !Objects.equals(x, "x")).map(Integer::parseInt).toArray(Integer[]::new);
    
    int min = 999999;
    int value = 0;
    for (Integer bus : busID) {
      int div = Math.floorDiv(time, bus);
      int diff = ((div + 1) * bus) - time;
      if (diff < min) {
        min = diff;
        value = diff * bus;
      }
    }
    
    return value;
  }
  
  public static long part2() {
    String[] input = readInput()[1].split(",");
    ArrayList<Long> busIDs = new ArrayList<>();
    ArrayList<Long> congruences = new ArrayList<>();
    
    for (int i = 0; i < input.length; i++) {
      if (input[i].equals("x")) continue;
      long busID = Long.parseLong(input[i]);
      busIDs.add(busID);
      congruences.add((busID - i % busID) % busID); // t ≡ (busID - offset) mod busID
    }
    
    // Chinese Remainder Theorem
    long M = 1;
    for (long busID : busIDs) M *= busID;
    
    long t = 0;
    for (int i = 0; i < busIDs.size(); i++) {
      long mi = busIDs.get(i);
      long bi = congruences.get(i);
      long Mi = M / mi;
      long inv = modInverse(Mi, mi);
      t += bi * Mi * inv;
    }
    
    return t % M;
  }
  
  // Compute modular inverse using Extended Euclidean Algorithm
  public static long modInverse(long a, long m) {
    long m0 = m, y = 0, x = 1;
    while (a > 1) {
      long q = a / m;
      long t = m;
      m = a % m;
      a = t;
      t = y;
      y = x - q * y;
      x = t;
    }
    if (x < 0) x += m0;
    return x;
  }
  
  public static void run() {
    System.out.println("----- Day 13 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
