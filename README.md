# deepcomet

## Requirements

Deep Comet requires Python 3 to run. Also you should have an access to this repository to install `deepcomet` package.

## Installation

Deep Comet is protected by Arontier Proprietary License. 
Only authorized users can access `deepcomet` package.
If you are interested, please send an email to `dhlee@arontier.co`.

Assuming you have an access to this repository,
you can install `deepcomet` package by using pip:

```bash
pip install git+ssh://git@github.com/arontier/deepcomet.git
```

If you want to install a specific version:

```bash
pip install git+ssh://git@github.com/arontier/deepcomet.git@version
```

where `version` above is something like `0.0.1`, well a *version*.

All package dependencies will be resolved automatically.
If you stuck with SSH key business, please read [https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account) to register your SSH key to GitHub.

## Quickstart

To test-drive, you will need an input image possibly containing comets to detect
and importantly a model file. Model files are too big to upload here,
so you may want to request these files too when you ask for access to this repository.

Image formats supported by `deepcomet` are: JPG (JPEG), PNG and TIF (TIFF).

After install `deepcomet`, make `input` and `output` directories and place
your images under `input` directory. Put your model file, say `rcnn.20191115.model`
in the next to `input` and `output` directories. I.e. the structure should
look like this:

```
rcnn.20191115.model
input/
   sample.jpg
   ...
output/
```

### Using binary

Run the following command to run `deepcomet`:

```bash
deepcomet -i input -o output -m rcnn.20191115.model
```

### Using library

Create an example Python file, say `example.py`:

```python
from deepcomet.rcnn import predict

predict(input_file_path='input', 
        output_file_path='output', 
        model_file_path='rcnn.20191115.model')
```

Run `example.py`:

```bash
python example.py
```

### Results

Here is a sample:

| Input | Output |
|---|---|
|![./docs/CC036_H0_26.png](./docs/CC036_H0_26.png)|![./docs/pred_CC036_H0_26.png](./docs/pred_CC036_H0_26.png)|

