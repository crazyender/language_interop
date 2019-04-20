# Automatically Convert C++ API to Python API
Wrap a given C++ API to Python API based on Cython and libclang.

## Requirements
- Windows 10
- Microsoft Visual C++ >= 11.0
- Python 2.7 32-bit

## Download
Download Clang 3.7 from [here](http://releases.llvm.org/download.html) and put `libclang.dll` to the root directory.

## Install Python Packages
```bash
pip install Cython clang==3.7
```

## Prepare C++ Files
Put all `.h` files to `include/`, and put all `.lib` files to `lib/`.

## Generate Cython Codes
do:
```bash
python C2py.py --head_path='$the path of your target head file$' --extern_pxd='' --extern_pyx=''
```
This will generate two Cython files: `.pxd` and `.pyx`. Note that if you have C functions imported from `.dll`, you have to firstly delete the C function declarations in the head files and then write some necessary codes in `utility.cpp`, `extern_pxd.txt`, and `extern_pyx.txt`. You can refer to examples about how to write these files in this project. After this, do:
```bash
python C2py.py --head_path='$the path of your target head file$' --extern_pxd='extern_pxd.txt' --extern_pyx='extern_pyx.txt'
```

## Build Python Extension
Make some necessary modifications in `setup.py` (the names of libraries and the name of `.pyx` file). Then run:
```bash
python setup.py build_ext --compiler=msvc --inplace --plat-name=win32
```
This will generate Python extension `.pyd`. Don't forget to put `.dll` files to the same path of `.pyd` file when using the generated Python API.

