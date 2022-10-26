<p align="center"> <img src="./icon.png" width="700" style="border:none;background:none;"/> </p>

# <p align="center"> Channel Flow Simulations </p>

This repository contains a lab notebook to test/demonstrate effects of a modified pressure outflow boundary condition on a simple channel flow simulation.

## Dependencies

Maple: https://github.com/akashdhruv/Maple
Jobrunner: https://github.com/akashdhruv/Jobrunner

## Organization

```
$ tree Channel-Flow

├── Jobfile
├── environment.sh
├── simulation
    ├── Jobfile
    ├── flash.par
    ├── Maplefile
    ├── neumann
    ├── outflowf
        ├── buffer01
        ├── buffer10
        ├── buffer15
        ├── buffer20
├── analysis
    ├── Jobfile
    ├── requirements.txt
    ├── Maplefile
```

## Usage

Once a user has installed necessary libaries/tools, i.e., Jobrunner, Maple, MPI, and ParaView, and designed their customized `environment.sh`, they can submit a simulation by running the following command from the project root directory,

```
jobrunner submit simulation/neumann
jobrunner submit simulation/outflow/buffer01
jobrunner submit simulation/outflow/buffer*
```

Make sure to edit Jobfiles as desired to change/update your schedular configuration.

TIP: use `--show` with `jobrunner setup` and `jobrunner submit` to see the parsed configuration for a working directory derived from Jobfiles along the directory tree.

To visualize data using ParaView run following from the working directory of a job run,

```
flashkit create xdmf -b <begin_number> -e <end_number>
```

The `<begin_number>` and `<end_number>` refer to the files containing the pattern `*_hdf5_plt_cnt_*`. The resulting `*.xmf` file is ParaView compatible.

