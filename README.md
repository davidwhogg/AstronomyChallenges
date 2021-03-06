# Astronomy Challenges

A repository for notes about hard inference or data analysis problems
in astronomy, astrophysics, and cosmology.

### Author:

David W. Hogg (NYU)

### Acknowledgements:

These ideas come from many quarters; at least I am indebted to
- Dustin Lang (Princeton)
- Hans-Walter Rix (MPIA)
- Sam Roweis (deceased)

### License:

Copyright 2012, 2013, 2014 the author.  **All rights reserved.**

### Revision history:

This document is a work in progress; it isn't even in a "first draft"
state.  This version is dated 2014-07-05.  I generally put the thing
I am most interested in first; that is, I tend to prepend.

## Three-dimensional modeling of the Milky Way

- Dust modeling in three dimensions
- Mass modeling with realistic models
- Phase-space models in 6-d that don't rely on integrability

## Cosmic microwave background

- Use spatial priors in addition to spectral-energy (wavelength or frequency dependence) priors to separate independent components or layers that contribute to the *Planck* (or other) imaging data.
- Use parameterized pdfs (for spatial covariance) in place of priors to do hierarchical inference of the fundamental cosmological signature, the secondary anisotropies, and the Galaxy.
- Try out standard unsupervised methods like ICA and so on to see if there are insights to be gleaned.

## Radio interferometry

Interferometers measure correlations (amplitude and phase) between
antennae, each of which sees a noisy sky (noisy because of finite
antenna temperature.  The standard practice in radio astronomy is to
run some form of *Clean*, which is an algorithm to reconstruct a plausible
sky image from the correlations on a finite set of baselines.  There are
many variants of Clean, but most (perhaps all) have many problems:

* There is no probabilistic model of the data stream; there is no likelihood function.
* Priors are either not specified or else extremely naive.
* Parts of the sky are often set to zero by hand.
* The algorithms do not generally return uncertainty estimates on the reconstructed scene.
* There is no way to quantitatively compare different scene options.

## Probabilistic catalogs

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

## Weak lensing

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

## Models of spectra

- Empirical (data-driven) models of spectra (or images or anything)
  that are *not* well described by linear subspaces.  Methods like
  PCA, HMF, and other matrix factorization methods are fastest and
  easiest and most used in astronomy when the data are thought of as
  filling a K-dimensional linear subspace.  I mean by this that it is
  assumed that *any* linear combination of data points would be a
  realistic, sensible new data point.  In reality, often the data live
  in a much smaller subspace that is *not* linear; that is, many
  possible linear combinations would not be sensible objects.  One
  very simple approach worth exploring would be to perform a matrix
  factorization but then permit very informative priors on the
  "coefficient space" to be learned, like a multi-component mixture of
  Gaussians.  Another approach is to apply a very strong L1-norm or
  other "sparseness" prior at the subspace learning stage to
  discourage mixing of the eigenspectra; then the matrix factorization
  should locate a set of archetypes rather than a subspace.

- One application of a non-linear data-driven model is in fitting
  stars, where it is understood that the fundamental physical model is
  driven by temperature, surface gravity, and metallicity, each of
  which affects the spectrum non-linearly.  A successful data-driven
  model of stars would capture their variation without being able to
  fit or generate obvious non-stars.  It would also find spectroscopic
  binaries, something that hasn't been done in large surveys to date
  (to my knowledge).

- Another application is in fitting quasars, where there is no precise
  physical model but it is known that linear combinations of quasars
  are not themselves realistic quasars!

- Continuing with the more general brain-storm: Use of sparse methods;
  modeling collections of spectra without previously classifying them
  into groups of similar types (galaxy, star, quasar, etc).

- simultaneous redshift estimation and spectral classification

- more specific: looking at stellar variations around emission
  lines to determine chromospheric activity; correlation of that
  against age indicators; data-driven age measure for stars?

- One holy grail is some principled combination of theory-driven and
  data-driven models; that is, there are pretty-good models and
  excellent observations; how do we tweak the models using the
  observations or otherwise combine data-driven and model-driven
  methods?

## Instrument calibration

- In many cases (most?) the science data are more valuable for
  calibration purposes than any specifically designed calibration data
  or program.  One interesting question is whether a telescope+camera
  flatfield, dark, and noise model could be inferred from a set of
  data with no reference to the calibration programs.  One place to
  try this is the HST Archive, where all HST data ever taken are
  available.  Question: Could HST have been calibrated without its
  (expensive, time-consuming) calibration programs!

- Related to the above, a question asked of me by Bernhard Schölkopf:
  If you had the library of every image ever taken by some digital
  camera, could you figure out its dark, flat, and noise properties?
  This is *harder* than the astronomy problem because the scenes are
  more complicated, but *easier* because more of the pixels are well
  illuminated in more photos.

- PSF estimation, especially for high dynamic-range imaging (eg,
  Fergus et al).

- Priors on calibration parameters, especially PSFs (which vary with
  the atmosphere and telescope configuration) and world-coordinate
  systems (astrometric calibration).  We generally infer these without
  priors, but for PSFs in particular, usually the data are noisy and
  the inferences are noisier than they could be given that we know a
  *lot* about what kinds of PSFs are possible.

- Probabilistic darks and flat-fields: We usually use point estimates
  for these, but is there any place where there is an advantage to
  having a probabilistic description and/or is this necessary?

- GPs for atmospheric calibration: The atmosphere varies
  stochastically (in brightness and transparency) but in a continuous
  fashion.  This sounds like a great application for Gaussian
  Processes.

- Spectroscopic extraction: Right now there is a lot of reliance on
  calibration data, with both too much and too little flexibility in
  the instrument model: Too much flexibility because each exposure
  sequence (arc, flat, science, flat, arc) is calibrated independently
  (no continuity or priors or etc).  Too little flexibility because
  the science exposure is supposed to be at the precise interpolated
  mean of the surrounding calibration data.

## Astrophysics at low signal-to-noise

Astronomers care about the sources at...

- time domain issues (moving and variable)

- source detection in online methods

- confusion noise and crowding

- Galactic center and the like

- outer SS objects and the like

## Stochastic variability

- Quasars and reverberation

- exoplanet transits at the variability limit

- quasi-periodic variable stars, like RR Lyrae

## Spatial models of galaxies

- stars, extinctions, HI, etc -> model of the Milky Way

- same for other galaxies

## Dynamical models of galaxies

- dynamical modeling, esp marginalization over the DF

## Networks of autonomous telescopes

## Adaptive optics
