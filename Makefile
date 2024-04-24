# Makefile for project

# Default target
all: run

# Target to pack the project
pack:
    @echo "=== Zabalím projekt ==="
    
    # Add commands to pack the project here

# Target to clean unnecessary files
clean:
    @echo "=== Mažu nepotřebné soubory ==="

    # Add commands to clean unnecessary files here

# Target to run the pre-compiled program
run:
    @echo "=== Spouštím program ==="
    ./src/main.py

# Target to profile the program with sample input
profile:
    @echo "=== Spouštím program pro výpočet směrodatné odchylky ==="
    .src/profile_stddev.py
    # Add commands to run program with sample input for profiling here

# Target to display help
help:
    @echo "=== Nápověda k použití ==="
    @echo "Příkazy:"
    @echo "  make            - Spustí cíl 'all' (tj. spustí program)"
    @echo "  make pack       - Zabalí projekt pro odevzdání"
    @echo "  make clean      - Smaže nepotřebné soubory"
    @echo "  make run        - Spustí program kalkulátor"
    @echo "  make profile    - Spustí program pro výpočet směrodatné odchylky s ukázkovým vstupem"
    @echo "  make help       - Zobrazí tuto nápovědu"

# Phony targets (targets that are not actual files)
.PHONY: all spustit pack clean run profile help
