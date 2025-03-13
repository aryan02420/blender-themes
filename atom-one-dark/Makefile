# # use this if blender executable is in your PATH
blender := blender

# # use this if you have blender installed via flatpak
blender := flatpak run org.blender.Blender

# # use this if you have a portable blender installation
# blender := ./blender-4.3.2-linux-x64/blender

current_dir := $(realpath .)

all: output/atom-one-dark.zip output/icon.png

# src/atom_one_dark.xml: ../theme-generator/atom_one_dark.json ../theme-generator/dark-template.xml
# 	python3 ../theme-generator/generate_theme.py -t ../theme-generator/dark-template.xml -d ../theme-generator/atom_one_dark.json -o ./src/atom_one_dark.xml 

output/atom-one-dark.zip: ./src/atom_one_dark.xml ./src/blender_manifest.toml
	mkdir -p output
	@echo -e "\033[1;34mMAKE:\033[0m Validating extension..."
	$(blender) --command extension validate $(current_dir)/src
	@echo -e "\033[1;34mMAKE:\033[0m Building extension..."
	$(blender) --command extension build --source-dir $(current_dir)/src --output-filepath $(current_dir)/output/atom-one-dark.zip

output/icon.png: ./assets/icon.svg
	mkdir -p output
	@echo -e "\033[1;34mMAKE:\033[0m Generating icon..."
	magick ./assets/icon.svg -resize 256x256 ./output/icon.png

clean:
	rm -rf output/*
