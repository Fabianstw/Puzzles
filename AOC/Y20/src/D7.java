import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class D7 {
  private static final Path INPUT = Path.of("src/inputs/d7.txt");
  
  private static String[] readInput() {
    try {
      List<String> lines = Files.readAllLines(INPUT);
      return lines.toArray(new String[0]);
    } catch (Exception e) {
      throw new RuntimeException("Failed to read input", e);
    }
  }
  
  public static long part1() {
    String[] lines = readInput();
    Map<String, Set<String>> canBeIn = new HashMap<>();
    
    Pattern outerPat = Pattern.compile("^(.+?) bags contain ");
    Pattern innerPat = Pattern.compile("(\\d+) (.+?) bag");
    
    for (String line : lines) {
      Matcher mOuter = outerPat.matcher(line);
      if (!mOuter.find()) continue;
      String outer = mOuter.group(1);
      
      if (line.contains("no other bags")) {
        continue;
      }
      
      Matcher mInner = innerPat.matcher(line);
      while (mInner.find()) {
        String inner = mInner.group(2);
        canBeIn.computeIfAbsent(inner, k -> new HashSet<>()).add(outer);
      }
    }
    
    String target = "shiny gold";
    Set<String> seen = new HashSet<>();
    Deque<String> queue = new ArrayDeque<>();
    queue.add(target);
    
    while (!queue.isEmpty()) {
      String cur = queue.removeFirst();
      for (String outer : canBeIn.getOrDefault(cur, Collections.emptySet())) {
        if (seen.add(outer)) {
          queue.addLast(outer);
        }
      }
    }
    
    return seen.size();
  }
  
  private static final class Child {
    final String color;
    final int count;
    
    Child(String color, int count) {
      this.color = color;
      this.count = count;
    }
  }
  
  public static long part2() {
    String[] lines = readInput();
    
    // outerColor -> list of (count, innerColor)
    Map<String, List<Child>> contains = new HashMap<>();
    
    Pattern outerPat = Pattern.compile("^(.+?) bags contain ");
    Pattern innerPat = Pattern.compile("(\\d+) (.+?) bag");
    
    for (String line : lines) {
      Matcher mOuter = outerPat.matcher(line);
      if (!mOuter.find()) continue;
      String outer = mOuter.group(1);
      
      List<Child> kids = new ArrayList<>();
      if (!line.contains("no other bags")) {
        Matcher mInner = innerPat.matcher(line);
        while (mInner.find()) {
          int count = Integer.parseInt(mInner.group(1));
          String inner = mInner.group(2);
          kids.add(new Child(inner, count));
        }
      }
      contains.put(outer, kids);
    }
    
    Map<String, Long> memo = new HashMap<>();
    return totalInside("shiny gold", contains, memo);
  }
  
  private static long totalInside(
    String color,
    Map<String, List<Child>> contains,
    Map<String, Long> memo
  ) {
    Long cached = memo.get(color);
    if (cached != null) return cached;
    
    long sum = 0;
    for (Child c : contains.getOrDefault(color, Collections.emptyList())) {
      // c.count * (the bag itself + everything inside it)
      sum += (long) c.count * (1L + totalInside(c.color, contains, memo));
    }
    
    memo.put(color, sum);
    return sum;
  }
  
  public static void run() {
    System.out.println("----- Day 7 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
