# Automatically Convert C++ API to Python API
Wrap a given C++ API to Python API based on Cython and libclang.

## Requirements
- Windows 10
- Microsoft Visual C++ >= 11.0
- Python 2.7 32-bit

## Download
Download Clang 3.7 from [here](http://releases.llvm.org/download.html) and put libclang.dll to the root directory.

## Install Python Packages
```bash
pip install Cython clang==3.7
```

## Prepare C++ Files
Put all `.h` files to `.include`, and put all `.lib` files to `.lib/`.

