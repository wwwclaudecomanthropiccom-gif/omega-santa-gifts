#!/bin/bash
while true; do
    git add gifts/*.py 2>/dev/null || true
    git commit -m "Santa Omega Gift \( (date +%s): \)(ls gifts/*.py 2>/dev/null | wc -l) problems solved" || true
    git push || true
    sleep 30
done
