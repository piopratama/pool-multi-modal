# PLAN
This document explain about what is plan in order to start this project.

# OBEJCTIVES
As what we have been explained in README.md file, we're gonna make a multimodal data pooling API.
what is that ?, simply-> it is a API that can receive any data from the client such as images, text, audio, and video. Any data will be store in vectorize format. With this kind of data structure we can easly to implement it into semantic search utilize LLM engine (Large Language Model such as LLama) out there.

# TECHNOLOGY
Programming Language : Python
Framework : Flask
Database : Chroma

# STARTER
Please "fork" to collaborate.
1. After you clone this project navigate to the root of this project.
2. Make sure you have installed python 3 and pip. execute "Python -V" and "pip --version" on your terminal to check.
3. Let's create virtual environtment first "python -m venv env" (execute that in terminal of POOL-MULTI-MODAL root project)
4. then we can activate it using .\env\Scripts\activate (for cmd) or .\env\Scripts\Activate.ps1 (for powershell)
5. Please install the requirements "pip install -r requirements.txt" (currently only chroma)
6. the code mainly reside in "main.py" file