# liquidroom

liquidroom is a collection of scripts that invokes [audio-separator](https://github.com/nomadkaraoke/python-audio-separator) to manipulate audio stems.

## Setup (MacOS)

1. Install Python

```bash
brew install python
```

If you get a `RuntimeError`, you might need to downgrade your Python version.

2. Clone this repo

```
git clone https://github.com/carrein/liquidroom.git
```

3. Create a virtual environment to avoid dependency conflicts

```bash
python -m venv liquidroom-env
source liquidroom-env/bin/activate
```

4. Install [audio-separator](https://github.com/nomadkaraoke/python-audio-separator) and its dependencies

```bash
pip install audio-separator onnxruntime
pip show audio-separator

...

Name: audio-separator
Version: 0.40.0
Summary: Easy to use audio stem separation, using various models from UVR trained primarily by @Anjok07
```

5. Copy audio files to be split into stems into `/input` A default, sample audio file is made available.

6. Invoke script of choice

```bash
python scripts/<your_script>.py
```

7. Check `/artifacts` for stems output.
