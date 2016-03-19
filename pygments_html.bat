@echo off
set string="%~1"

pygmentize -O full,style=solarizedlight -o "%~1".html "%~1"

@pause