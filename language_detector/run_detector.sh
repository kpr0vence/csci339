#!/bin/bash

echo "Running language_detector.py..."

# Check if we want to time it
if [[ "$1" == "time" ]]; then
    echo "Calculating execution time"
    time python language_detector.py data/train/en/all_en.txt data/train/es/all_es.txt data/test/
else
    python language_detector.py data/train/en/all_en.txt data/train/es/all_es.txt data/test/
fi
