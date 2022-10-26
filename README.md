<p align="center"> <img src="./icon.png" width="700" style="border:none;background:none;"/> </p>

# <p align="center"> Channel Flow Simulations </p>

This repository contains a lab notebook to test/demonstrate effects of a modified pressure outflow boundary condition on a simple channel flow simulation.

## Dependencies

## Organization

```
$ tree Boiling-Simulations

├── Jobfile
├── environment.sh
├── sites
    ├── hello
        ├── Makefile.h
├── software
    ├── Jobfile
    ├── Flash-X
    ├── AMReX
    ├── FlashKit
    ├── HDF5
├── simulation
    ├── PoolBoiling
        ├── Jobfile
        ├── flashOptions.sh
        ├── example2D
            ├── Jobfile
            ├── flashOptions.sh
            ├── flashBuild.sh
            ├── flashRun.sh
            ├── flash.par
    ├── FlowBoiling
├── analysis
    ├── Jobfile
    ├── requirements.txt
```

## Usage
