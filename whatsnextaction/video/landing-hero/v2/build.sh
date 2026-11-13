#!/bin/bash
# Landing hero v2 (13. 11. 2026): A canvas -> B inbox, brez zvoka, 1600x1000, 30 fps
set -e
cd "$(dirname "$0")/../.."
A=raw/hero-a-canvas.mov; B=raw/hero-b-canvas.mov   # B je v resnici Inbox
OUT=landing-hero/v2/landing-hero.mp4
# segment: start end speed
segs() { local src=$1; shift; local i=0 f=""; while [ $# -gt 0 ]; do
  f+="[$src:v]trim=$1:$2,setpts=(PTS-STARTPTS)/$3,fps=30,scale=1600:1000:flags=lanczos,setsar=1[$src$i];"; i=$((i+1)); shift 3; done; echo "$f"; }
FA=$(segs 0  1.6 3.3 1   3.3 9.5 8   9.5 11.5 1.5   11.5 24.5 13   24.5 31.6 2.5   31.6 33.6 1)
FB=$(segs 1  1.6 3.3 1   3.3 41.5 30   41.5 45.6 1.3   45.6 46.6 1   46.6 50.8 1.4)
L=""; for i in 0 1 2 3 4 5; do L+="[0$i]"; done; for i in 0 1 2 3 4; do L+="[1$i]"; done
ffmpeg -v error -y -i $A -i $B -filter_complex "${FA}${FB}${L}concat=n=11:v=1:a=0,format=yuv420p[v]" \
  -map "[v]" -an -c:v libx264 -preset slow -crf 24 -profile:v high -movflags +faststart -r 30 $OUT
ffmpeg -v error -y -i $OUT -frames:v 1 -q:v 3 landing-hero/v2/landing-hero-poster.jpg
ffprobe -v error -show_entries format=duration,size -of csv=p=0 $OUT
