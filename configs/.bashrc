#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return
PS1='[\u@\h \W]\$ '

alias ls='ls --color=auto'
alias ..="cd .."
alias ...="cd ../.."


# Bug with todoist app at Arch Linux
export DESKTOPINTEGRATION=false

export PATH="/home/mat/path-utils:$PATH"

fish

source /usr/share/nvm/init-nvm.sh
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/simbody/lib/x86_64-linux-gnu
export SIMBODY_HOME=~/simbody
