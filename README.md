# MacOS mouse and keyboard automator :apple:
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.7](https://img.shields.io/badge/python-3.8.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

Tools to record mouse & keyboard procedures on MacOS. Quickly automate boring stuff that don't have obvious APIs for monitoring. The scripts are leveraging the use of libraries such as pynput. More info [here](https://pynput.readthedocs.io/en/latest/limitations.html).

# QuickStart: One-time setup

Before anything, you must have pyenv installed in order to run the scripts smoothly.
[How to setup pyenv](#pyenv-guide-for-handling-multiple-python-versions-in-your-mac)

In case you have autoenv installed, the repo should get automatically set up as soon as you `cd macos-mouse-and-keyboard-automator`. :crystal_ball: 
[How to setup autoenv](#guide-for-ultimate-repository-setup-with-autoenv)

In case you don't like autoenv, you can also manually set up the environment by running:
```bash
cd macos-mouse-and-keyboard-automator
python -mvenv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
export PYTHONPATH=$(pwd)
```

You might also need to give some access rights to your editor/terminal before being able to run the scripts
```text
1. Settings -> Security & Privacy
2. Click on the Privacy tab
3. Go to Accessibility
3. Click the +
4. Navigate to the target application
5. Click okay.
```

Now you should be able to run the scripts, happy automating :robot:

If you want to contribute to the codebase, make sure you set the pre-commit hooks before committing code changes.
[How to set pre-commit hooks](#code-formatting)

# QuickStart: Run hello world sample

If you run 
```bash
python scripts/hello_world/hello_world.py
```

You should see the script taking control of your computer and launching the terminal.

# Code formatting
Code formatting is enforced with [Black](https://black.readthedocs.io/).
 
On your local repo, you can automatically run Black formatting using a pre-commit hook. 
The required configuration is in the file `.pre-commit-config.yaml`. 
You will need Python packages `black` and `pre-commit` install for this.

To install the pre-commit hook, run the following command inside your repo
```shell
$ pre-commit install
```

After having installed the pre-commit hook, a commit that is not formatted correctly will be aborted, 
and the offending code will automatically be reformatted. 
Review the formatting changes, stage them and re-run the commit.

# Pyenv guide for handling multiple python versions in your Mac

With [pyenv](https://formulae.brew.sh/formula/pyenv) you can easily switch python versions. It's specially handy when you work with multiple python-based repositories with particular dependencies and virtual environments.

Through pyenv, the current repository defines the Python version to be used in `.python-version`.

First, install pyenv through Homebrew
```shell
$ brew update
$ brew install pyenv
```

Then add pyenv init to your shell
```shell
$ # zsh:
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
$ # or bash:
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
```

Make sure to restart your shell so changes are applied
```shell
$ exec "$SHELL"
```

Optionally, you can install further dependencies (recommended)
```shell
$ brew install openssl readline sqlite3 xz zlib
```

Now install the required Python version

```shell
$ pyenv install 3.8.7
```

When running Python via pyenv, you might get an error such as:
```shell
$ python
version `3.8.7' is not installed (set by /some-path/macos-mouse-and-keyboard-automator/.python-version)
```
This could mean that the recommended Python version for this repository has been changed and you don't yet have it installed. 
You can easily install it using ```pyenv install [version]```. You will also have to recreate your virtual environment.

How to check the Python version used in the repository
```shell
$ cd macos-mouse-and-keyboard-automator
$ python --version
Python 3.7.10
```

You can read more abut the installation at https://github.com/pyenv/pyenv#homebrew-on-macos

As a side note, you can also set a version system-wide (not recommended)
```shell
$ pyenv install 3.8.7
$ pyenv global 3.8.7
$ cd some-random-dir
$ python --version
Python 3.8.7
$ # but this will not affect the local version
$ cd macos-mouse-and-keyboard-automator
$ python --version
Python 3.7.10
```

# Guide for ultimate repository setup with Autoenv

If you follow these steps, every time you cd in the repo, the virtual env
will be automatically launched. When you leave it, it'll be deactivated :star:
```bash
git clone git://github.com/inishchith/autoenv.git ~/.autoenv
echo 'AUTOENV_ENABLE_LEAVE="aaa"  # Set to non-null string to enable this' | cat - ~/.autoenv/activate.sh > temp && mv temp ~/.autoenv/activate.sh
$ # zsh:
$ echo 'source ~/.autoenv/activate.sh' >> ~/.zshrc
$ # or bash:
$ echo 'source ~/.autoenv/activate.sh' >> ~/.bash_profile

```

All done! Now when you cd to the repo the virtual environment settings should be applied
automatically!
