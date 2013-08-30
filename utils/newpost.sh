#!/bin/bash
#title      :newpost
#description:Setup a brand new pelican rst post on the current directory.
#           :This scripts depends on slugify Python module.
#           :https://pypi.python.org/pypi/slugify/
#           :Before use, make sure to:
#           :
#           :pip install slugify
#           :
#author     :Deny Dias (deny [at] macpress [dot] com [dot] br)
#date       :2013-08-30
#version    :0.1
#usage      :newpost "TITLE" ["AUTHOR"] ["CATEGORY"]
#license    :GPLv3 [http://www.gnu.org/licenses/gpl.html]
#==============================================================================

## Environment Variables
OUTPUTDIR=`pwd`
CURDATE=`date +%Y-%m-%d`
CURTIME=`date +%H:%M:%S`
POSTEXT="rst"

## Core Functions
# Tests for commad line arguments
function runtimetests () {
  if [[ $# -eq 0 || -z $1 ]]
  then
    echo "[newpost] Missing arguments (-1)."
    echo "[newpost] USAGE: newpost \"TITLE\" [\"AUTHOR\"] [\"CATEGORY\"]"
    exit 1
  fi
}

# Slugify the title
function slugit () {
  SLUG=`echo "$1" | slugify`
  CUTSLUG=`echo "$SLUG" | cut -d "-" -f-10`
}

# Write metadata to the article
function metadata () {
  echo "$1" > $NEWPOST
  TITLELENGTH=`echo "$1" | wc -m`
  let "TITLELENGTH--"
  eval printf "\#%.0s" {1..$TITLELENGTH} >> $NEWPOST
  printf '\n%s' >> $NEWPOST
  echo ":date: $CURDATE $CURTIME" >> $NEWPOST
  if [[ -z $2 ]]
  then
    echo ":author: !!!YOUR NAME!!!" >> $NEWPOST
  else
    echo ":author: $2" >> $NEWPOST
  fi
  if [[ -z $3 ]]
  then
    echo ":category: !!!SET A CATEGORY!!!" >> $NEWPOST
  else
    echo ":category: $3" >> $NEWPOST
  fi
  echo ":tags: !!!SET YOUR TAGS!!!" >> $NEWPOST
  echo ":slug: $CUTSLUG" >> $NEWPOST
  echo ":status: draft" >> $NEWPOST
  printf '\n%s' >> $NEWPOST
  echo "Write your post. Be smart and avoid bulshit!"  >> $NEWPOST
  echo "Delete the line \`\`:status: draft\`\` before publish." >> $NEWPOST
}

## The main script.
runtimetests "$1"
slugit "$1"

# Set the article file path
NEWPOST="$OUTPUTDIR/$CURDATE-$CUTSLUG.$POSTEXT"

# Create the article file
touch $NEWPOST

metadata "$1" "$2" "$3"