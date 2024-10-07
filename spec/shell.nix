/* 
 * This file is a nix expression which can be used to get an isolated
 * development environemt.
 *
 * When the nix package manager is installed run 
 *  > nix-shell ./scripts/dev-env.nix 
 * to get a shell with the dependenies of veriT present. This was only tested
 * on NixOS, but should work on other platforms which are supported by the Nix
 * packagemanger (such as MacOS X) too.
 */

{ pkgs ? import <nixpkgs> {} }:

pkgs.stdenvNoCC.mkDerivation {
  name = "alethe";

  hardeningDisable = [ "all" ];
  buildInputs = with pkgs; [
    gnumake
    entr
    python311Packages.pygments
	];
}
