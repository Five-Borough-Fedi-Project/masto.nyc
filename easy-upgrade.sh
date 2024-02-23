#!/bin/bash

# usage: ./easy-upgrade.sh 4.2.0 4.2.1
# once this has ran, run:
# kubectl -n mastodon apply -f cronjobs/ && kubectl -n mastodon apply -f mastodon/

find . \( -type d -name .git -prune \) -o -type f -print0 | xargs -0 sed -i 's/'"$1"'/'"$2"'/g'
git diff