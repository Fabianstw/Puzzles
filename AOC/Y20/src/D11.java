import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class D11 {
  private static final Path INPUT = Path.of("src/inputs/d11.txt");
  
  private static String[] readInput() {
    try {
      List<String> lines = Files.readAllLines(INPUT);
      return lines.toArray(new String[0]);
    } catch (Exception e) {
      throw new RuntimeException("Failed to read input", e);
    }
  }
  
  private static int countHashtags(char[][] input) {
    int count = 0;
    for (char[] line : input) {
      for (char c : line) {
        if (c == '#') count++;
      }
    }
    return count;
  }
  
  public static long part1() {
    int[][] neighbors = {{-1,-1}, {-1,0}, {-1,1}, {0,-1}, {0,1}, {1,-1}, {1,0}, {1,1}};
    String[] input = readInput();
    char[][] grid = new char[input.length][];
    for (int i = 0; i < input.length; i++) {
      grid[i] = input[i].toCharArray();
    }
    
    char[][] next = new char[input.length][];
    for (int i = 0; i < input.length; i++) {
      next[i] = new char[input[i].length()];
    }
    while (true) {
      boolean changed = false;
      
      for (int i = 0; i < grid.length; i++) {
        for (int j = 0; j < grid[i].length; j++) {
          
          char cell = grid[i][j];
          
          if (cell == '.') {
            next[i][j] = '.';
            continue;
          }
          
          int count = 0;
          for (int[] n : neighbors) {
            int ni = i + n[0], nj = j + n[1];
            if (ni < 0 || ni >= grid.length) continue;
            if (nj < 0 || nj >= grid[i].length) continue;
            if (grid[ni][nj] == '#') count++;
          }
          
          if (cell == 'L' && count == 0) next[i][j] = '#';
          else if (cell == '#' && count >= 4) next[i][j] = 'L';
          else next[i][j] = cell;
          
          if (next[i][j] != cell) changed = true;
        }
      }
      
      if (!changed) return countHashtags(grid);
      
      char[][] tmp = grid;
      grid = next;
      next = tmp;
    }
  }
  
  static int countVisibleOccupied(char[][] grid, int x, int y) {
    int[][] directions = {{-1,-1}, {-1,0}, {-1,1}, { 0,-1}, { 0,1}, { 1,-1}, { 1,0}, { 1,1}};
    int count = 0;
    for (int[] d : directions) {
      int i = x + d[0];
      int j = y + d[1];
      
      while (i >= 0 && i < grid.length &&
        j >= 0 && j < grid[i].length) {
        
        if (grid[i][j] == '#') {
          count++;
          break;
        }
        if (grid[i][j] == 'L') {
          break;
        }
        
        i += d[0];
        j += d[1];
      }
    }
    
    return count;
  }
  
  public static long part2() {
    String[] input = readInput();
    char[][] grid = new char[input.length][];
    for (int i = 0; i < input.length; i++) {
      grid[i] = input[i].toCharArray();
    }
    
    char[][] next = new char[input.length][];
    for (int i = 0; i < input.length; i++) {
      next[i] = new char[input[i].length()];
    }
    while (true) {
      boolean changed = false;
      
      for (int i = 0; i < grid.length; i++) {
        for (int j = 0; j < grid[i].length; j++) {
          
          char cell = grid[i][j];
          
          if (cell == '.') {
            next[i][j] = '.';
            continue;
          }
          
          int visible = countVisibleOccupied(grid, i, j);
          
          if (cell == 'L' && visible == 0) next[i][j] = '#';
          else if (cell == '#' && visible >= 5) next[i][j] = 'L';
          else next[i][j] = cell;
          
          if (next[i][j] != cell) changed = true;
        }
      }
      
      if (!changed) return countHashtags(grid);
      
      char[][] tmp = grid;
      grid = next;
      next = tmp;
    }
  }
  
  public static void run() {
    System.out.println("----- Day 11 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
