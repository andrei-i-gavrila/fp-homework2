def help():
    return "Shows this menu"


def add():
    return "Adds the complex number of form <a+bi>, <a> or <bi> to the list\nSyntax: add <number>"


def insert():
    return "Inserts complex number of form <a+bi>, <a> or <bi> at given position\nSyntax: insert <number> at <position>"


def remove():
    return "Removes numbers from the list\nSyntax: remove <position>\nSyntax: remove <start> to <end>"


def replace():
    return "Replaces all occurences of a given number to another\nSyntax: replace <old number> with <new number>"


def lists():
    return "Lists the numbers\nSyntax: list\nSyntax: list real <start> to <end>\nSyntax: list modulo [<|=|>] <number>"


def sums():
    return "Prints the sum of a given range\nSyntax: sum\nSyntax: sum <start> to <end>"


def product():
    return "Prints the product of a given range\nSyntax: product\nSyntax: product <start> to <end>"


def filter():
    return "Filters the numbers\nSyntax: filter real\nSyntax: filter modulo [<|=|>] <number>"
