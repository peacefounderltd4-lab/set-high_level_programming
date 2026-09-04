cat > main.py <<'EOF'
#!/usr/bin/python3
print("C is fun!")
EOF

export PYFILE=main.py
chmod +x 0-run
./0-run
