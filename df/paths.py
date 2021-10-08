HOME = "/home/mat/"
HOME_CONFIG = f"{HOME}.config/"
REPO_BASE = f"{HOME}github/dotfiles/configs/"

FILES = {
    # Fish
    f"{HOME_CONFIG}fish/config.fish": f"{REPO_BASE}fish/config.fish",
    # Qtile
    f"{HOME_CONFIG}qtile/autostart.sh": f"{REPO_BASE}qtile/autostart.sh",
    f"{HOME_CONFIG}qtile/config.py": f"{REPO_BASE}qtile/config.py",
    f"{HOME_CONFIG}qtile/text.py": f"{REPO_BASE}qtile/text.py",
    f"{HOME_CONFIG}qtile/qtile_gnome.desktop": f"{REPO_BASE}qtile/qtile_gnome.desktop",
    # Bash
    f"{HOME}.bashrc": f"{REPO_BASE}.bashrc",
    # Dmenu scripts
    f"{HOME_CONFIG}dmscripts/config": f"{REPO_BASE}dmscripts/config",
    # # My path utils
    f"{HOME}/path-utils/lock-screen": f"{REPO_BASE}path-utils/lock-screen",
    # # Doom emacs
    f"{HOME}.doom.d/init.el": f"{REPO_BASE}doom/init.el",
    f"{HOME}.doom.d/config.el": f"{REPO_BASE}doom/config.el",
    f"{HOME}.doom.d/packages.el": f"{REPO_BASE}doom/packages.el",
    f"{HOME}.doom.d/custom.el": f"{REPO_BASE}doom/custom.el",
    # Python
    f"{HOME}.pylintrc": f"{REPO_BASE}.pylintrc",
    # Alacritty
    f"{HOME}.alacritty.yml": f"{REPO_BASE}.alacritty.yml",
    # Vim
    f"{HOME}.vimrc": f"{REPO_BASE}.vimrc",
}
