#!/bin/zsh
# Completes the remaining image #10 "everyday carry" ASINs once the ChatGPT/Codex
# plan usage window has reset. Idempotent: skips scenes/composites already present.
RS="/Users/wetrade/Documents/Brand Image Generation/Atwood_Heritage_Amazon_Images/_research/_resume10"
IMG="/Users/wetrade/Documents/Brand Image Generation/Atwood_Heritage_Amazon_Images"
n=$(ls "$IMG"/*/10_everyday_carry.png 2>/dev/null | wc -l | tr -d ' ')
echo "=== resume $(date) — image10 before: $n/18 ==="
if [ "$n" -lt 18 ]; then
  /usr/bin/python3 "$RS/run_all_everyday.py"
fi
n=$(ls "$IMG"/*/10_everyday_carry.png 2>/dev/null | wc -l | tr -d ' ')
echo "=== image10 after: $n/18 ==="
[ "$n" -ge 18 ] && date > "$RS/RESUME_COMPLETE.marker" && echo "ALL 18 DONE"
