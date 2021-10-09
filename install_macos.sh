#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

ln -sf $DIR/plugins/windows_syscall.py "$HOME/Library/Application Support/Binary Ninja/plugins/windows_syscall.py"
