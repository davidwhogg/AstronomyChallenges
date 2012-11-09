"""
Punking Daft to make a map--reduce illustration.
"""

from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)
rc("./weaklensing.tex")
import daft

def recurse(pgm, nodename, level, c):
    if level > 5:
        return
    r = c / 2
    r1nodename = "r%02d%04d" % (level, r)
    if 2 * r == c:
        print "adding ", r1nodename
        pgm.add_node(daft.Node(r1nodename, r"reduce", 2**level * (r + 0.5) - .5, 3 - 0.75 * level, aspect=1.9))
    pgm.add_edge(nodename, r1nodename)
    if 2 * r == c:
        return recurse(pgm, r1nodename, level + 1, r)
    return

if __name__ == "__main__":
    pgm = daft.PGM([10, 6], origin=[-0.5, -1.5])

    pgm.add_node(daft.Node("query", r'\texttt{"kittens?"}', 3.5, 4.2, aspect=3., plot_params={"ec":"none"}))

    for c in range(16):
        nodename = "cpu%04d" % c
        pgm.add_node(daft.Node(nodename, r"\texttt{%s}" % nodename, c, 3., aspect=1.9))
        pgm.add_edge("query", nodename)
        level = 1
        recurse(pgm, nodename, level, c)

    pgm.render()
    pgm.figure.savefig("mapreduce.pdf")
    pgm.figure.savefig("mapreduce.png", dpi=200)
