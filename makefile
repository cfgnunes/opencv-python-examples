VENV_DIR=.venv
VENV_ACTIVATE=$(VENV_DIR)/bin/activate
PYTHON=$(VENV_DIR)/bin/python

.PHONY: help venv lint run clean

help:
	@echo "'make run': Run all examples."
	@echo "'make lint': Run a linter in all code."
	@echo "'make venv': Prepare development environment, use only once."
	@echo "'make clean': Cleans up generated files."
	@echo

venv: $(VENV_ACTIVATE)
$(VENV_ACTIVATE):
	@echo "Creating a virtualenv..."
	@python3 -m venv "$(VENV_DIR)"
	@echo "Installing packages in the virtualenv..."
	@. $(VENV_ACTIVATE); \
		pip3 install --upgrade pip setuptools; \
		pip3 install --upgrade --requirement "requirements.txt"
	@echo "Done!"
	@echo

lint: venv
	@echo "Running linters..."
	@. $(VENV_ACTIVATE); $(PYTHON) -m flake8 *.py
	@. $(VENV_ACTIVATE); $(PYTHON) -m pylint \
		--ignored-modules=cv2 \
		--disable=invalid-name \
		--disable=missing-function-docstring \
		--disable=duplicate-code *.py
	@echo "Done!"
	@echo

run: venv
	@echo "Running all examples..."
	@echo "Running example 01..."
	@. $(VENV_ACTIVATE); $(PYTHON) 01_reading_image.py
	@echo "Running example 02..."
	@. $(VENV_ACTIVATE); $(PYTHON) 02_saving_image.py
	@echo "Running example 03..."
	@. $(VENV_ACTIVATE); $(PYTHON) 03_convert_image_format.py
	@echo "Running example 04..."
	@. $(VENV_ACTIVATE); $(PYTHON) 04_image_scaling.py
	@echo "Running example 05..."
	@. $(VENV_ACTIVATE); $(PYTHON) 05_gaussian_filter.py
	@echo "Running example 06..."
	@. $(VENV_ACTIVATE); $(PYTHON) 06_corner_features.py
	@echo "Running example 07..."
	@. $(VENV_ACTIVATE); $(PYTHON) 07_reading_video_frame.py
	@echo "Running example 08..."
	@. $(VENV_ACTIVATE); $(PYTHON) 08_reading_video.py
	@echo "Running example 09..."
	@. $(VENV_ACTIVATE); $(PYTHON) 09_accessing_webcam.py
	@echo "Running example 10..."
	@. $(VENV_ACTIVATE); $(PYTHON) 10_face_detection.py
	@echo "Running example 11..."
	@. $(VENV_ACTIVATE); $(PYTHON) 11_webcam_features.py
	@echo "Done!"
	@echo

clean:
	@echo "Cleaning up generated files..."
	@rm -rf $(VENV_DIR)
	@rm -rf "__pycache__"
	@find . -type f \( -iname "*.py[cod]" -or -iname "output.*" \) \
		! -path "./.git/*" -delete
	@echo "Done!"
	@echo
