"""
Crowded field analysis
======================

The Brewer, Foreman-Mackey, Hogg paper

"""

from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)
import daft
pgm = daft.PGM([4.6, 3.2], origin=[1.2, 1.2])
wide = 1.5
verywide = 1.5 * wide
dy = 0.75

# pixels
el_x, el_y = 5., 2.
pgm.add_plate(daft.Plate([el_x - 0.6, el_y - 0.6, 1.2, 1 * dy + 0.3], label="pixels $i$"))
pgm.add_node(daft.Node("Ii", r"$I_i$", el_x, el_y + 0 * dy, observed=True))

# intensity fields
ph_x, ph_y = el_x - 1.5, el_y + 1 * dy
pgm.add_node(daft.Node("Ixyt", r"$I(x,y,t)$", ph_x, ph_y, aspect=verywide))
pgm.add_edge("Ixyt", "Ii")

# image
sc_x, sc_y = ph_x - 0.5, ph_y + 1.5 * dy
pgm.add_node(daft.Node("psf", r"psf", sc_x, sc_y + 0 * dy, aspect=wide))
pgm.add_edge("psf", "Ixyt")
pgm.add_node(daft.Node("sky", r"sky", sc_x + 1, sc_y + 0 * dy, aspect=wide))
pgm.add_edge("sky", "Ixyt")
pgm.add_node(daft.Node("noise", r"noise", sc_x + 2, sc_y + 0 * dy, aspect=wide))
pgm.add_edge("noise", "Ii")

# stars
star_x, star_y = el_x - 3, el_y + 0 * dy
pgm.add_plate(daft.Plate([star_x - 0.6, star_y - 0.6, 1.2, 2 * dy + 0.3], label="stars $n$"))
pgm.add_node(daft.Node("star flux", r"$S_n$", star_x, star_y + 1 * dy))
pgm.add_edge("star flux", "Ixyt")
pgm.add_node(daft.Node("star pos", r"$x_n,y_n$", star_x, star_y, aspect=wide))
pgm.add_edge("star pos", "Ixyt")

# hyper
pgm.add_node(daft.Node("lf", r"${\mathrm{d}}N/{\mathrm{d}}S$", star_x, sc_y, aspect=wide))
pgm.add_edge("lf", "star flux")

# done
pgm.render()
pgm.figure.savefig("crowded.pdf")
pgm.figure.savefig("crowded.png", dpi=150)
