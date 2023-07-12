#!/bin/bash

mkdir -p chp$1
pdftk Instructor-Sol.pdf cat $2-$3 output __solution__.pdf