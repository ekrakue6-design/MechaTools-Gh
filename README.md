# MechaTools — Python Edition

An interactive engineering learning toolkit built with Python and Streamlit.

## Features
- Stress, strain, and Young's modulus calculator
- Factor of safety calculator
- Ohm's law calculator
- Constant-acceleration kinematics calculator
- Engineering formula library
- Practice question with worked solution

## Requirements
- Python 3.10 or newer
- pip

## Run on Windows
Open a terminal in this folder and run:

```powershell
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py -m streamlit run app.py
```

If the `py` command is unavailable, try `python` instead.

Streamlit will start a local server and show a URL, usually http://localhost:8501. Open that address in your browser.

## Project files
- `app.py` — the complete Streamlit application
- `requirements.txt` — Python dependency list

## Engineering assumptions
- Stress calculator assumes axial loading and a uniform cross-section.
- Young's modulus is calculated using the linear-elastic relationship.
- Factor of safety uses failure strength divided by working stress.
- Kinematics assumes straight-line motion with constant acceleration.
- Ohm's law assumes an ohmic component under the stated conditions.

This is an educational project, not a substitute for professional engineering verification.
