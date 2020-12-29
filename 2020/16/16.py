import re
import numpy as np
import operator


def process_fields(field_lines):
    """Returns dictionary of {field name: list of range tuples}."""
    fields = {}
    for field_line in field_lines:
        # get field name
        field = re.match(r"(.*)\:", field_line).group(1)
        # get value ranges
        ranges = re.findall(r"[0-9]+\-[0-9]+", field_line)
        pairs = []
        for r in ranges:
            split = r.split('-')
            low = int(split[0])
            high = int(split[1])
            pairs.append((low, high))
        # add field and list of value ranges
        fields[field] = pairs
    return fields


def check_value(val, fields):
    """ Checks if a value is valid for every field."""
    valid_fields = []
    for ranges in fields.values():
        # if value is in any range of the field, then True, else False
        valid_ranges = [(l <= val <= h) for (l, h) in ranges]
        valid_fields.append(any(valid_ranges))
    # return True if value is valid in at least one field
    return any(valid_fields)


def part1(l):
    # process valid fields
    fields = process_fields(l[0].split("\n"))

    invalid_sum = 0
    # process nearby tickets
    for ticket in l[2].split("\n")[1:-1]:
        # process each value
        for val in ticket.split(','):
            # check if value is valid for every field
            valid_val = check_value(int(val), fields)
            # if value is not valid for any field, then add to sum
            if not valid_val:
                invalid_sum += int(val)
    return invalid_sum


def column_field(values, fields):
    """Returns a set of possible field names given column values."""
    possible = set()
    for k in fields.keys():
        if all([any([(l <= val <= h) for (l, h) in fields[k]]) for val in values]):
            possible.add(k)
    return possible


def part2(l):
    # process valid fields
    fields = process_fields(l[0].split("\n"))
    # process nearby tickets
    valid_tickets = []
    for ticket in l[2].split("\n")[1:-1]:
        valid_ticket = True
        # process each value
        for val in ticket.split(','):
            # check if value is valid for every field
            valid_val = check_value(int(val), fields)
            # if value is not valid, ticket is invalid
            if not valid_val:
                valid_ticket = False
                break
        if valid_ticket:
            valid_tickets.append(ticket.split(','))

    # process valid tickets
    possible = {} # map from column index to possible field names {int: set(str)}
    ticket_arr = np.array(valid_tickets).astype(int)
    for num, col in enumerate(ticket_arr.T):
        possible_fields = column_field(col, fields)
        possible[num] = possible_fields

    # find actual fields by filtering possible
    actual = {} # map from column index to actual field name {int: str}
    taken = set()
    while possible:
    # find single field
        single_idx, single_field = [(f,n) for (f, n) in possible.items() if len(n) == 1][0]
        taken.update(single_field)
        # record the actual field
        actual[single_idx] = next(iter(single_field))
        # remove idx from possible
        del possible[single_idx]
        # remove field from other columns
        for f in possible.keys():
            possible[f] -= single_field

    # return product of all departure fields of your ticket
    your_ticket = list(map(int, l[1].split('\n')[-1].split(",")))
    product = 1
    for index in [i for i in actual if actual[i].startswith('departure')]:
        product *= your_ticket[index]
    return product


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        l = list(f.read().split("\n\n"))
    print("Part 1:", part1(l))
    print("Part 2:", part2(l))
