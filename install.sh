#!/bin/bash
echo "Updating packages..."
pkg update -y && pkg upgrade -y

echo "Installing python..."
pkg install python -y

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Done! Run with: python main.py"
