#!/usr/bin/env bash

echo "Unpacking example files ..."
cd ExampleFiles

mkdir workdir
mkdir workdir/queue
mkdir workdir/folder1
mkdir workdir/folder2
mkdir workdir/folder3

unzip -d workdir/queue -o example01.tiff.zip
