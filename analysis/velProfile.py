# Standard libraries
import os
import itertools
import numpy
import matplotlib.pyplot as pyplot

# `boxkit` library
import boxkit.api as boxkit

# Define inputs
#
# `basename` - base name of the output files
#
# `simdir_list` - list of simulation directories
#
# `sim_legend` - simulation legend
#
# `filetag` - prefix of the HDF5 dataset file
#
# `xloc` - location along x-axis where we want
#          the data to be sliced. See flash.par
basename = "INS_Channel_Flow_hdf5_plt_cnt_"

simdir_list = [
    os.getenv("PROJECT_HOME") + os.sep + "simulation/neumann/",
    os.getenv("PROJECT_HOME") + os.sep + "simulation/outflow/buffer01/",
    os.getenv("PROJECT_HOME") + os.sep + "simulation/outflow/buffer10/",
]

sim_legend = [
    r"Reference",
    r"Buffer $1.0$",
    r"Buffer $1.5$",
]

filetag = 3
xloc = 7.0

# eps (epsilon) will be added to `xloc` when creating
# slice from dataset. This done to avoid undesired effects
# when `xloc` is at a block boundary
eps = 1e-12

# Create filenames with proper path. Since we want to compare
# two different boundary condition implementations
filenames = [simdir + basename + str(filetag).zfill(4) for simdir in simdir_list]

# Create a `boxkit` dataset from the list of filenames
# use `flash` as the source
dataset_list = [boxkit.read.dataset(filename, source="flash") for filename in filenames]

# Create slice objects from `boxkit` library
slice_list = [
    boxkit.create.slice(dataset, xmin=xloc - eps, xmax=xloc - eps)
    for dataset in dataset_list
]

# Create empty lists for profile values
# to store result from all the slices in `slice_list`
profile_loc_list = []
profile_val_list = []

# Outer loop over `slice_list`
for slice_ in slice_list:

    # Define empty array to store data from
    # current `slice_`
    profile_val = numpy.array([])
    profile_loc = numpy.array([])

    # Loop over `blocklist` in a given `slice_`
    for block in slice_.blocklist:

        # Get `xindex` corresponding to `xloc`
        # `zindex` is 0
        xindex = (numpy.abs(block.xrange("center") - xloc)).argmin()
        zindex = 0

        # Extract and append velocity and location values in
        # y-direction
        profile_loc = numpy.append(profile_loc, block.yrange("center"))
        profile_val = numpy.append(profile_val, block["velx"][zindex, :, xindex])

    # Append to the list storing values
    # for different slices
    profile_loc_list.append(profile_loc)
    profile_val_list.append(profile_val)


# Exact parabolic solution
# recycle value of `profile_exact`
# update result list
profile_exact = 1 - (2.0 * profile_loc) ** 2
profile_loc_list.append(profile_loc)
profile_val_list.append(profile_exact)

# Create a figure object and set styling
# font/text options. Request latex
pyplot.rc("font", family="serif", size=14, weight="bold")
pyplot.rc("axes", labelweight="bold", titleweight="bold")
pyplot.rc("text", usetex=True)
figure = pyplot.figure(figsize=(5, 3))

# Set marker and linestyle list
marker = itertools.cycle(("o", "s", "d", ".", "*"))
linestyle = itertools.cycle(("-", "--", "-."))

# create a subfigure object
ax = figure.add_subplot()

# Loop over result list and extra invidual values
# from slices
for profile_val, profile_loc in zip(profile_val_list, profile_loc_list):

    # Do the actual plot cycle through marker and linestyles
    # defined earlier
    ax.plot(
        profile_val / numpy.max(profile_val),
        profile_loc,
        # marker=next(marker),
        # markevery=[0] + [*range(1, len(profile_loc) - 1, 10)] + [len(profile_loc) - 1],
        # markersize=5,
        linestyle=next(linestyle),
    )

# Ticks and limits for x and y direction
ax.set_xticks([0.0, 0.5, 1.0])
ax.set_yticks([-0.5, 0.0, 0.5])

# Set labels, title, and legend
ax.set_xlabel(r"$U(y)/u_m$")
ax.set_ylabel(r"$y/l_0$")
ax.set_title(r"$x/l_0={0}$".format(xloc))
ax.legend(sim_legend + [r"Exact"])

# Save figure
pyplot.tight_layout()
pyplot.savefig("velProfile.png", dpi=300)