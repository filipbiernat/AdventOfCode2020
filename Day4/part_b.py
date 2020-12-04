import re


def convert_to_dict(passport_data):
    # Each passport is represented as a sequence of key:value pairs separated by spaces or newlines.
    property_value_list = passport_data.split()  # First split by whitespace.
    return dict([elem.split(":") for elem in property_value_list])  # Then split by colon and keep as key-value.


def passport_has_all_the_fields(passport_entry):
    # The expected fields are as follows:
    #     byr (Birth Year)
    #     iyr (Issue Year)
    #     eyr (Expiration Year)
    #     hgt (Height)
    #     hcl (Hair Color)
    #     ecl (Eye Color)
    #     pid (Passport ID)
    #     cid (Country ID)
    #     Missing cid is fine, but missing any other field is not
    return "byr" in passport_entry and \
        "iyr" in passport_entry and \
        "eyr" in passport_entry and \
        "hgt" in passport_entry and \
        "hcl" in passport_entry and \
        "ecl" in passport_entry and \
        "pid" in passport_entry


def is_byr_valid(val):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    return 1920 <= int(val) <= 2002


def is_iyr_valid(val):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    return 2010 <= int(val) <= 2020


def is_eyr_valid(val):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    return 2020 <= int(val) <= 2030


def is_hgt_valid(val):
    # hgt (Height) - a number followed by either cm or in.
    match = re.match(r"([0-9]+)(in|cm)", val)
    if match:
        num, unit = match.groups()
        # If cm, the number must be at least 150 and at most 193.
        if unit == "cm":
            return 150 <= int(num) <= 193
        # If in, the number must be at least 59 and at most 76.
        elif unit == "in":
            return 59 <= int(num) <= 76
    return False


def is_hcl_valid(val):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    return bool(re.match(r"#[a-f0-9]{6}", val))


def is_ecl_valid(val):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    return bool(re.match(r"(amb|blu|brn|gry|grn|hzl|oth)", val))


def is_pid_valid(val):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    return bool(re.match(r"^\d{9}$", val))


def is_passport_valid(passport_entry):
    # The line is moving more quickly now, but you overhear airport security talking about how passports
    # with invalid data are getting through. Better add some data validation, quick!
    # You can continue to ignore the cid field, but each other field has strict rules about what values
    # are valid for automatic validation.
    return passport_has_all_the_fields(passport_entry) and \
        is_byr_valid(passport_entry["byr"]) and \
        is_iyr_valid(passport_entry["iyr"]) and \
        is_eyr_valid(passport_entry["eyr"]) and \
        is_hgt_valid(passport_entry["hgt"]) and \
        is_hcl_valid(passport_entry["hcl"]) and \
        is_ecl_valid(passport_entry["ecl"]) and \
        is_pid_valid(passport_entry["pid"])


def run():
    print("\nDay 4 - Part B")

    # Passports are separated by blank lines.
    input_entries = open("Day4/input.txt").read().split("\n\n")
    passport_dictionaries = list(map(convert_to_dict, input_entries))

    # Count the number of valid passports - those that have all required fields and valid values.
    # Continue to treat cid as optional. In your batch file, how many passports are valid?
    print(sum(map(is_passport_valid, passport_dictionaries)))
