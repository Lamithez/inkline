\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{inkline}[2026/10/19 Inkline Chinese presentation class]

\RequirePackage{iftex}
\ifXeTeX\else
  \ClassError{inkline}{XeTeX is required}{Compile with XeLaTeX or Tectonic.}
\fi
\RequirePackage{kvoptions}
\RequirePackage{etoolbox}
\SetupKeyvalOptions{family=inkline,prefix=ink@}
\DeclareStringOption[small]{size}
\DeclareBoolOption[false]{bibliography}
\DeclareDefaultOption{\PassOptionsToClass{\CurrentOption}{beamer}}
\ProcessKeyvalOptions*

\newif\ifink@large
\ifdefstring{\ink@size}{large}{\ink@largetrue}{%
  \ifdefstring{\ink@size}{small}{}{%
    \ClassError{inkline}{Unknown size '\ink@size'}{Choose size=small or size=large.}}}
\ifink@large
  \LoadClass[aspectratio=169,t,14pt]{beamer}
\else
  \LoadClass[aspectratio=169,t,11pt]{beamer}
\fi

% inkline.cls 与 inkline/ 一起放在项目根目录；不读取任何示例内容或文献。
\makeatletter
\input{inkline/style.tex}
\input{inkline/fonts.tex}
\input{inkline/base.tex}
\input{inkline/colors.tex}
\input{inkline/layout.tex}
\input{inkline/toc.tex}
\input{inkline/blocks.tex}
\input{inkline/commands.tex}
\ink@applystyle
\setlength{\parskip}{0.5em}
\endinput
