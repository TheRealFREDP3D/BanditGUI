---
layout: default
gamename: bandit
level: 13
---

## Level Goal

The password for the next level is stored in the file **data.txt**,
which is a hexdump of a file that has been repeatedly compressed.
For this level it may be useful to create a directory under /tmp in
which you can work. Use mkdir with a hard to guess directory name.
Or better, use the command "mktemp -d".
Then copy the datafile using cp, and rename it using mv (read the
manpages!)

## Commands you may need to solve this level

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir,
cp, mv, file

## Helpful Reading Material

- [Hex dump on Wikipedia][]

[Hex dump on Wikipedia]: https://en.wikipedia.org/wiki/Hex_dump
