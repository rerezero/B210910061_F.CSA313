#!/bin/bash
# Lab03: Newman ашиглан Postman collection ажиллуулах

echo "=========================================="
echo "Lab 03: Postman API Testing with Newman"
echo "=========================================="

# Newman суулгах (хэрэв байхгүй бол)
if ! command -v newman &> /dev/null; then
    echo "Installing Newman..."
    npm install -g newman newman-reporter-htmlextra
fi

echo ""
echo "1. Running basic tests..."
newman run binance-collection.json

echo ""
echo "2. Running with 10 iterations..."
newman run binance-collection.json -n 10

echo ""
echo "3. Generating HTML report..."
newman run binance-collection.json \
    -r htmlextra \
    --reporter-htmlextra-export newman-report.html

echo ""
echo "=========================================="
echo "Tests completed! Check newman-report.html"
echo "=========================================="
