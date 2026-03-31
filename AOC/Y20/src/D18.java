import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class D18 {
  private static final Path INPUT = Path.of("src/inputs/d18.txt");
  
  private static String[] readInput() {
    try {
      List<String> lines = Files.readAllLines(INPUT);
      return lines.toArray(new String[0]);
    } catch (Exception e) {
      throw new RuntimeException("Failed to read input", e);
    }
  }
  
  abstract static class Node {
    abstract long evaluate();
  }
  
  static class NumberNode extends Node {
    long value;
    
    NumberNode(long value) {
      this.value = value;
    }
    
    @Override
    long evaluate() {
      return value;
    }
  }
  
  static class BinaryNode extends Node {
    char op;
    Node left;
    Node right;
    
    BinaryNode(char op, Node left, Node right) {
      this.op = op;
      this.left = left;
      this.right = right;
    }
    
    @Override
    long evaluate() {
      if (op == '+') {
        return left.evaluate() + right.evaluate();
      }
      return left.evaluate() * right.evaluate();
    }
  }
  
  class Tokenizer {
    
    static List<String> tokenize(String input) {
      List<String> tokens = new ArrayList<>();
      int i = 0;
      
      while (i < input.length()) {
        char c = input.charAt(i);
        
        if (Character.isWhitespace(c)) {
          i++;
        }
        else if (Character.isDigit(c)) {
          StringBuilder number = new StringBuilder();
          while (i < input.length() && Character.isDigit(input.charAt(i))) {
            number.append(input.charAt(i++));
          }
          tokens.add(number.toString());
        }
        else if (c == '+' || c == '*' || c == '(' || c == ')') {
          tokens.add(Character.toString(c));
          i++;
        }
        else {
          throw new RuntimeException("Unexpected character: " + c);
        }
      }
      
      return tokens;
    }
  }
  
  static class Parser {
    
    private final List<String> tokens;
    private int position = 0;
    
    Parser(List<String> tokens) {
      this.tokens = tokens;
    }
    
    Node parse() {
      Node result = parseExpression();
      if (position != tokens.size()) {
        throw new RuntimeException("Unexpected tokens at end");
      }
      return result;
    }
    
    private Node parseExpression() {
      Node node = parseTerm();
      
      while (position < tokens.size()) {
        String token = tokens.get(position);
        
        if (token.equals("+") || token.equals("*")) {
          position++;
          Node right = parseTerm();
          node = new BinaryNode(token.charAt(0), node, right);
        } else {
          break;
        }
      }
      
      return node;
    }
    
    private Node parseTerm() {
      String token = tokens.get(position);
      
      if (token.equals("(")) {
        position++;
        Node node = parseExpression();
        if (!tokens.get(position).equals(")")) {
          throw new RuntimeException("Missing closing parenthesis");
        }
        position++;
        return node;
      }
      
      if (Character.isDigit(token.charAt(0))) {
        position++;
        return new NumberNode(Long.parseLong(token));
      }
      
      throw new RuntimeException("Unexpected token: " + token);
    }
  }
  
  public static long part1() {
    String[] input = readInput();
    long sum = 0;
    
    for (String line : input) {
      Node tree = (new Parser(Tokenizer.tokenize(line))).parse();
      sum += tree.evaluate();
    }
    
    return sum;
  }
  
  static class Parser2 {
    
    private final List<String> tokens;
    private int position = 0;
    
    Parser2(List<String> tokens) {
      this.tokens = tokens;
    }
    
    Node parse() {
      Node result = parseMultiplication();
      if (position != tokens.size()) {
        throw new RuntimeException("Unexpected tokens at end");
      }
      return result;
    }
    
    // lowest precedence
    private Node parseMultiplication() {
      Node node = parseAddition();
      
      while (position < tokens.size() &&
        tokens.get(position).equals("*")) {
        
        position++;
        Node right = parseAddition();
        node = new BinaryNode('*', node, right);
      }
      
      return node;
    }
    
    // higher precedence
    private Node parseAddition() {
      Node node = parseTerm();
      
      while (position < tokens.size() &&
        tokens.get(position).equals("+")) {
        
        position++;
        Node right = parseTerm();
        node = new BinaryNode('+', node, right);
      }
      
      return node;
    }
    
    private Node parseTerm() {
      String token = tokens.get(position);
      
      if (token.equals("(")) {
        position++;
        Node node = parseMultiplication(); // IMPORTANT
        if (!tokens.get(position).equals(")")) {
          throw new RuntimeException("Missing ')'");
        }
        position++;
        return node;
      }
      
      if (Character.isDigit(token.charAt(0))) {
        position++;
        return new NumberNode(Long.parseLong(token));
      }
      
      throw new RuntimeException("Unexpected token: " + token);
    }
  }
  
  
  public static long part2() {
    String[] input = readInput();
    long sum = 0;
    
    for (String line : input) {
      Node tree = (new Parser2(Tokenizer.tokenize(line))).parse();
      sum += tree.evaluate();
    }
    
    return sum;
  }
  
  public static void run() {
    System.out.println("----- Day 18 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
