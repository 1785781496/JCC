from anytree import Node, RenderTree
from anytree.exporter import DotExporter


def init():
    udo = Node("Udo")
    marc = Node("Marc", parent=udo)
    lian = Node("Lian", parent=marc)
    dan = Node("Dan", parent=udo)
    jet = Node("Jet", parent=dan)
    jan = Node("Jan", parent=dan)
    joe = Node("Joe", parent=dan)

    print(udo)
    for pre, fill, node in RenderTree(udo):
        print("%s%s" % (pre, node.name))

    # graphviz needs to be installed for the next line!
    # DotExporter(udo).to_picture("udo.png")
    DotExporter(udo).to_dotfile("udo.dot")


if __name__ == '__main__':
    init()
