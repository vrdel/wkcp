#!/bin/bash

IFS=""
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# TODO: pyenv activate wkcp-py39
pyenv activate wkcp

wkcp $*
