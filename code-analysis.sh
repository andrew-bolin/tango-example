#!/usr/bin/env bash
echo "STATIC CODE ANALYSIS"
echo "===================="
echo

echo "MODULE ANALYSIS"
echo "---------------"
pylint andrewdev

echo "TESTS ANALYSIS"
echo "--------------"
pylint tests
