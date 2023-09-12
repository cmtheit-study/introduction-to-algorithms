find . -type f \( -name "*.py" -o -name "*.js" \) -exec cat {} \; | wc -l
