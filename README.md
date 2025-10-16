## Dataflow
- App (Run) → Controller
- Controller ⇄ View
- Controller ⇄ TransformerModel
- Controller ⇄ FileModel

## Builtin Packages Used
- os
- json

## Model Used
TheBloke/Mistral-7B-Instruct-v0.1-GGUF 

## Installation
1. Download and install **Visual Studio Build Tools**:  
   https://visualstudio.microsoft.com/visual-cpp-build-tools/ 
  - Select **Desktop Development with C++** in the installer.  
  - Make sure these components are checked:  
    - C++ build tools  
    - Windows 10 or 11 SDK  
    - MSVC compiler  
    - CMake  
2. Open a terminal and run:\
pip install ninja\
set CMAKE_GENERATOR=Ninja\
pip install llama-cpp-python[server]