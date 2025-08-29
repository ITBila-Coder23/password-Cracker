#!/usr/bin/env python3
"""
brute_force.py — Educational brute-force password "cracker" simulation.

This script demonstrates how brute-force attempts iterate over possible passwords.
Defaults are intentionally small (lowercase+digits, max length 3) to keep it safe to run.

Usage:
    python3 brute_force.py --hash <sha256-hash> [--max-length 3] [--charset abc012]

Warning: For real-world use, brute force is infeasible for strong passwords. Use this only on known
test targets or for learning.
"""
import argparse
import hashlib
import itertools
import time
import sys

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

def iterate_passwords(charset, max_len):
    for length in range(1, max_len+1):
        for tup in itertools.product(charset, repeat=length):
            yield ''.join(tup)

def main():
    parser = argparse.ArgumentParser(description="Educational brute-force password simulation")
    parser.add_argument("--hash", required=True, help="Target SHA-256 hash (hex)")
    parser.add_argument("--max-length", type=int, default=3, help="Maximum password length to try (default 3)")
    parser.add_argument("--charset", default="abcdefghijklmnopqrstuvwxyz0123456789",
                        help="Characters to try (default: lowercase + digits)")
    parser.add_argument("--show-progress", action="store_true", help="Print progress for each attempt (verbose)")
    args = parser.parse_args()

    target = args.hash.strip().lower()
    charset = args.charset
    max_len = args.max_length

    start = time.time()
    tried = 0
    print(f"[+] Starting educational brute-force simulation (max_len={max_len}, charset_len={len(charset)})")
    try:
        for pwd in iterate_passwords(charset, max_len):
            tried += 1
            h = sha256_hex(pwd)
            if args.show_progress and tried % 1000 == 0:
                elapsed = time.time() - start
                rate = tried / (elapsed + 1e-9)
                print(f"  tried={tried} pwd='{pwd}' rate={rate:.1f}/s")
            if h == target:
                elapsed = time.time() - start
                print(f"*** FOUND *** password='{pwd}' after {tried} attempts (time {elapsed:.2f}s)")
                return 0
        print("[!] Password not found within given parameters.")
        return 2
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Exiting.")
        return 130

if __name__ == "__main__":
    sys.exit(main())
