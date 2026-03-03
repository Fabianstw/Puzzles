import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

/**
 * Parsing and part2 with help of GPTs
 */
public class D16 {
  private static final Path INPUT = Path.of("src/inputs/d16.txt");
  
  private static List<String> readInput() {
    try {
      return Files.readAllLines(INPUT);
    } catch (IOException e) {
      throw new RuntimeException("Failed to read input", e);
    }
  }
  
  private static class InputData {
    List<String> rules = new ArrayList<>();
    List<Integer> yourTicket = new ArrayList<>();
    List<List<Integer>> nearbyTickets = new ArrayList<>();
  }
  
  private static InputData parseInput() {
    List<String> lines = readInput();
    InputData data = new InputData();
    int i = 0;
    while (!lines.get(i).isEmpty()) {
      data.rules.add(lines.get(i));
      i++;
    }
    i += 2;
    
    data.yourTicket = Arrays.stream(lines.get(i).split(","))
      .map(Integer::parseInt)
      .toList();
    i += 3;
    
    while (i < lines.size()) {
      List<Integer> ticket = Arrays.stream(lines.get(i).split(","))
        .map(Integer::parseInt)
        .toList();
      data.nearbyTickets.add(ticket);
      i++;
    }
    
    return data;
  }
  
  private static List<List<int[]>> parseRules(List<String> ruleLines) {
    List<List<int[]>> rules = new ArrayList<>();
    
    for (String line : ruleLines) {
      // Example: "class: 1-3 or 5-7"
      String[] parts = line.split(": ");
      String[] ranges = parts[1].split(" or ");
      
      List<int[]> ruleRanges = new ArrayList<>();
      
      for (String range : ranges) {
        String[] bounds = range.split("-");
        int min = Integer.parseInt(bounds[0]);
        int max = Integer.parseInt(bounds[1]);
        ruleRanges.add(new int[]{min, max});
      }
      
      rules.add(ruleRanges);
    }
    
    return rules;
  }
  
  public static long part1() {
    InputData data = parseInput();
    List<List<int[]>> rules = parseRules(data.rules);
    long sum = 0;
    for (int i = 0; i < data.nearbyTickets.size(); i++) {
      for (int j = 0; j < data.nearbyTickets.get(i).size(); j++) {
        boolean found = false;
        
        for (List<int[]> rule : rules) {
          for (int[] pair : rule) {
            if (data.nearbyTickets.get(i).get(j) >= pair[0] && data.nearbyTickets.get(i).get(j) <= pair[1]) {
              found = true;
              break;
            }
          }
          if (found) break;
        }
        
        if (!found) sum += data.nearbyTickets.get(i).get(j);
      }
    }
    
    return sum;
  }
  
  private static class Rule {
    String name;
    List<int[]> ranges = new ArrayList<>();
    
    boolean matches(int value) {
      for (int[] r : ranges) {
        if (value >= r[0] && value <= r[1]) return true;
      }
      return false;
    }
  }
  
  private static List<Rule> parseRulesWithNames(List<String> ruleLines) {
    List<Rule> rules = new ArrayList<>();
    
    for (String line : ruleLines) {
      String[] parts = line.split(": ");
      Rule rule = new Rule();
      rule.name = parts[0];
      
      String[] ranges = parts[1].split(" or ");
      for (String range : ranges) {
        String[] bounds = range.split("-");
        int min = Integer.parseInt(bounds[0]);
        int max = Integer.parseInt(bounds[1]);
        rule.ranges.add(new int[]{min, max});
      }
      
      rules.add(rule);
    }
    
    return rules;
  }
  
  public static long part2() {
    InputData data = parseInput();
    List<Rule> rules = parseRulesWithNames(data.rules);
    
    List<List<Integer>> validTickets = new ArrayList<>();
    
    for (List<Integer> ticket : data.nearbyTickets) {
      boolean validTicket = true;
      
      for (int value : ticket) {
        boolean validValue = false;
        for (Rule rule : rules) {
          if (rule.matches(value)) {
            validValue = true;
            break;
          }
        }
        if (!validValue) {
          validTicket = false;
          break;
        }
      }
      
      if (validTicket) validTickets.add(ticket);
    }
    
    int fieldCount = data.yourTicket.size();
    Map<Integer, Set<Rule>> possible = new HashMap<>();
    for (int i = 0; i < fieldCount; i++) {
      Set<Rule> candidates = new HashSet<>(rules);
      
      for (List<Integer> ticket : validTickets) {
        int value = ticket.get(i);
        candidates.removeIf(rule -> !rule.matches(value));
      }
      
      possible.put(i, candidates);
    }
    
    Map<Integer, Rule> resolved = new HashMap<>();
    while (resolved.size() < fieldCount) {
      for (int i = 0; i < fieldCount; i++) {
        Set<Rule> candidates = possible.get(i);
        
        candidates.removeAll(resolved.values());
        
        if (candidates.size() == 1) {
          Rule rule = candidates.iterator().next();
          resolved.put(i, rule);
        }
      }
    }
    
    long product = 1;
    
    for (Map.Entry<Integer, Rule> entry : resolved.entrySet()) {
      if (entry.getValue().name.startsWith("departure")) {
        product *= data.yourTicket.get(entry.getKey());
      }
    }
    
    return product;
  }
  
  public static void run() {
    System.out.println("----- Day 16 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
