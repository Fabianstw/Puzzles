import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.regex.Pattern;

public class D19 {
  private static final Path INPUT = Path.of("src/inputs/d19.txt");
  
  private static class InputData {
    Map<Integer, String> rules = new HashMap<>();
    List<String> messages = new ArrayList<>();
  }
  
  private static InputData readInput() {
    try {
      List<String> lines = Files.readAllLines(INPUT);
      InputData data = new InputData();
      
      boolean readingRules = true;
      
      for (String line : lines) {
        if (line.isEmpty()) {
          readingRules = false;
          continue;
        }
        
        if (readingRules) {
          String[] parts = line.split(": ");
          data.rules.put(Integer.parseInt(parts[0]), parts[1]);
        } else {
          data.messages.add(line);
        }
      }
      
      return data;
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
  }
  
  private static Map<Integer, String> memo = new HashMap<>();
  
  private static String buildRegex(int ruleId, Map<Integer, String> rules) {
    if (memo.containsKey(ruleId)) return memo.get(ruleId);
    
    String rule = rules.get(ruleId);
    
    // base case: "a" or "b"
    if (rule.contains("\"")) {
      String val = rule.replace("\"", "");
      memo.put(ruleId, val);
      return val;
    }
    
    StringBuilder sb = new StringBuilder();
    sb.append("(");
    
    String[] parts = rule.split(" \\| ");
    for (int i = 0; i < parts.length; i++) {
      if (i > 0) sb.append("|");
      
      String[] tokens = parts[i].split(" ");
      for (String token : tokens) {
        int subRule = Integer.parseInt(token);
        sb.append(buildRegex(subRule, rules));
      }
    }
    
    sb.append(")");
    String result = sb.toString();
    memo.put(ruleId, result);
    return result;
  }
  
  public static long part1() {
    InputData data = readInput();
    memo.clear();
    
    String regex = "^" + buildRegex(0, data.rules) + "$";
    Pattern pattern = Pattern.compile(regex);
    
    return data.messages.stream()
      .filter(m -> pattern.matcher(m).matches())
      .count();
  }
  
  public static long part2() {
    InputData data = readInput();
    memo.clear();
    
    String r42 = buildRegex(42, data.rules);
    String r31 = buildRegex(31, data.rules);
    
    Pattern p42 = Pattern.compile(r42);
    Pattern p31 = Pattern.compile(r31);
    
    long count = 0;
    
    for (String msg : data.messages) {
      int pos = 0;
      int count42 = 0;
      int count31 = 0;
      
      // match as many rule 42 as possible from start
      while (true) {
        var m = p42.matcher(msg);
        m.region(pos, msg.length());
        if (m.lookingAt()) {
          count42++;
          pos = m.end();
        } else break;
      }
      
      // then match rule 31
      while (true) {
        var m = p31.matcher(msg);
        m.region(pos, msg.length());
        if (m.lookingAt()) {
          count31++;
          pos = m.end();
        } else break;
      }
      
      // must consume whole string
      if (pos != msg.length()) continue;
      
      // must have more 42 than 31, and at least one 31
      if (count42 > count31 && count31 > 0) {
        count++;
      }
    }
    
    return count;
  }
  
  public static void run() {
    System.out.println("----- Day 19 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}