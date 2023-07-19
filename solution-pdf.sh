#!/bin/bash
chp=chp$1
mkdir -p $chp
pdftk Instructor-Sol.pdf cat $2-$3 output $chp/__solution__.pdf