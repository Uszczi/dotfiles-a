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
alias la="exa -la"
alias ll="exa -l"

alias emacs="emacsclient -c -a emacs"

alias aa=". ./.env.fish"

# Python
alias pa="autoflake --in-place --recursive --remove-all-unused-imports --ignore-init-module-imports --remove-duplicate-keys --remove-unused-variables"
alias pi="isort"
alias pb="black"
alias pm="mypy --ignore-missing-imports"

####


#### Some python settings
set -gx VIRTUAL_ENV_DISABLE_PROMPT false
set -ge _OLD_FISH_PROMPT_OVERRIDE
set -ge _OLD_VIRTUAL_PYTHONHOME
set -ge _OLD_VIRTUAL_PATH
####

#### Load functions that have to run automatically. 
.  ~/.config/fish/functions/autoenv.fish

fish_add_path ~/azure-functions-cli/
fish_add_path ~/.local/bin
