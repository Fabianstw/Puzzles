import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.List;

public class D4 {
  private static final Path INPUT = Path.of("src/inputs/d4.txt");

  private static String[] readInput() {
    try {
      List<String> lines = Files.readAllLines(INPUT);
      return lines.toArray(new String[0]);
    } catch (Exception e) {
      throw new RuntimeException("Failed to read input", e);
    }
  }

  private static HashMap<Integer, HashMap<String, String>> parseInput(String[] input) {
    HashMap<Integer, HashMap<String, String>> passports = new HashMap<>();
    int count = 0;
    passports.put(count, new HashMap<>());

    for (String line : input) {
      if (line.isBlank()) {
        count++;
        passports.put(count, new HashMap<>());
      } else {
        String[] parts = line.split(" ");
        for (String part : parts) {
          String[] kv = part.split(":", 2); // split only once
          passports.get(count).put(kv[0], kv[1]);
        }
      }
    }
    return passports;
  }

  public static long part1() {
    HashMap<Integer, HashMap<String, String>> passports = parseInput(readInput());
    int valid = 0;

    for (int i = 0; i < passports.size(); i++) {
      HashMap<String, String> passport = passports.get(i);
      if (passport.size() == 8) {
        valid++;
      } else if (passport.size() == 7 && !passport.containsKey("cid")) {
        valid++;
      }
    }

    return valid;
  }

  public static long part2() {
    HashMap<Integer, HashMap<String, String>> passports = parseInput(readInput());
    int valid = 0;

    for (int i = 0; i < passports.size(); i++) {
      HashMap<String, String> passport = passports.get(i);
      if (passport.size() == 8 || passport.size() == 7 && !passport.containsKey("cid")) {
        if (!(1920 <= Integer.parseInt(passport.get("byr"))
            && Integer.parseInt(passport.get("byr")) <= 2002)) {
          continue;
        }
        if (!(2010 <= Integer.parseInt(passport.get("iyr"))
            && Integer.parseInt(passport.get("iyr")) <= 2020)) {
          continue;
        }
        if (!(2020 <= Integer.parseInt(passport.get("eyr"))
            && Integer.parseInt(passport.get("eyr")) <= 2030)) {
          continue;
        }

        String h = passport.get("hgt");
        if (!((h.endsWith("cm")
                && 150 <= Integer.parseInt(h.split("cm")[0])
                && Integer.parseInt(h.split("cm")[0]) <= 193)
            || (h.endsWith("in")
                && 59 <= Integer.parseInt(h.split("in")[0])
                && Integer.parseInt(h.split("in")[0]) <= 76))) {
          continue;
        }
        if (!(passport.get("hcl").startsWith("#")
            && passport.get("hcl").split("#")[1].length() == 6
            && passport.get("hcl").split("#")[1].matches("[a-f0-9]+"))) {
          continue;
        }
        if (!(passport.get("ecl").equals("amb")
            || passport.get("ecl").equals("blu")
            || passport.get("ecl").equals("brn")
            || passport.get("ecl").equals("gry")
            || passport.get("ecl").equals("grn")
            || passport.get("ecl").equals("hzl")
            || passport.get("ecl").equals("oth"))) {
          continue;
        }
        if (!(passport.get("pid").length() == 9 && passport.get("pid").matches("[0-9]+"))) {
          continue;
        }
        valid++;
      }
    }

    return valid;
  }

  public static void run() {
    System.out.println("----- Day 4 -----");
    System.out.println("Part 1: " + part1());
    System.out.println("Part 2: " + part2());
    System.out.println("-----------------\n");
  }
}
