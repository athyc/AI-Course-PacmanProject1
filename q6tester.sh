#!/bin/bash
python autograder.py -p --test test_cases/q6/corner_sanity_1
sleep 3
python autograder.py -p --test test_cases/q6/corner_sanity_2
sleep 3
python autograder.py -p --test test_cases/q6/corner_sanity_3
sleep 3
python autograder.py -p --test test_cases/q6/medium_corners
