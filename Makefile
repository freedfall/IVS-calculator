# Makefile for project

# Default target
all: run

# Target to pack the project
pack:
	@echo "=== Zabalím projekt ==="
	# Add commands to pack the project here
	doxygen Doxyfile
	mkdir xkinin00_xdvory00_xshish02_xzhuka01
	cp -r doc xkinin00_xdvory00_xshish02_xzhuka01
	cd xkinin00_xdvory00_xshish02_xzhuka01
	mkdir repo
	cd ..
	cp -r * xkinin00_xdvory00_xshish02_xzhuka01/repo
	cd ..
	zip -r xkinin00_xdvory00_xshish02_xzhuka01

# Target to clean unnecessary files
clean:
	@echo "=== Mažu nepotřebné soubory ==="
	rm -rf doc 
	rm -rf xkinin00_xdvory00_xshish02_xzhuka01

# Target to run the pre-compiled program
run:
	@echo "=== Spouštím program ==="
	python3 ./src/main.py

# Target to profile the program with sample input
profile:
	@echo "=== Spouštím program pro výpočet směrodatné odchylky ==="
	python3 ./src/profile_stddev.py

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
.PHONY: all pack clean run profile help
