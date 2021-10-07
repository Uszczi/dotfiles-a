syntax on

" Issue with colors
let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
set termguicolors
"




" Too long time for exiting INSERT Mode 
set ttimeout
set ttimeoutlen=100
set timeoutlen=3000
"

set guicursor= " Lets keep this commented as long as I see normal cursor 
set noshowmatch
set relativenumber
set nohlsearch
set hidden
set backspace=indent,eol,start
set noerrorbells
set tabstop=4 softtabstop=4
set clipboard+=unnamedplus
set shiftwidth=4
set expandtab
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set scrolloff=8

let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif


" Give more space for displaying messages.
" set cmdheight=2

" Having longer updatetime (default is 4000 ms = 4 s) leads to noticeable
" delays and poor user experience.
set updatetime=50



set colorcolumn=80
highlight ColorColumn ctermbg=0 guibg=lightgrey

call plug#begin('~/.vim/plugged')

" Plug 'neoclide/coc.nvim', {'branch': 'release'}
" Plug 'tweekmonster/gofmt.vim'
" Plug 'tpope/vim-fugitive'
" Plug 'vim-utils/vim-man'
" Plug 'mbbill/undotree'
" Plug 'sheerun/vim-polyglot'
" Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
" Plug 'junegunn/fzf.vim'


" Zmiany dokonywane przemnie beda dodatkowo komentowane
" post install (yarn install | npm install) then load plugin only for editing
" supported files
" Plug 'prettier/vim-prettier', { 'do': 'yarn install' }
Plug 'preservim/nerdtree'

Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
" Aktualnie koncza sie w tym miejscu


Plug 'gruvbox-community/gruvbox'
" Plug 'sainnhe/gruvbox-material'
" Plug 'phanviet/vim-monokai-pro'
" Plug 'flazz/vim-colorschemes'

call plug#end()


" Zmiany potrzebne aby na save prettierowal
" let g:prettier#autoformat = 1
" let g:prettier#autoformat_require_pragma = 0
" ":map <F3> :Prettier <CR>

" autocmd StdinReadPre * let s:std_in=1
" autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | exe 'cd '.argv()[0] | endif
" map <F2> :NERDTreeToggle<CR>
" let NERDTreeShowHidden=1



let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#fnamemod = ':t'

nmap <leader>l :bnext<CR>
nmap <leader>k :bprev<CR>

colorscheme gruvbox
set background=dark


set splitright
set splitbelow




nnoremap <esc><esc> :noh<return>
set hlsearch








" ; For learning purpose
" noremap <Up> <Nop>
" noremap <Down> <Nop>
" noremap <Left> <Nop>
" noremap <Right> <Nop>





"; Strange behavouir in PowerShell 
let &t_SI.="\e[5 q"
let &t_SR.="\e[4 q"
let &t_EI.="\e[1 q"
"

map <Space> <Leader>

nnoremap  <leader>op :NERDTreeToggle<CR>
nnoremap  <leader>bk :bdelete<CR>
nnoremap  <leader>fs :w<CR>


nnoremap  <leader>wh <C-W>h
nnoremap  <leader>wj <C-W>j
nnoremap  <leader>wk <C-W>k
nnoremap  <leader>wl <C-W>l


nnoremap n nzzzv
nnoremap N Nzzzv
nnoremap J mzJ`z


inoremap , ,<c-g>u
inoremap . . <c-g>u
inoremap ? ? <c-g>u
inoremap ! ! <c-g>u


execute "set <A-j>=\ej"
execute "set <A-k>=\ek"

nnoremap <A-j> :m . +1<CR>==
nnoremap <A-k> :m . -2<CR>==
inoremap <A-j> <Esc>:m . +1<CR>==gi
inoremap <A-k> <Esc>:m . -2<CR>==gi
vnoremap <A-j> :m '>+1<CR>gv=gv
vnoremap <A-k> :m '<-2<CR>gv=gv


nnoremap <leader>hrr :source .vimrc<CR>





