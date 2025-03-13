with import <nixpkgs> {};

stdenv.mkDerivation {
	name = "bombsquad-tools";
	buildInputs = [
		python311
	];
}
