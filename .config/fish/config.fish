if status is-interactive
    # Commands to run in interactive sessions can go here
end


function fish_greeting
end

set EDITOR "emacsclient -t -a ''"
set VISUAL "emacsclient -c -a emacs"

#### Aliases
alias ve="source .env"
alias vv=". ./.venv/bin/activate.fish & set VIRTUAL_ENV ".venv""
alias va="ve; vv"

alias ..="cd .."
alias ...="cd ../.."

alias ls="exa"
alias la="exa -l a"
alias ll="exa -l"

alias emacs="emacsclient -c -a emacs"
####

#### Some python settings
set -gx VIRTUAL_ENV_DISABLE_PROMPT false
set -e _OLD_FISH_PROMPT_OVERRIDE
set -e _OLD_VIRTUAL_PYTHONHOME
set -e _OLD_VIRTUAL_PATH
####
