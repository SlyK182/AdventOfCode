# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/16

import portion

from AdventOfCode.common import load_input, timer


def get_fields_position(rules, valid_tickets):
    fields2pos = {}
    pos2fields = {}
    for col in range(len(valid_tickets[0])):
        available_fields = [
            f
            for f, v in rules.items()
            if all(t[col] in v for t in valid_tickets)
        ]
        pos2fields[col] = available_fields
    for c, af in sorted(pos2fields.items(), key=lambda x: len(x[1])):
        for field in af:
            if field not in fields2pos:
                fields2pos[field] = c
    return fields2pos


def get_rules(rules_as_string):
    rules = {}
    for rule in rules_as_string.split('\n'):
        name, values = rule.split(': ')
        rules[name] = portion.Interval()
        for value in values.split(' or '):
            interval = [int(v) for v in value.split('-')]
            interval.sort()
            rules[name] = rules[name].union(portion.closed(*interval))
    return rules


def get_ticket(ticket_as_string):
    return tuple(map(int, ticket_as_string.split(',')))


def split_ticket_values(ticket, rules):
    valid_intervals = portion.Interval(*list(rules.values()))
    valid_values, invalid_values = [], []
    for value in ticket:
        if value in valid_intervals:
            valid_values.append(value)
        else:
            invalid_values.append(value)
    return valid_values, invalid_values


@timer
def problem1_solution():
    raw_rules, _, other_t = ''.join(load_input(16, 1)).split('\n\n')
    rules = get_rules(raw_rules)
    other_tickets = [get_ticket(t) for t in other_t.split('\n')[1:]]
    ticket_error_rate = 0
    for ticket in other_tickets:
        _, invalid_values = split_ticket_values(ticket, rules)
        if invalid_values:
            ticket_error_rate += sum(invalid_values)
    return ticket_error_rate


@timer
def problem2_solution():
    raw_rules, my_t, other_t = ''.join(load_input(16, 1)).split('\n\n')
    rules = get_rules(raw_rules)
    my_ticket = get_ticket(my_t.split('\n')[1])
    other_tickets = [get_ticket(t) for t in other_t.split('\n')[1:]]
    valid_tickets = []
    for ticket in other_tickets:
        _, invalid_values = split_ticket_values(ticket, rules)
        if not invalid_values:
            valid_tickets.append(ticket)
    fields_position = get_fields_position(rules, valid_tickets)
    result = 1
    for field, pos in fields_position.items():
        if field.startswith('departure'):
            result *= my_ticket[pos]
    return result


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
