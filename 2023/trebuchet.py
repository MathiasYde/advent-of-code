INPUT_FILEPATH = "trebuchet.txt"

def trebuchet_part1():
    calibration_sum = 0
    
    with open(INPUT_FILEPATH, "r") as file:
        for line in file.readlines():
            line = line.strip()
            digits = [char for char in line if char.isdigit()]
            
            first_digit, last_digit = int(digits[0]), int(digits[-1])
            line_sum = first_digit * 10 + last_digit
            
            calibration_sum += line_sum
            print(line, digits, first_digit, last_digit)
    
    print(f"{calibration_sum=}")

def trebuchet_part2():
    calibration_sum = 0
    
    numbers = {
        "one": 1,"two": 2,"three": 3,
        "four": 4,"five": 5,"six": 6,
        "seven": 7,"eight": 8,"nine": 9,
        "1": 1,"2": 2,"3": 3,
        "4": 4,"5": 5,"6": 6,
        "7": 7,"8": 8,"9": 9
    }
    
    def parse_line(line: str):
        digits = []
        
        # this is probably a really shitty way to do this lol
        for i in range(0, len(line) + 1):
            for j in range(i, len(line) + 1):
                substring = line[i:j]
                if number := numbers.get(substring):
                    digits.append(number)
                    
        return digits
        
    def try_index(it, i, fail_value=None):
        try:
            return it[i]
        except Exception:
            return fail_value
    
    with open(INPUT_FILEPATH, "r") as file:
        for line in file.readlines():
            line = line.strip()
            digits = parse_line(line)
            
            first_digit = try_index(digits, 0)
            last_digit = try_index(digits, -1, first_digit)
            
            print(line, digits, first_digit, last_digit)
            calibration_sum += first_digit * 10 + last_digit
    
    print(f"{calibration_sum=}")

def main():
    trebuchet_part2()

if __name__ == "__main__":
    main()
