# Manually Annotated Drone Imagery Dataset for Automatic Coastline Delineation in Diverse Coastal Environments (MADRID)

This repository contains the corresponding code and training configurations for the dataset [MADRID v0.1](https://doi.org/10.5281/zenodo.11237140). The raw, unannotated full set of collected drone images can be found [here](https://doi.org/10.5281/zenodo.11237140).

## Installation

### Libraries

To install you'll need a Python virtual environment with Segmentation-models-pytorch and PyTorch.
(We used CUDA 12.1)

```bash
# Set up virtual environment
python3 -m venv ~/venvs/madridv1
. ~/venvs/madridv1/bin/activate

# Install dependencies
pip install --upgrade pip
pip install torch==2.2.1+cu121 torchvision==0.17.1+cu121 torchaudio==2.2.1+cu121 -f https://download.pytorch.org/whl/torch_stable.html
python -m pip install git+https://github.com/qubvel/segmentation_models.pytorch
```
We have provided a requirements file, we recommend using that to set up the remainder of the environment correctly.



## License

This project is release under the 
[BSD-3-Clause license](https://github.com/DataMadrid/MADRID/blob/main/LICENSE)
