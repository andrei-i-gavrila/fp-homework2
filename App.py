import UI
import traceback
import Helper

def cmds_list():
    return {
        "help": UI.help,
        "add": UI.add,
        "insert": UI.insert,
        "remove": UI.remove,
        "replace": UI.replace,
        "list": UI.lists,
        "sum": UI.sums,
        "product": UI.product,
        "filter": UI.filter,
        "gen": Helper.fake_fill,
        "clear": Helper.clear
    }


def invalid(ls, args):
    print("Invalid command. You could use some help")


def get_cmd(command):
    cmds = cmds_list()
    if command in cmds:
        return cmds[command]
    else:
        return invalid


def read_command():
    long_cmd = input(">>").split()
    if(len(long_cmd)) == 0:
        return "gibberish", ["irrelevant"]
    return long_cmd[0], long_cmd[1:]


def run():
    ls = []
    Helper.fake_fill(ls, [])
    while True:
        cmd, args = read_command()
        if cmd == "exit":
            return
        cmd = get_cmd(cmd)

        try:
            cmd(ls, args)
        except Exception as ex:
            # traceback.print_exc()
            print(ex)
