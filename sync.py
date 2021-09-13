import os
import shutil

# TODO add reverse copy
# TODO add tests
# TODO add coping whole directory

HOME = "/home/mat/"
HOME_CONFIG = f"{HOME}.config/"
REPO_BASE = f"{HOME}github/dotfiles/"
REPO_CONFIG_BASE = f"{REPO_BASE}.config/"
FILES_MAPPING = {
    # Fish
    f"{HOME_CONFIG}fish/config.fish": f"{REPO_CONFIG_BASE}fish/",
    # Qtile
    f"{HOME_CONFIG}qtile/autostart.sh": f"{REPO_CONFIG_BASE}qtile/",
    f"{HOME_CONFIG}qtile/config.py": f"{REPO_CONFIG_BASE}qtile/",
    f"{HOME_CONFIG}qtile/text.py": f"{REPO_CONFIG_BASE}qtile/",
    f"{HOME_CONFIG}qtile/qtile_gnome.desktop": f"{REPO_CONFIG_BASE}qtile/",
    # Bash
    f"{HOME}.bashrc": f"{REPO_BASE}",
    # Dmenu scripts
    f"{HOME_CONFIG}dmscripts/config": f"{REPO_CONFIG_BASE}dmscripts/",
    # # My path utils
    f"{HOME}/path-utils/lock-screen": f"{REPO_BASE}path-utils/",
    # # Doom emacs
    f"{HOME}.doom.d/init.el": f"{REPO_BASE}/.doom.d/",
    f"{HOME}.doom.d/config.el": f"{REPO_BASE}/.doom.d/",
    f"{HOME}.doom.d/packages.el": f"{REPO_BASE}/.doom.d/",
    f"{HOME}.doom.d/custom.el": f"{REPO_BASE}/.doom.d/",
    # Python
    f"{HOME}.pylintrc": f"{REPO_BASE}",
}


def main():
    for org_path, des_path in FILES_MAPPING.items():
        try:
            shutil.copy(org_path, des_path)
        except FileNotFoundError:
            os.makedirs(des_path)
            shutil.copy(org_path, des_path)

    print("Done.")


if __name__ == "__main__":
    main()
