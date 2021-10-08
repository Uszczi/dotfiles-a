;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-


(setq user-full-name "Mateusz Papuga"
      user-mail-address "mateuszpapuga24@gmail.com")

(setq doom-theme 'doom-one)
(setq org-directory "~/org/")
(setq display-line-numbers-type "relative")


;; Here are some additional functions/macros that could help you configure Doom:
;;
;; - `load!' for loading external *.el files relative to this one
;; - `use-package!' for configuring packages
;; - `after!' for running code after a package has loaded
;; - `add-load-path!' for adding directories to the `load-path', relative to
;;   this file. Emacs searches the `load-path' when you load packages with
;;   `require' or `use-package'.
;; - `map!' for binding new keys
;;
;; To get information about any of these functions/macros, move the cursor over
;; the highlighted symbol at press 'K' (non-evil users must press 'C-c c k').
;; This will open documentation for it, including demos of how they are used.
;;
;; You can also try 'gd' (or 'C-c c d') to jump to their definition and see how
;; they are implemented.

;; General
(add-to-list 'display-buffer-alist '(" server log\\*\\'" display-buffer-no-window))

(use-package evil-nerd-commenter
  :bind ("M-/" . evilnc-comment-or-uncomment-lines))

;; Uncoment that some day, dont know why but stop working.
;; (treemacs-follow-mode +1)

(add-hook 'pdf-view-mode-hook
          (lambda () (local-key-binding (kbd "C-o") 'pdf-history-backward)))


;; Projectile
(setq projectile-project-search-path '("~/RoC/" "~/github/" "~/github/map-app"))


;; LSP
(defun efs/lsp-mode-setup ()
  (setq lsp-headerline-breadcrumb-segments '(path-up-to-project file symbols))
  (lsp-headerline-breadcrumb-mode))

(with-eval-after-load 'lsp-mode
  (add-hook 'lsp-mode-hook #'lsp-enable-which-key-integration))

;; TODO check if that do something
;; (use-package lsp-ui)

(use-package lsp-treemacs
  :after lsp)


;; Python
;; Dont know why but stop working and so far lsp-pyright works better.
;; (use-package lsp-python-ms
;;   :ensure t
;;   :init (setq lsp-python-ms-auto-install-server t)
;;   :hook (python-mode . (lambda ()
;;                           (require 'lsp-python-ms)
;;                           (lsp))))  ; or lsp-deferred

(use-package lsp-pyright
  :ensure t
  :hook (python-mode . (lambda ()
                          (require 'lsp-pyright)
                          (lsp))))  ; or lsp-deferred

(use-package! python-black
  :demand t
  :after python
  :config
  (add-hook! 'python-mode-hook #'python-black-on-save-mode)
  ;; Feel free to throw your own personal keybindings here
  (map! :leader :desc "Blacken Buffer" "m b b" #'python-black-buffer)
  (map! :leader :desc "Blacken Region" "m b r" #'python-black-region)
  (map! :leader :desc "Blacken Statement" "m b s" #'python-black-statement)
)

(use-package dap-mode)
(require 'dap-python)

(use-package dap-mode
  :custom
  (dap-auto-configure-features '(session locals tooltip))
 (setq lsp-enable-dap-auto-configure nil)
  :config
  (dap-ui-mode 1)
  (general-define-key
    :keymaps 'lsp-mode-map
    :prefix lsp-keymap-prefix
    "d" '(dap-hydra t :wk "debugger"))
  )

(map!  :leader
        "d" #'dap-hydra)

;; (use-package pyvenv
;;   :diminish
;;   :config
;;   (setq pyvenv-mode-line-indicator
;;         '(pyvenv-virtual-env-name ("[venv:" pyvenv-virtual-env-name "] ")))
;;   (pyvenv-mode +1))

(use-package python
 :delight "π "
 :bind (("M-[" . python-indent-shift-left)
        ("M-]" . python-indent-shift-right))
 )

(defun python-remove-unused-imports()
  "Removes unused imports and unused variables with autoflake."
  (interactive)
  (if (executable-find "autoflake")
      (progn
        (shell-command (format "autoflake --remove-all-unused-imports -i %s"
                               (shell-quote-argument (buffer-file-name))))
        (revert-buffer t t t))
    (warn "python-mode: Cannot find autoflake executable.")))

(use-package py-isort
  :after python
  :hook ((python-mode . pyvenv-mode)
         (before-save . py-isort-before-save)))

;; TypeScript
(require 'prettier-js)
(use-package typescript-mode
  :mode "\\.ts\\'"
  :hook (typescript-mode . lsp-deferred)
  :config
  (setq typescript-indent-level 2))

(use-package typescript-mode
  :mode "\\.js\\'"
  :hook (typescript-mode . lsp-deferred)
  :config
  (setq typescript-indent-level 2)
  (require 'dap-node)
  (dap-node-setup))

(use-package typescript-mode
  :mode "\\.tsx\\'"
  :hook ((typescript-mode . lsp-deferred) (typescript-mode . prettier-js-mode))
  :config
  (setq typescript-indent-level 2)
  (require 'dap-node)
  (dap-node-setup))


;; Evil snipe
(evil-snipe-mode +1)
(evil-snipe-override-mode +1)
(setq evil-snipe-scope 'whole-buffer)
(setq evil-snipe-auto-scroll t)
(setq evil-snipe-tab-increment t)


;; Ivy


(ivy-mode 1)
(setq ivy-use-virtual-buffers t)
(setq enable-recursive-minibuffers t)
;; enable this if you want `swiper' to use it
(setq search-default-mode #'char-fold-to-regexp)
(global-set-key "\C-s" 'swiper)
(global-set-key (kbd "C-c C-r") 'ivy-resume)
(global-set-key (kbd "<f6>") 'ivy-resume)
(global-set-key (kbd "M-x") 'counsel-M-x)
(global-set-key (kbd "C-x C-f") 'counsel-find-file)
(global-set-key (kbd "<f1> f") 'counsel-describe-function)
(global-set-key (kbd "<f1> v") 'counsel-describe-variable)
(global-set-key (kbd "<f1> o") 'counsel-describe-symbol)
(global-set-key (kbd "<f1> l") 'counsel-find-library)
(global-set-key (kbd "<f2> i") 'counsel-info-lookup-symbol)
(global-set-key (kbd "<f2> u") 'counsel-unicode-char)
(global-set-key (kbd "C-c g") 'counsel-git)
(global-set-key (kbd "C-c j") 'counsel-git-grep)
(global-set-key (kbd "C-c k") 'counsel-ag)
(global-set-key (kbd "C-x l") 'counsel-locate)
(global-set-key (kbd "C-S-o") 'counsel-rhythmbox)
(define-key minibuffer-local-map (kbd "C-r") 'counsel-minibuffer-history)

(map! :leader "f r" #'counsel-recentf)
