# Swirl Net

This is a tutorial on using deep neural networks to predict intense rotation near the surface in thunderstorms.

# Requirements

* jupyter
* numpy
* scipy
* matplotlib
* xarray
* pandas
* tensorflow
* keras

If you want to install these libraries on your local machine, the [Miniconda](https://conda.io/miniconda.html) Python package manager is recommended. Please follow the link and instructions to install the appropriate Miniconda for your OS. After Miniconda is installed, either install the packages directly with `conda install` or create a conda environment (bash shell required). Tensorflow with GPU support requires a NVIDIA GPU with CUDA and cuDNN to be installed. Specific installation instructions are beyond the scope of this tutorial, but more information about installing tensorflow can be found [here](https://www.tensorflow.org/install/). The easiest way to get access to a GPU with deep learning capabilities is to use a Deep Learning image on AWS, Google Cloud, or Azure or find an appropriate docker container. To install the necessary libraries without GPU support, please use the following commands:

```bash
conda create --name deep -c conda-forge python=3.6 numpy scipy matplotlib pandas netcdf4 xarray jupyter
# Activate the environment
source activate deep
# Install tensorflow and keras from their PyPI binaries
pip install tensorflow
pip install keras
```

