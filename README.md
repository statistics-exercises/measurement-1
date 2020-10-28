# Measurement

Last week we introduced the method of moments.  In doing so we firmed up the notion of a __statistic__ by showing how statistics can be calculated by sampling from a distribution multiple times.  We then introduced the method of moments allows us to derive estimators for the parameters of an underlying random variable.  We saw that some of these estimators provided a good estimate for the parameters of the underlying distribution.  Some of these estimators generated terrible estimators for the underlying variable, however.  In this series of exercises, we are thus going to try to introduce some theory to determine whether or not the estimators that we derive are good or bad.  

So as to look at this a different way we are going to consider how we would use statistics when analysing the results from a series of experiments.  The experiment we are going to imagine that we have done involves using an agitator to generate some bubbles in the water.  When we look at the water that was agitated through a microscope we see something that looks like this: 

![](bubbles.jpg)

In other words, we have a number of bubbles all of which have different sizes.  We quantify the sizes of the bubbles by measuring their radii.  We can then talk about the distribution of bubble sizes.  In the file called bubbles.dat that you look at by clicking the tab called bubbles in the panel on the left, I have a list of radii in micrometres for 200 of these bubbles.  

To complete the exercise make a plot of these bubble radii.  The x-coordinates of the points should just be the integers starting at 0 and finishing at 199.  The y-coordinates will be the bubble radii.
