import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class D14 {
  private static final Path INPUT = Path.of("src/inputs/d14.txt");
  
  private static String[][] readInput() {
    try {
      List<String> lines = Files.readAllLines(INPUT);
      
      List<List<String>> groups = new ArrayList<>();
      List<String> currentGroup = null;
      
      for (String line : lines) {
        
        if (line.startsWith("mask")) {
          // Start new group
          currentGroup = new ArrayList<>();
          groups.add(currentGroup);
        }
        
        assert currentGroup != null;
        currentGroup.add(line);
      }
      
      // Convert to String[][]
      String[][] result = new String[groups.size()][];
      
      for (int i = 0; i < groups.size(); i++) {
        result[i] = groups.get(i).toArray(new String[0]);
      }
      
      return result;
      
    } catch (Exception e) {
      throw new RuntimeException("Failed to read input", e);
    }
  }
  
  public static long part1() {
    String[][] input = readInput();
    long finalsum = 0;

    HashMap<Integer, Long> sums = new HashMap<>();
    for (String[] group : input) {
      String mask = group[0].split("mask = ")[1];
      for (int i = 1; i < group.length; i++) {
        String[] parts = group[i].split("] = ");
        int mem = Integer.parseInt(parts[0].split("mem\\[")[1]);
        int value = Integer.parseInt(parts[1]);
        String binValue = String.format("%36s", Integer.toBinaryString(value))
          .replace(' ', '0');
        StringBuilder result = new StringBuilder();
        for (int j = 0; j < mask.length(); j++) {
          if (mask.charAt(j) == 'X') {
            result.append(binValue.charAt(j));
          } else if (mask.charAt(j) == '1' || mask.charAt(j) == '0') {
            result.append(mask.charAt(j));
          }
        }
        sums.put(mem, Long.parseLong(result.toString(), 2));
      }
    }
    for (Integer key : sums.keySet()) {
      finalsum += sums.get(key);
    }
    
    return finalsum;
  }
  
  public static ArrayList<Long> getCombinations(String value) {
    ArrayList<Long> values = new ArrayList<>();
    
    for (int i = 0; i < value.length(); i++) {
      if (value.charAt(i) == 'X') {
        StringBuilder value_1 = new StringBuilder(value);
        value_1.setCharAt(i, '1');
        StringBuilder value_0 = new StringBuilder(value);
        value_0.setCharAt(i, '0');
        values.addAll(getCombinations(String.valueOf(value_1)));
        values.addAll(getCombinations(String.valueOf(value_0)));
        return values;
      }
    }
    values.add(Long.parseLong(value, 2));
    return values;
  }
  
  public static long part2() {
    String[][] input = readInput();
    long finalsum = 0;
    HashMap<Long, Long> sums = new HashMap<>();
    
    for (String[] group : input) {
      String mask = group[0].split("mask = ")[1];
      for (int i = 1; i < group.length; i++) {
        String[] parts = group[i].split("] = ");
        int mem = Integer.parseInt(parts[0].split("mem\\[")[1]);
        int value = Integer.parseInt(parts[1]);
        String binValue = String.format("%36s", Integer.toBinaryString(mem))
          .replace(' ', '0');
        StringBuilder result = new StringBuilder();
        for (int j = 0; j < mask.length(); j++) {
          if (mask.charAt(j) == 'X') {
            result.append('X');
          } else if (mask.charAt(j) == '1') {
            result.append('1');
          } else if (mask.charAt(j) == '0') {
            result.append(binValue.charAt(j));
          }
        }
        for (long com : getCombinations(result.toString())) {
          System.out.println(com);
          sums.put(com, (long) value);
        }
      }
    }
    
    for (Long key : sums.keySet()) {
      finalsum += sums.get(key);
    }
    
    return finalsum;
  }
  
  public static void run() {
    System.out.println("----- Day 14 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
