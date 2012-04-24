# Astronomy Challenges

A repository for notes about hard inference or data analysis problems
in astronomy, astrophysics, and cosmology.

### Author:

David W. Hogg (NYU)

### License:

Copyright 2012 the author.  You may copy and distribute this provided
you make no changes to it whatsoever.

### Revision history:

This document is a work in progress; it isn't even in a "first draft"
state.  This version is dated 2012-04-23.

### Probabilistic catalogs

A catalog is, in some sense, a quantitative explanation of an image.
In probabilistic inference, there ought to be a posterior PDF over the
set of all possible catalogs that could explain some set of imaging
data.  This problem is a hard one, for various reasons, not limited
to:

- Different catalogs will have different model complexities and
  numbers of parameters.  Some sources will have ambiguous properties:
  Is this one galaxy or two?  Is this a star or a galaxy?  And so on.
  Any description of the PDF in catalog space must face this.

- There are various ideas about sampling in complex spaces like this,
  including reversible-jump MCMC and non-parametric sampling methods.
  These have almost never been applied in Astronomy (though see papers
  on future LISA data and rumors from Feroz at Cambridge).  An
  efficient method for sampling in catalog space at non-fixed
  complexity could have an enormous effect on astrophysics, and it is
  a non-trivial problem.

- For many applications, we would like to construct a catalog that
  makes use of all the imaging data available on each included source,
  and which can adapt and improve as new data arrive.  That requires
  significant computational resources but also some ideas about
  frameworks that are practical and useful.

- There are relationships between image modeling, catalog estimation,
  noise-model inference, and PSF estimation, of course.  More about
  some of this below.

### Weak lensing

In studies of weak lensing, the objective is to find the shear
map---the tensor distortion field being applied to galaxies---as a
function of sky position and redshift (distance).  This is challenging
because:

- Galaxies have non-trivial morphologies.  There is currently no
  "prior PDF" over galaxy morphologies or appearances, so heuristics
  are used to estimate the shear map in an average way over a set of
  galaxies deemed large enough to be treated as being circular *on
  average*.  That is, there is no way to obtain reliable shear
  information from any single or small set of galaxies.  A prior PDF
  over galaxy images might help enormously with this.  To my knowledge
  there has never even been an attempt at this; my intuition is that
  even simple attempts might yield excellent results.  An extremely
  simple attempt would be to pixelize the galaxies on some physical
  scale, and then do hierarchical inference on compact distributions
  in the space of pixel values.

- Telescopes have non-trivial and temporally and spatially varying
  point-spread functions.  That is, every galaxy in every image is
  convolved with its own unique point-spread function.  Current
  methods for inferring, interpolating, and deconvolving the
  point-spread function are limited in their approaches and
  capabilities.  There is much room for improvement.

### Astrophysics at low signal-to-noise

Astronomers care about the sources at...

- time domain issues (moving and variable)

- source detection in online methods

- confusion noise and crowding

- Galactic center and the like

- outer SS objects and the like

### Stochastic variability

- Quasars and reverberation

- exoplanet transits at the variability limit

- quasi-periodic variable stars

### Spectroscopic modeling and classification

- sparse methods

- simultaneous redshift estimation and spectral classification

- combining theory-driven and data-driven models sensibly

### Spatial models of galaxies

- stars, extinctions, HI, etc -> model of the Milky Way

- same for other galaxies

### Dynamical models of galaxies

- dynamical modeling, esp marginalization over the DF

### Instrument calibration

- PSF estimation, especially for high dynamic-range imaging (eg, Fergus et al)

- self calibration

- probabilistic darks and flat-fields

- GPs for atmospheric calibration

- spectroscopic extraction

### Networks of autonomous telescopes

### Adaptive optics
