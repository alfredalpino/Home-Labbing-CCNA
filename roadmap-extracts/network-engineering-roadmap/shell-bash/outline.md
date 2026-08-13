# Shell / Bash

- **Source:** [https://roadmap.sh/shell-bash](https://roadmap.sh/shell-bash)
- **Category:** network-engineering-roadmap
- **Description:** Learn to master Shell and Bash in 2026
- **Related roadmaps:** [`backend`](https://roadmap.sh/backend), [`full-stack`](https://roadmap.sh/full-stack), [`devops`](https://roadmap.sh/devops), [`system-design`](https://roadmap.sh/system-design), [`nodejs`](https://roadmap.sh/nodejs)
- **AI Tutor courses (titles):** Bash Scripting Fundamentals, Shell Variables and Control Flow, Text Processing with Bash, Working with Files and Directories, Automating Tasks with Shell Scripts, Command Line Arguments, Pipes and Redirection, Regular Expressions in Bash, Error Handling in Scripts, Debugging Shell Scripts
- **Stats:** 30 topics · 144 subtopics · 174 content pages · 453 resource links (407 unique URLs)
- **Resource types:** article: 279, video: 154, official: 13, opensource: 4, course: 2, book: 1

## On-roadmap navigation links

- [roadmap.sh](https://roadmap.sh)
- [Linux](https://roadmap.sh/linux)
- [Backend](https://roadmap.sh/backend)
- [DevOps](https://roadmap.sh/devops)
- [Network Engineer](https://roadmap.sh/network-engineer)

## Topic outline + resources

### (ungrouped)

#### What is Bash?

Bash, short for Bourne Again Shell, is a command-line interpreter and a shell scripting language. It's essentially a program that allows users to interact with the operating system by typing commands. Bash interprets these commands and instructs the operating system to perform specific actions, such as running programs, manipulating files, and managing system resources. It also provides features f…

- [book] [Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/Bash-Beginners-Guide.pdf)
- [official] [Bash Docs](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html)
- [article] [Bash Tutorial](https://www.w3schools.com/bash/)
- [video] [Bash Scripting Tutorial for Beginners](https://www.youtube.com/watch?v=tK9Oc6AEnR4)

#### dash

dash (Debian Almquist Shell) is a Unix shell that is smaller, faster, and requires fewer resources compared to Bash. It's often used as the default `/bin/sh` on Debian-based systems and is designed to be POSIX-compliant, focusing on speed and efficiency in script execution. This makes it suitable for boot scripts and other system-level tasks where resource usage is critical.

- [article] [Dash - Wikipedia](https://en.wikipedia.org/wiki/Almquist_shell#dash)
- [article] [Dash](https://wiki.archlinux.org/title/Dash)
- [article] [What is Dash Shell in Linux?](https://linuxhandbook.com/dash-shell/)

#### bash

Bash, short for Bourne Again Shell, is a command-line interpreter and a shell scripting language. It's a program that allows users to interact with the operating system by typing commands. Bash interprets these commands and instructs the operating system to perform specific actions, making it a fundamental tool for system administration, automation, and software development.

- [article] [https://en.wikipedia.org/wiki/Bash_(Unix_shell)#:~:text=Bash (short for "Bourne Again,Chet Ramey)](https://en.wikipedia.org/wiki/Bash_(Unix_shell)
- [article] [Bash Tutorial](https://www.w3schools.com/bash/)
- [video] [Bash Scripting Full Course 3 Hours](https://www.youtube.com/watch?v=e7BufAVwDiM)
- [video] [Bash Scripting Tutorial for Beginners](https://www.youtube.com/watch?v=tK9Oc6AEnR4)

### Introduction

Shell, often referred to as Bash (Bourne Again Shell), is a command-line interpreter. It acts as an interface between the user and the operating system, allowing users to execute commands, run scripts, and manage files. It interprets the commands entered by the user and instructs the operating system to perform the corresponding actions.

**Section resources:**
- [article] [Shell - Wikipedia](https://en.wikipedia.org/wiki/Shell_(computing)
- [article] [The Shell Scripting Tutorial](https://www.shellscript.sh/philosophy.html)
- [video] [What Is a Shell ? | Learn How Shell Commands Work in the Terminal](https://www.youtube.com/watch?v=-qLrgCFynzE)
- [video] [Shell Scripting Tutorial for Beginners 1 - Introduction](https://www.youtube.com/watch?v=cQepf9fY6cE&list=PLS1QulWo1RIYmaxcEqw5JhK3b-6rgdWO_)

#### CLI vs GUI

A Command Line Interface (CLI) is a text-based interface used to interact with a computer system by typing commands. A Graphical User Interface (GUI), on the other hand, utilizes visual elements such as windows, icons, and menus to enable users to interact with the system using a mouse, touchpad, or touchscreen.

- [article] [What is a CLI (Command Line Interface)?](https://aws.amazon.com/what-is/cli/)
- [article] [What Is a GUI?](https://www.coursera.org/articles/gui)
- [video] [What's the difference between a GUI and a CLI?](https://www.youtube.com/watch?v=w9u0d4C95Zs)

#### zsh

Zsh, also known as the Z shell, is a Unix shell that can be used as an interactive login shell and as a shell script command interpreter. It's designed to be highly customizable and offers features like improved tab completion, shared command history across multiple terminal windows, and powerful theming options. Zsh is often considered an alternative to Bash, offering enhanced functionality and a…

- [article] [Z Shell - Wikipedia](https://en.wikipedia.org/wiki/Z_shell)
- [article] [zsh - The Z shell](https://www.ibm.com/docs/en/zos/3.1.0?topic=descriptions-zsh-z-shell)
- [video] [Zsh: The Developer's Dream Shell! Say Goodbye to Bash! 💻✨](https://www.youtube.com/watch?v=5F4T_iTeN08)

#### fish

fish is a user-friendly command-line shell for UNIX-like operating systems. It focuses on providing a more interactive and discoverable experience compared to traditional shells like Bash or Zsh. Key features include autosuggestions, syntax highlighting, and a simplified scripting language.

- [opensource] [fish-shell](https://github.com/fish-shell/fish-shell)
- [article] [Finally, a command line shell for the 90s](https://fishshell.com/)
- [article] [Why I use Fish Shell](https://medium.com/@desjoerdhaan/why-i-use-fish-shell-e5272e0770bf)
- [video] [FISH (Friendly Interactive Shell) by Bash Boomer](https://www.youtube.com/watch?v=C2a7jJTh3kU)

#### What is scripting?

Scripting is the process of writing a series of commands that are executed in a specific order by a program or scripting engine. These commands, often written in a simple, human-readable language, automate tasks, control software applications, or interact with operating systems. Instead of manually entering commands one by one, a script allows you to run a sequence of instructions with a single co…

- [article] [What is scripting?](https://coralogix.com/blog/what-is-scripting/)
- [article] [What's the difference between Programming and Scripting?](https://www.youtube.com/watch?v=7-0iBZxNq74)
- [article] [Bash Scripting Tutorial – Linux Shell Script and Command Line for Beginners](https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/)
- [video] [Bash Scripting on Linux](https://www.youtube.com/playlist?list=PLT98CRl2KxKGj-VKtApD8-zCqSaN2mD4w)

#### tcsh

tcsh is an enhanced version of the C shell (csh), a Unix shell program. It's designed as an interactive login shell and a shell script command processor. tcsh provides features like command-line editing, filename completion, and a history mechanism, making it more user-friendly than its predecessor.

- [official] [tcsh](https://www.tcsh.org/)
- [article] [tcsh - Wikipedia](https://en.wikipedia.org/wiki/Tcsh)

#### ksh

ksh, or the Korn shell, is an interactive command language and scripting language. It's designed to be backward-compatible with the Bourne shell (sh) while incorporating many features from other shells like csh. ksh offers improvements in scripting capabilities, command-line editing, and job control, making it a powerful tool for both interactive use and automating tasks.

- [article] [ksh](http://www.kornshell.com/)
- [article] [ksh - Wikipedia](https://en.wikipedia.org/wiki/KornShell)

### Popular Shells

A shell is a command-line interpreter that provides a user interface for interacting with an operating system. Different shells offer varying features, syntax, and capabilities, leading to the existence of several popular choices. These shells determine how you interact with the system, execute commands, and automate tasks.

**Section resources:**
- [article] [8 Types of Linux Shells](https://phoenixnap.com/kb/linux-shells)
- [article] [What are the Different Types of Shells in Linux?](https://www.digitalocean.com/community/tutorials/different-types-of-shells-in-linux)

#### cmd

cmd, also known as the Command Prompt, is the default command-line interpreter on Windows operating systems. It allows users to interact with the operating system by entering text-based commands. These commands can be used to navigate the file system, execute programs, and perform various system administration tasks.

- [article] [Command Line Commands – CLI Tutorial](https://www.freecodecamp.org/news/command-line-commands-cli-tutorial/)
- [article] [cmd](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)

#### PowerShell

PowerShell is a cross-platform task automation and configuration management framework, consisting of a command-line shell and associated scripting language. It's built on the .NET Common Language Runtime (CLR) and accepts and returns .NET objects, which allows for more complex and structured data manipulation compared to traditional text-based shells. PowerShell is designed to be extensible and ca…

- [official] [What is PowerShell?](https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.5)
- [official] [PowerShell Docs](https://learn.microsoft.com/en-us/powershell/)
- [opensource] [PowerShell](https://github.com/PowerShell/PowerShell)
- [video] [Learn PowerShell in Less Than 2 Hours](https://www.youtube.com/watch?v=ZOoCaWyifmI)

### Setting Up Bash

Setting up Bash involves configuring your shell environment to suit your preferences and workflow. This includes customizing the appearance of your command prompt, defining aliases for frequently used commands, setting environment variables to control program behavior, and creating custom functions to automate tasks. Properly setting up Bash can significantly improve your productivity and make working with the command line more efficient.

**Section resources:**
- [article] [Setting up the Bash Environment](https://letsdefend.io/blog/how-to-install-bash-on-windows)
- [article] [How to configure or customize Bash: My first steps for my setup](https://www.youtube.com/watch?v=wy1q5egFW6I)

#### stdin, stdout, stderr

In computing, standard streams are preconnected input and output communication channels between a computer program and its environment. Specifically, _stdin_ (standard input) is the channel through which a program receives input, typically from the keyboard or another program. _stdout_ (standard output) is the channel through which a program writes its normal output, usually displayed on the scree…

- [article] [Standard Streams - Wikipedia](https://en.wikipedia.org/wiki/Standard_streams)
- [article] [stdin, stdout, stderr](https://www.learnlinux.org.za/courses/build/shell-scripting/ch01s04)
- [video] [Linux Crash Course - Data Streams (stdin, stdout & stderr)](https://www.youtube.com/watch?v=zMKacHGuIHI)

### Files & Directories

Files and directories are fundamental building blocks of a file system. Files store data, such as text, images, or executable code. Directories, also known as folders, organize files and other directories in a hierarchical structure, allowing users to navigate and manage their data effectively.

### Tab Completion

Tab completion is a feature in command-line interfaces that automatically completes commands, filenames, or other input based on what you've already typed. By pressing the Tab key, the shell attempts to fill in the rest of the word you're typing, saving you time and reducing errors. If multiple possibilities exist, pressing Tab twice usually displays a list of options.

**Section resources:**
- [article] [https://www.gnu.org/software/gnuastro/manual/html_node/Bash-TAB-completion-tutorial.html](https://www.gnu.org/software/gnuastro/manual/html_node/Bash-TAB-completion-tutorial.html)

#### Output redirection

Output redirection in shell scripting allows you to control where the output of a command is sent. Instead of displaying on the terminal, you can redirect it to a file, either overwriting the file or appending to it. This is achieved using special operators like `>`, `>>`, `2>`, and `&>`. These operators provide a way to manage standard output (stdout), standard error (stderr), and both, making it…

- [article] [Unix / Linux - Shell Input/Output Redirections](https://www.tutorialspoint.com/unix/unix-io-redirections.htm#:~:text=The%20output%20from%20a%20command,is%20known%20as%20output%20redirection.)
- [article] [Linux Question: What is /dev/null 2\>&1 ?](https://hemantjain.medium.com/linux-question-what-is-dev-null-2-1-82d75a156b5c)
- [video] [Linux Commands for Beginners 16 - Output Redirection](https://www.youtube.com/watch?v=NUjpOLlYv7Q)

### Repeat Commands

In the shell, you can easily access and reuse previously executed commands. The most common way to do this is using the up and down arrow keys to navigate through your command history. Alternatively, you can use the `history` command to view a numbered list of past commands, and then execute a specific command by typing `!n`, where `n` is the command's number in the history list. You can also use `!!` to repeat the last command, or `!string` to execute the most recent command that starts with "s…

**Section resources:**
- [article] [How To Use Bash History Commands and Expansions on a Linux VPS](https://www.digitalocean.com/community/tutorials/how-to-use-bash-history-commands-and-expansions-on-a-linux-vps)
- [video] [Bash History | Your Linux Command History Explained](https://www.youtube.com/watch?v=Bth-1rLKjGU)

#### Input redirection

Input redirection enables a command to obtain its input from a source other than the standard input (typically the keyboard). Instead of typing input directly, a command can read data from a file or another command's output. This is achieved using operators like `<` to specify the input source.

- [article] [Unix / Linux - Shell Input/Output Redirections](https://www.tutorialspoint.com/unix/unix-io-redirections.htm)
- [video] [Linux Basics: How to use Linux Standard Input and Output](https://www.youtube.com/watch?v=YYz8Y_UBrvw&t=116s)

#### pwd

`pwd` (print working directory) is a command-line utility that displays the absolute path of the current directory you are working in. It essentially tells you where you are located within the file system hierarchy from the root directory. This is useful for navigating and understanding your position within the directory structure.

- [article] [How To Use pwd Command In Linux / UNIX {with examples}](https://www.cyberciti.biz/faq/pwd-linux-unix-command-examples/)
- [article] [Bash pwd Command - Print Working Directory](https://www.w3schools.com/bash/bash_pwd.php)
- [video] [How to use the pwd command: 2-Minute Linux Tips](https://www.youtube.com/watch?v=bBM_flm2Ths)

#### ls

`ls` is a command-line utility used to list files and directories within a specified directory. By default, it displays the contents of the current working directory. It offers various options to control the output, such as displaying file sizes, modification dates, permissions, and hidden files.

- [article] [Bash ls Command - List Directory Contents](https://www.w3schools.com/bash/bash_ls.php)
- [video] [Learn the "ls" command! Lil' Linux Lesson!](https://www.youtube.com/watch?v=gwo--XHaz7s)

#### cd

`cd` is a fundamental command used to change the current working directory in a shell environment. It allows you to navigate through the file system, moving from one directory to another. By specifying a target directory as an argument, `cd` updates the shell's internal record of the current location, affecting subsequent commands that operate relative to that location.

- [article] [Bash cd - Change Directory](https://www.w3schools.com/bash/bash_cd.php)
- [video] [There's more to learn about the "cd" command. Lil' Linux Lesson!](https://www.youtube.com/watch?v=ZRlQxx1rmng)

#### echo

`echo` is a fundamental command-line utility used to display lines of text. It essentially prints its arguments to standard output, which is typically your terminal screen. This makes it useful for displaying messages, variable values, or the output of other commands within shell scripts.

- [article] [Bash echo Command - Display Text](https://www.w3schools.com/bash/bash_echo.php)
- [video] [The Echo Command | Linux Essential Commands](https://www.youtube.com/watch?v=Tj-9tahWvok)

### Help Commands

Help commands in a shell environment provide users with information about available commands, their syntax, and options. They are essential tools for understanding how to use commands effectively and discovering new functionalities within the shell. These commands allow users to quickly access documentation and usage examples directly from the command line.

**Section resources:**
- [article] [Bash man Command - User Manual](https://www.w3schools.com/bash/bash_man.php)
- [article] [How to get help in Bash](https://nipunarat1997.medium.com/how-to-get-help-in-bash-9b101ee7d65a)
- [video] [07 The Help Command Linux Shell Tutorials](https://www.youtube.com/watch?v=D4bSUqqaX3c)

#### Error redirection

Error redirection in shell scripting involves capturing and managing error messages generated by commands. By default, standard error (stderr) is displayed on the terminal. Error redirection allows you to redirect these error messages to a file, discard them, or pipe them to another command for further processing, providing better control over script output and debugging.

- [article] [How to Redirect Standard (stderr) Error in Bash](https://www.geeksforgeeks.org/linux-unix/how-to-redirect-standard-stderr-error-in-bash/)
- [video] [Understanding stdin, stdout, stderr in Python](https://www.youtube.com/watch?v=4HY0VBBY7ok)

#### mkdir

`mkdir` is a command-line utility used to create new directories (folders) in a file system. It allows users to organize files by grouping them into logical structures. The command takes the name(s) of the directory(s) to be created as arguments, and it can also be used to create multiple directories at once or create parent directories if they don't already exist.

- [article] [Bash mkdir Command - Make Directories](https://www.w3schools.com/bash/bash_mkdir.php)
- [video] [Linux Command Line Tutorial For Beginners 6 - mkdir Command](https://www.youtube.com/watch?v=qixSaXSUs-U)

#### touch

The `touch` command is a fundamental utility used to update the access and modification times of files and directories. If a file doesn't exist, `touch` creates an empty file with the specified name. It's commonly used to create new, empty files or to quickly update the timestamps of existing files without modifying their content.

- [article] [Bash touch Command - Change File Timestamps](https://www.w3schools.com/bash/bash_touch.php)
- [video] [Touch Command Made Easy (Linux Crash Course)](https://www.youtube.com/watch?v=bP0dwXU8B64)

#### rm

The `rm` command in Unix-like operating systems is used to remove files or directories. It permanently deletes the specified files, so caution is advised when using it. By default, `rm` does not remove directories; specific options are needed to remove directories and their contents recursively.

- [article] [Bash rm Command - Remove Files or Directories](https://www.w3schools.com/bash/bash_rm.php)
- [video] [Linux Command Line Tutorial For Beginners 7 - rm and rmdir commands for linux](https://www.youtube.com/watch?v=yrw6Uxs-yJk)

#### rmdir

`rmdir` is a command-line utility used to remove empty directories. It's a straightforward tool that helps in cleaning up directory structures by deleting directories that no longer contain any files or subdirectories. The command will return an error if the directory is not empty.

- [article] [Deleting or removing directories (rmdir command)](https://www.ibm.com/docs/en/aix/7.2.0?topic=directories-deleting-removing-rmdir-command)
- [video] [Linux Command Line Tutorial For Beginners 7 - rm and rmdir commands for linux](https://www.youtube.com/watch?v=yrw6Uxs-yJk)

### Bash Alias

A Bash alias is a shortcut or a custom name you assign to a command or a sequence of commands. Instead of typing a long command every time, you can create an alias that represents it. When you type the alias in the terminal, Bash replaces it with the original command before executing it. This simplifies command-line usage and improves efficiency.

**Section resources:**
- [article] [Bash Alias](https://www.w3schools.com/bash/bash_alias.php)
- [video] [Linux Crash Course - Bash Aliases](https://www.youtube.com/watch?v=Ok_kD_sgNcs)

#### Pipes

Pipes in shell scripting are a form of redirection that allows you to send the output of one command as the input to another command. This creates a chain of commands where the data flows from one process to the next, enabling you to perform complex data manipulation and filtering concisely and efficiently. The pipe operator, represented by the vertical bar `|`, connects the standard output of the…

- [article] [Pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html)
- [article] [Bash shell basics — pipes, redirection, and coprocesses](https://paulguerin.medium.com/bash-shell-basics-pipe-and-redirection-fbb4c2c1c0ed)
- [video] [Bash Shell Scripting for Beginners - Using Pipes](https://www.youtube.com/watch?v=FICwAKYc0Pg)

#### mv

The `mv` command in Unix-like operating systems is used to move or rename files and directories. It allows you to relocate files from one directory to another, effectively changing their location within the file system. Additionally, `mv` can be used to change the name of a file or directory without altering its location.

- [article] [Bash mv Command - Move or Rename Files](https://www.w3schools.com/bash/bash_mv.php)
- [video] [Linux Commands for Beginners 06 - Moving and Renaming Files](https://www.youtube.com/watch?v=cSBYvSA9rDM)

#### cp

The `cp` command in Unix-like operating systems is used to copy files and directories from one location to another. It creates an exact duplicate of the source file or directory at the specified destination, leaving the original intact. The command can be used to copy single files, multiple files, or entire directory structures.

- [article] [Bash cp - Copy Files and Directories](https://www.w3schools.com/bash/bash_cp.php)
- [video] [Linux Command Line Tutorial For Beginners 8 - cp command](https://www.youtube.com/watch?v=Bnx_GAHM0wo)

#### cat

`cat` is a command-line utility that is primarily used to display the contents of one or more files on the standard output (usually your terminal screen). It can also be used to concatenate files, meaning to combine them into a single output stream. The name "cat" is short for "concatenate."

- [article] [Bash cat Command - Concatenate and Display Files](https://www.w3schools.com/bash/bash_cat.php)
- [video] [The cat Command in Linux (Featuring Real Cats) - Linux Crash Course Series](https://www.youtube.com/watch?v=z3nJlyrJYW4)

#### find

The `find` command is a powerful utility used to locate files and directories within a file system hierarchy. It allows you to search based on various criteria, such as name, size, modification time, permissions, and file type. The `find` command recursively traverses directories, making it suitable for locating files across an entire file system or within specific subdirectories.

- [article] [10 ways to use the Linux find command](https://www.redhat.com/en/blog/linux-find-command)
- [video] [Linux Crash Course - The find command](https://www.youtube.com/watch?v=skTiK_6DdqU)

### Stop Execution

Stopping execution in a shell script refers to halting the script's progress, often due to an error, a specific condition being met, or a user's request. This can be achieved through various commands and techniques that control the flow of the script, ensuring that it doesn't continue running when it shouldn't. Properly stopping execution is crucial for preventing unintended consequences and maintaining the integrity of the system.

**Section resources:**
- [article] [Bash kill Command - Terminate Processes](https://www.w3schools.com/bash/bash_kill.php)
- [article] [How to exit from Bash script](https://linuxconfig.org/how-to-exit-from-bash-script)
- [video] [Killing Processes Linux Shell Tutorial](https://www.youtube.com/watch?v=03umJo33aQg)

#### Command substitution

Command substitution allows you to use the output of a command as an argument to another command. It essentially captures the standard output of a command and inserts it into the command line of another command, enabling you to dynamically generate arguments or values based on the results of other commands. This is useful for tasks like assigning the output of a command to a variable, using the ou…

- [article] [Command substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html)
- [article] [Command substitution - Wikipedia](https://en.wikipedia.org/wiki/Command_substitution)
- [video] [How to use Command Substitution in Bash](https://www.youtube.com/watch?v=b8U_fz0pc-g)

#### Navigate between dirs

Navigating between directories in a shell environment involves moving from one location in the file system to another. This is primarily achieved using the `cd` (change directory) command, which allows users to specify the destination directory, whether it's a relative path from the current location or an absolute path from the root directory. Special notations like `.` (current directory), `..` (…

- [article] [What are the differences between absolute and relative paths?](https://www.redhat.com/en/blog/linux-path-absolute-relative)
- [article] [Navigating the file system with Terminal](https://gomakethings.com/navigating-the-file-system-with-terminal/)
- [video] [What is the difference between absolute and relative paths?](https://www.youtube.com/watch?v=bxr4p5Ik4js)
- [video] [Absolute and Relative Paths](https://www.youtube.com/watch?v=ephId3mYu9o)

#### Process substitution

Process substitution allows you to treat the output of a process as if it were a file. It provides a way to pass the output of one command as input to another command, without using temporary files or named pipes. This is achieved by creating a temporary file-like object (either a named pipe or a file in `/dev/fd`) that the command writes its output to, and then passing the name of this object to…

- [article] [Process Substitution](https://tldp.org/LDP/abs/html/process-sub.html)
- [article] [Handy Bash feature: Process Substitution](https://medium.com/@joewalnes/handy-bash-feature-process-substitution-8eb6dce68133)
- [video] [Command vs. Process substitution in Bash - explaining the difference.](https://www.youtube.com/watch?v=f3eIK5xk4vg)
- [video] [Process Substitution in BASH - Commands for Linux](https://www.youtube.com/watch?v=dR0X0-B9ObA)

### Redirects & Pipelines

Redirects and pipelines are fundamental features in the shell that allow you to control the flow of data between commands. Redirects change where a command's input comes from or where its output goes, allowing you to read from files or write to files. Pipelines connect the output of one command directly to the input of another, enabling you to chain commands together to perform complex operations in a sequence.

**Section resources:**
- [official] [Redirections](https://www.gnu.org/software/bash/manual/html_node/Redirections.html)
- [article] [Unix / Linux - Shell Input/Output Redirections](https://www.tutorialspoint.com/unix/unix-io-redirections.htm)
- [video] [IO Redirection in Bash EXPLAINED](https://www.youtube.com/watch?v=7VaO2dxs_kg)

#### grep

`grep` is a command-line utility used for searching plain-text data sets for lines matching a regular expression. It outputs the lines that contain the specified pattern, making it a powerful tool for filtering and locating specific information within files or streams of data. Its name comes from the ed command `g/re/p` (globally search a regular expression and print).

- [article] [Mastering Grep command in Linux/Unix: A Beginner's Tutorial](https://www.digitalocean.com/community/tutorials/grep-command-in-linux-unix)
- [article] [Bash grep Command - Search Text Using Patterns](https://www.w3schools.com/bash/bash_grep.php)
- [video] [Linux Crash Course - The grep Command](https://www.youtube.com/watch?v=Tc_jntovCM0)

#### cut, paste

`cut` and `paste` are command-line utilities used for manipulating text files. `cut` extracts specific sections (columns) from each line of a file based on delimiters or character positions. `paste` merges lines from multiple files into a single output stream, typically by concatenating corresponding lines side-by-side.

- [article] [Cut Command in Linux | Linuxize](https://linuxize.com/post/linux-cut-command/)
- [article] [Paste Command in Linux (Merge Lines) | Linuxize](https://linuxize.com/post/paste-command-in-linux/)
- [video] [Linux Crash Course - The cut Command](https://www.youtube.com/watch?v=GYP2T34v56E)
- [video] [Linux Tutorials | paste command](https://www.youtube.com/watch?v=ilV6dcTJzzE)

#### wc

`wc` is a command-line utility that displays the number of lines, words, and bytes (or characters) in a file. It's a simple yet powerful tool for quickly getting a summary of the size and content of text files. You can use it to count the number of lines in a log file, the number of words in a document, or the size of a configuration file.

- [article] [Wc Command - Count Number of Lines, Words, and Characters](https://www.tecmint.com/wc-command-examples/)

#### *

The asterisk (\*) is a wildcard character that represents zero or more characters. It's used in commands and file paths to match multiple files or directories based on a pattern. For example, `*.txt` will match all files ending with ".txt", and `data*` will match files or directories starting with "data".

- [article] [Wildcards](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm)
- [article] [Wildcard characters in Shell Script Linux](https://nkugwamarkwilliam.medium.com/wildcard-characters-in-shell-script-linux-6e885b624565)
- [video] [Bash Globbing Basics! How to use wildcards on the shell](https://www.youtube.com/watch?v=gsucx2W-9sg)

#### less, more

`less` and `more` are command-line utilities used to view the contents of text files, one screen at a time. They allow users to navigate through the file, search for specific patterns, and perform other basic text manipulation tasks directly from the terminal. `less` is generally preferred over `more` because it offers more features, including the ability to scroll backwards.

- [article] [More Command](https://www.ibm.com/docs/en/aix/7.2.0?topic=m-more-command)
- [article] [Less Command in Linux](https://linuxize.com/post/less-command-in-linux/)
- [video] [How to Use Unix MORE Command](https://www.youtube.com/watch?v=at7l0REMi04)
- [video] [Linux Command Line Tutorial For Beginners 10 - less command](https://www.youtube.com/watch?v=06GsFVeuWNk)

#### join, split

`join` and `split` are command-line utilities used for manipulating text files. `join` combines lines from two files based on a common field, creating a new file with the merged data. `split`, conversely, divides a single file into multiple smaller files, either by line count, file size, or a custom pattern.

- [article] [Use Join Command in Linux: A Detailed Guide](https://linuxconfig.org/join)
- [article] [Linux split Command {13 Examples}](https://phoenixnap.com/kb/linux-split)
- [video] [LPIC-1 101 Using the join command](https://www.youtube.com/watch?v=b3Ybtr6xti4)
- [video] [Linux - How to split larger files into smaller parts](https://www.youtube.com/watch?v=DaC5AWjmQXk)

#### sort

`sort` is a command-line utility that arranges lines of text in a specific order. It can sort alphabetically, numerically, by month, or even based on custom criteria. By default, `sort` treats each line as a string and sorts them in ascending ASCII order, but its behavior can be modified using various options to handle different data types and sorting preferences.

- [article] [Bash sort Command - Sort Lines of Text Files](https://www.w3schools.com/bash/bash_sort.php)
- [video] [Bash sort Command - Sort Lines of Text Files](https://www.youtube.com/watch?v=2B16aYGzIEQ)

#### ?

The question mark (?) wildcard is a single-character wildcard. It matches exactly one occurrence of any character. This means that when used in a pattern, it will be replaced by any single character in a filename or string, allowing you to match files or strings with slight variations in their names or content.

- [article] [How To Use Unix Wildcards](https://www.warp.dev/terminus/linux-wildcards)
- [article] [Wildcard characters in Shell Script Linux](https://nkugwamarkwilliam.medium.com/wildcard-characters-in-shell-script-linux-6e885b624565)
- [video] [Bash Globbing Basics! How to use wildcards on the shell](https://www.youtube.com/watch?v=gsucx2W-9sg)

#### head, tail

`head` and `tail` are command-line utilities used to display the beginning or end of a file, respectively. `head` shows the first few lines of a file, while `tail` shows the last few lines. They are useful for quickly inspecting log files, configuration files, or any text-based data without opening the entire file in a text editor.

- [article] [Bash head Command - Display the beginning of a file](https://www.w3schools.com/bash/bash_head.php)
- [article] [Bash tail Command - Display Last Part of Files](https://www.w3schools.com/bash/bash_tail.php)
- [video] [Linux Crash Course - The head and tail Commands](https://www.youtube.com/watch?v=5EqL6Fc7NNw)

#### tr

The `tr` command in Unix-like operating systems is a command-line utility that translates or deletes characters. It reads standard input, performs the specified transformations, and writes the result to standard output. `tr` is often used for tasks like converting uppercase to lowercase, deleting specific characters, or replacing one set of characters with another.

- [article] [Linux tr Command with Examples](https://phoenixnap.com/kb/linux-tr)
- [video] [Linux Crash Course - The tr Command](https://www.youtube.com/watch?v=4qP5xA_epXo)

#### uniq

`uniq` is a command-line utility that filters adjacent matching lines from an input file (or standard input) and writes a single copy of the matching line to the output. It's primarily used to remove duplicate lines, but it requires that the duplicates be next to each other to be effective. Options allow you to count the number of occurrences of each line, display unique lines, or display only dup…

- [article] [How to use the uniq command to process lists in Linux](https://www.redhat.com/en/blog/uniq-command-lists)
- [video] [Uniq utility (commands for linux)](https://www.youtube.com/watch?v=VRrd9ErU13w)

#### [...]

Square brackets `[]` in shell wildcards define a character class, matching any single character _within_ the brackets. This allows you to specify a range or set of characters to match in a filename or string. For example, `[abc]` will match either 'a', 'b', or 'c'. You can also use ranges like `[a-z]` to match any lowercase letter or `[0-9]` to match any digit. A caret `^` inside the brackets nega…

- [article] [Standard Wildcards / Globbing Patterns in Linux](https://www.putorius.net/standard-wildcards-globbing-patterns-in.html)
- [video] [wildcards in linux | asterisk , question mark , square brackets , curly brackets , escape character](https://www.youtube.com/watch?v=_J9JwnIzJ9o)

#### find

`find` is a command-line utility for searching files and directories within a specified directory hierarchy. It allows you to locate files based on various criteria, such as name, type, size, modification time, permissions, and more. The `find` command recursively traverses the directory structure, applying the specified search criteria to each file and directory it encounters, and then displays t…

- [article] [10 ways to use the Linux find command](https://www.redhat.com/en/blog/linux-find-command)
- [video] [Linux Crash Course - The find command](https://www.youtube.com/watch?v=skTiK_6DdqU)

#### sed

`sed` (Stream EDitor) is a powerful command-line utility used for text transformation. It operates on a stream of text, performing operations like searching, replacing, deleting, and inserting text based on patterns or line numbers. `sed` is commonly used in shell scripting for automating text editing tasks and manipulating data within files or pipelines.

- [article] [Bash sed Command - Stream Editor](https://www.w3schools.com/bash/bash_sed.php)
- [article] [Mastering sed Command in Linux: A Comprehensive Guide | DigitalOcean](https://www.digitalocean.com/community/tutorials/linux-sed-command)
- [video] [Linux Crash Course - The sed Command](https://www.youtube.com/watch?v=nXLnx8ncZyE)

#### awk

`awk` is a powerful text processing tool in Unix-like operating systems. It scans input files line by line, searching for lines that match a specified pattern. When a matching line is found, `awk` performs a specified action on that line, such as printing it, modifying it, or extracting specific fields. It's particularly useful for manipulating data within files and generating reports.

- [article] [AWK command in Linux/Unix | DigitalOcean](https://www.digitalocean.com/community/tutorials/awk-command-linux-unix)
- [article] [The Linux AWK Command – Linux and Unix Usage Syntax Examples](https://www.freecodecamp.org/news/the-linux-awk-command-linux-and-unix-usage-syntax-examples/)
- [video] [Linux Crash Course - awk](https://www.youtube.com/watch?v=oPEnvuj9QrI)

#### nl

`nl` is a command-line utility that numbers the lines of a file or standard input. It reads lines, adds line numbers, and writes the result to standard output. You can customize the numbering style, starting number, and increment between numbers. It's useful for adding line numbers to code, documents, or any text file for easier reference.

- [article] [Use nl Command in Linux - Step-by-Step Guide](https://linuxconfig.org/nl)
- [video] [nl command in Linux with Examples](https://www.youtube.com/watch?v=WqrRKfJWqqM)

#### {...}

Curly braces `{}` are used for multiple matches. Each string can be an exact name, or a wildcard. It will find anything that matches any of the given strings using an or relationship (one OR the other). For example, `touch file{1,2,3}.txt` will create three files: `file1.txt`, `file2.txt`, and `file3.txt`.

- [article] [Standard Wildcards / Globbing Patterns in Linux](https://www.putorius.net/standard-wildcards-globbing-patterns-in.html)
- [video] [wildcards in linux | asterisk , question mark , square brackets , curly brackets , escape character](https://www.youtube.com/watch?v=_J9JwnIzJ9o)

### Text Editors

Text editors are software programs that allow users to create, open, view, and modify plain text files. They are fundamental tools for writing code, scripts, configuration files, and general text-based documents. Unlike word processors, text editors focus on the raw text content without applying rich formatting or styles.

### Basic Editor Ops.

Basic editor operations involve fundamental actions performed within a text editor to create, modify, and manage files. These operations include opening, saving, and closing files, as well as inserting, deleting, copying, and pasting text. Navigating through a file, searching for specific content, and replacing text are also key components of basic editor operations.

**Section resources:**
- [article] [Beginner's Guide to Nano Text Editor](https://itsfoss.com/nano-editor-guide/)
- [article] [GNU Emacs - Guided Tour](https://www.gnu.org/software/emacs/tour/)
- [video] [Linux Crash Course - nano (command-line text editor)](https://www.youtube.com/watch?v=DLeATFgGM-A)
- [video] [The Basics of Emacs as a Text Editor](https://www.youtube.com/watch?v=jPkIaqSh3cA)

#### Direct Execution

Direct execution involves running a shell script by specifying its path directly to the shell. This method requires the script to have execute permissions set. When you directly execute a script, the operating system uses the shebang line (e.g., `#!/bin/bash`) at the beginning of the script to determine which interpreter should be used to execute the script's commands.

- [article] [Sourcing vs Executing Script Directly](https://dillionmegida.com/p/sourcing-vs-executing-script-directly/)
- [video] [Source Shell Script vs Executing Shell Script - The Real Difference](https://www.youtube.com/watch?v=ZIqRmp-XBRY)

### Bash Script Anatomy

A Bash script is essentially a plain text file containing a series of commands that the Bash interpreter executes sequentially. It typically starts with a shebang line specifying the interpreter to use, followed by comments explaining the script's purpose, and then the actual commands that perform the desired actions, including variable assignments, control structures (like loops and conditional statements), and function definitions.

**Section resources:**
- [course] [Bash Scripting](https://linuxhandbook.com/courses/bash/)
- [article] [Bash Script](https://www.w3schools.com/bash/bash_script.php)
- [video] [Bash Scripting Tutorial for Beginners](https://www.youtube.com/watch?v=tK9Oc6AEnR4)

#### Running with Bash

Running a shell script with Bash involves explicitly invoking the Bash interpreter to execute the commands within the script. This is typically done by using the `bash` command followed by the script's filename as an argument. This method ensures that the script is interpreted and executed using the Bash shell, regardless of the script's shebang line or the user's default shell.

- [article] [Bash Scripting Tutorial – Linux Shell Script and Command Line for Beginners](https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/)
- [video] [How to run bash script in Linux | Linux in a Minute](https://www.youtube.com/watch?v=iViofyFir9o)

### Running Shell Scripts

Running a shell script involves executing a file containing a series of commands that the shell interprets and performs. This allows you to automate tasks, create reusable tools, and manage system operations by grouping commands into a single executable unit. The script is typically a plain text file with a `.sh` extension, and it needs execute permissions to be run directly.

**Section resources:**
- [article] [How to run the .sh file in Linux](https://www.hostinger.com/tutorials/how-to-run-sh-file-in-linux)
- [article] [How To Run the .sh File Shell Script In Linux / UNIX](https://www.cyberciti.biz/faq/run-execute-sh-shell-script/)
- [video] [How to run bash script in Linux | Linux in a Minute](https://www.youtube.com/watch?v=iViofyFir9o)

#### Nano

Nano is a simple, beginner-friendly text editor for Unix-like operating systems. It's designed to be easy to use, with a straightforward interface that displays command shortcuts at the bottom of the screen. Nano is often pre-installed on many systems, making it readily available for quick text editing tasks.

- [official] [nano – Text editor](https://www.nano-editor.org/)
- [article] [How to Use Nano, the Linux Command Line Text Editor](https://linuxize.com/post/how-to-use-nano-text-editor/)
- [video] [How to Use Nano | Command Line Text Editor](https://www.youtube.com/watch?v=PDWHxh9HUF8)

#### Vim

Vim is a highly configurable text editor built to enable efficient text editing. It's an improved version of the vi editor distributed with most UNIX systems. Vim is known for its modal editing, allowing users to switch between different modes for inserting, deleting, and navigating text, making it a powerful tool for developers and system administrators.

- [course] [OpenVim - Interactive Vim Tutorial](https://openvim.com/)
- [official] [Vim](https://www.vim.org/)
- [article] [Getting started with Vim: The basics](https://opensource.com/article/19/3/getting-started-vim)
- [video] [Vim As Your Editor - Introduction](https://www.youtube.com/watch?v=X6AR2RMB5tE)

#### Running with Source

Sourcing a shell script executes the commands within the script in the _current_ shell environment, rather than in a subshell. This means that any variables, functions, or aliases defined or modified within the script will directly affect the shell you're currently working in. This is in contrast to simply executing a script, which creates a new process and any changes are isolated to that process…

- [article] [https://dillionmegida.com/p/sourcing-vs-executing-script-directly/](https://dillionmegida.com/p/sourcing-vs-executing-script-directly/)
- [video] [Source Shell Script vs Executing Shell Script - The Real Difference](https://www.youtube.com/watch?v=ZIqRmp-XBRY)

#### Emacs

Emacs is a highly customizable and extensible text editor, known for its powerful features and extensive ecosystem of extensions. It's more than just a text editor; it's often described as an operating system within an operating system due to its ability to handle tasks like file management, email, and even web browsing, all within its environment. Emacs is favored by programmers and power users w…

- [official] [GNU Emacs](https://www.gnu.org/software/emacs/)
- [article] [How To Use the Emacs Editor in Linux | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-use-the-emacs-editor-in-linux)
- [video] [The Absolute Beginner's Guide to Emacs](https://www.youtube.com/watch?v=48JlgiBpw_I)

#### Vi

Vi is a powerful text editor that's been a standard part of Unix-like systems for decades. It operates in different modes, primarily command mode for issuing instructions and insert mode for typing text. Vi is known for its efficiency and keyboard-centric approach, allowing users to perform complex editing tasks without relying heavily on a mouse.

- [article] [An introduction to the vi editor](https://www.redhat.com/en/blog/introduction-vi-editor)
- [video] [Basics of VI editor in under 8 minutes | Vi editor Tutorial](https://www.youtube.com/watch?v=-_DvfdgR-LA)

#### Strings

In Bash, strings are sequences of characters. They can be enclosed in single quotes (`'...'`) or double quotes (`"..."`). Single quotes treat everything literally, meaning no variable substitution or command execution happens within them. Double quotes, on the other hand, allow for variable expansion and command substitution. Suppose you want to include a literal single quote within a single-quote…

- [article] [Bash Data Types](https://www.w3schools.com/bash/bash_data_types.php)
- [article] [Bash Scripting - String](https://www.geeksforgeeks.org/linux-unix/bash-scripting-string/)
- [article] [Manipulating Strings](https://tldp.org/LDP/abs/html/string-manipulation.html)

#### Numeric

Bash, by default, treats all variables as strings. However, Bash can perform arithmetic operations on variables that contain numeric values. While Bash doesn't have explicit data types like integers or floats in the same way as other programming languages, it interprets strings as numbers when used in arithmetic contexts. This allows you to perform calculations, comparisons, and other numeric mani…

- [article] [Arithmetic - Bash Scripting Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/bash-arithmetic.php)

#### Environment vs Shell vars.

Environment variables are a set of dynamic named values that can affect the way running processes will behave on a computer. They are part of the environment in which a process runs. Shell variables, on the other hand, are variables that are specific to the current shell session and are not automatically inherited by child processes. They are used to store temporary values or configure the shell's…

- [article] [Environment and Shell variables In Linux](https://www.futurelearn.com/info/courses/linux-for-bioinformatics/0/steps/201724)
- [article] [How To Read and Set Environmental and Shell Variables on Linux](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux)
- [video] [shell vs environment variables (and env, export, etc.) (intermediate) anthony explains](https://www.youtube.com/watch?v=h36Xc38SDHg)

#### Read user input

Reading user input in a shell script allows the script to interact with the person running it. This is achieved by pausing the script's execution and waiting for the user to type something and press Enter. The entered text can then be stored in a variable and used later in the script for various purposes, such as making decisions or providing customized output.

- [article] [User Input!](https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php)
- [article] [Reading User Input](https://www.warp.dev/terminus/bash-reading-user-input)
- [video] [How do I read user input into a variable in Bash | Shell Scripting Tutorial for Beginners](https://www.youtube.com/watch?v=Sc2v6Dj3Z4M)

#### Arrays

Arrays are ordered collections of elements, where each element can be accessed using an index. They allow you to store multiple values under a single variable name, making it easier to manage and manipulate related data. In Bash, arrays can hold strings or numbers, and they are indexed starting from zero.

- [article] [Bash Arrays](https://www.w3schools.com/bash/bash_arrays.php)
- [video] [Arrays in Pure Bash - You Suck at Programming](https://www.youtube.com/watch?v=r4Sc-DpIprk)
- [video] [Arrays in Bash Explained in 7 Minutes! - Indexed, Associative, and Nested / Multi-Dimensional](https://www.youtube.com/watch?v=asHJ-xfuyno)

#### Create, Print, Modify

Variables in shell scripting are named storage locations that hold data. You can create a variable by assigning a value to a name. Printing a variable displays its stored value, and modifying a variable involves changing the value it holds, allowing you to update data within your scripts dynamically.

- [article] [Understanding Shell Script Variables - The Shell Scripting Tutorial](https://www.shellscript.sh/variables1.html)
- [article] [Unix Tutorial #4: Shells and Path Variables — Andy's Brain Book 1.0 documentation](https://andysbrainbook.readthedocs.io/en/latest/unix/Unix_04_ShellsVariables.html)
- [article] [Unix / Linux - Using Shell Variables](https://www.tutorialspoint.com/unix/unix-using-variables.htm)
- [video] [How To Use Shell Environment Variables](https://www.youtube.com/watch?v=9ZpL8iDU7LY)

#### printf formatting

`printf` is a command-line utility used to format and print text in a specific way. It allows you to control the appearance of output by using format specifiers, which define how different types of data (strings, numbers, etc.) should be displayed. This includes specifying the width, precision, alignment, and other attributes of the output.

- [article] [Bash printf Command](https://linuxize.com/post/bash-printf-command/)
- [article] [Bash printf](https://www.warp.dev/terminus/bash-printf)
- [video] [Bash: printf usage and example](https://www.youtube.com/watch?v=_mi0O52_gwU)

#### Associative Arrays

Associative arrays, also known as dictionaries or hash maps in other programming languages, are data structures that store key-value pairs. Unlike regular arrays which use numerical indexes to access elements, associative arrays use strings (or other data types in some languages) as keys. This allows you to retrieve values based on meaningful names rather than just positions.

- [article] [Associative arrays in Bash](https://rednafi.com/misc/associative-arrays-in-bash/)
- [article] [Creating And Using An Associative Array In A Bash Script | by Linux Root Room](https://medium.com/@linuxrootroom/create-and-use-associative-array-in-bash-script-5f4e32a00577)
- [video] [Arrays in Bash Explained in 7 Minutes! - Indexed, Associative, and Nested / Multi-Dimensional](https://www.youtube.com/watch?v=asHJ-xfuyno)

#### Variable Scopes

Variable scope determines the region of a program where a declared variable can be accessed. It defines the visibility and lifetime of a variable. Understanding variable scope is crucial for writing clean, maintainable, and bug-free shell scripts, as it helps prevent naming conflicts and ensures that variables are used in the intended context.

- [article] [Bash shell basics — scoping](https://paulguerin.medium.com/bash-shell-basics-scoping-d59c8e1468b4)
- [article] [How to Work with Shell Variables and Functions](https://labex.io/fr/tutorials/shell-how-to-work-with-shell-variables-and-functions-392774)
- [video] [Bash Shell Scripting For Beginners - Local and Global Variables](https://www.youtube.com/watch?v=4GR0wum_pOQ)

#### Here documents

Here documents (or "heredocs") are a way to redirect multiple lines of input to a command. Instead of typing input directly into the terminal or reading from a file, you can embed the input directly within your script. This is particularly useful for passing multi-line strings or configuration data to commands.

- [article] [Here documents](https://tldp.org/LDP/abs/html/here-docs.html)
- [article] [Heredoc: A Deep Dive](https://medium.com/@oduwoledare/heredoc-a-deep-dive-23c82992e522)
- [video] [Heredocs in Bash! Understanding how they work and a few gotchas. You Suck at Programming](https://www.youtube.com/watch?v=-a1VAole01s)

#### Special variables

Special variables in shell scripting are predefined variables that automatically hold specific values related to the shell's operation or the script's execution environment. These variables provide access to information like the script's name, the number of arguments passed to it, the exit status of the last command, and process IDs. They are read-only in most cases, meaning you can't directly mod…

- [article] [Special variables](https://www.tutorialspoint.com/unix/unix-special-variables.htm)
- [article] [Special Variable Types](https://tldp.org/LDP/abs/html/othertypesv.html)
- [video] [Special Variables | Shell Scripting Tutorial For Beginners](https://www.youtube.com/watch?v=PfxzX4XNYRE)

#### Here strings

Here strings provide a way to pass strings to commands as standard input. They are a simplified form of here documents, designed for single-line input. Instead of redirecting a file or typing input directly, you can embed the string directly within the command using the `<<<` operator. This is particularly useful for commands that expect input from stdin but you want to provide it inline within yo…

- [article] [Here Strings](https://tldp.org/LDP/abs/html/x17837.html)
- [video] [Here Strings in Bash! Redirecting a string into stdin. You Suck at Programming](https://www.youtube.com/watch?v=0cWuZvw8lXc)

### Bash Data Types

Bash, unlike some other programming languages, doesn't have explicit data types like integers, floats, or strings that you need to declare. Instead, everything is treated as a string. However, Bash can perform arithmetic operations on strings that contain numbers, effectively treating them as numerical values when needed. Arrays are also supported, allowing you to store collections of string values.

**Section resources:**
- [article] [Bash Data Types](https://www.w3schools.com/bash/bash_data_types.php)
- [article] [The Type System of Bash](https://www.celantur.com/blog/bash-type-system/)

#### Variables best practices

Using variables effectively in shell scripts involves following certain guidelines to improve readability, maintainability, and prevent errors. This includes choosing descriptive names, initializing variables before use, using appropriate scoping, and quoting variables to avoid unexpected behavior due to word splitting and globbing. Adhering to these practices leads to more robust and understandab…

- [article] [Guide to Naming Conventions for Shell Variables](https://www.baeldung.com/linux/shell-variable-naming-conventions)
- [article] [Shell Script Best Practices](https://sharats.me/posts/shell-script-best-practices/)

### Input/Output

Input/Output (I/O) refers to the communication between a computer program and the outside world. This involves receiving data (input) from sources like the keyboard, files, or other programs, and sending data (output) to destinations such as the terminal, files, or other programs. In essence, it's how a program interacts with its environment to receive instructions and display results.

### Comments

Comments are explanatory notes added to code to make it easier to understand. They are ignored by the interpreter or compiler, meaning they don't affect how the program runs. They are primarily for human readers to understand the purpose and logic behind the code.

**Section resources:**
- [article] [Writing Comments in Bash Scripts](https://linuxize.com/post/bash-comments/)
- [article] [How to Comment in Bash](https://phoenixnap.com/kb/bash-comment)
- [video] [Comments - Bash Scripting](https://www.youtube.com/watch?v=Ky9AiwIeORA)

### Bash Operators

Bash operators are special symbols or characters that perform specific actions or comparisons within a Bash script or command line. They are fundamental building blocks for controlling program flow, manipulating data, and performing various operations like arithmetic calculations, string comparisons, file manipulations, and logical evaluations. Understanding and using these operators effectively is crucial for writing robust and efficient Bash scripts.

**Section resources:**
- [article] [Bash Operators](https://www.w3schools.com/bash/bash_operators.php)
- [article] [Operators](https://tldp.org/LDP/abs/html/ops.html)

#### Arithmetic

Arithmetic operators in Bash are symbols used to perform mathematical calculations within shell scripts. These operators allow you to add, subtract, multiply, divide, and find the remainder of numbers directly within your scripts, enabling you to perform calculations and manipulate numerical data. Bash primarily uses integer arithmetic, but there are ways to work with floating-point numbers as wel…

- [article] [Bash Math Operations (Bash Arithmetic) Explained](https://phoenixnap.com/kb/bash-math)
- [article] [Bash Operators](https://www.w3schools.com/bash/bash_operators.php)
- [video] [Arithmetic Expressions - Bash Programming Tutorial](https://www.youtube.com/watch?v=rjuB3X8MOQc)

#### Arithmetic expansion

Arithmetic expansion allows you to perform mathematical calculations directly within your shell scripts. It uses the `$((...))` syntax to evaluate expressions, treating the contents inside the parentheses as an arithmetic expression. This enables you to perform operations like addition, subtraction, multiplication, division, and modulo, and assign the results to variables or use them in conditiona…

- [article] [Arithmetic Expansion (Bash Reference Manual)](https://www.gnu.org/software/bash/manual/html_node/Arithmetic-Expansion.html)
- [article] [Bash Math Operations (Bash Arithmetic) Explained {+11 Examples}](https://phoenixnap.com/kb/bash-math)
- [video] [Arithmetic Expressions - Bash Programming Tutorial 4](https://www.youtube.com/watch?v=rjuB3X8MOQc)

#### Comparison

Comparison operators in Bash are used to compare values, typically numbers or strings. These operators allow you to create conditional statements within your scripts, enabling different code blocks to execute based on whether a comparison is true or false. They are fundamental for making decisions and controlling the flow of execution in your Bash scripts.

- [article] [Other Comparison Operators](https://tldp.org/LDP/abs/html/comparison-ops.html)
- [article] [Bash Operators](https://www.w3schools.com/bash/bash_operators.php)
- [article] [Shell Scripting: Comparison Operators and If Statements](https://medium.com/@kadimasam/shell-scripting-comparison-operators-and-if-statements-9e0277fd60b8)
- [video] [Comparison Operators and Square Brackets - Bash Programming Tutorial](https://www.youtube.com/watch?v=XSLj65wnP90)

#### expr

`expr` is a command-line utility used to evaluate expressions. It can perform arithmetic operations, string manipulations, and logical comparisons. The `expr` command takes arguments as operands and operators, evaluates the expression, and writes the result to standard output. It's often used in shell scripts for performing calculations and making decisions based on numerical or string values.

- [article] [Practical examples of “expr” command in Linux](https://tecadmin.net/expr-command-examples/)
- [video] [Linux Tutorial for Beginners | expr command | Evaluate Expressions in Linux](https://www.youtube.com/watch?v=6LbMLSBoLGY)

#### bc

`bc` is a command-line utility for arbitrary-precision arithmetic. It allows you to perform calculations with numbers of any size and with a specified level of decimal precision, making it suitable for tasks where standard shell arithmetic is insufficient. `bc` can be used interactively or non-interactively, reading expressions from standard input or from files.

- [article] [Linux Handbook | bc command in Linux](https://linuxhandbook.com/bc-command/)
- [article] [Linux bc Command with Examples](https://phoenixnap.com/kb/linux-bc)
- [video] [Shell Scripting Tutorial for Beginners 11 - Floating point math operations in bash | bc Command](https://www.youtube.com/watch?v=yqpY-Wk-i9k)

#### $1, $2, $3

Positional parameters in shell scripting are variables that hold the command-line arguments passed to a script. These parameters are represented by special variables like `$1`, `$2`, `$3`, and so on, where each number corresponds to the order in which the argument was provided when the script was executed. `$1` holds the first argument, `$2` the second, and so forth, allowing scripts to access and…

- [article] [Bash Positional Parameters](https://adminschoice.com/bash-positional-parameters/)
- [article] [Positional Parameters](https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html)

#### $0

In shell scripting, `$0` is a special variable that holds the name of the script being executed. It essentially represents the command used to invoke the script. This can be the script's filename, or if the script was invoked with a path, it will contain that path. `$0` is useful for identifying the script itself within the script's code, for example, in logging or error messages.

- [article] [Understanding Special Parameters in Linux Shell Scripting](https://medium.com/@tradingcontentdrive/understanding-special-parameters-in-linux-shell-scripting-0-62768f49fb34)
- [video] [Using BASH Script Arguments](https://www.youtube.com/watch?v=vsRBWCfMf9A)

#### String operators

String operators in Bash are symbols or keywords used to perform operations on strings, such as checking if a string is empty, comparing strings, extracting substrings, or determining the length of a string. These operators are essential for manipulating and evaluating string values within shell scripts, enabling conditional logic and data processing based on string content.

- [article] [Bash String Comparison: The Comprehensive Guide](https://www.namehero.com/blog/bash-string-comparison-the-comprehensive-guide/)
- [article] [String Operators](https://www.oreilly.com/library/view/learning-the-bash/1565923472/ch04s03.html)

#### let

The `let` command in Bash is used to perform arithmetic operations. It allows you to evaluate arithmetic expressions and assign the result to a variable. It's a way to do integer calculations directly within your shell scripts without needing external commands like `expr`.

- [article] [How to Use the Bash let Command {with Examples}](https://phoenixnap.com/kb/bash-let)
- [article] [Arithmetic](https://ryanstutorials.net/bash-scripting-tutorial/bash-arithmetic.php)
- [video] [Bash: The "let" builtin command](https://www.youtube.com/watch?v=OmZVThsrdp0)

#### awk

Awk is a powerful text processing tool that can also perform numeric calculations. It reads input line by line and executes a set of instructions for each line. These instructions can include arithmetic operations, comparisons, and variable assignments, making awk useful for tasks like calculating sums, averages, and performing other data manipulations directly within the shell.

- [article] [How To Use awk In Bash Scripting](https://www.cyberciti.biz/faq/bash-scripting-using-awk/)
- [article] [Bash awk - Pattern Scanning and Processing Language](https://www.w3schools.com/bash/bash_awk.php)
- [video] [Learning Awk Is Essential For Linux Users](https://www.youtube.com/watch?v=9YOZmI-zWok)

#### $@

`$@` is a special variable in shell scripting that expands to all the positional parameters (arguments) passed to a script. Each argument is treated as a separate word, even if it contains spaces, ensuring that the script receives and processes each argument individually. This is particularly useful when you need to iterate over or manipulate each argument provided to your script.

- [article] [Understanding Special Parameters in Linux Shell Scripting:](https://medium.com/@tradingcontentdrive/understanding-special-parameters-in-linux-shell-scripting-0-62768f49fb34)

#### $*

`$*` is a special variable in shell scripting that expands to all the positional parameters (arguments) passed to a script or function. It represents all the arguments as a single string, with each argument separated by the first character of the `IFS` (Internal Field Separator) variable, which defaults to a space, tab, and newline. This allows you to easily access and iterate over all the argumen…

- [article] [Understanding Special Parameters in Linux Shell Scripting](https://medium.com/@tradingcontentdrive/understanding-special-parameters-in-linux-shell-scripting-0-62768f49fb34)

#### Logical

Logical operators in Bash are used to combine or modify conditional expressions. They allow you to create more complex tests within your scripts, enabling you to execute commands based on multiple conditions being true or false. The primary logical operators are `&&` (AND), `||` (OR), and `!` (NOT). These operators are essential for controlling the flow of your scripts based on the evaluation of d…

- [article] [How to program with Bash: Logical operators and shell expansions](https://opensource.com/article/19/10/programming-bash-logical-operators-shell-expansions)
- [video] [Logical Operators - Bash Programming Tutorial 8](https://www.youtube.com/watch?v=sDRHmbRlNT8)

#### $#

`$#` is a special variable in shell scripting that represents the number of arguments passed to a script when it is executed. It's a simple integer value that allows you to determine how many inputs the user provided when running your script, enabling you to write logic that handles different scenarios based on the number of arguments.

- [article] [Understanding Special Parameters in Linux Shell Scripting](https://medium.com/@tradingcontentdrive/understanding-special-parameters-in-linux-shell-scripting-0-62768f49fb34)

#### shift

The `shift` command in shell scripting renames the command-line arguments. Specifically, it moves each argument one position to the left. The value of `$2` becomes `$1`, the value of `$3` becomes `$2`, and so on. The original value of `$1` is lost. This is particularly useful when you need to process a variable number of arguments passed to a script.

- [video] [BASH Shifting Argument Variables Linux Shell Tutorial](https://www.youtube.com/watch?v=fJSUVGlQ1E8)

#### File test

File test operators in Bash are used to check the type and attributes of files. These operators allow you to determine if a file exists, if it's a regular file or a directory, if it's readable, writable, or executable, and other file-related properties. The result of a file test is a boolean value (true or false), which can be used in conditional statements to control the flow of a script.

- [article] [File test operators](https://tldp.org/LDP/abs/html/fto.html)
- [article] [Bash Tests](https://docs.rockylinux.org/10/books/learning_bash/05-tests/)
- [video] [Shell Scripting Tutorial for Beginners 6 - File test operators](https://www.youtube.com/watch?v=uVi5o38NGi0)

### Script Arguments

Script arguments are values passed to a shell script when it is executed. These arguments allow you to customize the script's behavior without modifying the script's code directly. They are accessed within the script using positional parameters like `$1`, `$2`, `$3`, and so on, where `$1` represents the first argument, `$2` the second, and so forth. The special variable `$0` holds the name of the script itself, and `$#` contains the number of arguments passed.

**Section resources:**
- [article] [Using Arguments in Bash Scripts](https://refine.dev/blog/bash-script-arguments/#introduction)
- [article] [Adding arguments and options to your Bash scripts](https://www.redhat.com/en/blog/arguments-options-bash-scripts)
- [video] [Passing Arguments to the Script | Shell Scripting Tutorial for Beginners](https://www.youtube.com/watch?v=Gexu9M7p5aU)

### String Manipulation

String manipulation involves modifying or extracting parts of text data. This can include tasks like finding specific characters, replacing substrings, changing the case of letters, or extracting portions of a string based on delimiters or patterns. These operations are fundamental for processing and transforming textual information.

**Section resources:**
- [article] [Manipulating Strings](https://tldp.org/LDP/abs/html/string-manipulation.html)

### Exit Codes

Exit codes are numerical values returned by a program or script upon completion. These codes signal whether the execution was successful or if any errors occurred. By convention, an exit code of 0 typically indicates success, while any non-zero value signifies a failure or specific error condition. These codes are crucial for scripting and automation, allowing scripts to make decisions based on the outcome of previous commands.

**Section resources:**
- [article] [Linux bash exit status and how to set exit status in bash](https://www.cyberciti.biz/faq/linux-bash-exit-status-set-exit-statusin-bash/)

#### String length

Determining the length of a string is a common task in scripting. It involves finding the number of characters present in a given string, which can be useful for validation, formatting, or other string processing operations. In shell scripting, there are several ways to achieve this, each with its own syntax and potential use cases.

- [article] [Bash String Manipulation Examples – Length, Substring, Find and Replace](https://www.thegeekstuff.com/2010/07/bash-string-manipulation/)
- [video] [Counting Characters in a Bash String - Quick Tip](https://www.youtube.com/watch?v=mK7hutk2yCE)

#### $?

Exit codes are numerical values returned by a program or script upon completion, signaling whether it executed successfully or encountered an error. The special variable `$?` in Bash stores the exit code of the most recently executed command. A value of 0 typically indicates success, while any non-zero value signifies failure, with different numbers often representing specific error types.

- [article] [$? - Linux Bash Shell Scripting Tutorial Wiki](https://bash.cyberciti.biz/guide/$%3F)

#### exit

Exit codes are numerical values returned by a program or script upon completion. These codes signal whether the execution was successful or if any errors occurred. By convention, an exit code of 0 typically indicates success, while any non-zero value signifies a failure or specific error condition. These codes are crucial for scripting and automation, allowing scripts to make decisions based on th…

_No linked resources in content file._

#### Substring extraction

Substring extraction involves selecting a portion of a string based on its position within the string. This is done by specifying the starting point and the length of the desired substring. It allows you to isolate and work with specific parts of a larger text string.

- [article] [Extracting a Substring in Bash](https://www.baeldung.com/linux/bash-substring)
- [article] [How to Extract Bash Substring](https://kodekloud.com/blog/bash-substring/)
- [video] [Creating substrings in Bash - Basic String Manipulation - You Suck at Programming #045](https://www.youtube.com/watch?v=KPVm06L55gc)

#### Success vs failure

Exit codes are numerical values returned by a program or script upon completion, signaling whether it executed successfully or encountered an error. A zero (0) exit code typically indicates success, while any non-zero value signifies failure, with different non-zero codes often representing specific types of errors. These codes are crucial for scripting and automation, allowing scripts to make dec…

_No linked resources in content file._

### File Permissions

File permissions in Unix-like operating systems, such as Linux and macOS, control who can access and modify files and directories. These permissions are typically represented by three categories: owner, group, and others. Each category can have read, write, and execute permissions, determining what actions users in that category can perform on the file or directory.

**Section resources:**
- [article] [File permissions](https://linuxcommand.org/lc3_lts0090.php)
- [video] [Linux File Permissions in 5 Minutes | MUST Know!](https://www.youtube.com/watch?v=LnKoncbQBsM)

#### Pattern replacement

Pattern replacement in shell scripting involves finding specific patterns within strings and substituting them with other strings. This is a fundamental text processing technique used to modify and transform data, allowing for tasks like cleaning up input, standardizing formats, or extracting relevant information. Shell tools like `sed`, parameter expansion, and `awk` are commonly used to achieve…

- [article] [Parameter Substitution](https://tldp.org/LDP/abs/html/parameter-substitution.html)
- [article] [How to Use Bash String Substitution Effectively](https://labex.io/tutorials/shell-how-to-use-bash-string-substitution-effectively-398333)
- [video] [sed: Easily replace strings across files | #7 Practical Bash](https://www.youtube.com/watch?v=91msRzo0VYw)

#### rwx

In Unix-like operating systems, file permissions control who can access and modify files and directories. The "rwx" notation represents the three fundamental permission types: "r" for read, allowing users to view the contents of a file or list the contents of a directory; "w" for write, allowing users to modify a file or create/delete files within a directory; and "x" for execute, allowing users t…

- [article] [Permissions](https://linuxcommand.org/lc3_lts0090.php)
- [video] [Linux Crash Course - Understanding File Permissions](https://www.youtube.com/watch?v=4N4Q576i3zA)

#### chmod

`chmod` is a command-line utility used to change the access permissions of files or directories. These permissions determine who can read, write, or execute a file. It allows you to control access to your files, ensuring security and proper functionality within a system.

- [article] [Permissions](https://linuxcommand.org/lc3_lts0090.php)
- [video] [Linux Crash Course - Understanding File Permissions](https://www.youtube.com/watch?v=4N4Q576i3zA)

#### Case conversion

Case conversion involves changing the case of characters within a string. This typically means converting lowercase letters to uppercase, uppercase letters to lowercase, or applying title case (where the first letter of each word is capitalized). It's a common operation for standardizing data, improving readability, or fulfilling specific formatting requirements.

- [article] [Bash Shell Convert Uppercase to Lowercase in Linux](https://www.cyberciti.biz/faq/linux-unix-shell-programming-converting-lowercase-uppercase/)
- [article] [How to Transform Text Case in Bash](https://labex.io/tutorials/shell-how-to-transform-text-case-in-bash-391560)
- [video] [Bash Shell Scripting For Beginners - Case Statement](https://www.youtube.com/watch?v=DA-Ilf15_r8)

#### chown

`chown` is a command-line utility used to change the ownership of files or directories. It allows you to modify the user and/or group associated with a file, effectively controlling who has access and what they can do with it. This is crucial for managing security and access control within a Linux or Unix-like operating system.

- [article] [Permissions](https://linuxcommand.org/lc3_lts0090.php)
- [video] [Linux Crash Course - Understanding File Permissions](https://www.youtube.com/watch?v=4N4Q576i3zA)

#### chgrp

`chgrp` is a command-line utility used to change the group ownership of a file or directory. It allows you to specify a new group that should be associated with the file, controlling which users have specific access rights based on group membership. This is a fundamental tool for managing file access and security in Unix-like operating systems.

- [article] [Permisions](https://linuxcommand.org/lc3_lts0090.php)
- [video] [Linux Crash Course - Understanding File Permissions](https://www.youtube.com/watch?v=4N4Q576i3zA)

#### for

A "for" loop is a control flow statement that allows you to repeatedly execute a block of code a specific number of times or for each item in a list. It's a fundamental programming construct used to automate repetitive tasks and iterate over collections of data. The loop continues until a specified condition is met, making it a powerful tool for processing data and performing actions multiple time…

- [article] [Bash Loops](https://www.w3schools.com/bash/bash_loops.php)
- [article] [Bash For Loop Examples](https://www.cyberciti.biz/faq/bash-for-loop/)

#### while

A `while` loop in shell scripting repeatedly executes a block of code as long as a specified condition remains true. It's a fundamental control flow statement that allows you to automate repetitive tasks based on a dynamic condition that can change during the loop's execution. The loop continues iterating until the condition becomes false.

- [article] [Bash While Loop Examples](https://www.cyberciti.biz/faq/bash-while-loop/)
- [article] [Bash Loops](https://www.w3schools.com/bash/bash_loops.php)
- [video] [How To Write Bash Scripts In Linux - Complete Guide (Part 7 - While Loops)](https://www.youtube.com/watch?v=R0tTsdQ_9Vw)

#### until

An `until` loop in shell scripting repeatedly executes a block of code as long as a specified condition is false. The loop continues to iterate until the condition becomes true, at which point the loop terminates. It's essentially the opposite of a `while` loop, providing a way to execute commands until a desired state is reached.

- [article] [Bash Until Loop](https://linuxize.com/post/bash-until-loop/)
- [video] [Bash until Loop](https://www.youtube.com/watch?v=8x2EfVSGwQc)

#### Function Scopes

Function scope determines the visibility and accessibility of variables within a function. In shell scripting, variables can have either global or local scope. Global variables are accessible from anywhere in the script, including within functions, while local variables are only accessible within the function where they are defined. Understanding scope is crucial for avoiding naming conflicts and…

- [article] [Bash Functions](https://linuxize.com/post/bash-functions/)
- [article] [Bash Functions – Declaration, Scope, Arguments, etc](https://www.webservertalk.com/bash-functions/)
- [video] [Crash-Course! Functions in Bash quickly explained and demystified!](https://www.youtube.com/watch?v=0tycTrpbWKs)

#### break, continue

`break` and `continue` are control flow statements used within loops to alter their execution. The `break` statement immediately terminates the loop, transferring control to the next statement after the loop. The `continue` statement skips the rest of the current iteration of the loop and proceeds to the next iteration.

- [article] [Bash Loops](https://www.w3schools.com/bash/bash_loops.php)
- [article] [Bash break and continue](https://linuxize.com/post/bash-break-continue/)
- [article] [Break and continue](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_05.html)
- [video] [Shell Scripting Tutorial - Break & Continue Statement](https://www.youtube.com/watch?v=3Dg6j_zSk_0)

#### Recursive Functions

Recursive functions are functions that call themselves within their own definition. This allows a function to repeat a process until a specific condition is met, breaking down a complex problem into smaller, self-similar subproblems. Each call adds a new layer to the execution stack, and it's crucial to have a base case to prevent infinite loops.

- [article] [Recursive function](https://bash.cyberciti.biz/guide/Recursive_function)
- [article] [How to implement a recursive function in a Bash script?](https://labex.io/questions/how-to-implement-a-recursive-function-in-a-bash-script-18293)
- [video] [What is Recursion in bash (Bash 23)](https://www.youtube.com/watch?v=K_BgGxtK2gE)

### Conditionals

Conditionals in shell scripting allow you to execute different blocks of code based on whether a certain condition is true or false. This enables your scripts to make decisions and respond dynamically to different situations, making them more versatile and powerful. Common conditional statements include `if`, `elif` (else if), and `else`, which are used to control the flow of execution based on the evaluation of expressions.

**Section resources:**
- [article] [Bash Conditional Expressions (Bash Reference Manual)](https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html)
- [article] [Bash If...Else](https://www.w3schools.com/bash/bash_conditions.php)
- [video] [How To Write Bash Scripts In Linux - Complete Guide (Part 5 - If Statements)](https://www.youtube.com/watch?v=YrE1Qg-Aw0Q)

### Loops

Loops are programming constructs that allow you to repeatedly execute a block of code. They automate repetitive tasks by iterating over a sequence of values or until a certain condition is met. This avoids writing the same code multiple times and makes scripts more efficient and easier to maintain.

**Section resources:**
- [article] [Bash Loops](https://www.w3schools.com/bash/bash_loops.php)

### Functions

Functions in shell scripting are reusable blocks of code that perform a specific task. They allow you to organize your scripts, avoid repetition, and make your code more readable and maintainable. You can define a function, give it a name, and then call it multiple times throughout your script, passing arguments if needed.

**Section resources:**
- [article] [Bash Functions](https://www.w3schools.com/bash/bash_functions.php)
- [video] [Crash-Course! Functions in Bash quickly explained and demystified!](https://www.youtube.com/watch?v=0tycTrpbWKs)

#### set -x

`set -x` is a debugging tool used in shell scripts to trace the execution of commands. When enabled, the shell will print each command to standard error (stderr) before it is executed, preceded by a `+` symbol. This allows you to see exactly what commands are being run and in what order, making it easier to identify errors or unexpected behavior in your scripts.

- [article] [Mastering Selective Debugging in Bash/Shell Scripts with set -x and set +x](https://medium.com/@maheshwar.ramkrushna/mastering-selective-debugging-in-bash-shell-scripts-with-set-x-and-set-x-ef6b7e83fb37)
- [article] [Difference between bash -x and set -x](https://how.dev/answers/bash--x-and-set--x)
- [article] [Using set -x and set -e in Shell Scripting: A Guide for Enhanced Debugging and Error Handling](https://www.hackerone.com/blog/using-set-x-and-set-e-shell-scripting-guide-enhanced-debugging-and-error-handling)
- [video] [How to Debug Bash - Using bash -x or set -x in bash - You Suck at Programming #044](https://www.youtube.com/watch?v=4TAx3Z9OgPs)

#### bash -n

The `bash -n` option is a debugging tool that allows you to perform a syntax check on your Bash script without actually executing it. This is useful for identifying errors like typos, missing keywords, or incorrect syntax before running the script and potentially causing unintended consequences. It essentially parses the script and reports any syntax errors it finds.

- [article] [Bash Script ‘-n’ Operator Explained: Evaluating Expressions](https://ioflood.com/blog/n-flag-in-bash/)

#### if

The `if` statement in shell scripting allows you to execute different blocks of code based on whether a certain condition is true or false. It's a fundamental control flow mechanism that enables scripts to make decisions and behave differently depending on the input or state of the system. The `if` statement evaluates an expression, and if the expression is true, a specific set of commands is exec…

- [article] [Bash If...Else](https://www.w3schools.com/bash/bash_conditions.php)
- [video] [How To Write Bash Scripts In Linux - Complete Guide (Part 5 - If Statements)](https://www.youtube.com/watch?v=YrE1Qg-Aw0Q)

#### case

Case statements provide a way to execute different blocks of code based on the value of a variable or expression. They offer a structured alternative to multiple `if-elif-else` statements, making code more readable and maintainable when dealing with several possible conditions. Each condition is associated with a specific pattern, and when the variable's value matches a pattern, the corresponding…

- [article] [Case statements](https://linuxize.com/post/bash-case-statement/)
- [article] [Using case statements](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_03.html)
- [video] [Bash Shell Scripting For Beginners - Case Statement](https://www.youtube.com/watch?v=DA-Ilf15_r8)

#### shellcheck

Shellcheck is a static analysis tool for shell scripts. It helps identify and fix common syntax errors, semantic issues, and stylistic problems in your Bash/Shell scripts before you even run them. By analyzing your code, shellcheck can suggest improvements and help prevent potential bugs, resulting in more robust and maintainable scripts.

- [official] [Shellcheck](https://www.shellcheck.net/)
- [opensource] [Shellcheck](https://github.com/koalaman/shellcheck)
- [article] [ShellCheck: Script Analysis Tool for Shell Scripts](https://trunk.io/linters/shell/shellcheck)
- [video] [Fix Your Shell Scripts With Shellcheck](https://www.youtube.com/watch?v=X3BIc9EHBuk)

#### Bash Debug

The Bash Debug extension for VS Code, powered by `bashdb`, allows you to debug Bash scripts directly within the VS Code editor. It provides features like breakpoints, stepping through code, inspecting variables, and evaluating expressions, making it easier to identify and fix errors in your Bash scripts. This helps streamline the debugging process, offering a more visual and interactive experience…

- [official] [vscode-bash-debug](https://github.com/rogalmic/vscode-bash-debug)
- [official] [Bash Debug](https://marketplace.visualstudio.com/items?itemName=rogalmic.bash-debug)

#### Basic regex syntax

Regular expressions (regex) are sequences of characters that define a search pattern. They are used to match, locate, and manipulate text based on patterns. Basic regex syntax involves using special characters and metacharacters to represent different types of patterns, such as specific characters, character classes, repetitions, and anchors within a string. These patterns are then used by tools l…

- [article] [Regular expressions](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_01.html)
- [article] [Regular expressions](https://computing.stat.berkeley.edu/tutorial-using-bash/regex.html)
- [article] [Bash Regex Tutorial for Beginners (regular expressions)](https://www.fullstackfoundations.com/blog/bash-regex)
- [video] [Regular Expressions for Beginners](https://www.youtube.com/watch?v=NhcaKdt3NdM)

### Debugging

Debugging is the process of identifying and removing errors or defects from software code. It involves systematically testing, analyzing, and correcting issues that cause a program to behave unexpectedly or produce incorrect results. Effective debugging relies on using tools and techniques to trace the flow of execution, inspect variable values, and pinpoint the source of the problem.

**Section resources:**
- [article] [Debugging Bash scripts](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_02_03.html)

### Error Handling

Error handling in shell scripting refers to the methods and techniques used to detect, manage, and respond to errors that occur during the execution of a script. It involves checking the exit status of commands, using conditional statements to handle different error scenarios, and implementing mechanisms to gracefully exit or recover from errors, ensuring the script's reliability and preventing unexpected behavior.

**Section resources:**
- [article] [Error handling in Bash scripts](https://www.redhat.com/en/blog/error-handling-bash-scripting)
- [article] [Writing Bash Scripts Like A Pro - Part 2 - Error Handling](https://dev.to/unfor19/writing-bash-scripts-like-a-pro-part-2-error-handling-46ff)
- [video] [Shell Script Error Handling: Master Bash Scripting for Robust Code](https://www.youtube.com/watch?v=uFJiDD1B5I4)

#### Extended regex

Extended regular expressions (EREs) are a more powerful and flexible version of basic regular expressions. They offer additional metacharacters and features that simplify pattern matching and make complex searches easier to express. EREs are commonly used with tools like `grep -E`, `awk`, and `sed -E` in shell scripting.

- [article] [Extended Regular Expressions](https://pressbooks.senecapolytechnic.ca/uli101/chapter/extended-regular-expressions/)

### Regular Expressions

Regular expressions (regex) are sequences of characters that define a search pattern. They are used to match, locate, and manipulate text based on specific patterns. Regex provides a powerful way to search for strings that match a certain format, such as email addresses, phone numbers, or specific keywords within a larger body of text.

**Section resources:**
- [article] [Regular expressions](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_01.html)
- [article] [Bash Regex: How to Use Regex in a Shell Script](https://kodekloud.com/blog/regex-shell-script/)
- [article] [Beginners Guide to Bash Regex (With Code Examples)](https://zerotomastery.io/blog/bash-regex/)

#### set -e

`set -e` is a shell command that instructs the shell to exit immediately if a command exits with a non-zero status. This is a way to ensure that your script stops executing as soon as an error occurs, preventing subsequent commands from running based on potentially incorrect or incomplete results. It's a common practice to include `set -e` at the beginning of a script to enforce stricter error che…

- [article] [Executing Code after an Error Occurs with Bash When Using set e](https://nickjanetakis.com/blog/executing-code-after-an-error-occurs-with-bash-when-using-set-e)
- [article] [Allowing for Errors in Bash When You Have set -e Defined](https://nickjanetakis.com/blog/allowing-for-errors-in-bash-when-you-have-set-e-defined)
- [video] [Shell Script Error Handling: Master Bash Scripting for Robust Code](https://www.youtube.com/watch?v=uFJiDD1B5I4)

#### set -o

The `set -o` command in shell scripting is used to modify shell options, which control the behavior of the shell. These options can affect how the shell interprets commands, handles errors, and performs other tasks. By using `set -o` with specific option names, you can customize the shell's environment to suit your needs, enabling features like error handling, debugging, and more strict command ex…

- [article] [Prevent Unset Variables in Your Shell / Bash Scripts with set nounset](https://nickjanetakis.com/blog/prevent-unset-variables-in-your-shell-bash-scripts-with-set-nounset)
- [article] [set -e, -u, -o, -x pipefail explanation](https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425)
- [video] [Prevent Unset Variables in Your Shell / Bash Scripts with set -o nounset](https://www.youtube.com/watch?v=Kly_6DhfHwE)

#### set -u

The `set -u` command in shell scripting treats unset variables as an error. When this option is enabled, the script will exit immediately if it tries to use a variable that has not been assigned a value. This helps to catch potential bugs caused by typos or missing variable assignments, making scripts more robust.

- [article] [set -e, -u, -o, -x pipefail explanation](https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425)

#### trap

`trap` is a shell command used to specify actions to be taken upon receiving signals. Signals are notifications sent to a process to indicate an event, such as termination, interruption, or an error. The `trap` command allows you to define custom handlers that execute when a specific signal is received, enabling you to gracefully handle errors, clean up resources, or perform other necessary action…

- [article] [Bash trap Command Explained](https://phoenixnap.com/kb/bash-trap-command)
- [article] [The Bash Trap Command](https://www.linuxjournal.com/content/bash-trap-command)
- [video] [Trapping signals with trap in Bash! Responding to Unix signals. You Suck at Programming #064](https://www.youtube.com/watch?v=aXovP1sUtoE)

### Process Management

Process management involves controlling and monitoring the execution of programs within an operating system. It includes tasks such as creating new processes, scheduling their execution, allocating resources, and handling inter-process communication. Effective process management ensures efficient utilization of system resources and prevents conflicts between running programs.

**Section resources:**
- [article] [Managing processes](https://computing.stat.berkeley.edu/tutorial-using-bash/managing-processes.html)
- [article] [ProcessManagement - Greg's Wiki  Greg's](https://mywiki.wooledge.org/ProcessManagement)
- [article] [Bash Process Management: How to Tame Your Shell Like a Pro](https://itldc.com/en/blog/bash-process-management-how-to-tame-your-shell-like-a-pro/)
- [video] [#4 - Bash command for Process Management](https://www.youtube.com/watch?v=O4C6_TJ-iws)

#### Error logging

Error logging is the process of recording errors that occur during the execution of a script or program. This involves capturing information about the error, such as the type of error, the time it occurred, and the location in the code where it happened. Effective error logging facilitates debugging, troubleshooting, and monitoring application health by providing a historical record of issues.

- [article] [Bash Logging and Error Reporting Exercises, Solutions & Explanation](https://www.w3resource.com/bash-script-exercises/logging-and-error-reporting.php)
- [article] [Standard Error and Logging in Shell Scripts](https://codesignal.com/learn/courses/bash-script-error-handling/lessons/standard-error-and-logging-in-shell-scripts)

#### jobs

In a shell environment, a job represents a process or a group of processes that are running in the background or foreground. The `jobs` command provides a way to list the currently active jobs, check their status (running, stopped, terminated), and manage them, such as bringing them to the foreground or terminating them. It's a crucial tool for controlling and monitoring processes initiated from t…

- [article] [Job Control Basics](https://www.gnu.org/software/bash/manual/html_node/Job-Control-Basics.html)
- [article] [Jobs and Job Control in Bash Shell](https://www.baeldung.com/linux/jobs-job-control-bash)
- [video] [099 Bash Jobs & Signals - Bringing Jobs Back To The Command Line](https://www.youtube.com/watch?v=xu2lGV-kISI)

#### nohup

`nohup` is a command-line utility used to run a command immune to hangups, with output redirected to a file. This allows a process to continue running in the background even after the user who started the process logs out or closes the terminal. It's particularly useful for long-running tasks that shouldn't be interrupted by a terminal disconnection.

- [article] [How to use the nohup command in Linux](https://www.hostinger.com/tutorials/nohup-command-in-linux)
- [article] [How to Use the nohup Command in Linux](https://www.digitalocean.com/community/tutorials/nohup-command-in-linux)
- [video] [Nohup - Hangup Immune Commands - Commands for Linux](https://www.youtube.com/watch?v=rTB-HuuszLs)
- [video] [How to use the nohup command](https://www.youtube.com/watch?v=E96yxNUS84c)

#### ping

Ping is a command-line utility used to test the reachability of a host on an Internet Protocol (IP) network. It works by sending Internet Control Message Protocol (ICMP) "echo request" packets to the target host and waiting for ICMP "echo reply" packets. The ping command measures the round-trip time (RTT) for these packets, indicating the latency of the connection, and also reports any packet loss…

- [article] [Bash ping Command - Send Request to Network Hosts](https://www.w3schools.com/bash/bash_ping.php)
- [article] [Ping Command in Linux](https://linuxize.com/post/linux-ping-command/)
- [video] [Simple PING commands](https://www.youtube.com/watch?v=KYmtMBsuA50)
- [video] [Ping Command Explained | Real World Example](https://www.youtube.com/watch?v=7sv5pL-XgSg)

#### curl

curl is a command-line tool used to transfer data with URLs. It supports various protocols like HTTP, HTTPS, FTP, and more, allowing you to download files, send data to servers, and interact with APIs directly from the command line. It's a versatile tool for automating tasks involving network communication.

- [official] [The Art Of Scripting HTTP Requests Using curl](https://curl.se/docs/httpscripting.html)
- [opensource] [curl](https://github.com/curl/curl)
- [video] [Supercharge Your Workflow with cURL | Understanding The cURL Command-Line Tool](https://www.youtube.com/watch?v=-nnJ82uc2ic)
- [video] [You NEED to know how to use CURL!](https://www.youtube.com/watch?v=q2sqkvXzsw8)

#### fg, bg

`fg` and `bg` are shell commands used to manage processes. `bg` moves a process to the background, allowing you to continue using the terminal while the process runs. `fg` brings a background process to the foreground, giving it control of the terminal. This is useful for managing long-running tasks or temporarily pausing a process.

- [article] [Linux Commands: jobs, bg, and fg](https://www.redhat.com/en/blog/jobs-bg-fg)
- [article] [Job Control Commands](https://tldp.org/LDP/abs/html/x9644.html)
- [article] [How To Use Bash's Job Control to Manage Foreground and Background Processes](https://www.digitalocean.com/community/tutorials/how-to-use-bash-s-job-control-to-manage-foreground-and-background-processes)
- [video] [Master the Linux Command Line: Background & Foreground Jobs to Swap Tasks with the fg and bg Command](https://www.youtube.com/watch?v=Ak7cFJ1-Ewo)

#### disown

`disown` is a shell built-in command used to remove jobs from the shell's job control. When you start a process in the background (using `&`), the shell keeps track of it. If you close the terminal, the shell usually sends a SIGHUP signal to these background processes, which often causes them to terminate. `disown` removes a process from this job control, preventing the shell from sending that sig…

- [article] [Linux / Unix: disown Command Examples](https://www.cyberciti.biz/faq/unix-linux-disown-command-examples-usage-syntax/)
- [article] [How to Use Disown Command in Linux](https://phoenixnap.com/kb/disown-command-linux)
- [video] [Linux | Background Process Basics and Signals | & , disown, nohup](https://www.youtube.com/watch?v=OQpnQgvmbhY)
- [video] [How to use the disown command: 2-Minute Linux Tipsv](https://www.youtube.com/watch?v=B66HKmP03Xo)

#### wget

`wget` is a command-line utility used to retrieve files from the internet. It supports downloading files using HTTP, HTTPS, and FTP protocols. `wget` is non-interactive, meaning it can work in the background without user intervention, making it suitable for scripting and automation.

- [article] [GNU Wget](https://www.gnu.org/software/wget/)
- [article] [What is the wget command and how to use it (12 examples included)](https://www.hostinger.com/tutorials/wget-command-examples)
- [video] [The wget Command | How to Download Files From a Server](https://www.youtube.com/watch?v=zszbBJ81_YU)

#### ssh

SSH (Secure Shell) is a cryptographic network protocol that enables secure communication between two computers over an insecure network. It's commonly used for remote command-line access, remote execution of commands, and secure file transfer. SSH encrypts the data transmitted between the client and the server, protecting it from eavesdropping and tampering.

- [article] [SSH Essentials: Working with SSH Servers, Clients, and Keys](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
- [article] [A beginner’s guide to SSH for remote connection on Linux](https://opensource.com/article/20/9/ssh)
- [video] [SSH for Beginners: The Ultimate Getting Started Guide](https://www.youtube.com/watch?v=YS5Zh7KExvE)
- [video] [Learn SSH In 6 Minutes - Beginners Guide to SSH Tutorial](https://www.youtube.com/watch?v=v45p_kJV9i4)

#### ps

`ps` is a command-line utility that displays information about active processes running on a Linux or Unix-like operating system. It provides a snapshot of the current processes, including their process IDs (PIDs), resource usage, and other relevant details. This allows users and administrators to monitor system activity and identify processes that may be consuming excessive resources or causing i…

- [article] [Bash ps Command - Snapshot of Current Processes](https://www.w3schools.com/bash/bash_ps.php)
- [article] [List Processes Linux: ps command for beginners](https://www.fullstackfoundations.com/blog/list-processes-linux)
- [video] [Linux Crash Course - The ps Command](https://www.youtube.com/watch?v=wYwGNgsfN3I)
- [video] [Process and System Management on Linux and Mac (Bash)](https://www.youtube.com/watch?v=lfN2RE8720E)

#### top, htop

`top` and `htop` are command-line utilities used for real-time system monitoring. They display a dynamic, ordered list of processes running on a system, along with information about CPU usage, memory consumption, and other system resources. `htop` is an enhanced, interactive version of `top`, offering features like color-coding, improved process management, and horizontal scrolling.

- [article] [Bash top Command - Display Linux Tasks](https://www.w3schools.com/bash/bash_top.php)
- [article] [How to use top and htop Linux command for Process Management](https://www.layerstack.com/resources/tutorials/How-to-use-top-and-htop-Linux-command-for-Process-Management)
- [video] [Understanding Linux System Performance | The Top Command](https://www.youtube.com/watch?v=3r_PBLaZoFQ)
- [video] [The htop Command | Linux Essentials Tutorial](https://www.youtube.com/watch?v=bKWZJ3_5ODc)

#### Process substitution

Process substitution allows you to treat the output of a process as if it were a file. It achieves this by creating a temporary file (or using a pipe in some systems) and connecting the standard output of a command to it. This temporary file's name is then substituted into the command line, allowing commands that expect file arguments to read the output of another command. This is particularly use…

- [article] [Process Substitution](https://tldp.org/LDP/abs/html/process-sub.html)
- [article] [Handy Bash feature: Process Substitution](https://medium.com/@joewalnes/handy-bash-feature-process-substitution-8eb6dce68133)
- [video] [Command vs. Process substitution in Bash - explaining the difference. You Suck at Programming #073](https://www.youtube.com/watch?v=f3eIK5xk4vg)

#### scp

`scp`, short for secure copy, is a command-line utility that allows you to securely transfer files between a local host and a remote host or between two remote hosts. It uses the SSH protocol for data transfer, ensuring that the data is encrypted during transmission, thus protecting it from eavesdropping. `scp` is commonly used for tasks like uploading website files to a server, backing up data to…

- [article] [How to Use SCP Command to Securely Transfer Files](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)
- [article] [How to use SCP command to copy and transfer files in Linux](https://www.hostinger.com/tutorials/linux-scp-command)
- [video] [Transferring files with the scp Command (Linux Crash Course Series)](https://www.youtube.com/watch?v=Aa7tKMmeFZI)

#### rsync

rsync is a command-line utility for efficiently transferring and synchronizing files between a computer and an external hard drive or across networked computers. It minimizes data transfer by only copying the differences between the source and destination, making it faster than simple copy commands, especially for large files or directories. rsync is commonly used for backups, mirroring data, and…

- [article] [Rsync Command in Linux with Examples](https://linuxize.com/post/how-to-use-rsync-for-local-and-remote-data-transfer-and-synchronization/)
- [article] [How To Use Rsync to Sync Local and Remote Directories](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories)
- [article] [Bash rsync Command - Remote (and local) File-copying](https://www.w3schools.com/bash/bash_rsync.php)
- [video] [Linux File Transfers Made Easy with rsync](https://www.youtube.com/watch?v=KG78O53u8rY)

#### free

`free` is a command-line utility used to display the amount of free and used physical and swap memory in a system. It provides a snapshot of the memory usage at a given point in time, showing total memory, used memory, free memory, shared memory, buffer/cache memory, and available memory. This information is crucial for understanding how efficiently a system is utilizing its memory resources and i…

- [article] [Bash free Command - Display Free and Used Memory](https://www.w3schools.com/bash/bash_free.php)
- [article] [Free Command in Linux](https://linuxize.com/post/free-command-in-linux/)
- [article] [Using the Linux Free Command With Examples](https://www.turing.com/kb/how-to-use-the-linux-free-command)

#### df, du

`df` (disk free) and `du` (disk usage) are command-line utilities used to monitor disk space on Unix-like operating systems. `df` provides a summary of available and used disk space on mounted file systems, while `du` estimates the file space usage of files and directories. Together, they help system administrators understand how storage is being utilized and identify potential space issues.

- [article] [Bash df Command - File System Disk Space Usage](https://www.w3schools.com/bash/bash_df.php)
- [article] [Bash du Command - File Space Usage](https://www.w3schools.com/bash/bash_du.php)
- [video] [Linux Crash Course - The df and du Commands](https://www.youtube.com/watch?v=ZRs5zVv_1UU)

#### netstat, ss

`netstat` and `ss` are command-line tools used to display network connections, routing tables, interface statistics, masquerade connections, and multicast memberships. They provide insights into the network activity of a system, allowing users to diagnose network issues, monitor connections, and understand network traffic patterns. While `netstat` has been a long-standing tool, `ss` (socket statis…

- [article] [How To Use Linux SS Command](https://phoenixnap.com/kb/ss-command)
- [article] [Netstat Command in Linux - 25 Commands with Examples](https://phoenixnap.com/kb/netstat-command)
- [video] [How to Use the ss Command (Linux Crash Course Series)](https://www.youtube.com/watch?v=phY8Q7Woxsw)
- [video] [Netstat Commands - Network Administration Tutorial](https://www.youtube.com/watch?v=bxFwpm4IobU)

#### ifconfig, ip

`ifconfig` and `ip` are command-line utilities used to configure and manage network interfaces on Unix-like operating systems. They allow you to view, configure, and control network interfaces, including assigning IP addresses, setting network masks, and enabling or disabling interfaces. While `ifconfig` is an older tool, `ip` is the modern replacement offering more features and flexibility.

- [article] [Linux ifconfig Command With Examples](https://phoenixnap.com/kb/linux-ifconfig)
- [article] [Linux ip Command with Examples](https://phoenixnap.com/kb/linux-ip-command-examples)
- [video] [How to Use the ip Command in Linux: A Beginner’s Guide](https://www.youtube.com/watch?v=wHfIFZlDxtU)
- [video] [Using IPCONFIG for Network Troubleshooting](https://www.youtube.com/watch?v=k1qgpqQ0Mo4)

#### uptime

Uptime is a command-line utility that displays how long the system has been running. It provides a concise summary of the current time, how long the system has been up, the number of users currently logged in, and the system's load average over the past 1, 5, and 15 minutes. This information is useful for quickly assessing the system's stability and resource utilization.

- [article] [Bash uptime Command - System Runtime](https://www.w3schools.com/bash/bash_uptime.php)
- [article] [Uptime Command in Linux](https://linuxize.com/post/linux-uptime-command/)
- [video] [Uptime command in Linux with Examples - How to Check Uptime in Linux Command Line](https://www.youtube.com/watch?v=slf7GAuzIQ4)

#### iostat, vmstat

`iostat` and `vmstat` are command-line utilities used for system monitoring. `iostat` reports CPU utilization and disk I/O statistics, providing insights into storage device performance. `vmstat` reports virtual memory statistics, including information about processes, memory, paging, block I/O, traps, and CPU activity, helping to identify performance bottlenecks related to memory and CPU usage.

- [article] [Linux Performance Monitoring with Vmstat and Iostat Commands](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/)
- [article] [Linux Performance Monitoring: Using Tools Like top, vmstat, and iostat](https://www.linuxjournal.com/content/linux-performance-monitoring-using-tools-top-vmstat-and-iostat)
- [article] [Linux Performance Monitoring with Vmstat and Iostat Commands](https://www.tutorialspoint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands)
- [video] [037 Performance Monitoring with Vmstat and lostat](https://www.youtube.com/watch?v=c_My7gRuDb8)

#### apt

`apt` (Advanced Package Tool) is a command-line package management system used primarily on Debian-based Linux distributions like Ubuntu. It simplifies the process of installing, updating, removing, and managing software packages by retrieving them from configured repositories and handling dependencies automatically. `apt` provides a user-friendly interface for interacting with the underlying Debi…

- [article] [apt Command in Linux](https://linuxize.com/post/how-to-use-apt-command/)
- [article] [apt Linux Command with Examples](https://phoenixnap.com/kb/apt-linux)
- [video] [Linux Crash Course - The apt Command](https://www.youtube.com/watch?v=1kicKTbK768)

#### brew

Homebrew is a package manager for macOS (and Linux). It simplifies the installation of software on these operating systems by automating the process of downloading, compiling, and installing software packages from the command line. It's often used to install tools and utilities that aren't included by default in the operating system.

- [official] [brew](https://brew.sh/)
- [article] [How To Install and Use Homebrew on Linux](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-homebrew-on-linux)
- [video] [Homebrew Tutorial: Simplify Software Installation on Mac Using This Package Manager](https://www.youtube.com/watch?v=SELYgZvAZbU)

#### yum

yum (Yellowdog Updater, Modified) is a command-line package management tool for systems using the RPM Package Manager. It automates the process of installing, updating, removing, and searching for software packages and their dependencies from configured repositories. yum simplifies software management by resolving dependencies automatically, ensuring that all required components are installed for…

- [article] [How to install Yum on Linux](https://linuxconfig.org/how-to-install-yum-on-linux)
- [article] [Linux package management with YUM and RPM](https://www.redhat.com/en/blog/how-manage-packages)

#### dnf

dnf is a package manager for RPM-based Linux distributions, serving as the successor to YUM (Yellowdog Updater, Modified). It is used to install, update, and remove software packages, as well as manage dependencies. dnf aims to improve upon YUM by offering better performance, more features, and a more modern architecture.

- [article] [Using the DNF software package manager](https://docs.fedoraproject.org/en-US/quick-docs/dnf/)
- [video] [Linux Crash Course - The dnf Command](https://www.youtube.com/watch?v=mL1hMBYP1bQ&t=1529s)

#### tar

`tar` (Tape Archive) is a command-line utility in Unix-like operating systems used for archiving and extracting files. It combines multiple files into a single archive file, often referred to as a "tarball." While `tar` itself doesn't compress the archive, it's commonly used in conjunction with compression tools like gzip or bzip2 to create compressed archives (e.g., `.tar.gz` or `.tar.bz2` files)…

- [article] [Bash tar Command - An archiving utility](https://www.w3schools.com/bash/bash_tar.php)
- [article] [How to use the tar command in Linux](https://www.hostinger.com/tutorials/linux-tar-command-with-examples)
- [article] [Linux tar Command with Practical Examples](https://labex.io/es/tutorials/linux-linux-tar-command-with-practical-examples-422951)
- [video] [How to Archive Folders in Linux (tar and gzip tutorial) - Linux Crash Course Series](https://www.youtube.com/watch?v=2iwumBcfd58)

#### zip, unzip

`zip` and `unzip` are command-line utilities used for compressing and decompressing files and directories. `zip` packages files into a single archive, reducing their size and making them easier to share or store. `unzip` extracts the contents of a zip archive, restoring the original files and directories.

- [article] [Bash zip Command - Package and compress (archive) files](https://www.w3schools.com/bash/bash_zip.php)
- [article] [Bash unzip Command - Extract from ZIP archive](https://www.w3schools.com/bash/bash_unzip.php)
- [video] [How to Unzip and Zip Files on Linux (Desktop and Command Line)](https://www.youtube.com/watch?v=xqcHiuQK9lY)

#### cron, crontab

cron is a time-based job scheduler in Unix-like operating systems. It allows users to schedule tasks (commands or scripts) to run automatically at specific times, dates, or intervals. The crontab (cron table) is a file that contains the schedule of cron jobs for a user. Each user has their own crontab file, and the system also has a system-wide crontab for administrative tasks.

- [article] [Bash crontab Command - Schedule Tasks](https://www.w3schools.com/bash/bash_cron.php)
- [article] [What is a cron job: understanding cron syntax and how to configure cron jobs](https://www.hostinger.com/tutorials/cron-job)
- [video] [Linux Crash Course - Scheduling Tasks with Cron](https://www.youtube.com/watch?v=7cbP7fzn0D8)

#### at

The `at` command in Unix-like operating systems is used to schedule commands to be executed at a specific time. It allows you to specify a time and date, and then provide a command that will be run automatically at that designated time. This is useful for automating tasks that need to be performed at a later time without requiring manual intervention.

- [article] [At Command in Linux](https://linuxize.com/post/at-command-in-linux/)
- [article] [How to Use the Linux at Command](https://phoenixnap.com/kb/linux-at-command)
- [video] [How to Use The "at" Command On Linux](https://www.youtube.com/watch?v=0Lvvw4yA6Ag)

#### gzip, gunzip

`gzip` is a command-line utility used to compress files, reducing their size and making them easier to store or transmit. The compressed files typically have a `.gz` extension. `gunzip` is the corresponding command used to decompress files that have been compressed with `gzip`, restoring them to their original state.

- [article] [Using gzip and gunzip in Linux](https://www.baeldung.com/linux/gzip-and-gunzip)
- [article] [Linux gzip and gunzip: How to work with compressed files](https://alvinalexander.com/blog/post/linux-unix/how-work-compressed-files-gzip-zgrep-zcat/)
- [video] [How to Archive Folders in Linux (tar and gzip tutorial) - Linux Crash Course Series](https://www.youtube.com/watch?v=2iwumBcfd58&t)

#### bzip2, xz

`bzip2` and `xz` are command-line tools used for file compression in Unix-like operating systems. They reduce the size of files, making them easier to store and transfer. `bzip2` generally offers higher compression than `gzip` but is slower, while `xz` provides even better compression ratios and is often used for distributing software packages, though it can be slower than both `gzip` and `bzip2`.

- [article] [Guide to the Linux bzip2 Command With Examples](https://www.baeldung.com/linux/bzip2-guide)
- [article] [Learn XZ (Lossless Data Compression Tool) in Linux with Examples](https://www.tecmint.com/xz-command-examples-in-linux/)
- [video] [Learn About These Tools!! Compressing and Archiving Files in the Linux Console (tar, xz, bzip2, zip)](https://www.youtube.com/watch?v=d4PAEbHcLVg)

#### systemd timers

Systemd timers are a systemd feature that allows you to schedule tasks to run at specific times or intervals, similar to cron. They provide a more flexible and powerful alternative to cron, offering features like dependency management, event-based activation, and integration with systemd's logging and service management capabilities. Systemd timers are defined using unit files, just like systemd s…

- [article] [Working with systemd timers](https://yieldcode.blog/post/working-with-systemd-timers/)
- [article] [Systemd timers — The alternative to cron jobs](https://medium.com/@tolulinux/systemd-timers-the-alternative-to-cron-jobs-be479172ae12)
- [video] [Automate Your Tasks with systemd Timers: A Step-by-Step Guide](https://www.youtube.com/watch?v=n6BuUgkZ5T0)

### Package Management

Package management is the process of installing, updating, configuring, and removing software packages on a computer system. It provides a standardized way to handle software dependencies, ensuring that all necessary components are present and compatible. Package managers also simplify the process of keeping software up-to-date and removing unwanted applications cleanly.

## All unique resource URLs

- [article] [ksh](http://www.kornshell.com/) — _ksh_
- [article] [Bash Positional Parameters](https://adminschoice.com/bash-positional-parameters/) — _Positional Parameters_
- [article] [Linux gzip and gunzip: How to work with compressed files](https://alvinalexander.com/blog/post/linux-unix/how-work-compressed-files-gzip-zgrep-zcat/) — _gzip and gunzip_
- [article] [Unix Tutorial #4: Shells and Path Variables — Andy's Brain Book 1.0 documentation](https://andysbrainbook.readthedocs.io/en/latest/unix/Unix_04_ShellsVariables.html) — _Variables in Shell Scripting_
- [article] [What is a CLI (Command Line Interface)?](https://aws.amazon.com/what-is/cli/) — _CLI vs GUI_
- [article] [$? - Linux Bash Shell Scripting Tutorial Wiki](https://bash.cyberciti.biz/guide/$%3F) — _Exit Codes and $?_
- [article] [Recursive function](https://bash.cyberciti.biz/guide/Recursive_function) — _Recursive Functions_
- [article] [Standard Error and Logging in Shell Scripts](https://codesignal.com/learn/courses/bash-script-error-handling/lessons/standard-error-and-logging-in-shell-scripts) — _Error Logging_
- [article] [Managing processes](https://computing.stat.berkeley.edu/tutorial-using-bash/managing-processes.html) — _Process Management_
- [article] [Regular expressions](https://computing.stat.berkeley.edu/tutorial-using-bash/regex.html) — _Basic Regex Syntax_
- [article] [What is scripting?](https://coralogix.com/blog/what-is-scripting/) — _What is Scripting?_
- [article] [Writing Bash Scripts Like A Pro - Part 2 - Error Handling](https://dev.to/unfor19/writing-bash-scripts-like-a-pro-part-2-error-handling-46ff) — _Error Handling_
- [article] [https://dillionmegida.com/p/sourcing-vs-executing-script-directly/](https://dillionmegida.com/p/sourcing-vs-executing-script-directly/) — _Running Shell Scripts with Source_
- [article] [Using the DNF software package manager](https://docs.fedoraproject.org/en-US/quick-docs/dnf/) — _dnf_
- [article] [Bash Tests](https://docs.rockylinux.org/10/books/learning_bash/05-tests/) — _File Test Operators_
- [article] [Dash - Wikipedia](https://en.wikipedia.org/wiki/Almquist_shell#dash) — _dash_
- [article] [https://en.wikipedia.org/wiki/Bash_(Unix_shell)#:~:text=Bash (short for "Bourne Again,Chet Ramey)](https://en.wikipedia.org/wiki/Bash_(Unix_shell) — _Bash_
- [article] [Command substitution - Wikipedia](https://en.wikipedia.org/wiki/Command_substitution) — _Command Substitution_
- [article] [ksh - Wikipedia](https://en.wikipedia.org/wiki/KornShell) — _ksh_
- [article] [Shell - Wikipedia](https://en.wikipedia.org/wiki/Shell_(computing) — _Introduction_
- [article] [Standard Streams - Wikipedia](https://en.wikipedia.org/wiki/Standard_streams) — _stdin, stdout, and stderr_
- [article] [tcsh - Wikipedia](https://en.wikipedia.org/wiki/Tcsh) — _tcsh_
- [article] [Z Shell - Wikipedia](https://en.wikipedia.org/wiki/Z_shell) — _zsh_
- [article] [Finally, a command line shell for the 90s](https://fishshell.com/) — _fish_
- [article] [set -e, -u, -o, -x pipefail explanation](https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425) — _set -u_
- [article] [Navigating the file system with Terminal](https://gomakethings.com/navigating-the-file-system-with-terminal/) — _Navigate Between Directories_
- [article] [Linux Question: What is /dev/null 2\>&1 ?](https://hemantjain.medium.com/linux-question-what-is-dev-null-2-1-82d75a156b5c) — _Output Redirection_
- [article] [Difference between bash -x and set -x](https://how.dev/answers/bash--x-and-set--x) — _set -x_
- [article] [Bash Script ‘-n’ Operator Explained: Evaluating Expressions](https://ioflood.com/blog/n-flag-in-bash/) — _Bash -n_
- [article] [Bash Process Management: How to Tame Your Shell Like a Pro](https://itldc.com/en/blog/bash-process-management-how-to-tame-your-shell-like-a-pro/) — _Process Management_
- [article] [Beginner's Guide to Nano Text Editor](https://itsfoss.com/nano-editor-guide/) — _Basic Editor Operations_
- [article] [How to Extract Bash Substring](https://kodekloud.com/blog/bash-substring/) — _Substring Extraction_
- [article] [Bash Regex: How to Use Regex in a Shell Script](https://kodekloud.com/blog/regex-shell-script/) — _Regular Expressions_
- [article] [Linux tar Command with Practical Examples](https://labex.io/es/tutorials/linux-linux-tar-command-with-practical-examples-422951) — _tar_
- [article] [How to Work with Shell Variables and Functions](https://labex.io/fr/tutorials/shell-how-to-work-with-shell-variables-and-functions-392774) — _Variable Scopes_
- [article] [How to implement a recursive function in a Bash script?](https://labex.io/questions/how-to-implement-a-recursive-function-in-a-bash-script-18293) — _Recursive Functions_
- [article] [How to Transform Text Case in Bash](https://labex.io/tutorials/shell-how-to-transform-text-case-in-bash-391560) — _Case Conversion_
- [article] [How to Use Bash String Substitution Effectively](https://labex.io/tutorials/shell-how-to-use-bash-string-substitution-effectively-398333) — _Pattern Replacement_
- [article] [cmd](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd) — _cmd_
- [article] [Setting up the Bash Environment](https://letsdefend.io/blog/how-to-install-bash-on-windows) — _Setting Up Bash_
- [article] [Permissions](https://linuxcommand.org/lc3_lts0090.php) — _rwx File Permissions_
- [article] [How to exit from Bash script](https://linuxconfig.org/how-to-exit-from-bash-script) — _Stop Execution_
- [article] [How to install Yum on Linux](https://linuxconfig.org/how-to-install-yum-on-linux) — _yum_
- [article] [Use Join Command in Linux: A Detailed Guide](https://linuxconfig.org/join) — _Join and Split_
- [article] [Use nl Command in Linux - Step-by-Step Guide](https://linuxconfig.org/nl) — _nl_
- [article] [Linux Handbook | bc command in Linux](https://linuxhandbook.com/bc-command/) — _bc_
- [article] [What is Dash Shell in Linux?](https://linuxhandbook.com/dash-shell/) — _dash_
- [article] [At Command in Linux](https://linuxize.com/post/at-command-in-linux/) — _at_
- [article] [Bash break and continue](https://linuxize.com/post/bash-break-continue/) — _Break and Continue in Loops_
- [article] [Case statements](https://linuxize.com/post/bash-case-statement/) — _Case Statements_
- [article] [Writing Comments in Bash Scripts](https://linuxize.com/post/bash-comments/) — _Comments_
- [article] [Bash Functions](https://linuxize.com/post/bash-functions/) — _Function Scopes_
- [article] [Bash printf Command](https://linuxize.com/post/bash-printf-command/) — _printf Formatting_
- [article] [Bash Until Loop](https://linuxize.com/post/bash-until-loop/) — _Until Loops_
- [article] [Free Command in Linux](https://linuxize.com/post/free-command-in-linux/) — _Free_
- [article] [apt Command in Linux](https://linuxize.com/post/how-to-use-apt-command/) — _apt_
- [article] [How to Use Nano, the Linux Command Line Text Editor](https://linuxize.com/post/how-to-use-nano-text-editor/) — _Nano_
- [article] [Rsync Command in Linux with Examples](https://linuxize.com/post/how-to-use-rsync-for-local-and-remote-data-transfer-and-synchronization/) — _rsync_
- [article] [How to Use SCP Command to Securely Transfer Files](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/) — _scp_
- [article] [Less Command in Linux](https://linuxize.com/post/less-command-in-linux/) — _less and more_
- [article] [Cut Command in Linux | Linuxize](https://linuxize.com/post/linux-cut-command/) — _cut and paste_
- [article] [Ping Command in Linux](https://linuxize.com/post/linux-ping-command/) — _Ping_
- [article] [Uptime Command in Linux](https://linuxize.com/post/linux-uptime-command/) — _Uptime_
- [article] [Paste Command in Linux (Merge Lines) | Linuxize](https://linuxize.com/post/paste-command-in-linux/) — _cut and paste_
- [article] [Why I use Fish Shell](https://medium.com/@desjoerdhaan/why-i-use-fish-shell-e5272e0770bf) — _fish_
- [article] [Handy Bash feature: Process Substitution](https://medium.com/@joewalnes/handy-bash-feature-process-substitution-8eb6dce68133) — _Process Substitution_
- [article] [Shell Scripting: Comparison Operators and If Statements](https://medium.com/@kadimasam/shell-scripting-comparison-operators-and-if-statements-9e0277fd60b8) — _Comparison Operators in Bash_
- [article] [Creating And Using An Associative Array In A Bash Script | by Linux Root Room](https://medium.com/@linuxrootroom/create-and-use-associative-array-in-bash-script-5f4e32a00577) — _Associative Arrays_
- [article] [Mastering Selective Debugging in Bash/Shell Scripts with set -x and set +x](https://medium.com/@maheshwar.ramkrushna/mastering-selective-debugging-in-bash-shell-scripts-with-set-x-and-set-x-ef6b7e83fb37) — _set -x_
- [article] [Heredoc: A Deep Dive](https://medium.com/@oduwoledare/heredoc-a-deep-dive-23c82992e522) — _Here Documents_
- [article] [Systemd timers — The alternative to cron jobs](https://medium.com/@tolulinux/systemd-timers-the-alternative-to-cron-jobs-be479172ae12) — _Systemd Timers_
- [article] [Understanding Special Parameters in Linux Shell Scripting](https://medium.com/@tradingcontentdrive/understanding-special-parameters-in-linux-shell-scripting-0-62768f49fb34) — _Number of Script Arguments ($#)_
- [article] [ProcessManagement - Greg's Wiki  Greg's](https://mywiki.wooledge.org/ProcessManagement) — _Process Management_
- [article] [Allowing for Errors in Bash When You Have set -e Defined](https://nickjanetakis.com/blog/allowing-for-errors-in-bash-when-you-have-set-e-defined) — _set -e_
- [article] [Executing Code after an Error Occurs with Bash When Using set e](https://nickjanetakis.com/blog/executing-code-after-an-error-occurs-with-bash-when-using-set-e) — _set -e_
- [article] [Prevent Unset Variables in Your Shell / Bash Scripts with set nounset](https://nickjanetakis.com/blog/prevent-unset-variables-in-your-shell-bash-scripts-with-set-nounset) — _set -o_
- [article] [How to get help in Bash](https://nipunarat1997.medium.com/how-to-get-help-in-bash-9b101ee7d65a) — _Help Commands_
- [article] [Wildcard characters in Shell Script Linux](https://nkugwamarkwilliam.medium.com/wildcard-characters-in-shell-script-linux-6e885b624565) — _Wildcard Question Mark (?)_
- [article] [How to program with Bash: Logical operators and shell expansions](https://opensource.com/article/19/10/programming-bash-logical-operators-shell-expansions) — _Logical Operators in Bash_
- [article] [Getting started with Vim: The basics](https://opensource.com/article/19/3/getting-started-vim) — _Vim_
- [article] [A beginner’s guide to SSH for remote connection on Linux](https://opensource.com/article/20/9/ssh) — _SSH_
- [article] [Bash shell basics — pipes, redirection, and coprocesses](https://paulguerin.medium.com/bash-shell-basics-pipe-and-redirection-fbb4c2c1c0ed) — _Pipes_
- [article] [Bash shell basics — scoping](https://paulguerin.medium.com/bash-shell-basics-scoping-d59c8e1468b4) — _Variable Scopes_
- [article] [apt Linux Command with Examples](https://phoenixnap.com/kb/apt-linux) — _apt_
- [article] [How to Comment in Bash](https://phoenixnap.com/kb/bash-comment) — _Comments_
- [article] [How to Use the Bash let Command {with Examples}](https://phoenixnap.com/kb/bash-let) — _Let Command_
- [article] [Bash Math Operations (Bash Arithmetic) Explained](https://phoenixnap.com/kb/bash-math) — _Arithmetic Operators in Bash_
- [article] [Bash trap Command Explained](https://phoenixnap.com/kb/bash-trap-command) — _Trap_
- [article] [How to Use Disown Command in Linux](https://phoenixnap.com/kb/disown-command-linux) — _disown_
- [article] [How to Use the Linux at Command](https://phoenixnap.com/kb/linux-at-command) — _at_
- [article] [Linux bc Command with Examples](https://phoenixnap.com/kb/linux-bc) — _bc_
- [article] [Linux ifconfig Command With Examples](https://phoenixnap.com/kb/linux-ifconfig) — _ifconfig and ip Commands_
- [article] [Linux ip Command with Examples](https://phoenixnap.com/kb/linux-ip-command-examples) — _ifconfig and ip Commands_
- [article] [8 Types of Linux Shells](https://phoenixnap.com/kb/linux-shells) — _Popular Shells_
- [article] [Linux split Command {13 Examples}](https://phoenixnap.com/kb/linux-split) — _Join and Split_
- [article] [Linux tr Command with Examples](https://phoenixnap.com/kb/linux-tr) — _tr Command_
- [article] [Netstat Command in Linux - 25 Commands with Examples](https://phoenixnap.com/kb/netstat-command) — _netstat and ss_
- [article] [How To Use Linux SS Command](https://phoenixnap.com/kb/ss-command) — _netstat and ss_
- [article] [Extended Regular Expressions](https://pressbooks.senecapolytechnic.ca/uli101/chapter/extended-regular-expressions/) — _Extended Regular Expressions_
- [article] [Associative arrays in Bash](https://rednafi.com/misc/associative-arrays-in-bash/) — _Associative Arrays_
- [article] [Using Arguments in Bash Scripts](https://refine.dev/blog/bash-script-arguments/#introduction) — _Script Arguments_
- [article] [Arithmetic - Bash Scripting Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/bash-arithmetic.php) — _Numeric Data in Bash_
- [article] [User Input!](https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php) — _Read User Input_
- [article] [Shell Script Best Practices](https://sharats.me/posts/shell-script-best-practices/) — _Variables Best Practices_
- [article] [Practical examples of “expr” command in Linux](https://tecadmin.net/expr-command-examples/) — _Expr_
- [article] [Debugging Bash scripts](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_02_03.html) — _Debugging_
- [article] [Regular expressions](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_01.html) — _Regular Expressions_
- [article] [Using case statements](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_03.html) — _Case Statements_
- [article] [Break and continue](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_05.html) — _Break and Continue in Loops_
- [article] [Wildcards](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm) — _Asterisk Wildcard_
- [article] [Other Comparison Operators](https://tldp.org/LDP/abs/html/comparison-ops.html) — _Comparison Operators in Bash_
- [article] [File test operators](https://tldp.org/LDP/abs/html/fto.html) — _File Test Operators_
- [article] [Here documents](https://tldp.org/LDP/abs/html/here-docs.html) — _Here Documents_
- [article] [Operators](https://tldp.org/LDP/abs/html/ops.html) — _Bash Operators_
- [article] [Special Variable Types](https://tldp.org/LDP/abs/html/othertypesv.html) — _Special Variables_
- [article] [Parameter Substitution](https://tldp.org/LDP/abs/html/parameter-substitution.html) — _Pattern Replacement_
- [article] [Process Substitution](https://tldp.org/LDP/abs/html/process-sub.html) — _Process Substitution_
- [article] [Manipulating Strings](https://tldp.org/LDP/abs/html/string-manipulation.html) — _Strings in Bash_
- [article] [Here Strings](https://tldp.org/LDP/abs/html/x17837.html) — _Here Strings_
- [article] [Job Control Commands](https://tldp.org/LDP/abs/html/x9644.html) — _fg and bg_
- [article] [ShellCheck: Script Analysis Tool for Shell Scripts](https://trunk.io/linters/shell/shellcheck) — _Shellcheck_
- [article] [Dash](https://wiki.archlinux.org/title/Dash) — _dash_
- [article] [Extracting a Substring in Bash](https://www.baeldung.com/linux/bash-substring) — _Substring Extraction_
- [article] [Guide to the Linux bzip2 Command With Examples](https://www.baeldung.com/linux/bzip2-guide) — _bzip2 and xz_
- [article] [Using gzip and gunzip in Linux](https://www.baeldung.com/linux/gzip-and-gunzip) — _gzip and gunzip_
- [article] [Jobs and Job Control in Bash Shell](https://www.baeldung.com/linux/jobs-job-control-bash) — _Jobs_
- [article] [Guide to Naming Conventions for Shell Variables](https://www.baeldung.com/linux/shell-variable-naming-conventions) — _Variables Best Practices_
- [article] [The Type System of Bash](https://www.celantur.com/blog/bash-type-system/) — _Bash Data Types_
- [article] [What Is a GUI?](https://www.coursera.org/articles/gui) — _CLI vs GUI_
- [article] [Bash For Loop Examples](https://www.cyberciti.biz/faq/bash-for-loop/) — _For Loops_
- [article] [How To Use awk In Bash Scripting](https://www.cyberciti.biz/faq/bash-scripting-using-awk/) — _Awk for Numeric Operations_
- [article] [Bash While Loop Examples](https://www.cyberciti.biz/faq/bash-while-loop/) — _While Loops_
- [article] [Linux bash exit status and how to set exit status in bash](https://www.cyberciti.biz/faq/linux-bash-exit-status-set-exit-statusin-bash/) — _Exit Codes_
- [article] [Bash Shell Convert Uppercase to Lowercase in Linux](https://www.cyberciti.biz/faq/linux-unix-shell-programming-converting-lowercase-uppercase/) — _Case Conversion_
- [article] [How To Use pwd Command In Linux / UNIX {with examples}](https://www.cyberciti.biz/faq/pwd-linux-unix-command-examples/) — _pwd_
- [article] [How To Run the .sh File Shell Script In Linux / UNIX](https://www.cyberciti.biz/faq/run-execute-sh-shell-script/) — _Running Shell Scripts_
- [article] [Linux / Unix: disown Command Examples](https://www.cyberciti.biz/faq/unix-linux-disown-command-examples-usage-syntax/) — _disown_
- [article] [AWK command in Linux/Unix | DigitalOcean](https://www.digitalocean.com/community/tutorials/awk-command-linux-unix) — _awk_
- [article] [What are the Different Types of Shells in Linux?](https://www.digitalocean.com/community/tutorials/different-types-of-shells-in-linux) — _Popular Shells_
- [article] [Mastering Grep command in Linux/Unix: A Beginner's Tutorial](https://www.digitalocean.com/community/tutorials/grep-command-in-linux-unix) — _grep_
- [article] [How To Install and Use Homebrew on Linux](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-homebrew-on-linux) — _Homebrew_
- [article] [How To Read and Set Environmental and Shell Variables on Linux](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux) — _Environment vs. Shell Variables_
- [article] [How To Use Bash History Commands and Expansions on a Linux VPS](https://www.digitalocean.com/community/tutorials/how-to-use-bash-history-commands-and-expansions-on-a-linux-vps) — _Repeat Commands_
- [article] [How To Use Bash's Job Control to Manage Foreground and Background Processes](https://www.digitalocean.com/community/tutorials/how-to-use-bash-s-job-control-to-manage-foreground-and-background-processes) — _fg and bg_
- [article] [How To Use Rsync to Sync Local and Remote Directories](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories) — _rsync_
- [article] [How To Use the Emacs Editor in Linux | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-use-the-emacs-editor-in-linux) — _Emacs_
- [article] [Mastering sed Command in Linux: A Comprehensive Guide | DigitalOcean](https://www.digitalocean.com/community/tutorials/linux-sed-command) — _sed_
- [article] [How to Use the nohup Command in Linux](https://www.digitalocean.com/community/tutorials/nohup-command-in-linux) — _nohup_
- [article] [SSH Essentials: Working with SSH Servers, Clients, and Keys](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys) — _SSH_
- [article] [Bash Scripting Tutorial – Linux Shell Script and Command Line for Beginners](https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/) — _What is Scripting?_
- [article] [Command Line Commands – CLI Tutorial](https://www.freecodecamp.org/news/command-line-commands-cli-tutorial/) — _cmd_
- [article] [The Linux AWK Command – Linux and Unix Usage Syntax Examples](https://www.freecodecamp.org/news/the-linux-awk-command-linux-and-unix-usage-syntax-examples/) — _awk_
- [article] [Bash Regex Tutorial for Beginners (regular expressions)](https://www.fullstackfoundations.com/blog/bash-regex) — _Basic Regex Syntax_
- [article] [List Processes Linux: ps command for beginners](https://www.fullstackfoundations.com/blog/list-processes-linux) — _ps_
- [article] [Environment and Shell variables In Linux](https://www.futurelearn.com/info/courses/linux-for-bioinformatics/0/steps/201724) — _Environment vs. Shell Variables_
- [article] [Bash Scripting - String](https://www.geeksforgeeks.org/linux-unix/bash-scripting-string/) — _Strings in Bash_
- [article] [How to Redirect Standard (stderr) Error in Bash](https://www.geeksforgeeks.org/linux-unix/how-to-redirect-standard-stderr-error-in-bash/) — _Error Redirection_
- [article] [Arithmetic Expansion (Bash Reference Manual)](https://www.gnu.org/software/bash/manual/html_node/Arithmetic-Expansion.html) — _Arithmetic Expansion_
- [article] [Bash Conditional Expressions (Bash Reference Manual)](https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html) — _Conditionals_
- [article] [Command substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html) — _Command Substitution_
- [article] [Job Control Basics](https://www.gnu.org/software/bash/manual/html_node/Job-Control-Basics.html) — _Jobs_
- [article] [Pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html) — _Pipes_
- [article] [Positional Parameters](https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html) — _Positional Parameters_
- [article] [GNU Emacs - Guided Tour](https://www.gnu.org/software/emacs/tour/) — _Basic Editor Operations_
- [article] [https://www.gnu.org/software/gnuastro/manual/html_node/Bash-TAB-completion-tutorial.html](https://www.gnu.org/software/gnuastro/manual/html_node/Bash-TAB-completion-tutorial.html) — _Tab Completion_
- [article] [GNU Wget](https://www.gnu.org/software/wget/) — _wget_
- [article] [Using set -x and set -e in Shell Scripting: A Guide for Enhanced Debugging and Error Handling](https://www.hackerone.com/blog/using-set-x-and-set-e-shell-scripting-guide-enhanced-debugging-and-error-handling) — _set -x_
- [article] [What is a cron job: understanding cron syntax and how to configure cron jobs](https://www.hostinger.com/tutorials/cron-job) — _cron and crontab_
- [article] [How to run the .sh file in Linux](https://www.hostinger.com/tutorials/how-to-run-sh-file-in-linux) — _Running Shell Scripts_
- [article] [How to use SCP command to copy and transfer files in Linux](https://www.hostinger.com/tutorials/linux-scp-command) — _scp_
- [article] [How to use the tar command in Linux](https://www.hostinger.com/tutorials/linux-tar-command-with-examples) — _tar_
- [article] [How to use the nohup command in Linux](https://www.hostinger.com/tutorials/nohup-command-in-linux) — _nohup_
- [article] [What is the wget command and how to use it (12 examples included)](https://www.hostinger.com/tutorials/wget-command-examples) — _wget_
- [article] [Deleting or removing directories (rmdir command)](https://www.ibm.com/docs/en/aix/7.2.0?topic=directories-deleting-removing-rmdir-command) — _rmdir_
- [article] [More Command](https://www.ibm.com/docs/en/aix/7.2.0?topic=m-more-command) — _less and more_
- [article] [zsh - The Z shell](https://www.ibm.com/docs/en/zos/3.1.0?topic=descriptions-zsh-z-shell) — _zsh_
- [article] [How to use top and htop Linux command for Process Management](https://www.layerstack.com/resources/tutorials/How-to-use-top-and-htop-Linux-command-for-Process-Management) — _top and htop_
- [article] [stdin, stdout, stderr](https://www.learnlinux.org.za/courses/build/shell-scripting/ch01s04) — _stdin, stdout, and stderr_
- [article] [The Bash Trap Command](https://www.linuxjournal.com/content/bash-trap-command) — _Trap_
- [article] [Linux Performance Monitoring: Using Tools Like top, vmstat, and iostat](https://www.linuxjournal.com/content/linux-performance-monitoring-using-tools-top-vmstat-and-iostat) — _iostat and vmstat_
- [article] [Bash String Comparison: The Comprehensive Guide](https://www.namehero.com/blog/bash-string-comparison-the-comprehensive-guide/) — _String Operators_
- [article] [String Operators](https://www.oreilly.com/library/view/learning-the-bash/1565923472/ch04s03.html) — _String Operators_
- [article] [Standard Wildcards / Globbing Patterns in Linux](https://www.putorius.net/standard-wildcards-globbing-patterns-in.html) — _Curly Braces Wildcards_
- [article] [Adding arguments and options to your Bash scripts](https://www.redhat.com/en/blog/arguments-options-bash-scripts) — _Script Arguments_
- [article] [Error handling in Bash scripts](https://www.redhat.com/en/blog/error-handling-bash-scripting) — _Error Handling_
- [article] [Linux package management with YUM and RPM](https://www.redhat.com/en/blog/how-manage-packages) — _yum_
- [article] [An introduction to the vi editor](https://www.redhat.com/en/blog/introduction-vi-editor) — _Vi_
- [article] [Linux Commands: jobs, bg, and fg](https://www.redhat.com/en/blog/jobs-bg-fg) — _fg and bg_
- [article] [10 ways to use the Linux find command](https://www.redhat.com/en/blog/linux-find-command) — _Find_
- [article] [What are the differences between absolute and relative paths?](https://www.redhat.com/en/blog/linux-path-absolute-relative) — _Navigate Between Directories_
- [article] [How to use the uniq command to process lists in Linux](https://www.redhat.com/en/blog/uniq-command-lists) — _uniq_
- [article] [The Shell Scripting Tutorial](https://www.shellscript.sh/philosophy.html) — _Introduction_
- [article] [Understanding Shell Script Variables - The Shell Scripting Tutorial](https://www.shellscript.sh/variables1.html) — _Variables in Shell Scripting_
- [article] [Linux Performance Monitoring with Vmstat and Iostat Commands](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/) — _iostat and vmstat_
- [article] [Wc Command - Count Number of Lines, Words, and Characters](https://www.tecmint.com/wc-command-examples/) — _wc_
- [article] [Learn XZ (Lossless Data Compression Tool) in Linux with Examples](https://www.tecmint.com/xz-command-examples-in-linux/) — _bzip2 and xz_
- [article] [Bash String Manipulation Examples – Length, Substring, Find and Replace](https://www.thegeekstuff.com/2010/07/bash-string-manipulation/) — _String Length_
- [article] [Using the Linux Free Command With Examples](https://www.turing.com/kb/how-to-use-the-linux-free-command) — _Free_
- [article] [Linux Performance Monitoring with Vmstat and Iostat Commands](https://www.tutorialspoint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands) — _iostat and vmstat_
- [article] [Unix / Linux - Shell Input/Output Redirections](https://www.tutorialspoint.com/unix/unix-io-redirections.htm) — _Redirects & Pipelines_
- [article] [Unix / Linux - Shell Input/Output Redirections](https://www.tutorialspoint.com/unix/unix-io-redirections.htm#:~:text=The%20output%20from%20a%20command,is%20known%20as%20output%20redirection.) — _Output Redirection_
- [article] [Special variables](https://www.tutorialspoint.com/unix/unix-special-variables.htm) — _Special Variables_
- [article] [Unix / Linux - Using Shell Variables](https://www.tutorialspoint.com/unix/unix-using-variables.htm) — _Variables in Shell Scripting_
- [article] [Bash Logging and Error Reporting Exercises, Solutions & Explanation](https://www.w3resource.com/bash-script-exercises/logging-and-error-reporting.php) — _Error Logging_
- [article] [Bash Tutorial](https://www.w3schools.com/bash/) — _What is Bash?_
- [article] [Bash Alias](https://www.w3schools.com/bash/bash_alias.php) — _Bash Alias_
- [article] [Bash Arrays](https://www.w3schools.com/bash/bash_arrays.php) — _Arrays_
- [article] [Bash awk - Pattern Scanning and Processing Language](https://www.w3schools.com/bash/bash_awk.php) — _Awk for Numeric Operations_
- [article] [Bash cat Command - Concatenate and Display Files](https://www.w3schools.com/bash/bash_cat.php) — _cat_
- [article] [Bash cd - Change Directory](https://www.w3schools.com/bash/bash_cd.php) — _cd_
- [article] [Bash If...Else](https://www.w3schools.com/bash/bash_conditions.php) — _Conditionals - if_
- [article] [Bash cp - Copy Files and Directories](https://www.w3schools.com/bash/bash_cp.php) — _cp Command_
- [article] [Bash crontab Command - Schedule Tasks](https://www.w3schools.com/bash/bash_cron.php) — _cron and crontab_
- [article] [Bash Data Types](https://www.w3schools.com/bash/bash_data_types.php) — _Strings in Bash_
- [article] [Bash df Command - File System Disk Space Usage](https://www.w3schools.com/bash/bash_df.php) — _df and du Commands_
- [article] [Bash du Command - File Space Usage](https://www.w3schools.com/bash/bash_du.php) — _df and du Commands_
- [article] [Bash echo Command - Display Text](https://www.w3schools.com/bash/bash_echo.php) — _Echo_
- [article] [Bash free Command - Display Free and Used Memory](https://www.w3schools.com/bash/bash_free.php) — _Free_
- [article] [Bash Functions](https://www.w3schools.com/bash/bash_functions.php) — _Functions_
- [article] [Bash grep Command - Search Text Using Patterns](https://www.w3schools.com/bash/bash_grep.php) — _grep_
- [article] [Bash head Command - Display the beginning of a file](https://www.w3schools.com/bash/bash_head.php) — _head and tail_
- [article] [Bash kill Command - Terminate Processes](https://www.w3schools.com/bash/bash_kill.php) — _Stop Execution_
- [article] [Bash Loops](https://www.w3schools.com/bash/bash_loops.php) — _While Loops_
- [article] [Bash ls Command - List Directory Contents](https://www.w3schools.com/bash/bash_ls.php) — _ls_
- [article] [Bash man Command - User Manual](https://www.w3schools.com/bash/bash_man.php) — _Help Commands_
- [article] [Bash mkdir Command - Make Directories](https://www.w3schools.com/bash/bash_mkdir.php) — _mkdir_
- [article] [Bash mv Command - Move or Rename Files](https://www.w3schools.com/bash/bash_mv.php) — _mv Command_
- [article] [Bash Operators](https://www.w3schools.com/bash/bash_operators.php) — _Comparison Operators in Bash_
- [article] [Bash ping Command - Send Request to Network Hosts](https://www.w3schools.com/bash/bash_ping.php) — _Ping_
- [article] [Bash ps Command - Snapshot of Current Processes](https://www.w3schools.com/bash/bash_ps.php) — _ps_
- [article] [Bash pwd Command - Print Working Directory](https://www.w3schools.com/bash/bash_pwd.php) — _pwd_
- [article] [Bash rm Command - Remove Files or Directories](https://www.w3schools.com/bash/bash_rm.php) — _rm Command_
- [article] [Bash rsync Command - Remote (and local) File-copying](https://www.w3schools.com/bash/bash_rsync.php) — _rsync_
- [article] [Bash Script](https://www.w3schools.com/bash/bash_script.php) — _Bash Script Anatomy_
- [article] [Bash sed Command - Stream Editor](https://www.w3schools.com/bash/bash_sed.php) — _sed_
- [article] [Bash sort Command - Sort Lines of Text Files](https://www.w3schools.com/bash/bash_sort.php) — _Sort_
- [article] [Bash tail Command - Display Last Part of Files](https://www.w3schools.com/bash/bash_tail.php) — _head and tail_
- [article] [Bash tar Command - An archiving utility](https://www.w3schools.com/bash/bash_tar.php) — _tar_
- [article] [Bash top Command - Display Linux Tasks](https://www.w3schools.com/bash/bash_top.php) — _top and htop_
- [article] [Bash touch Command - Change File Timestamps](https://www.w3schools.com/bash/bash_touch.php) — _touch_
- [article] [Bash unzip Command - Extract from ZIP archive](https://www.w3schools.com/bash/bash_unzip.php) — _zip and unzip_
- [article] [Bash uptime Command - System Runtime](https://www.w3schools.com/bash/bash_uptime.php) — _Uptime_
- [article] [Bash zip Command - Package and compress (archive) files](https://www.w3schools.com/bash/bash_zip.php) — _zip and unzip_
- [article] [Bash printf](https://www.warp.dev/terminus/bash-printf) — _printf Formatting_
- [article] [Reading User Input](https://www.warp.dev/terminus/bash-reading-user-input) — _Read User Input_
- [article] [How To Use Unix Wildcards](https://www.warp.dev/terminus/linux-wildcards) — _Wildcard Question Mark (?)_
- [article] [Bash Functions – Declaration, Scope, Arguments, etc](https://www.webservertalk.com/bash-functions/) — _Function Scopes_
- [article] [What's the difference between Programming and Scripting?](https://www.youtube.com/watch?v=7-0iBZxNq74) — _What is Scripting?_
- [article] [How to configure or customize Bash: My first steps for my setup](https://www.youtube.com/watch?v=wy1q5egFW6I) — _Setting Up Bash_
- [article] [Working with systemd timers](https://yieldcode.blog/post/working-with-systemd-timers/) — _Systemd Timers_
- [article] [Beginners Guide to Bash Regex (With Code Examples)](https://zerotomastery.io/blog/bash-regex/) — _Regular Expressions_
- [book] [Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/Bash-Beginners-Guide.pdf) — _What is Bash?_
- [course] [Bash Scripting](https://linuxhandbook.com/courses/bash/) — _Bash Script Anatomy_
- [course] [OpenVim - Interactive Vim Tutorial](https://openvim.com/) — _Vim_
- [official] [brew](https://brew.sh/) — _Homebrew_
- [official] [The Art Of Scripting HTTP Requests Using curl](https://curl.se/docs/httpscripting.html) — _curl_
- [official] [vscode-bash-debug](https://github.com/rogalmic/vscode-bash-debug) — _Bash Debug_
- [official] [PowerShell Docs](https://learn.microsoft.com/en-us/powershell/) — _PowerShell_
- [official] [What is PowerShell?](https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.5) — _PowerShell_
- [official] [Bash Debug](https://marketplace.visualstudio.com/items?itemName=rogalmic.bash-debug) — _Bash Debug_
- [official] [Bash Docs](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html) — _What is Bash?_
- [official] [Redirections](https://www.gnu.org/software/bash/manual/html_node/Redirections.html) — _Redirects & Pipelines_
- [official] [GNU Emacs](https://www.gnu.org/software/emacs/) — _Emacs_
- [official] [nano – Text editor](https://www.nano-editor.org/) — _Nano_
- [official] [Shellcheck](https://www.shellcheck.net/) — _Shellcheck_
- [official] [tcsh](https://www.tcsh.org/) — _tcsh_
- [official] [Vim](https://www.vim.org/) — _Vim_
- [opensource] [PowerShell](https://github.com/PowerShell/PowerShell) — _PowerShell_
- [opensource] [curl](https://github.com/curl/curl) — _curl_
- [opensource] [fish-shell](https://github.com/fish-shell/fish-shell) — _fish_
- [opensource] [Shellcheck](https://github.com/koalaman/shellcheck) — _Shellcheck_
- [video] [Bash Scripting on Linux](https://www.youtube.com/playlist?list=PLT98CRl2KxKGj-VKtApD8-zCqSaN2mD4w) — _What is Scripting?_
- [video] [Basics of VI editor in under 8 minutes | Vi editor Tutorial](https://www.youtube.com/watch?v=-_DvfdgR-LA) — _Vi_
- [video] [Heredocs in Bash! Understanding how they work and a few gotchas. You Suck at Programming](https://www.youtube.com/watch?v=-a1VAole01s) — _Here Documents_
- [video] [Supercharge Your Workflow with cURL | Understanding The cURL Command-Line Tool](https://www.youtube.com/watch?v=-nnJ82uc2ic) — _curl_
- [video] [What Is a Shell ? | Learn How Shell Commands Work in the Terminal](https://www.youtube.com/watch?v=-qLrgCFynzE) — _Introduction_
- [video] [Killing Processes Linux Shell Tutorial](https://www.youtube.com/watch?v=03umJo33aQg) — _Stop Execution_
- [video] [Linux Command Line Tutorial For Beginners 10 - less command](https://www.youtube.com/watch?v=06GsFVeuWNk) — _less and more_
- [video] [How to Use The "at" Command On Linux](https://www.youtube.com/watch?v=0Lvvw4yA6Ag) — _at_
- [video] [Here Strings in Bash! Redirecting a string into stdin. You Suck at Programming](https://www.youtube.com/watch?v=0cWuZvw8lXc) — _Here Strings_
- [video] [Crash-Course! Functions in Bash quickly explained and demystified!](https://www.youtube.com/watch?v=0tycTrpbWKs) — _Functions_
- [video] [Linux Crash Course - The apt Command](https://www.youtube.com/watch?v=1kicKTbK768) — _apt_
- [video] [Bash sort Command - Sort Lines of Text Files](https://www.youtube.com/watch?v=2B16aYGzIEQ) — _Sort_
- [video] [How to Archive Folders in Linux (tar and gzip tutorial) - Linux Crash Course Series](https://www.youtube.com/watch?v=2iwumBcfd58) — _tar_
- [video] [How to Archive Folders in Linux (tar and gzip tutorial) - Linux Crash Course Series](https://www.youtube.com/watch?v=2iwumBcfd58&t) — _gzip and gunzip_
- [video] [Shell Scripting Tutorial - Break & Continue Statement](https://www.youtube.com/watch?v=3Dg6j_zSk_0) — _Break and Continue in Loops_
- [video] [Understanding Linux System Performance | The Top Command](https://www.youtube.com/watch?v=3r_PBLaZoFQ) — _top and htop_
- [video] [The Absolute Beginner's Guide to Emacs](https://www.youtube.com/watch?v=48JlgiBpw_I) — _Emacs_
- [video] [Bash Shell Scripting For Beginners - Local and Global Variables](https://www.youtube.com/watch?v=4GR0wum_pOQ) — _Variable Scopes_
- [video] [Understanding stdin, stdout, stderr in Python](https://www.youtube.com/watch?v=4HY0VBBY7ok) — _Error Redirection_
- [video] [Linux Crash Course - Understanding File Permissions](https://www.youtube.com/watch?v=4N4Q576i3zA) — _rwx File Permissions_
- [video] [How to Debug Bash - Using bash -x or set -x in bash - You Suck at Programming #044](https://www.youtube.com/watch?v=4TAx3Z9OgPs) — _set -x_
- [video] [Linux Crash Course - The tr Command](https://www.youtube.com/watch?v=4qP5xA_epXo) — _tr Command_
- [video] [Linux Crash Course - The head and tail Commands](https://www.youtube.com/watch?v=5EqL6Fc7NNw) — _head and tail_
- [video] [Zsh: The Developer's Dream Shell! Say Goodbye to Bash! 💻✨](https://www.youtube.com/watch?v=5F4T_iTeN08) — _zsh_
- [video] [Linux Tutorial for Beginners | expr command | Evaluate Expressions in Linux](https://www.youtube.com/watch?v=6LbMLSBoLGY) — _Expr_
- [video] [IO Redirection in Bash EXPLAINED](https://www.youtube.com/watch?v=7VaO2dxs_kg) — _Redirects & Pipelines_
- [video] [Linux Crash Course - Scheduling Tasks with Cron](https://www.youtube.com/watch?v=7cbP7fzn0D8) — _cron and crontab_
- [video] [Ping Command Explained | Real World Example](https://www.youtube.com/watch?v=7sv5pL-XgSg) — _Ping_
- [video] [Bash until Loop](https://www.youtube.com/watch?v=8x2EfVSGwQc) — _Until Loops_
- [video] [sed: Easily replace strings across files | #7 Practical Bash](https://www.youtube.com/watch?v=91msRzo0VYw) — _Pattern Replacement_
- [video] [Learning Awk Is Essential For Linux Users](https://www.youtube.com/watch?v=9YOZmI-zWok) — _Awk for Numeric Operations_
- [video] [How To Use Shell Environment Variables](https://www.youtube.com/watch?v=9ZpL8iDU7LY) — _Variables in Shell Scripting_
- [video] [Transferring files with the scp Command (Linux Crash Course Series)](https://www.youtube.com/watch?v=Aa7tKMmeFZI) — _scp_
- [video] [Master the Linux Command Line: Background & Foreground Jobs to Swap Tasks with the fg and bg Command](https://www.youtube.com/watch?v=Ak7cFJ1-Ewo) — _fg and bg_
- [video] [How to use the disown command: 2-Minute Linux Tipsv](https://www.youtube.com/watch?v=B66HKmP03Xo) — _disown_
- [video] [Linux Command Line Tutorial For Beginners 8 - cp command](https://www.youtube.com/watch?v=Bnx_GAHM0wo) — _cp Command_
- [video] [Bash History | Your Linux Command History Explained](https://www.youtube.com/watch?v=Bth-1rLKjGU) — _Repeat Commands_
- [video] [FISH (Friendly Interactive Shell) by Bash Boomer](https://www.youtube.com/watch?v=C2a7jJTh3kU) — _fish_
- [video] [07 The Help Command Linux Shell Tutorials](https://www.youtube.com/watch?v=D4bSUqqaX3c) — _Help Commands_
- [video] [Bash Shell Scripting For Beginners - Case Statement](https://www.youtube.com/watch?v=DA-Ilf15_r8) — _Case Statements_
- [video] [Linux Crash Course - nano (command-line text editor)](https://www.youtube.com/watch?v=DLeATFgGM-A) — _Basic Editor Operations_
- [video] [Linux - How to split larger files into smaller parts](https://www.youtube.com/watch?v=DaC5AWjmQXk) — _Join and Split_
- [video] [How to use the nohup command](https://www.youtube.com/watch?v=E96yxNUS84c) — _nohup_
- [video] [Bash Shell Scripting for Beginners - Using Pipes](https://www.youtube.com/watch?v=FICwAKYc0Pg) — _Pipes_
- [video] [Linux Crash Course - The cut Command](https://www.youtube.com/watch?v=GYP2T34v56E) — _cut and paste_
- [video] [Passing Arguments to the Script | Shell Scripting Tutorial for Beginners](https://www.youtube.com/watch?v=Gexu9M7p5aU) — _Script Arguments_
- [video] [Linux File Transfers Made Easy with rsync](https://www.youtube.com/watch?v=KG78O53u8rY) — _rsync_
- [video] [Creating substrings in Bash - Basic String Manipulation - You Suck at Programming #045](https://www.youtube.com/watch?v=KPVm06L55gc) — _Substring Extraction_
- [video] [Simple PING commands](https://www.youtube.com/watch?v=KYmtMBsuA50) — _Ping_
- [video] [What is Recursion in bash (Bash 23)](https://www.youtube.com/watch?v=K_BgGxtK2gE) — _Recursive Functions_
- [video] [Prevent Unset Variables in Your Shell / Bash Scripts with set -o nounset](https://www.youtube.com/watch?v=Kly_6DhfHwE) — _set -o_
- [video] [Comments - Bash Scripting](https://www.youtube.com/watch?v=Ky9AiwIeORA) — _Comments_
- [video] [Linux File Permissions in 5 Minutes | MUST Know!](https://www.youtube.com/watch?v=LnKoncbQBsM) — _File Permissions_
- [video] [Linux Commands for Beginners 16 - Output Redirection](https://www.youtube.com/watch?v=NUjpOLlYv7Q) — _Output Redirection_
- [video] [Regular Expressions for Beginners](https://www.youtube.com/watch?v=NhcaKdt3NdM) — _Basic Regex Syntax_
- [video] [#4 - Bash command for Process Management](https://www.youtube.com/watch?v=O4C6_TJ-iws) — _Process Management_
- [video] [Linux | Background Process Basics and Signals | & , disown, nohup](https://www.youtube.com/watch?v=OQpnQgvmbhY) — _disown_
- [video] [Linux Crash Course - Bash Aliases](https://www.youtube.com/watch?v=Ok_kD_sgNcs) — _Bash Alias_
- [video] [Bash: The "let" builtin command](https://www.youtube.com/watch?v=OmZVThsrdp0) — _Let Command_
- [video] [How to Use Nano | Command Line Text Editor](https://www.youtube.com/watch?v=PDWHxh9HUF8) — _Nano_
- [video] [Special Variables | Shell Scripting Tutorial For Beginners](https://www.youtube.com/watch?v=PfxzX4XNYRE) — _Special Variables_
- [video] [How To Write Bash Scripts In Linux - Complete Guide (Part 7 - While Loops)](https://www.youtube.com/watch?v=R0tTsdQ_9Vw) — _While Loops_
- [video] [Homebrew Tutorial: Simplify Software Installation on Mac Using This Package Manager](https://www.youtube.com/watch?v=SELYgZvAZbU) — _Homebrew_
- [video] [How do I read user input into a variable in Bash | Shell Scripting Tutorial for Beginners](https://www.youtube.com/watch?v=Sc2v6Dj3Z4M) — _Read User Input_
- [video] [Linux Crash Course - The grep Command](https://www.youtube.com/watch?v=Tc_jntovCM0) — _grep_
- [video] [The Echo Command | Linux Essential Commands](https://www.youtube.com/watch?v=Tj-9tahWvok) — _Echo_
- [video] [Uniq utility (commands for linux)](https://www.youtube.com/watch?v=VRrd9ErU13w) — _uniq_
- [video] [nl command in Linux with Examples](https://www.youtube.com/watch?v=WqrRKfJWqqM) — _nl_
- [video] [Fix Your Shell Scripts With Shellcheck](https://www.youtube.com/watch?v=X3BIc9EHBuk) — _Shellcheck_
- [video] [Vim As Your Editor - Introduction](https://www.youtube.com/watch?v=X6AR2RMB5tE) — _Vim_
- [video] [Comparison Operators and Square Brackets - Bash Programming Tutorial](https://www.youtube.com/watch?v=XSLj65wnP90) — _Comparison Operators in Bash_
- [video] [SSH for Beginners: The Ultimate Getting Started Guide](https://www.youtube.com/watch?v=YS5Zh7KExvE) — _SSH_
- [video] [Linux Basics: How to use Linux Standard Input and Output](https://www.youtube.com/watch?v=YYz8Y_UBrvw&t=116s) — _Input Redirection_
- [video] [How To Write Bash Scripts In Linux - Complete Guide (Part 5 - If Statements)](https://www.youtube.com/watch?v=YrE1Qg-Aw0Q) — _Conditionals - if_
- [video] [Source Shell Script vs Executing Shell Script - The Real Difference](https://www.youtube.com/watch?v=ZIqRmp-XBRY) — _Running Shell Scripts with Source_
- [video] [Learn PowerShell in Less Than 2 Hours](https://www.youtube.com/watch?v=ZOoCaWyifmI) — _PowerShell_
- [video] [There's more to learn about the "cd" command. Lil' Linux Lesson!](https://www.youtube.com/watch?v=ZRlQxx1rmng) — _cd_
- [video] [Linux Crash Course - The df and du Commands](https://www.youtube.com/watch?v=ZRs5zVv_1UU) — _df and du Commands_
- [video] [wildcards in linux | asterisk , question mark , square brackets , curly brackets , escape character](https://www.youtube.com/watch?v=_J9JwnIzJ9o) — _Curly Braces Wildcards_
- [video] [Bash: printf usage and example](https://www.youtube.com/watch?v=_mi0O52_gwU) — _printf Formatting_
- [video] [Trapping signals with trap in Bash! Responding to Unix signals. You Suck at Programming #064](https://www.youtube.com/watch?v=aXovP1sUtoE) — _Trap_
- [video] [Arrays in Bash Explained in 7 Minutes! - Indexed, Associative, and Nested / Multi-Dimensional](https://www.youtube.com/watch?v=asHJ-xfuyno) — _Associative Arrays_
- [video] [How to Use Unix MORE Command](https://www.youtube.com/watch?v=at7l0REMi04) — _less and more_
- [video] [LPIC-1 101 Using the join command](https://www.youtube.com/watch?v=b3Ybtr6xti4) — _Join and Split_
- [video] [How to use Command Substitution in Bash](https://www.youtube.com/watch?v=b8U_fz0pc-g) — _Command Substitution_
- [video] [How to use the pwd command: 2-Minute Linux Tips](https://www.youtube.com/watch?v=bBM_flm2Ths) — _pwd_
- [video] [The htop Command | Linux Essentials Tutorial](https://www.youtube.com/watch?v=bKWZJ3_5ODc) — _top and htop_
- [video] [Touch Command Made Easy (Linux Crash Course)](https://www.youtube.com/watch?v=bP0dwXU8B64) — _touch_
- [video] [Netstat Commands - Network Administration Tutorial](https://www.youtube.com/watch?v=bxFwpm4IobU) — _netstat and ss_
- [video] [What is the difference between absolute and relative paths?](https://www.youtube.com/watch?v=bxr4p5Ik4js) — _Navigate Between Directories_
- [video] [Shell Scripting Tutorial for Beginners 1 - Introduction](https://www.youtube.com/watch?v=cQepf9fY6cE&list=PLS1QulWo1RIYmaxcEqw5JhK3b-6rgdWO_) — _Introduction_
- [video] [Linux Commands for Beginners 06 - Moving and Renaming Files](https://www.youtube.com/watch?v=cSBYvSA9rDM) — _mv Command_
- [video] [037 Performance Monitoring with Vmstat and lostat](https://www.youtube.com/watch?v=c_My7gRuDb8) — _iostat and vmstat_
- [video] [Learn About These Tools!! Compressing and Archiving Files in the Linux Console (tar, xz, bzip2, zip)](https://www.youtube.com/watch?v=d4PAEbHcLVg) — _bzip2 and xz_
- [video] [Process Substitution in BASH - Commands for Linux](https://www.youtube.com/watch?v=dR0X0-B9ObA) — _Process Substitution_
- [video] [Bash Scripting Full Course 3 Hours](https://www.youtube.com/watch?v=e7BufAVwDiM) — _Bash_
- [video] [Absolute and Relative Paths](https://www.youtube.com/watch?v=ephId3mYu9o) — _Navigate Between Directories_
- [video] [Command vs. Process substitution in Bash - explaining the difference.](https://www.youtube.com/watch?v=f3eIK5xk4vg) — _Process Substitution_
- [video] [BASH Shifting Argument Variables Linux Shell Tutorial](https://www.youtube.com/watch?v=fJSUVGlQ1E8) — _Shift_
- [video] [Bash Globbing Basics! How to use wildcards on the shell](https://www.youtube.com/watch?v=gsucx2W-9sg) — _Wildcard Question Mark (?)_
- [video] [Learn the "ls" command! Lil' Linux Lesson!](https://www.youtube.com/watch?v=gwo--XHaz7s) — _ls_
- [video] [shell vs environment variables (and env, export, etc.) (intermediate) anthony explains](https://www.youtube.com/watch?v=h36Xc38SDHg) — _Environment vs. Shell Variables_
- [video] [How to run bash script in Linux | Linux in a Minute](https://www.youtube.com/watch?v=iViofyFir9o) — _Running with Bash_
- [video] [Linux Tutorials | paste command](https://www.youtube.com/watch?v=ilV6dcTJzzE) — _cut and paste_
- [video] [The Basics of Emacs as a Text Editor](https://www.youtube.com/watch?v=jPkIaqSh3cA) — _Basic Editor Operations_
- [video] [Using IPCONFIG for Network Troubleshooting](https://www.youtube.com/watch?v=k1qgpqQ0Mo4) — _ifconfig and ip Commands_
- [video] [Process and System Management on Linux and Mac (Bash)](https://www.youtube.com/watch?v=lfN2RE8720E) — _ps_
- [video] [Counting Characters in a Bash String - Quick Tip](https://www.youtube.com/watch?v=mK7hutk2yCE) — _String Length_
- [video] [Linux Crash Course - The dnf Command](https://www.youtube.com/watch?v=mL1hMBYP1bQ&t=1529s) — _dnf_
- [video] [Automate Your Tasks with systemd Timers: A Step-by-Step Guide](https://www.youtube.com/watch?v=n6BuUgkZ5T0) — _Systemd Timers_
- [video] [Linux Crash Course - The sed Command](https://www.youtube.com/watch?v=nXLnx8ncZyE) — _sed_
- [video] [Linux Crash Course - awk](https://www.youtube.com/watch?v=oPEnvuj9QrI) — _awk_
- [video] [How to Use the ss Command (Linux Crash Course Series)](https://www.youtube.com/watch?v=phY8Q7Woxsw) — _netstat and ss_
- [video] [You NEED to know how to use CURL!](https://www.youtube.com/watch?v=q2sqkvXzsw8) — _curl_
- [video] [Linux Command Line Tutorial For Beginners 6 - mkdir Command](https://www.youtube.com/watch?v=qixSaXSUs-U) — _mkdir_
- [video] [Arrays in Pure Bash - You Suck at Programming](https://www.youtube.com/watch?v=r4Sc-DpIprk) — _Arrays_
- [video] [Nohup - Hangup Immune Commands - Commands for Linux](https://www.youtube.com/watch?v=rTB-HuuszLs) — _nohup_
- [video] [Arithmetic Expressions - Bash Programming Tutorial](https://www.youtube.com/watch?v=rjuB3X8MOQc) — _Arithmetic Operators in Bash_
- [video] [Logical Operators - Bash Programming Tutorial 8](https://www.youtube.com/watch?v=sDRHmbRlNT8) — _Logical Operators in Bash_
- [video] [Linux Crash Course - The find command](https://www.youtube.com/watch?v=skTiK_6DdqU) — _Find_
- [video] [Uptime command in Linux with Examples - How to Check Uptime in Linux Command Line](https://www.youtube.com/watch?v=slf7GAuzIQ4) — _Uptime_
- [video] [Bash Scripting Tutorial for Beginners](https://www.youtube.com/watch?v=tK9Oc6AEnR4) — _What is Bash?_
- [video] [Shell Script Error Handling: Master Bash Scripting for Robust Code](https://www.youtube.com/watch?v=uFJiDD1B5I4) — _set -e_
- [video] [Shell Scripting Tutorial for Beginners 6 - File test operators](https://www.youtube.com/watch?v=uVi5o38NGi0) — _File Test Operators_
- [video] [Learn SSH In 6 Minutes - Beginners Guide to SSH Tutorial](https://www.youtube.com/watch?v=v45p_kJV9i4) — _SSH_
- [video] [Using BASH Script Arguments](https://www.youtube.com/watch?v=vsRBWCfMf9A) — _$0 in Shell Scripting_
- [video] [What's the difference between a GUI and a CLI?](https://www.youtube.com/watch?v=w9u0d4C95Zs) — _CLI vs GUI_
- [video] [How to Use the ip Command in Linux: A Beginner’s Guide](https://www.youtube.com/watch?v=wHfIFZlDxtU) — _ifconfig and ip Commands_
- [video] [Linux Crash Course - The ps Command](https://www.youtube.com/watch?v=wYwGNgsfN3I) — _ps_
- [video] [How to Unzip and Zip Files on Linux (Desktop and Command Line)](https://www.youtube.com/watch?v=xqcHiuQK9lY) — _zip and unzip_
- [video] [099 Bash Jobs & Signals - Bringing Jobs Back To The Command Line](https://www.youtube.com/watch?v=xu2lGV-kISI) — _Jobs_
- [video] [Shell Scripting Tutorial for Beginners 11 - Floating point math operations in bash | bc Command](https://www.youtube.com/watch?v=yqpY-Wk-i9k) — _bc_
- [video] [Linux Command Line Tutorial For Beginners 7 - rm and rmdir commands for linux](https://www.youtube.com/watch?v=yrw6Uxs-yJk) — _rmdir_
- [video] [The cat Command in Linux (Featuring Real Cats) - Linux Crash Course Series](https://www.youtube.com/watch?v=z3nJlyrJYW4) — _cat_
- [video] [Linux Crash Course - Data Streams (stdin, stdout & stderr)](https://www.youtube.com/watch?v=zMKacHGuIHI) — _stdin, stdout, and stderr_
- [video] [The wget Command | How to Download Files From a Server](https://www.youtube.com/watch?v=zszbBJ81_YU) — _wget_
