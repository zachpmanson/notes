#!/usr/bin/env bash
# cronchgif.sh

set -e

[ ! -z "${DEBUG}" ] && set -x

if [ $# -ne 2 ]; then
	echo "usage: cronchgif.sh <input> <output>"
	exit 2
fi

input="${1}"
output="${2}"

        
ffmpeg -i "${input}" -vf "fps=30,scale='if(gt(iw,800),800,iw)':'if(gt(iw,800),-2,ih)'" -c:v pam -f image2pipe - | \
	convert -delay 3 - -loop 0 -layers optimize gif:- | \
	ffmpeg -i - -movflags faststart -pix_fmt yuv420p \
	-vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" "${output}"
