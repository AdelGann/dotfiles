# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:/usr/local/bin:$PATH:$HOME/.local/share/zen

export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="darkblood"

plugins=( 
    git
    dnf
    zsh-autosuggestions
    zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh

# check the dnf plugins commands here
# https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/dnf


# Display Pokemon-colorscripts
# Project page: https://gitlab.com/phoneybadger/pokemon-colorscripts#on-other-distros-and-macos
#pokemon-colorscripts --no-title -s -r #without fastfetch
fastfetch

# fastfetch. Will be disabled if above colorscript was chosen to install
#fastfetch -c $HOME/.config/fastfetch/config-compact.jsonc

# Set-up FZF key bindings (CTRL R for fuzzy history finder)
source <(fzf --zsh)

HISTFILE=~/.zsh_history
HISTSIZE=10000
SAVEHIST=10000
setopt appendhistory

# Set-up icons for files/directories in terminal using lsd
alias ls='lsd'
alias l='ls -l'
alias la='ls -a'
alias lla='ls -la'
alias lt='ls --tree'
alias cl='clear; fastfetch'

#  ┌─┐┬  ┬┌─┐┌─┐
#  ├─┤│  │├─┤└─┐
#  ┴ ┴┴─┘┴┴ ┴└─┘

alias ga="git add"
alias gc="git commit"
alias gs="git status"
alias glg="git log --graph"

if command -v lazygit >/dev/null 2>&1; then
alias lg="lazygit"
fi

if command -v zellij >/dev/null 2>&1; then
alias zs="zellij attach"
alias z="zellij"
fi

### DNF CONFIG ALIAS
if command -v dnf >/dev/null 2>&1; then
## Aliases

local dnfprog="dnf"

# Prefer dnf5 if installed
command -v dnf5 > /dev/null && dnfprog=dnf5

alias dnfl="${dnfprog} list"                       # List packages
alias dnfli="${dnfprog} list installed"            # List installed packages
alias dnfgl="${dnfprog} grouplist"                 # List package groups
alias dnfmc="${dnfprog} makecache"                 # Generate metadata cache
alias dnfp="${dnfprog} info"                       # Show package information
alias dnfs="${dnfprog} search"                     # Search package

alias dnfu="sudo ${dnfprog} upgrade"               # Upgrade package
alias dnfi="sudo ${dnfprog} install"               # Install package
alias dnfgi="sudo ${dnfprog} groupinstall"         # Install package group
alias dnfr="sudo ${dnfprog} remove"                # Remove package
alias dnfgr="sudo ${dnfprog} groupremove"          # Remove package group
alias dnfc="sudo ${dnfprog} clean all"             # Clean cache


fi
