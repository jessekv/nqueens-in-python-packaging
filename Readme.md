# N-Queens in Python Packaging

Solve N-queens not in python, but with python packages.

Obligatory story featuring Criss: https://jessekv.com/post/packaging-the-technical-interview/

Inspired by:

- https://github.com/konstin/sudoku-in-python-packaging (original source of this fork)
- https://aphyr.com/posts/342-typing-the-technical-interview
- https://www.richard-towers.com/2023/03/11/typescripting-the-technical-interview.html


Each position in the chessboard grid is a package `queen_{a-h}` and the version (1-8) is the row, so you can write a pyproject.toml and the installed packages are the solution.

## Usage

Define the `requiements.in`, optionally with some initial positions:

```shell
$ cat requirements.in
queen-a
queen-b
queen-c==1
queen-d
queen-e
queen-f==8
queen-g
queen-h==4
```

Solve it with your favourite package manager, e.g:

```shell
uv pip compile --find-links packages/ --no-annotate --no-header requirements.in > requirements.txt
```

View the solution:

```shell
$ cat requirements.txt
queen-a==5
queen-b==3
queen-c==1
queen-d==7
queen-e==2
queen-f==8
queen-g==6
queen-h==4
```

Or as a oneliner:

```shell
$ uvx --find-links packages/ --with-requirements requirements.in python render_solution.py

   a b c d e f g h
 ┌─────────────────┐
8│ · · · · · Q · · │8
7│ · · · Q · · · · │7
6│ · · · · · · Q · │6
5│ Q · · · · · · · │5
4│ · · · · · · · Q │4
3│ · Q · · · · · · │3
2│ · · · · Q · · · │2
1│ · · Q · · · · · │1
 └─────────────────┘
   a b c d e f g h
```
