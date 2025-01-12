# # use this if blender executable is in your PATH
blender := blender

# # otherwise, uncomment next line and replace with the path to your blender executable
# blender := ./blender-4.3.2-linux-x64/blender # Do not commit this line

atom-one-dark.zip: ./atom-one-dark/atom_one_dark.xml ./atom-one-dark/blender_manifest.toml
	$(blender) --version
	$(blender) --command extension build --source-dir ./atom-one-dark --output-filepath atom-one-dark.zip

clean:
	rm -rf atom-one-dark.zip
