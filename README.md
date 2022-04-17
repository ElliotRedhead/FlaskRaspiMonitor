# FlaskRaspiMonitor

A collection of utility routes suitable for display on a small Raspberry Pi LCD built in Flask.

## Summary of Utilities

### Clock
A digital representation of the system time, formatted HH:MM:SS.

### RTMP / Video Feed
Display of an RTMP feed, inspired by ONVIF CCTV streaming capability.

## Getting started

### Pre-requisites

- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/downloads)

### Run Locally

- Clone the repository:
```console
git clone https://github.com/ElliotRedhead/FlaskRaspiMonitor
```
- Create a virtual environment:
```console
python -m venv flaskraspimonitor
```
- Activate the virtual environment:
```console
source venv/bin/activate
```
- Install project dependencies:
```console
pip install -r requirements.txt
```
- Run the python app:
```console
python app.py
```
- Check access in the browser by navigating to the ip/port in the terminal output on startup.
