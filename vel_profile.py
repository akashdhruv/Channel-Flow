# Standard libraries
import itertools
import numpy
import matplotlib.pyplot as pyplot

# BoxKit library
import boxkit.api as boxkit

# Define inputs filetag and xslice location
filetag = 100
xslice_loc = 5

# Create filenames with proper path
filenames = [
    "neumann/INS_Channel_Flow_hdf5_plt_cnt_" + str(filetag).zfill(4),
    "outflow/INS_Channel_Flow_hdf5_plt_cnt_" + str(filetag).zfill(4),
]

# Create a BoxKit dataset
dataset_list = [boxkit.read.dataset(filename, source="flash") for filename in filenames]

# Create the slice object from BoxKit
xslice_list = [
    boxkit.create.slice(dataset, xmin=xslice_loc, xmax=xslice_loc)
    for dataset in dataset_list
]

# Create empty lists for profile values
profile_loc_list = []
profile_val_list = []

# Loop over blocks in the slice
for xslice in xslice_list:

    profile_val = numpy.array([])
    profile_loc = numpy.array([])

    for block in xslice.blocklist:

        # Find center locations
        xcenter, ycenter = (
            numpy.linspace(
                block.xmin + block.dx / 2, block.xmax - block.dx / 2, block.nxb
            ),
            numpy.linspace(
                block.ymin + block.dy / 2, block.ymax - block.dy / 2, block.nyb
            ),
        )

        # Get xindex corresponding to xslice_loc
        xindex = (numpy.abs(xcenter - xslice_loc)).argmin()

        # Build velocity profile information
        profile_loc = numpy.append(profile_loc, ycenter)
        profile_val = numpy.append(profile_val, block["velx"][0, :, xindex])

    profile_loc_list.append(profile_loc)
    profile_val_list.append(profile_val)

# Create a figure object and set styling
pyplot.rc("font", family="serif", size=15)
figure = pyplot.figure()

# Set marker list
marker = itertools.cycle(("o", "s", "d", ".", "*"))

# Loop over data and plot
for profile_val, profile_loc in zip(profile_val_list, profile_loc_list):
    pyplot.plot(
        profile_val,
        profile_loc,
        marker=next(marker),
        markevery=[0] + [*range(1, len(profile_loc) - 1, 10)] + [len(profile_loc) - 1],
        markersize=5,
    )

# Set labels, title, and legend
pyplot.xlabel(r"$U(y)$")
pyplot.ylabel(r"$y$")
pyplot.title("Velocity profile, " + r"$x={0}$".format(xslice_loc))
pyplot.legend(["without Forcing", "with Forcing"])

# Save figure
pyplot.tight_layout()
pyplot.savefig("vel_profile.png", dpi=200)
