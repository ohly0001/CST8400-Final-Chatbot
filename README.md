## Installation
You can skip certain steps if not installing from scatch.
1. Download and install the [Python](https://www.python.org/downloads/) language onto your system. *Recommended using Python version 3.13.0 or below, as newer versions are not fully supported by AI libraries yet.*
2. Install [VS Code](https://code.visualstudio.com/) and its [Python language support](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extensions. *Or use another IDE with Python support.*
3. Download and install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/):  
    - Select **Desktop Development with C++** in the installer.  
    - Make sure these components are checked:  
      - C++ build tools  
      - Windows 10 or 11 SDK  
      - MSVC compiler  
      - CMake  
2. Open a terminal on your desktop, or IDE application and run the following:\
`pip install ninja`\
`set CMAKE_GENERATOR=Ninja`\
`pip install llama-cpp-python[server]`\
`pip install keras`

## Running
1. Perform [Installation Steps](#Installation) as required.
2. Run App.py using your IDE's application launch button (▶) or via a CLI.

## Model Used
TheBloke/Mistral-7B-Instruct-v0.1-GGUF 

## Dataflow
- App (Run) → Controller
- Controller ⇄ View
- Controller ⇄ TransformerModel
- Controller ⇄ FileModel
