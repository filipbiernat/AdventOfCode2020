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


def run():
    print("\nDay 4 - Part A")

    # Passports are separated by blank lines.
    input_entries = open("Day4/input.txt").read().split("\n\n")
    passport_dictionaries = list(map(convert_to_dict, input_entries))

    # Count the number of valid passports - those that have all required fields.
    # Treat cid as optional. In your batch file, how many passports are valid?
    print(sum(map(passport_has_all_the_fields, passport_dictionaries)))
