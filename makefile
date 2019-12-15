VENV_DIR=.venv
VENV_ACTIVATE=$(VENV_DIR)/bin/activate
PYTHON=$(VENV_DIR)/bin/python

.PHONY: help lint venv run clean

help:
	@echo "'make run': Run all examples."
	@echo "'make lint': Run a linter in all code."
	@echo "'make venv': Prepare development environment, use only once."
	@echo "'make clean': Cleans up generated files."

lint:
	@flake8 *.py

venv:
	@test -d "$(VENV_DIR)" || echo "Creating new virtualenv..."; python3 -m venv "$(VENV_DIR)"
	@echo "Installing packages in the virtualenv..."
	@. "$(VENV_ACTIVATE)"; \
		pip3 install --upgrade pip; \
		pip3 install --upgrade --requirement "requirements.txt"

run:
	@test -d "$(VENV_DIR)" || make venv
	@echo "Running example 01..."
	@$(PYTHON) 01_reading_image.py
	@echo "Running example 02..."
	@$(PYTHON) 02_saving_image.py
	@echo "Running example 03..."
	@$(PYTHON) 03_convert_image_format.py
	@echo "Running example 04..."
	@$(PYTHON) 04_image_scaling.py
	@echo "Running example 05..."
	@$(PYTHON) 05_gaussian_filter.py
	@echo "Running example 06..."
	@$(PYTHON) 06_corner_features.py
	@echo "Running example 07..."
	@$(PYTHON) 07_reading_video_frame.py
	@echo "Running example 08..."
	@$(PYTHON) 08_reading_video.py
	@echo "Running example 09..."
	@$(PYTHON) 09_accessing_webcam.py
	@echo "Running example 10..."
	@$(PYTHON) 10_face_detection.py
	@echo "Running example 11..."
	@$(PYTHON) 11_webcam_features.py

clean:
	@rm -rf $(VENV_DIR)
	@find . -type f \( \
		-iname "*.py[cod]" \
		-or -iname "output.*" \
		\) ! -path "./.git/*" -delete
