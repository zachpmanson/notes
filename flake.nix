{
  description = "notes static-site generator";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells.default = pkgs.mkShell {
          # nix owns the toolchain (interpreter + uv); uv owns the packages.
          packages = [
            pkgs.python314
            pkgs.uv
          ];

          shellHook = ''
            # Keep uv from downloading its own Python; use the nix one.
            export UV_PYTHON_DOWNLOADS=never
            export UV_PYTHON=${pkgs.python314}/bin/python3.14
          '';
        };
      });
}
